from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Poll, Choice


def index(request):
    latest_polls = Poll.objects.order_by('-publication_date')[:5]
    context = {
        'latest_polls_list': latest_polls,
        }
    return render(request, 'polls/index.html', context)


def detail(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)

    context = {
        'poll': poll,
        }
    return render(
        request,
        'polls/detail.html',
        context)


def show_polls_from(request, year, month=None, day=None):
    return HttpResponse(
        """Show polls from a specific date. Received:
        year: {}
        month: {}
        day: {}
        """.format(year, month, day))


def ajax_vote(request, poll_id, choice_id):
    return HttpResponse(
        """This should return JSON
        poll_id: {}
        choice_id: {}
        """.format(poll_id, choice_id))
