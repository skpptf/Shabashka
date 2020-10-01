from django.urls import path
from django.conf import settings


from . import views

app_name ='main'
urlpatterns = [
    path('', views.index, name="index"),
    path('accounts/login/', views.ShaLogin.as_view(), name="login"),
    # path('single', views.single, name="single"),
    path('<str:page>/', views.other_page, name="other")

]