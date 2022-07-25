from django.shortcuts import render

from .models import Article


def article_view(request, id):
    article = Article.objects.get(id=id)
    context = {"article": article}
    return render(request, "articles/details.html", context)
