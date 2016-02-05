import datetime
from django.test import TestCase
from django.utils import timezone
from .models import Poll


class PollMethodTest(TestCase):
    def test_was_published_recently_with_future_poll(self):
        """Poll.was_published_recently() should return False for polls whose
        publication_date is in the future."""

        time = timezone.now() + datetime.timedelta(days=30)
        future_poll = Poll(publication_date=time)
        self.assertEqual(future_poll.was_published_recently(), False)

    def test_was_published_recently_with_old_poll(self):
        """Poll.was_published_recently() should return False for polls whose
        publication_date is older than 1 day."""

        time = timezone.now() - datetime.timedelta(days=2)
        old_poll = Poll(publication_date=time)
        self.assertEqual(old_poll.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        """Poll.was_published_recently() should return True for polls whose
        publication_date is within the last day."""

        time = timezone.now() - datetime.timedelta(hours=23)
        recent_poll = Poll(publication_date=time)
        self.assertEqual(recent_poll.was_published_recently(), True)
