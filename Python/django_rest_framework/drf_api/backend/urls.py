from django.urls import path, include
# from .views import article_list, article_details
# from .views import ArticleList, ArticleDetails
from .views import ArticleViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('articles', ArticleViewSet, basename='articles')

urlpatterns = [
    # == routers for Viesets ==
    path('', include(router.urls))

    # == for CBVs ==
    # path('articles/', ArticleList.as_view()),
    # path('articles/<slug:slug>', ArticleDetails.as_view())

    # == for function-based views ==
    # path('articles/', article_list),
    # path('articles/<slug:slug>', article_details)
]