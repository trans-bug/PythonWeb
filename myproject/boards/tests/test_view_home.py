from django.test import TestCase

# Create your tests here.

from django.urls import resolve,reverse

from ..views import home
from ..models import Board




class HomeTests(TestCase):
    def setUp(self):
        self.board = Board.objects.create(name='Django', description='Django board.')
        url = reverse('home')
        self.response = self.client.get(url)
    def test_home_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
    def test_home_url_resolves_home_view(self):
        View=resolve('/')
        self.assertEquals(View.func,home)#mark,这儿可能出现问题
    def test_home_view_contains_link_to_topics_page(self):
        board_topics_url = reverse('board_topics', kwargs={'pk': self.board.pk})
        self.assertContains(self.response, 'href="{0}"'.format(board_topics_url))
        
