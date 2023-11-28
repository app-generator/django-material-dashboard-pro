import datetime
from django import forms
from django.forms import ValidationError

"""
        "email_solicitante":"alfonsogil.degea@grupofuertes.com",
        #"document_file_name" = 
        #"document_description" = 
        "signer_name":"Alfonso De Gea",
        "signer_email":"alfonsogil.degea@grupofuertes.com",
        #"signer_nif" = 
        #"signer_mobile" = 
        #"expiration_date" = 
        "pdf_original":r"\\grupofuertes.corp\grupofuertes\repositorio_gf\tmp\docuten\kairos.pdf", 
        #"metadatos" = 
        #"aplicativo": aplicativo
        #"ref_aplicativo" = 
        "pdf_original_base64" = 
        #"des_empresa_email" = 
        #"plantilla_email" = 
        #"mensaje_email" = 
        #"idioma_email" = 
        #"opentext_bo_type" = 
        #"opentext_id_bo" = 
        #"opentext_foldername" = 
        #"opentext_name" = 
        #"descargar_pdf_firmado" = 
        #"approver_email" = 
        #"cc_email" =     
"""        


class SFirmaForm(forms.Form):
    """
        "document_title":"Título del documento",
        "signer_name":"Alfonso De Gea",
        "signer_email":"alfonsogil.degea@grupofuertes.com",
        "pdf_original_base64" = 
        "email_solicitante":"alfonsogil.degea@grupofuertes.com",
    """    

    document_title = forms.CharField(widget=forms.TextInput(
        attrs={
            "placeholder": "Título del documento",
        }
    ))
    signer_name = forms.CharField(widget=forms.TextInput(
        attrs={
            "placeholder": "Nombre del firmante",
        }
    ))
    signer_email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            "placeholder": "Email del firmante",
        }
    ))
    expiration_date = forms.DateField(input_formats=['%d/%m/%Y'],
        widget=forms.DateInput(
            attrs={
                "placeholder": "Fecha de expiración",
            }
    ))
    email_solicitante = forms.EmailField(widget=forms.EmailInput(
        attrs={
            "placeholder": "Email del solicitante",
        }
    ))
    fichero_pdf = forms.FileField(required=False)

    def clean_expiration_date(self):
        expiration_date = self.cleaned_data['expiration_date']
        if expiration_date < datetime.date.today():
            raise ValidationError("La fecha de expiración no puede ser anterior a la fecha actual")
        return expiration_date


    def __init__(self, *args, **kwargs):
        super(SFirmaForm, self).__init__(*args, **kwargs)
        
        # Valores por defecto 
        self.fields['expiration_date'].initial=datetime.date.today()+datetime.timedelta(days=30) 
                                      
        if kwargs.get('initial', None):
            if kwargs['initial'].get('email_solicitante', None):
                email_solicitante = kwargs['initial'].pop('email_solicitante')
                self.fields['email_solicitante'].initial = email_solicitante
        
        




