from django.urls import path
from news.api.views import (ArticleListCreateAPIView, ArticleDetailAPIView,
                            JournalistListCreateAPIView,JournalistDetailAPIView)

#from news.api.views import article_list_create_view_api, detail_api_view

urlpatterns = [
     path("articles/", ArticleListCreateAPIView.as_view(), name="article-list"),
     path("articles/<int:pk>", ArticleDetailAPIView.as_view(), name="detail-article"),
     path("Journalist/", JournalistListCreateAPIView.as_view(), name="Journalist-list"),
     path("Journalist/<int:pk>", JournalistDetailAPIView.as_view(), name="Journalist-list")
]
