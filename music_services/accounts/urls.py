from django.urls import path, include
from music_services.accounts.views import UserRegisterView, UserLoginView, UserLogoutView, UserDetailsView, \
    UserEditView, UserDeleteView

urlpatterns = (
    path('login/', UserLoginView.as_view(), name='login user'),
    path('register/', UserRegisterView.as_view(), name='register user'),
    path('logout/', UserLogoutView.as_view(), name='logout user'),
    path('accounts/<int:pk>/', include([
        path('', UserDetailsView.as_view(), name='details user'),
        path('edit/', UserEditView.as_view(), name='edit user'),
        path('delete/', UserDeleteView.as_view(), name='delete user'),
    ])),
)
