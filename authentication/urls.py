from django.conf.urls import url, include
from authentication.views import RegistrationAPIView, LoginAPIView, UserListViewSet

urlpatterns = [
    url(r'^users/$', UserListViewSet.as_view({'get': 'list'}), name='user_list'),  # ...auth/users/ (show users)
    url(r'^users/register/$', RegistrationAPIView.as_view(), name='register'),  # ...auth/users/register/ (create user)
    url(r'^users/login/$', LoginAPIView.as_view(), name='login'),  # ...auth/users/login/ (user login)
]
