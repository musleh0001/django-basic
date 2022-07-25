from django.shortcuts import render

from articles.models import Article


def home_view(request):
    context = {"articles": Article.objects.all()}
    return render(request, "home.html", context)
