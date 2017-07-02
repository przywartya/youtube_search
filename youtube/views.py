from django.shortcuts import render
from django.contrib import messages
from django.views.generic.edit import FormView
from django.views.generic import TemplateView, ListView, View
from django.http import HttpResponse


from .forms import SearchForm, CommentForm
from .models import Comment
from yt_api.search import youtube_search



class HomeSearchView(FormView):
    template_name = 'home.html'
    form_class = SearchForm
    success_url = '/results/'

    def form_valid(self, form):
        query = form.cleaned_data.get('query')
        self.success_url += query
        return super(HomeSearchView, self).form_valid(form)

class SearchResultsView(TemplateView):
        
    def get_context_data(self, **kwargs):
        query = kwargs['query']
        search_results = youtube_search(query, 25)
        if not search_results:
            messages.error(request, "We couldn't find appropriate video.")
    
        context = super(SearchResultsView, self).get_context_data(**kwargs)
        context['search_results'] = search_results
        return context

class VideoCommentsListView(FormView, TemplateView):
    form_class = CommentForm
    success_url = '/view/'

    def form_valid(self, form, **kwargs):
        if self.request.user.is_authenticated():
            form.instance.user = self.request.user
            link = kwargs['link']
            form.instance.video = link
            self.success_url += link
            return super(VideoCommentsListView, self).form_valid(form)
        else:
            self.success_url += kwargs['link']
            messages.error(self.request, "Please login to add a comment.")
            return super(VideoCommentsListView, self).form_invalid(form)

    def get_context_data(self, **kwargs):
        link = kwargs['link']
        self.success_url += link
        queryset = Comment.objects.filter(video=link).order_by("-timestamp")
        context = super(VideoCommentsListView, self).get_context_data(**kwargs)
        context['comments'] = queryset
        return context