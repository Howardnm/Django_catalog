from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'apps/app_catalog/home.html'
