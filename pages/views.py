from django.views.generic.base import TemplateView

class HomePageView(TemplateView):
    template_name = 'index.html'

class FormPageView(TemplateView):
    template_name = 'form.html'

class SalirPageView(TemplateView):
    template_name = 'salir.html'