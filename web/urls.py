from django.urls import path, include
from django.contrib.auth.views import LoginView
from . import views

#from .views import web_index

#app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', LoginView.as_view(template_name='web/login.html') , name='login'),
    path('map/', views.map, name='map'),
    path('rzd/', include('rzd.urls')),
]
