__author__ = 'edx'

from django.conf.urls import patterns, url
from .views import Perfil, ModificarPerfil, ChangepasswordForm
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',
                        #url(r'^login/$',Login.as_view(),name='login'),

                        url(r'^modificar-perfil/$', login_required(ModificarPerfil.as_view()), name='modificar_perfil'),
                        url(r'^perfil/(?P<user_name>[-\w]+)/$', login_required(Perfil.as_view()), name='perfil'),
                        url(r'^cambiar-clave/$', login_required(ChangepasswordForm.as_view()), name='actualizar_clave'),
                       )
