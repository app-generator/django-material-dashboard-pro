import base64
import datetime
import json
import os
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse, Http404
from django.template import loader
from django.views.decorators.csrf import csrf_exempt


import requests
import logging
from home.forms import SFirmaForm
from home.decorators import happy_login_required

logger = logging.getLogger(__name__)

# Create your views here.

@happy_login_required
@login_required(login_url="/accounts/login/")
def index(request):

    context = {
        "happyuser": json.loads(request.session.get("happyuser", "{}"))
    }

    # Botones de prueba
    context['botones'] = ["Isaac Newton", "Marie Curie", "Albert Einstein", "Galileo Galilei", "Nikola Tesla", "Charles Darwin", "Stephen Hawking", "Carl Sagan",
        "Jane Goodall", "Max Planck", "Richard Feynman", "Rosalind Franklin", "Gregor Mendel", "James Clerk Maxwell", "Barbara McClintock", "Erwin Schrödinger",
        "Edwin Hubble", "Werner Heisenberg", "Ada Lovelace", "Linus Pauling" ]

    # Page from the theme 
    return render(request, 'pages/index-happy.html', context)


@happy_login_required
def test_request(request):

    logger.warn('test_request')
    logger.error('test_request !!!!!')

    headers={}
    for k,v in request.META.items():
        if k.startswith("HTTP_"):
            headers[k]=v

    resultado = {
        "headers": headers,
        "get": request.GET.dict(),
        "post": request.POST.dict(),
        "path": request.path,
        "body": str(request.body),
        "happydonia": request.session.get("happydonia", ''),
    }
    if request.user:
        resultado["is_authenticated"] = request.user.is_authenticated
        resultado["username"] = request.user.username
        if not request.user.is_anonymous:
            resultado["fullname"] = request.user.get_full_name(),
            resultado["email"] = request.user.email

    logger.warn(json.dumps(resultado, indent=4))

    return JsonResponse(resultado)


@login_required(login_url="/accounts/login/")
def sfirma_nuevo(request):

    if request.method == 'POST':

        sFirma_form = SFirmaForm(request.POST, request.FILES)
        if sFirma_form.is_valid():

            print(sFirma_form.cleaned_data)

            # PDF en base64
            fichero_pdf = request.FILES['fichero_pdf']
            fichero_pdf_base64 = base64.b64encode(fichero_pdf.read())
            document_file_name = fichero_pdf.name

            # Fecha de expiración
            expiration_date = sFirma_form.cleaned_data.get("expiration_date",datetime.date.today())

    
            # Crea la firma
            json_solicitud = {
                "email_solicitante": sFirma_form.cleaned_data.get("email_solicitante",""),
                "document_title": sFirma_form.cleaned_data.get("document_title",""),
                "document_file_name": document_file_name,
#                "document_description": sFirma_form.cleaned_data.get("document_description",""),
                "signer_name": sFirma_form.cleaned_data.get("signer_name",""),
                "signer_email": sFirma_form.cleaned_data.get("signer_email",""),
#                "signer_nif": sFirma_form.cleaned_data.get("signer_nif",""),
#                "signer_mobile": sFirma_form.cleaned_data.get("signer_mobile",""),
                "expiration_date": expiration_date.strftime("%Y-%m-%d"),
#                "pdf_original": sFirma_form.cleaned_data.get("pdf_original",""),
#                "metadatos": sFirma_form.cleaned_data.get("metadatos",""),
                "aplicativo": "GFWEB",
#                "ref_aplicativo": sFirma_form.cleaned_data.get("ref_aplicativo",""),
                "pdf_original_base64": fichero_pdf_base64.decode("utf-8"),
#                "des_empresa_email": sFirma_form.cleaned_data.get("des_empresa_email",""),
#                "plantilla_email": sFirma_form.cleaned_data.get("plantilla_email",""),
#                "mensaje_email": sFirma_form.cleaned_data.get("mensaje_email",""),
#                "idioma_email": sFirma_form.cleaned_data.get("idioma_email",""),
#                "opentext_bo_type": sFirma_form.cleaned_data.get("opentext_bo_type",""),
#                "opentext_id_bo": sFirma_form.cleaned_data.get("opentext_id_bo",""),
#                "opentext_foldername": sFirma_form.cleaned_data.get("opentext_foldername",""),
#                "opentext_name": sFirma_form.cleaned_data.get("opentext_name",""),
#                "descargar_pdf_firmado": sFirma_form.cleaned_data.get("descargar_pdf_firmado",""),
#                "approver_email": sFirma_form.cleaned_data.get("approver_email",""),
#                "cc_email": sFirma_form.cleaned_data.get("cc_email",""),
            }

            logger.info(f'Crea solicitud: {json_solicitud["document_title"]} ')
            url = f'http://scloudw040:1100/sfirma/solicitud/0'
            r = requests.post(url, json=json_solicitud, headers={'Content-type': 'application/json'})
            logger.info(r.text)            

            return redirect('sfirma_consulta')
    
    else:

        initial = {
            'email_solicitante': 'alfonsogil.degea@grupofuertes.com',
        }
        sFirma_form = SFirmaForm(initial=initial)

    context = {
        'happyuser': json.loads(request.session.get('happyuser', '{}')),
        'form': sFirma_form,
    }
    

    html_template = loader.get_template('pages/sfirma_nuevo.html')
    return HttpResponse(html_template.render(context, request))



@login_required(login_url="/accounts/login/")
def sfirma_consulta(request):

    context = {
        "happyuser": json.loads(request.session.get("happyuser", "{}"))
    }

    # Recupera las solicitudes de firma 
    datos = requests.get(f"http://scloudw040:1100/sfirma/solicitudes/where/aplicativo='GFWEB'")
    if datos.status_code != 200:
        return HttpResponse(f'Error al obtener los datos')
    else:
        context['datos'] = datos.json()

    html_template = loader.get_template('pages/sfirma_consulta.html')
    return HttpResponse(html_template.render(context, request))    


@login_required(login_url="/accounts/login/")
def sfirma_descarga_pdf(request, doc_id, status):

    try:
        
        match status:
            case 'ENDED':
                PDF_base64_json = requests.get(f'http://scloudw040:1100/sfirma/docuten/{doc_id}/firmado').json()
                PDF_base64 = PDF_base64_json['data']['signed']
            case _:
                PDF_base64_json = requests.get(f'http://scloudw040:1100/sfirma/docuten/{doc_id}/original').json()
                PDF_base64 = PDF_base64_json['data']['original']
        
    except Exception as e:
        logger.error('Error en PDF_Original', exc_info=True)
        msg = 'EL DOCUMENTO '+str(doc_id)+' NO SE PUEDE DESCARGAR ('+str(e)+')'
        logger.error(msg)
        raise Http404

    PDF_base64_bytes = str(PDF_base64).encode('utf-8')
    pdf_content = base64.decodebytes(PDF_base64_bytes)
    response = HttpResponse(pdf_content, content_type="application/pdf")
    response['Content-Disposition'] = f'inline; filename={doc_id}_{status}.pdf'
    return response

