from django.shortcuts import render, redirect

# Create your views here.
from django.template import RequestContext
from django.views.generic import TemplateView
from django.shortcuts import render_to_response


class Home(TemplateView):
    def get(self, request, *args, **kwargs):
        return render_to_response(
            'home.html', locals(), context_instance=RequestContext(request)
        )

class Registro(TemplateView):
    def post(self, request, *args, **kwargs):
        request.session['password'] = request.POST['password']
        backend = request.session['partial_pipeline']['backend']
        url = '/complete/%s/' % backend
        return redirect(url)

    def get(self, request, *args, **kwargs):
        usuario = request.session['usuario']
        print(usuario)
        return render_to_response(
            'registro.html', locals(), context_instance=RequestContext(request)
        )