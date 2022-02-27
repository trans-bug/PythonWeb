from importlib.resources import path
from django.test import TestCase

# Create your tests here.

from django.urls import resolve,reverse

from django.contrib.auth.models import User
from ..views import new_topic
from ..models import Board,Topic,Post

from ..forms import NewTopicForm

        
class NewTopicTests(TestCase):
    def setUp(self):
        Board.objects.create(name='Django', description='Django board.')
        User.objects.create_user(username='john', email='john@doe.com', password='123')  # <- included this line here

        
    def test_new_topic_view_success_status_code(self):
        url = reverse('new_topic', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        
    def test_new_topic_view_not_found_status_code(self):
        url = reverse('new_topic', kwargs={'pk': 99})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)
        
    def test_new_topic_url_resolves_new_topic_view(self):
        view = resolve('/boards/1/new/')
        self.assertEquals(view.func, new_topic)
        
    def test_new_topic_view_contains_link_back_to_board_topics_view(self):
        new_topic_url = reverse('new_topic', kwargs={'pk': 1})
        board_topics_url = reverse('board_topics', kwargs={'pk': 1})
        response = self.client.get(new_topic_url)
        self.assertContains(response, 'href="{0}"'.format(board_topics_url))
    # setUp：创建一个测试中使用的 Board 实例
    # test_new_topic_view_success_status_cod：检查发给 view 的请求是否成功
    # test_new_topic_view_not_found_status_code：检查当 Board 不存在时 view 是否会抛出一个 404 的错误
    # test_new_topic_url_resolves_new_topic_view：检查是否正在使用正确的 view
    # test_new_topic_view_contains_link_back_to_board_topics_view：确保导航能回到 topics 的列表
    def test_csrf(self):
        url = reverse('new_topic', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertContains(response, 'csrfmiddlewaretoken')
    def test_new_topic_valid_post_data(self):
        url = reverse('new_topic', kwargs={'pk': 1})
        data = {
            'subject': 'Test title',
            'message': 'Lorem ipsum dolor sit amet'
        }
        response = self.client.post(url, data)
        self.assertTrue(Topic.objects.exists())
        self.assertTrue(Post.objects.exists())
    def test_new_topic_invalid_post_data(self):
        '''
        Invalid post data should not redirect
        The expected behavior is to show the form again with validation errors
        '''
        url = reverse('new_topic', kwargs={'pk': 1})
        response = self.client.post(url, data={})
        self.assertEquals(response.status_code, 200)
    def test_new_topic_invalid_post_data_empty_fields(self):
        '''
        Invalid post data should not redirect
        The expected behavior is to show the form again with validation errors
        '''
        url = reverse('new_topic', kwargs={'pk': 1})
        data = {
            'subject': '',
            'message': ''
        }
        response = self.client.post(url, data)
        self.assertEquals(response.status_code, 200)
        self.assertFalse(Topic.objects.exists())
        self.assertFalse(Post.objects.exists())
    # setUp：包含 User.objects.create_user 以创建用于测试的 User 实例。
    # test_csrf：由于 CSRF Token 是处理 Post 请求的基本部分，我们需要保证我们的 HTML 包含 token。
    # test_new_topic_valid_post_data：发送有效的数据并检查视图函数是否创建了 Topic 和 Post 实例。
    # test_new_topic_invalid_post_data：发送一个空字典来检查应用的行为。
    # test_new_topic_invalid_post_data_empty_fields：类似于上一个测试，但是这次我们发送一些数据。预期应用程序会验证并且拒绝空的 subject 和 message。
    def test_contains_form(self):  # <- new test
        url = reverse('new_topic', kwargs={'pk': 1})
        response = self.client.get(url)
        form = response.context.get('form')
        self.assertIsInstance(form, NewTopicForm)
    def test_new_topic_invalid_post_data(self):  # <- updated this one
        '''
        Invalid post data should not redirect
        The expected behavior is to show the form again with validation errors
        '''
        url = reverse('new_topic', kwargs={'pk': 1})
        response = self.client.post(url, {})
        form = response.context.get('form')
        self.assertEquals(response.status_code, 200)
        self.assertTrue(form.errors)
        
class LoginRequiredNewTopicTests(TestCase):
    def setUp(self):
        Board.objects.create(name='Django', description='Django board.')
        self.url = reverse('new_topic', kwargs={'pk': 1})
        self.response = self.client.get(self.url)
    def test_redirection(self):
        login_url = reverse('login')
        self.assertRedirects(self.response, '{login_url}?next={url}'.format(login_url=login_url, url=self.url))