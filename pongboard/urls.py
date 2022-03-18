"""pongboard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from leaderboard.views import home_page, all_matches, add_player, add_match, view_player

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', view=home_page, name='home'),
    url(r'accounts/', include('django.contrib.auth.urls')),
    url(r'matches/', view=all_matches, name='all_matches'),
    url(r'addmatch/', view=add_match, name='add_match'),
    url(r'addplayer/', view=add_player, name='add_player'),
    url(r'^player/(?P<pk>[0-9]+)', view=view_player, name='view_player'),
]
urlpatterns += staticfiles_urlpatterns()