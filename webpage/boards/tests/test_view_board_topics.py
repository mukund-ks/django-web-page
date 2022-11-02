from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse,resolve
from ..views import board_topics
from ..models import Board

class BoardTopicsTests(TestCase):
    def setUP(self):
        self.board=Board.objects.create(name='Django', description='Django Board.')
    
    def test_board_topics_view_success_status_code(self):
        url=reverse('board_topics',kwargs={'pk':1})
        response=self.client.get(url)
        self.assertEquals(response.status_code,200)
    
    def test_board_topics_view_not_found_status_code(self):
        url=reverse('board_topics',kwargs={'pk':99})
        response=self.client.get(url)
        self.assertEquals(response.status_code,404)
    
    def test_board_topics_url_resolves_board_topics_view(self):
        view=resolve('/boards/1/')
        self.assertEquals(view.func,board_topics)
    
    def test_board_topics_view_contains_link_back_to_homepage(self):
        board_topics_url=reverse('board_topics',kwargs={'pk':1})
        response=self.client.get(board_topics_url)
        homepage_url=reverse('home')
        self.assertContains(response,'href="{0}'.format(homepage_url))