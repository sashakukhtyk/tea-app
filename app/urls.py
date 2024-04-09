from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="Home"),
    path('signup', views.signup, name="signup"),
    path('login', views.user_login, name="login"),
    path('logout', views.user_logout, name="logout"),
    path('catalog/', views.catalog, name="Catalog"),
    path('collection/', views.collection, name="Collection"),
    path('ai/', views.ai, name="AI"),
]