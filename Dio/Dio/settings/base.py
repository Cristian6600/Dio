"""
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
from unipath import Path
BASE_DIR = Path(__file__).ancestor(3)



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'u5h4i@k8zl$24!dhx)=22c)ue@5y%$pg)hpr&@#*wt6rcjx0)f'



# Application definition

INSTALLED_APPS = [
    # 'captcha',
    # 'material',
    # 'material.admin',
    # 'simple_history',
    'import_export',

    # 'grappelli',
    # 'rest_framework',
    # 'rest_framework.authtoken',
    # 'related_admin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    #apps
    'applications.base_cliente',
    'applications.cliente',
    'applications.datos_g',
    'applications.guia',
    'applications.fisico',   
    'applications.courrier', 
    'applications.users',
    'applications.home',
    'applications.call',
    'applications.ruta',

]
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',  # <-- And here
    ],
}
SILENCED_SYSTEM_CHECKS = ['captcha.recaptcha_test_key_error']

MATERIAL_ADMIN_SITE  = {
    'HEADER' :   ( 'Bienvenido a Dio' ),   # Encabezado del sitio de administración 
    'TITLE' :    ( 'Bienvenido a Dio' ),   # Título del sitio de administración 
    'FAVICON' :   'img/Logo.jpg' ,   # Favicon del sitio de administración (se debe especificar la ruta a la estática) 
    'MAIN_BG_COLOR' :   'black ' ,   # Color principal del sitio de administración, se debe especificar el color css 
    'MAIN_HOVER_COLOR' :   '#115559' ,   # 
    # Color de desplazamiento principal del sitio de administración,El color css debe especificarse 'PROFILE_PICTURE' :  'ruta / a / imagen' ,   # Imagen de perfil del sitio de administración (se debe especificar la ruta a la estática) 
    'PROFILE_BG' :   'img/7q.gif' ,   # Fondo del perfil del sitio de administración (se debe especificar la ruta a la estática) 
    # 'LOGIN_LOGO' :   'img/Logo.jpg'  ,  # Logotipo del sitio de administración en la página de inicio de sesión (se debe especificar la ruta a la estática) 
    'LOGOUT_BG' :   'img/2q.gif'  ,   # Fondo del sitio de administración en las páginas de inicio / cierre de sesión (la ruta a la estática debe ser especificado) 
    'SHOW_THEMES' :   True ,   # Mostrar el botón de temas de administrador predeterminado 
    # 'TRAY_REVERSE' : Verdadero ,  # Ocultar las herramientas de objeto y la línea de envío adicional de forma predeterminada 
    # 'NAVBAR_REVERSE' : Verdadero ,   # Ocultar la barra de navegación lateral de forma predeterminada 
    # 'SHOW_COUNTS' : Verdadero , # Mostrar recuentos de instancias para cada modelo 
    # 'APP_ICONS' : {   # Establecer iconos para aplicaciones (minúsculas ), incluidas las aplicaciones de terceros, {'application_name': 'material_icon_name', ...} 
    #     'sites' : 'send' ,
    # },
    # 'MODEL_ICONS' : {   # Establecer iconos para modelos (minúsculas), incluidos modelos de terceros, {'model_name': 'material_icon_name', ...} 
    #     'site' : 'contact_mail' ,
    # }
}

GRAPPELLI_ADMIN_TITLE = 'Firstsource'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'simple_history.middleware.HistoryRequestMiddleware',
   
]

ROOT_URLCONF = 'Dio.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR.child('templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Dio.wsgi.application'


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

AUTH_USER_MODEL = 'users.User'

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'es-CO'

TIME_ZONE = 'America/Bogota'

USE_I18N = True

USE_L10N = True

USE_TZ = True

#Historial

SIMPLE_HISTORY_REVERT_DISABLED=True

MULTI_CAPTCHA_ADMIN  = {
     'motor' : 'recaptcha2' , 
}



