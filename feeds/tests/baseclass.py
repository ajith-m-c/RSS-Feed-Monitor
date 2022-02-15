from feeds.models import RSSFeeds, Subscription, User


class TestBaseClass:

    @classmethod
    def setUpTestData(cls):
        cls.create_initial_values()

    @classmethod
    def create_initial_values(cls):
        cls.user = cls.create_user(email='tester@feeds.com')
        cls.rssfeed = cls.create_rssfeed(url='http://rss.cnn.com/rss/cnn_topstories.rss')
        cls.subscription = cls.create_subscription(cls.user.id, cls.rssfeed.id)

    @staticmethod
    def create_user(email, **kwargs):
        user = User.objects.create(email=email)
        for key, value in kwargs.items():
            setattr(user, key, value)
        user.save()
        return user

    @staticmethod
    def create_rssfeed(url):
        return RSSFeeds.objects.create(url=url)

    @staticmethod
    def create_subscription(user_id, rssfeed_id=None, url=None):
        if url:
            rssfeed, _ = RSSFeeds.objects.get_or_create(url=url)
            return Subscription.objects.create(user_id=user_id, rssfeed_id=rssfeed.id)
        else:
            return Subscription.objects.create(user_id=user_id, rssfeed_id=rssfeed_id)
