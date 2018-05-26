from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class ChatRoom(models.Model):
	roomname = models.CharField(max_length=8, unique=True)

	def __unicode__(self):
		return self.roomname


class RoomAccount(models.Model):
	username = models.ForeignKey(User,on_delete=False)
	roomname = models.ForeignKey(ChatRoom,on_delete=False)

	def __unicode__(self):
		return unicode(self.username)


class ChatPool(models.Model):
	roomname = models.ForeignKey(ChatRoom,on_delete=False)
	msg = models.CharField(max_length=1024)

	def __unicode__(self):
		return unicode(self.roomname)