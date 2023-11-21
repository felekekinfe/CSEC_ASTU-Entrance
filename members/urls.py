from django.urls import path
from .views import MemberLoginView,logincheck,EditMemberProfile

urlpatterns = [
    path('login/',MemberLoginView.as_view(),name='login'),
     path('login1/',logincheck,name='login1'),
     path('edit_profile/<int:pk>',EditMemberProfile.as_view(),name='edit')
    
]
