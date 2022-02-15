from django.contrib import admin

from feeds.models import RSSFeeds, Subscription, User


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email')


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'rssfeed')


class RSSFeedAdmin(admin.ModelAdmin):
    list_display = ('id', '__str__')


admin.site.register(User, UserAdmin)
admin.site.register(Subscription, SubscriptionAdmin)
admin.site.register(RSSFeeds, RSSFeedAdmin)
