from rest_framework import serializers

from .models import RSSFeeds, Subscription, User


class SubscriptionSerializer(serializers.Serializer):
    url = serializers.URLField(write_only=True)

    def create(self, validated_data):
        user = User.objects.get(email=self.context['request'].user.email)
        rssfeed, _ = RSSFeeds.objects.get_or_create(url=validated_data['url'])
        return Subscription.objects.create(user_id=user.id, rssfeed_id=rssfeed.id)
