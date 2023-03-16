from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView,LogoutView
from django.views.generic import TemplateView

class LoginPage(LoginRequiredMixin,LoginView):
    success_url = "/details"
    def get_context_data(self, **kwargs):
        context = super(LoginPage, self).get_context_data(**kwargs)
        context["succes_url"] = self.request.GET.get(next) or self.success_url
        return context
    
class DetailsPage(TemplateView):
    template_name = "details.html"

class IndexPage(TemplateView):
    template_name = "home.html"


class LogoutPage(LogoutView):
    pass
# Create your views here.
