# Generated by Django 4.1 on 2022-08-24 22:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_remove_posts_article_id_articles_post_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articles',
            name='post_id',
        ),
        migrations.AddField(
            model_name='posts',
            name='article_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.articles'),
        ),
    ]
