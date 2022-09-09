from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views 

urlpatterns = [
   # path('',views.home, name='home'),
    path('k',views.ApiViewBlog.as_view(),name="k"),
    path('mail',views.sendinblue,name='mail'),
    path('api/token',obtain_auth_token,name='token')
]
