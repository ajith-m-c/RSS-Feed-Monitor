from django.db.models import Count
from django.forms import model_to_dict
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import RSSFeeds, Subscription, User
from .serializers import SubscriptionSerializer


class SubscriptionViewset(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    http_method_names = ['get', 'post', 'delete']

    def get_topten_urls(self):
        return Subscription.objects.values('rssfeed__url').annotate(url_count=Count('rssfeed__url')).order_by('-url_count')[:10]

    @action(detail=False, url_path='topten')
    def get_topten(self, request):
        return Response([i['rssfeed__url'] for i in self.get_topten_urls()])

    @action(detail=False, url_path='topten-subscription')
    def topten_subscription(self, request):
        data = list()
        for url_count in self.get_topten_urls():
            url = url_count['rssfeed__url']
            user = User.objects.get(email=self.request.user.email)
            rssfeed, _ = RSSFeeds.objects.get_or_create(url=url)
            sub, _ = Subscription.objects.get_or_create(user_id=user.id, rssfeed_id=rssfeed.id)
            data.append(model_to_dict(sub))
        return Response(data)
