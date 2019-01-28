"""
high level support for doing this and that.
"""
from django.shortcuts import render
from .models import Article

# Create your views here.
def article_list(request):
    articles = Article.objects.all().order_by('date')
    #order_by lets you order items by a field of the table eg date
    return render(request, 'articles/article_list.html', {'articles':articles})