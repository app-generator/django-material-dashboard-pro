import json
from django.contrib.auth import REDIRECT_FIELD_NAME
#from django.shortcuts import render, resolve_url
#from myapp.settings import cfg
#from myapp import settings
#from urllib.parse import urlparse
#import uuid

import functools

from django.shortcuts import redirect, render
from django.contrib import messages
import jwt

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Clave pública
#clave_publica_crt = r'C:\TRABAJO\Python\Django\material_jwt\pruebas\token_dev.crt'
#with open(clave_publica_crt) as f:
#    public_key = f.read()
#print(public_key)

public_key_postman = """
-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA6S7asUuzq5Q/3U9rbs+P
kDVIdjgmtgWreG5qWPsC9xXZKiMV1AiV9LXyqQsAYpCqEDM3XbfmZqGb48yLhb/X
qZaKgSYaC/h2DjM7lgrIQAp9902Rr8fUmLN2ivr5tnLxUUOnMOc2SQtr9dgzTONY
W5Zu3PwyvAWk5D6ueIUhLtYzpcB+etoNdL3Ir2746KIy/VUsDwAM7dhrqSK8U2xF
CGlau4ikOTtvzDownAMHMrfE7q1B6WZQDAQlBmxRQsyKln5DIsKv6xauNsHRgBAK
ctUxZG8M4QJIx3S6Aughd3RZC4Ca5Ae9fd8L8mlNYBCrQhOZ7dS0f4at4arlLcaj
twIDAQAB
-----END PUBLIC KEY-----
"""

from cryptography.x509 import load_pem_x509_certificate
from cryptography.hazmat.backends import default_backend

cert_happydonia = b"""
-----BEGIN CERTIFICATE-----
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
-----END CERTIFICATE-----
"""

cert_obj = load_pem_x509_certificate(cert_happydonia, default_backend())
public_key_happydonia = cert_obj.public_key()



def happy_login_required(
    function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url=None
):
    """
    Happydonia envia un JWT con el usuario
    """

    @functools.wraps(function)
    def wrapper(request, *args, **kwargs):
        #print(f"happy_login_required {request.user}")

        http_authorization = request.META.get("HTTP_AUTHORIZATION",'')
        token_jwt = request.GET.get("token_jwt",'')

        if 'Bearer ' in http_authorization or token_jwt:

            # Recupera el token
            if 'Bearer ' in http_authorization:
                token = http_authorization.replace('Bearer ','')
            else:
                token = token_jwt
            print(f"token {token}")

            # Decodifica el token -> recupera payload
            if 'Postman' in request.META.get("HTTP_USER_AGENT",''):
                decoded = jwt.decode(token, public_key_postman, algorithms=['RS256'], options={"verify_signature": True})
            else:
                decoded = jwt.decode(token, public_key_happydonia, algorithms=['RS256'], options={"verify_signature": False})
            print(decoded)

            # Comprueba si el happyuser ya está logueado
            happyuser = json.loads(request.session.get("happyuser", "{}"))
            if happyuser:
                if decoded['external_id'] == happyuser['usuario']:
                    return function(request,*args, **kwargs)

            # Cambia al usuario "happyuser"
            user = authenticate(request=request, username="happyuser", password="contraseña")
            if user:

                # Loggea con happyuser
                login(request, user)

                # Guarda los datos del payload en la session
                happyuser = {
                    'usuario': decoded['external_id'],
                    'nombre': decoded['username'],
                    'email': decoded['identifier'],
                }
                request.session["happydonia"] = json.dumps(decoded)
                request.session["happyuser"] = json.dumps(happyuser)

        else:
            if request.user.is_authenticated:
                happyuser = {
                    'usuario': request.user.username,
                    'nombre': request.user.get_full_name(),
                    'email': request.user.email
                }
                request.session["happyuser"] = json.dumps(happyuser)

        return function(request,*args, **kwargs)
            
    
    return wrapper

