from django.views.generic import TemplateView
from django.urls import reverse_lazy


class HomePageView(TemplateView):
    template_name = 'home.html'


class AboutPageView(TemplateView):  # new
    template_name = 'about.html'
