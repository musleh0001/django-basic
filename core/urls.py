from django.contrib import admin
from django.urls import path

from .views import home_view
from articles.views import article_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home_view, name="home"),
    path("articles/<int:id>/", article_view, name="article-details"),
]
