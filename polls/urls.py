from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        r'^$',
        views.index,
        name='polls_index'),

    url(
        r'^(?P<poll_id>\d+)$',
        views.detail,
        name='polls_detail'),

    url(
        r'^year/(?P<year>\d{4})$',
        views.show_polls_from,
        name='polls_show_polls_from'),

    url(
        r'^year/(?P<year>\d{4})/month/(?P<month>\d{2})$',
        views.show_polls_from,
        name='polls_show_polls_from'),

    url(
        r'^year/(?P<year>\d{4})/month/(?P<month>\d{2})/day/(?P<day>\d{2})$',
        views.show_polls_from,
        name='polls_show_polls_from'),

    # AJAX
    url(
        r'^(?P<poll_id>\d+)/vote/choice/(?P<choice_id>\d+)$',
        views.ajax_vote,
        name="polls_ajax_vote"),
    ]
