from django.urls import path
from .views import login,signup,logout_view
urlpatterns = [ 

    path('',signup,name='signup'),
    path('login/',login,name='login'),
    path('logout/',logout_view,name='logout'),
]