# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatPool',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('msg', models.CharField(max_length=1024)),
                ('roomname', models.ForeignKey(to='chat.ChatRoom',on_delete=False)),
                ('username', models.ForeignKey(to=settings.AUTH_USER_MODEL,on_delete=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
