# Generated by Django 3.1.2 on 2020-11-04 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog', '0018_auto_20201104_1511'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='blog_id',
        ),
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.IntegerField(default=0),
        ),
    ]