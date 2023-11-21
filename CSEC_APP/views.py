from django.shortcuts import render,redirect
from .models import Members,Events
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView,CreateView,DeleteView,ListView,DetailView
from .forms import MembersRegistrationForm,AddEventForm
from django.urls import reverse_lazy

def home(request):
    members=Members.objects.all()
    events=Events.objects.all()
    form=MembersRegistrationForm()

    context={'members':members,'events':events,'form':form}


    # if request.user.is_staff:
    #     return render(request, '/home/tor/djproj/CSEC_ASTU/CSEC_APP/templates/admin_dashboard.html',context)

    
    return render(request, '/home/tor/djproj/CSEC_ASTU/CSEC_APP/templates/members_dashboard.html',context)


class AddMembersView(CreateView):
    model=Members
    template_name='/home/tor/djproj/CSEC_ASTU/CSEC_APP/templates/add_memeber.html'
    form_class=MembersRegistrationForm

# def addmember(request):
#     form=MembersRegistrationForm()

#     if request.method=='POST':
#         form=MembersRegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             redirect('home')
#     return render(request,'/home/tor/djproj/CSEC_ASTU/CSEC_APP/templates/add_memeber.html',{'form':form})

class AddEventsView(CreateView):
    model=Events
    template_name='/home/tor/djproj/CSEC_ASTU/CSEC_APP/templates/add_events.html'
    fields='__all__'
    success_url=reverse_lazy('home')

class DeleteMember(DeleteView):
    model=Members
    template_name='delete_member.html'
    success_url=reverse_lazy('home')

class EventView(ListView):
    model=Events
    template_name='events.html'
    #ordering=['-events_date']

class EventDetailView(DetailView):
    model=Events
    template_name='/home/tor/djproj/CSEC_ASTU/CSEC_APP/templates/event_detail.html'



