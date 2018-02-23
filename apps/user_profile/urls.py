from django.conf.urls import url

from .views import user_profile, follow_user, profile_photo

urlpatterns = [
    url(r'^(?P<username>[\w.@+-]+)/$', user_profile, name='user_profile'),
    url(r'^(?P<username>[\w.@+-]+)/follow$', follow_user, name='follow_user'),
    url(r'^(?P<username>[\w.@+-]+)/profile_photo$', profile_photo, name="profile_photo"),
    ]