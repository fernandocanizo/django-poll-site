from django.conf.urls import url
from . import views


app_name = 'polls'
urlpatterns = [
    url(
        r'^$',
        views.IndexView.as_view(),
        name='index'),

    url(
        r'^(?P<pk>\d+)$',
        views.DetailView.as_view(),
        name='detail'),

    url(
        r'^(?P<pk>\d+)/results$',
        views.ResultsView.as_view(),
        name='results'),

    url(
        r'^year/(?P<year>\d{4})$',
        views.show_polls_from,
        name='show_polls_from'),

    url(
        r'^year/(?P<year>\d{4})/month/(?P<month>\d{2})$',
        views.show_polls_from,
        name='show_polls_from'),

    url(
        r'^year/(?P<year>\d{4})/month/(?P<month>\d{2})/day/(?P<day>\d{2})$',
        views.show_polls_from,
        name='show_polls_from'),

    # AJAX
    url(
        r'^(?P<poll_id>\d+)/vote$',
        views.ajax_vote,
        name="ajax_vote"),
    ]
