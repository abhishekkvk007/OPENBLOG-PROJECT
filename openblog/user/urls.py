from django.urls import path
from .views import *

urlpatterns=[
    path('userhome/',UserHome.as_view(),name="uhome"),
    path('profile/',ProfileView.as_view(),name="profile"),
    path('addprofile/',AddProfile.as_view(),name="addprofile"),
    path('cpassword/',CPassView.as_view(),name="cpassword"),
]