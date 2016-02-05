from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
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


def results(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    context = {
        'poll': poll,
        }
    return render(
        request,
        'polls/results.html',
        context)


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
        selected_choice.votes += 1
        selected_choice.save()
        # always return an HttpResponseRedirect after successfully dealing with
        # POST data. This prevents data from being posted twice if a user hits
        # the back button
        return HttpResponseRedirect(reverse(
            'polls:results',
            args=(poll.id,)))
