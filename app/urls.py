from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="Home"),
    path('signup', views.signup, name="signup"),
    path('login', views.user_login, name="login"),
    path('logout', views.user_logout, name="logout"),
    path('catalog/', views.catalog, name="Catalog"),
    path('ai/', views.ai, name="AI"),
    path('product/<int:pk>', views.product, name="Product"),
    path('my_collection/', views.my_collection, name="my_collection"),
    path('<int:pk>/add', views.collection_add, name="collection_add"),
    path('<int:pk>/delete', views.collection_delete, name="collection_delete"),
]