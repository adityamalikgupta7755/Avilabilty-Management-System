from django.urls import path
from cmsapp import views

urlpatterns = [
        path('', views.home, name='home'),
        path('expotcsvfile', views.expotcsvfile, name='expotcsvfile'),

]