from django.urls import include, path, re_path
from .views import SignUp, ForgotPassword, user_detail, user_list, user_add

urlpatterns = [
    path('api/signup/', SignUp.as_view(),
         name='sign_up'),
    path('api/forgot/password', ForgotPassword.as_view(),
         name='forgot_password'),
    path('api/user/add', user_add,
         name='user_post'),
    path('api/user/list', user_list,
         name='user_list'),
    path('api/user/detail/<int:pk>/', user_detail,
         name='user_detail'),
]
