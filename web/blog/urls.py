
from django.urls import path





from .views import ListBlog,DetailBlog,search


urlpatterns = [
    
    path('', ListBlog , name='list'),
    path ('blog/<slug>/', DetailBlog,  name = "detail"),
    path ('search/',search, name='search'),
]
