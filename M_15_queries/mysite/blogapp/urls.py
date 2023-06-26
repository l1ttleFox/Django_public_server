from django.urls import path


from .views import (
    ArticlesListView,
    ArticleCreateView,
)

app_name = "blogapp"

urlpatterns = [
    path("articles/", ArticlesListView.as_view(), name="articles_list"),
    path("articles/create/", ArticleCreateView.as_view(), name="create_article"),
]
