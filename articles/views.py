from django.shortcuts import render, redirect

from .models import Article


def article_view(request, id):
    article = Article.objects.get(id=id)
    context = {"article": article}
    return render(request, "articles/details.html", context)


def article_create_view(request):
    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]
        if title and content:
            new_article = Article.objects.create(title=title, content=content)
            return redirect("home", id=new_article.id)
    return render(request, "articles/create.html")


def article_search_view(request):
    query = request.GET["q"]
    qr = None
    context = {}
    if query.isdigit():
        qr = Article.objects.get(id=query)
    if qr:
        context["object"] = qr
    return render(request, "articles/search.html", context)
