from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from django.conf import settings
from django.contrib.auth import views as auth_views
from . import views 
from rest_framework_swagger.views import get_swagger_view
from rest_framework.documentation import include_docs_urls




# router = DefaultRouter()
# # router.register(r'list',views..as_view())
# # router.register(r'post',views.PostListCreate.as_view())
# router.register(r'gen',views.ApiGenerics.as_view())

schema_view = get_swagger_view(title='Post API')

# app_name = 'core'
urlpatterns = [
   # path('',views.home, name='home'),
    path('mail',views.sendinblue,name='mail'),


    path('list/',views.PostListCreate.as_view(),name="list"),
    path('post/',views.PostListCreate.as_view(),name="post"),


    path('detail/<int:pk>/',views.PostDetail.as_view(),name="detail"),
    path('create-user/',views.CreateUser.as_view(),name='create-user'),



    path('api/token',obtain_auth_token,name='token'),
    

    path('create/',views.ApiGenerics.as_view(),name='create'),
    path('retrieve/<int:pk>/',views.ApiGenericsret.as_view(),name='retrieve'),
    path('update/<int:pk>/',views.ApiGenericsupd.as_view(),name='update'),
    path('destroy/<int:pk>/',views.ApiGenericsdes.as_view(),name='destroy'),
    

    path('create-profile',views.ProfileCreateView.as_view(),name='profile'),
    path('profile/<int:pk>',views.ProfileView.as_view(),name='profile'),

    path('<int:year>/<int:month>/<int:day>/<slug:post>/',views.post_detail,name='detail-post'),
    path('list-post',views.postlist,name='list-post'),
    

    path('password-change',auth_views.PasswordChangeView.as_view(),name='password-change'),
    path('password-change-done',auth_views.PasswordChangeDoneView.as_view(),name='password-change-done')

]



# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)