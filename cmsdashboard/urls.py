from django.urls import path
from . import views

urlpatterns = [
        path('', views.dashboardhome, name='homedashboard'),
        path('dashboardlogin', views.dashboardlogin, name='dashboardlogin'),
        path('dashboardlogout', views.dashboardlogout, name='dashboardlogout'),
        path('dashboardfileupload', views.dashboardfileupload, name='dashboardfileupload'),
        path('dashboardaddemp', views.dashboardaddemp, name='dashboardaddemp'),
        path('dashboardeditEmp/<empid>', views.dashboardeditEmp, name='dashboardeditEmp'),
        path('dashboardeditStatus/<statusid>', views.dashboardeditStatus, name='dashboardeditStatus'),
        # path('record_delete', views.record_delete, name='record_delete'),
]