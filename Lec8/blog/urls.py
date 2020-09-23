from django.urls import path 
from .views import BlogListView , BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView

urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    #Read
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail') ,
    #Creation
    path('post/new/', BlogCreateView.as_view(), name='post_new'),
    #Update
    path('post/<int:pk>/edit/', BlogUpdateView.as_view(), name='post_edit'),
    #Delete
    path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name='post_delete'),
]

"""
    post/12/ ===> pk = 12
"""