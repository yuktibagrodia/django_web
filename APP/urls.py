from django.urls import path
from.import views
urlpatterns = [
    path('', views.home,name='login'),
    path('about/',views.about,name='profile'),
    ]