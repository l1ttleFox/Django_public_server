from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from blogapp.models import Article


class ArticlesListView(ListView):
    """ CBV для отображения списка всех статей. """
    
    template_name = 'blogapp/articles_list.html'
    queryset = Article.objects.select_related("author", "category").prefetch_related("tags").defer("content").all()
    context_object_name = "articles"
    
    
class ArticleCreateView(CreateView):
    model = Article
    fields = "title", "content", "author", "category", "tags"
    success_url = reverse_lazy("blogapp:articles_list")
