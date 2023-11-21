from django.shortcuts import render,redirect
from django.contrib.auth.views import LoginView
from .forms import MemberLoginForm
from django.urls import reverse_lazy
from CSEC_APP.models import Members
from django.views.generic import UpdateView
from .forms import EditMemberProfile
# Create your views here.


class MemberLoginView(LoginView):
    form_class=MemberLoginForm
    template_name='/home/tor/djproj/CSEC_ASTU/members/templates/registration/login.html'
    success_url=reverse_lazy('home')

    def get_success_url(self):

        return self.success_url
def logincheck(request):
    member=Members.objects.all()

    if request.method=="POST":
        id=request.POST.get('id')
        username=request.get('username')
        password=request.POST.get('password')
        if Members.objects.filter(ID_Number=id,username=username,password=password):
            return redirect('login')
    else:
        return render(request, '/home/tor/djproj/CSEC_ASTU/members/templates/registration/login1.html')

class EditMemberView(UpdateView):
    model=Members
    template_name='registration/editmemberprofile.html'
    form_class=EditMemberProfile
