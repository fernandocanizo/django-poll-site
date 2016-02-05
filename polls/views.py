from django.http import HttpResponse


def index(request):
    return HttpResponse("Latest polls...")


def detail(request, poll_id):
    return HttpResponse("Shows detailed view for poll {}".format(poll_id))


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
