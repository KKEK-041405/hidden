from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView,FormView
from django.contrib.auth.models import User,Group
from .forms import StudentDetaislForm,GetStudentDetails,UpdateStdDetails
from django.contrib.auth import authenticate, login,logout
from .helper import CreateUser,convert
from .models import Document
#login view
class LoginPage(LoginView):
    success_url = "/details"

    def get_context_data(self, **kwargs):
        context = super(LoginPage, self).get_context_data(**kwargs)
        context["succes_url"] = self.request.GET.get(next) or self.success_url
        return context

    
class DetailsPage(LoginRequiredMixin,TemplateView):
    template_name = "details.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["Name"] = self.request.user.get_username()
        #print(self.request.user.get_username())
        return context
    
class UpdateDetails(TemplateView,FormView):
    def __init__(self, *args):
        super(UpdateDetails, self).__init__(*args)
    template_name = "UpdateDetails.html"
    form_class = UpdateStdDetails
        
    
class UploadDetails(FormView):
    template_name = "upload.html"
    form_class = GetStudentDetails
    success_url = "/details"
    def  form_valid(self, form):
        newdoc = Document(docfile = self.request.FILES.get("csvfile"))
        newdoc.save()
        convert()
        return super().form_valid(self)
    
        
class IndexPage(TemplateView):
    template_name = "home.html"

#logout view
class LogoutPage(LogoutView):
    template_name = "details.html"

#register Here
class RegisterPage(FormView,TemplateView):
    template_name = "Register.html"
    form_class = StudentDetaislForm
    success_url = "/details/"
    def form_valid(self, form):
        Cleaned_data = form.cleaned_data
        if CreateUser(Cleaned_data):
            user = authenticate(self.request,username=Cleaned_data["pinno"],password=Cleaned_data["password"])
            login(self.request,user)
            return super().form_valid(form)
        else:
            form.errors["pinno"] = "User already exists" 
            return super().form_invalid(form)
# Create your views here.
