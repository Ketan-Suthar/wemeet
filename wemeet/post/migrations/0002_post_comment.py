# Generated by Django 3.1 on 2020-08-16 13:21

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post_Comment',
            fields=[
                ('postCommentId', models.AutoField(primary_key=True, serialize=False)),
                ('commentDescription', models.CharField(max_length=1000)),
                ('createdOn', models.DateTimeField(default=datetime.datetime.now)),
                ('createdBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('postId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.post')),
            ],
        ),
    ]
