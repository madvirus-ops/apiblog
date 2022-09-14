from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views 
app_name = 'core'
urlpatterns = [
   # path('',views.home, name='home'),
    path('create1',views.ApiViewBlog.as_view(),name="create1"),
    path('mail',views.sendinblue,name='mail'),
    path('api/token',obtain_auth_token,name='token'),
    path('create',views.ApiGenerics.as_view(),name='create'),
    path('update',views.ApiGenerics.as_view(),name='update'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',views.post_detail,name='detail'),
    path('list',views.postlist,name='list')
]
