
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('',include('CSEC_APP.urls')),
    path('member/',include('members.urls')),
   
]
