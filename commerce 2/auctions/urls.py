from unicodedata import name
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path('createList', views.create_view, name='createList'),
    path('<int:listing_id>/listing', views.listing, name='listing'),
    path('<int:user_id>/watchlist', views.watchlist, name='watchlist'),
    path('categories', views.categories, name='categories'),
    path('<str:category>/indexCats', views.indexCats, name='indexCats')
]
