from django.contrib import admin
from django.urls import path

from .views import home_view
from articles.views import article_view, article_search_view, article_create_view
from accounts.views import login_view, logout_view, register_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home_view, name="home"),
    path("login/", login_view, name="login"),
    path("articles/", article_search_view, name="article-search"),
    path("articles/create/", article_create_view, name="article-create"),
    path("articles/<int:id>/", article_view, name="article-details"),
]
