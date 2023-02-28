from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView, \
    PasswordResetView
from . import views

# from .views import web_index

# app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', LoginView.as_view(template_name='web/login.html'), name='login'),
    #    path('logout/', LogoutView.as_view(next_page="index"), name='logout'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('password_reset/', PasswordResetView.as_view(template_name='web/password_reset.html'), name='password_reset'),
    path('password_change/', PasswordChangeView.as_view(template_name='web/password_change.html'), name='password_change'),
    path('password_change/done/', PasswordChangeDoneView.as_view(template_name='web/password_changed.html'), name='password_change_done'),
    path('map/', views.map, name='map'),
    path('rzd/', include('rzd.urls')),
]
