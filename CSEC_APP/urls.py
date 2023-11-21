from django.urls import path
from .views import home,AddMembersView,AddEventsView,EventView,EventDetailView

urlpatterns = [
    path('',home,name='home'),
    path('add_member/',AddMembersView.as_view(),name='addmember'),
    path('add_event',AddEventsView.as_view(),name='addevent'),
     path('upcommingevent',EventView.as_view(),name='events'),
     path('eventdetail/<int:pk>',EventDetailView.as_view(),name='eventdetail')
]


