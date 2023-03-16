from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView,LogoutView
from django.views.generic import TemplateView


#login view
class LoginPage(LoginView):
    success_url = "/details"
    def get_context_data(self, **kwargs):
        context = super(LoginPage, self).get_context_data(**kwargs)
        context["succes_url"] = self.request.GET.get(next) or self.success_url
        return context
    
class DetailsPage(LoginRequiredMixin,TemplateView):
    template_name = "details.html"

class IndexPage(TemplateView):
    template_name = "home.html"

#logout view
class LogoutPage(LogoutView):
    template_name = "details.html"
# Create your views here.
