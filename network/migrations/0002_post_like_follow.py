# Generated by Django 4.1.3 on 2023-10-16 07:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userPosted', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postLiked', models.ManyToManyField(related_name='postsLiked', to='network.post')),
                ('userLiking', models.ManyToManyField(related_name='usersLiking', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userFollowed', models.ManyToManyField(related_name='usersFollowed', to=settings.AUTH_USER_MODEL)),
                ('userFollowing', models.ManyToManyField(related_name='usersFollowing', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
