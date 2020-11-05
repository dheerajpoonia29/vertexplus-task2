# Generated by Django 3.1.2 on 2020-11-04 20:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog', '0019_auto_20201104_2159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='user_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='author_points_to_user', to='app_blog.user'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='author_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_points_to_author', to='app_blog.author'),
        ),
    ]