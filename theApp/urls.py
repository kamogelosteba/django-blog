
from django.urls import path
from .views import HomeView,ArticleView,AddPost,EditPost,DeletePost

urlpatterns = [
    #Here we are using the class based view and not the
    #path('',views.HomeView, name="home"),
    path('',HomeView.as_view(), name="home"),
    path('article/<int:pk>/edit', EditPost.as_view(), name="edit"),
    path('article/<int:pk>', ArticleView.as_view(), name="article-detail"),
    path('Add/', AddPost.as_view(), name="add-post"),
    path('article/<int:pk>/delete/', DeletePost.as_view(), name='delete'),


]

