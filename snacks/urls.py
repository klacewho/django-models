from django.views.generic import TemplateView
from django.views.generic.base import View

class BaseView(TemplateView):
  template_name = 'base.html'