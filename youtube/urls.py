from django.conf.urls import include, url
from django.contrib import admin
from .views import HomeSearchView, SearchResultsView, VideoCommentsListView

urlpatterns = [
    url(r'^$', HomeSearchView.as_view()),
    url(r'^results/(?P<query>.*)$', SearchResultsView.as_view(template_name="home.html")),
    url(r'^view/(?P<link>\w+)$', VideoCommentsListView.as_view(template_name="video_view.html")),
    url(r'^view/(?P<link>[\w-]+)$', VideoCommentsListView.as_view(template_name="video_view.html")),
    url(r'^accounts/profile/$', HomeSearchView.as_view()),
]
