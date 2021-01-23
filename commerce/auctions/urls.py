from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("list", views.list, name="list"),
    path("item/<str:item_id>", views.item, name="item"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("watchlist/<str:item_id>", views.watchlist, name="watchlist"),
    path("filter", views.filter, name="filter"),
]