from django.contrib import admin
from django.urls import path

from account import views as account_views
from chat import views as chat_views
from account import urls as account_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/login/', account_views.login),
    path('account/logout/', account_views.logout),
    path('chat/', chat_views.index),
    path('chat/<int:roomid>/', chat_views.room),
    path('chat/getmsg/', chat_views.getmsg),
    path('chat/putmsg/', chat_views.putmsg),
    path('chat/exitchat/', chat_views.exituser),
    path('chat/onlinelist/', chat_views.onlineuser),
    path('', chat_views.index),
]
