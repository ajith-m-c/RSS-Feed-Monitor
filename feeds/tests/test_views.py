from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from .baseclass import TestBaseClass


class TestSubscriptionAPI(TestBaseClass, APITestCase):

    @classmethod
    def setUpClass(cls):
        super(TestSubscriptionAPI, cls).setUpClass()
        cls.url = reverse('subscribe-list')

    def setUp(self):
        self.set_authentication(user=self.user)

    def set_authentication(self, user):
        self.client.force_authenticate(user)

    def tearDown(self, *args, **kwargs):
        self.client.force_authenticate(user=None)
        super().tearDown(*args, **kwargs)

    def test_subscription_list_api(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_subscription_api(self):
        payload = {'url': 'https://www.testsite.rss/'}
        response = self.client.post(self.url, data=payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_topten_subscription_list_api(self):
        user1 = self.create_user(email='user1@test.com')
        user2 = self.create_user(email='user2@test.com')
        self.create_subscription(user_id=user1.id, url='https://test1.rss/')
        self.create_subscription(user_id=user1.id, url='https://test2.rss/')
        self.create_subscription(user_id=user2.id, url='https://test2.rss/')
        url = reverse('subscribe-get-topten')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_subscribe_top10_api(self):
        user1 = self.create_user(email='user1@test.com')
        user2 = self.create_user(email='user2@test.com')
        self.create_subscription(user_id=user1.id, url='https://test1.rss/')
        self.create_subscription(user_id=user1.id, url='https://test2.rss/')
        self.create_subscription(user_id=user2.id, url='https://test2.rss/')
        url = reverse('subscribe-topten-subscription')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_subscription_api(self):
        url = reverse('subscribe-detail', args=[f"{self.subscription.id}"])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
