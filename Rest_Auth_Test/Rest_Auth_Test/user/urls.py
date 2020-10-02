from django.urls import include, path, re_path
from .views import SignUp, ForgotPassword, user_detail, user_list

urlpatterns = [
    path('signup/', SignUp.as_view(),
         name='sign_up'),
    path('forgot/password', ForgotPassword.as_view(),
         name='forgot_password'),
    path('api/user/list', user_list,
         name='user_list'),
    path('api/user/detail/<int:pk>/', user_detail,
         name='user_detail'),
]
