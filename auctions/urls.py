from django.urls import path

from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("list", views.list, name="list"),
    path("item/<str:item_id>", views.item, name="item"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("watchlist/<str:item_id>", views.watchlist, name="watchlist"),
    path("filter/<str:filter>", views.filter, name="filter"),
    path("close_auction/<str:item_id>", views.close_auction, name="close_auction"),
] +static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)