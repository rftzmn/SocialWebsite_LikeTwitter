from django import forms
from django.forms.utils import ErrorList
from django.shortcuts import render, get_object_or_404
from django.views.generic import (
                DetailView,
                ListView,
                CreateView,
                UpdateView,
                DeleteView
                )
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Tweet
from .forms import TweetModelForm
from .mixins import FormUserNeededMixin
from django.db.models import Q
# Create your views here.

#Create
class TweetCreateView(FormUserNeededMixin, CreateView):
	# queryset = Tweet.objects.all()
	form_class = TweetModelForm
	template_name = "tweets/create_view.html"
	# success_url = reverse_lazy("tweet:detail")
	# login_url = '/admin/'

# Update
class TweetUpdateView(LoginRequiredMixin, UpdateView):
	queryset = Tweet.objects.all()
	form_class = TweetModelForm
	template_name = "tweets/update_view.html"
	# success_url = "/tweet/"

# Delete
class TweetDeleteView(LoginRequiredMixin, DeleteView):
    model = Tweet
    template_name = 'tweets/delete_confirm.html'
    success_url = reverse_lazy("tweet:list")


# Retrieve
class TweetDetailView(DetailView):
    queryset = Tweet.objects.all()
    template_name = "tweets/detail_view.html"

class TweetListView(ListView):
    # template_name = "tweets/list_view.html"
    # queryset = Tweet.objects.all()
    def get_queryset(self, *args, **kwargs):
        qs = Tweet.objects.all()
        print(self.request.GET)
        query = self.request.GET.get("q", None)
        if query is not None:
            qs = qs.filter(
                Q(content__icontains=query)|
                Q(user__username__icontains=query)|
                Q(timestamp__gte=query)
                )
        return qs

    def get_context_data(self,*args, **kwargs):
        context = super(TweetListView,self).get_context_data(*args, **kwargs)
        context['create_form']=TweetModelForm()
        context['create_url']=reverse_lazy("tweet:create")
        return context
