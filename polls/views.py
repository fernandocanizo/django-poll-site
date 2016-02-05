from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.views import generic
from django.db.models import F
from .models import Poll, Choice
from poll_site.settings import LATEST_POLLS


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_polls_list'

    def get_queryset(self):
        """Returns last published polls"""
        return Poll.objects.order_by('-publication_date')[:LATEST_POLLS]


class DetailView(generic.DetailView):
    model = Poll
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Poll
    template_name = 'polls/results.html'


def show_polls_from(request, year, month=None, day=None):
    return HttpResponse(
        """Show polls from a specific date. Received:
        year: {}
        month: {}
        day: {}
        """.format(year, month, day))


def ajax_vote(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = poll.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # redisplay poll voting form
        context = {
            'poll': poll,
            'error_message': "You didn't select a choice",
            }
        return render(
            request,
            'polls/detail.html',
            context,
            )
    else:
        selected_choice.votes = F('votes') + 1
        selected_choice.save()
        # always return an HttpResponseRedirect after successfully dealing with
        # POST data. This prevents data from being posted twice if a user hits
        # the back button
        poll.refresh_from_db()
        return HttpResponseRedirect(reverse(
            'polls:results',
            args=(poll.id,)))
