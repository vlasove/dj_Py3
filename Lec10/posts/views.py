from django.views.generic import (
    ListView,
    UpdateView,
    DeleteView,
    DetailView,
    CreateView,
)

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied

from django.urls import reverse_lazy

from .models import Post 

class PostListView(LoginRequiredMixin, ListView):
    model = Post 
    template_name = 'post_list.html'
    context_object_name = 'post_list'
    login_url = 'login'


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post 
    template_name = 'post_edit.html'
    fields = ('title', 'body')
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object() # Возвращает объект для данного view
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)



class PostDetailView(LoginRequiredMixin,DetailView):
    model = Post 
    template_name = 'post_detail.html'
    context_object_name = 'post'
    login_url = 'login'

class PostDeleteView(LoginRequiredMixin,DeleteView):
    model = Post 
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')
    context_object_name = 'post'
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object() # Возвращает объект для данного view
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post 
    template_name = 'post_new.html'
    fields = ('title', 'body')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user 
        return super().form_valid(form)