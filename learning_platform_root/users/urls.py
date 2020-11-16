from django.urls import path
from .views import profile, update_profile, community
from django.contrib.auth import views as auth_views

app_name = 'users'
urlpatterns = [
    path('profile/<int:user_id>', profile, name = 'profile'),
    path('login/', auth_views.LoginView.as_view(template_name = 'users/login.html'), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'users/logged_out.html'), name = 'logout'),
    path('update/', update_profile, name = 'update_profile'),
    path('community/', community, name = 'community'),
]