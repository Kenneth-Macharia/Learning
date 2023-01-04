import json

from django.shortcuts import render, get_object_or_404
from .models import Article
from .serializers import ArticleSerializer
from rest_framework.parsers import JSONParser
from django.http import JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from rest_framework.views import APIView

from rest_framework import mixins
from rest_framework import generics

from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


# Create your views here
# ModelViewset inherit from the generic APIView with implementation for various actions via
# mixins classes. Action provided include list, create, retrieve, update, partial_update and
# destroy
class ArticleViewSet(viewsets.ModelViewSet):
    lookup_field = 'slug'
    queryset = Article.objects.all()  # type: ignore
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # adds the request user as author when creating an article
        serializer.save(author=self.request.user)


# Generic Viewset, inheriting from Generic APIView provides get_object, get_queryset and
# other APIView behaviour but no actions by default. To use these, add mixin classes or
# explicitly define the actual implementation
# class ArticleViewSet(viewsets.GenericViewSet,
#                      mixins.ListModelMixin,
#                      mixins.CreateModelMixin,
#                      mixins.RetrieveModelMixin,
#                      mixins.UpdateModelMixin,
#                      mixins.DestroyModelMixin):
#
#     lookup_field = 'slug'
#     queryset = Article.objects.all()  # type: ignore
#     serializer_class = ArticleSerializer

# Viewsets abstract url configurations and allow fast modelling of the view and API
# interactions based on common conventions. Viewset classes are bound only on instantiation to
# HTTP method handlers when views are defined using router classes
# class ArticleViewSet(viewsets.ViewSet):
#     lookup_field = 'slug'
#
#     def list(self, request):
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def create(self, request):
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def retrieve(self, request, slug):
#         queryset = Article.objects.all()
#         article = get_object_or_404(queryset, slug=slug)
#         serializer = ArticleSerializer(article)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def update(self, request, slug):
#         # FIXME: Creates new instance
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, slug):
#         queryset = Article.objects.all()
#         article = get_object_or_404(queryset, slug=slug)
#         article.delete()
#         return Response(status=status.HTTP_200_OK)


# Generics class based views to further trim down the API implementations
# class ArticleList(generics.ListCreateAPIView):
#     queryset = Article.objects.all()  # type: ignore
#     serializer_class = ArticleSerializer


# class ArticleDetails(generics.RetrieveUpdateDestroyAPIView):
#     lookup_field = 'slug'
#     queryset = Article.objects.all()  # type: ignore
#     serializer_class = ArticleSerializer

# ===== CBVs with mixin classes that abstract the common CBV functionalities =====
# Generics class provides the CBV core functionality and the mixin classes the specific
# actions methods
# Also provides a form in the browser API client
# class ArticleList(mixins.CreateModelMixin,
#                   mixins.ListModelMixin,
#                   generics.GenericAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
#
#
# class ArticleDetails(mixins.RetrieveModelMixin,
#                      mixins.UpdateModelMixin,
#                      mixins.DestroyModelMixin,
#                      generics.GenericAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#     lookup_field = 'slug'
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)


# ==== Class based view (help re-use of common functionalities ensuring DRY code) =====
# class ArticleList(APIView):
#     def get(self, request):
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def post(self, request):
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class ArticleDetails(APIView):
#     def get_object(self, slug):
#         try:
#             return Article.objects.get(slug=slug)
#         except Article.DoesNotExist:
#             return Http404
#
#     def get(self, request, slug):
#         article = self.get_object(slug)
#         serializer = ArticleSerializer(article)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def put(self, request, slug):
#         article = self.get_object(slug)
#         serializer = ArticleSerializer(article, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, slug):
#         article = self.get_object(slug)
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# ====== API View decorators (allows faster implementation of function based views and
# auto creates a browseable API client in the browser) ======
# @api_view(['GET', 'POST'])
# def article_list(request):
#     if request.method == 'GET':
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     elif request.method == 'POST':
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def article_details(request, slug):
#     try:
#         article = Article.objects.get(slug=slug)
#     except Article.DoesNotExist:
#         return Response({"error": "Article not found"}, status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = ArticleSerializer(article)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     elif request.method == 'PUT':
#         serializer = ArticleSerializer(article, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         article.delete()
#         return Response({"success": "Article deleted"}, status=status.HTTP_200_OK)


# ====== Function based Views ======
# @csrf_exempt
# def article_list(request):
#     """ get all articles """
#     if request.method == 'GET':
#         articles = Article.objects.all()
#         # add many=True when serializing querysets i.e many instances
#         serializer = ArticleSerializer(articles, many=True)
#         return JsonResponse(serializer.data, safe=False, status=200)
#
# elif request.method == 'POST':
#     data = JSONParser().parse(request)
#     serializer = ArticleSerializer(data=data)
#     if serializer.is_valid():
#         serializer.save()
#         return JsonResponse(serializer.data, status=201)
#     return JsonResponse(serializer.errors, status=400)


# @csrf_exempt
# def article_details(request, slug):
#     try:
#         article = Article.objects.get(slug=slug)
#     except Article.DoesNotExist:
#         return JsonResponse({"error": "Article not found"}, status=404)
#
#     if request.method == 'GET':
#         serializer = ArticleSerializer(article)
#         return JsonResponse(serializer.data)
#
#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = ArticleSerializer(article, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=200)
#         return JsonResponse(serializer.errors, status=400)
#
#     elif request.method == 'DELETE':
#         article.delete()
#         return JsonResponse({"success": "Article not found"}, status=200)
