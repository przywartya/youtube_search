from django.test import TestCase
from .models import Comment
# Create your tests here.

class ViedoViewTestCase(TestCase):
    def test_view(self):
        resp = self.client.get('')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('search_form' in resp.context)

class CommentFormTest(TestCase):
    def set_up(self):
        user = get_user_model().objects.create_user('tester')
        self.entry = Comment.objects.create(author=user, content="Some very special content",rating=3)
        self.assertContains(response, 'Some very special content')
        self.assertContains(response, 3)

    def two_comments(self):
        Comment.objects.create(content="...................", rating=5, author=self.user)
        Comment.objects.create(content="Hello Hello Hello", rating=1, author=self.user)
        response = self.client.get('/')
        self.assertContains(response, '...................')
        self.assertContains(response, 'Hello Hello Hello')
        self.assertContains(response, 1)

