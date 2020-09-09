from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("article_register",views.article_register,name="article_register"),
    path("Items",views.Items,name="Items"),
    path("category_page",views.category_page,name="category_page"),
    path("category/<str:link>",views.category,name="category"),
    path("details/<str:type>",views.details,name="details"),
    path("place_bid/<str:type>",views.place_bid,name="place_bid"),
    path("review/<str:type>",views.review,name="review"),
    path("watchlist",views.watchlist,name="watchlist"),
    path("add_watch/<str:type>",views.add_watch,name="add_watch"),
    path("remove/<str:type>",views.remove,name="remove"),
    path("close_bid/<str:watchitem>",views.close_bid,name="close_bid"),
    path("won",views.won,name="won")
    ]
