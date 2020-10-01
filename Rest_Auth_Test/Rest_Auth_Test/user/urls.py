from django.urls import include, path, re_path
from .views import get_post_users, UpdateUser, SignUp, ForgotPassword

urlpatterns = [
    path('get/post/user', get_post_users.as_view(),
         name='get_post_users'),
    path('update/user', UpdateUser.as_view(),
         name='update_user'),
    path('signup/', SignUp.as_view(),
         name='sign_up'),
    path('forgot/password', ForgotPassword.as_view(),
         name='forgot_password'),
]
