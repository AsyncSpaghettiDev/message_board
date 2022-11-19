from django.views.generic import TemplateView


class PageHomeView(TemplateView):
    template_name = 'pages/home.html'


class PageAboutView(TemplateView):
    template_name = 'pages/about.html'
