# Generated by Django 4.0.6 on 2022-07-11 08:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_title', models.CharField(max_length=50, verbose_name='게시물 제옥')),
                ('article_contents', models.TextField(max_length=500, verbose_name='게시물 내용')),
                ('article_image', models.ImageField(blank=True, upload_to='', verbose_name='이미지')),
                ('article_post_date', models.DateField(auto_now_add=True, verbose_name='게시 일자')),
                ('article_exposure_date', models.DateField(blank=True, verbose_name='게시 만료 일자')),
                ('article_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='작성자')),
            ],
        ),
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50, verbose_name='게시판 이름')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50, verbose_name='카테고리 이름')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_contents', models.TextField(max_length=100, verbose_name='내용')),
                ('comment_created_at', models.DateTimeField(auto_now_add=True, verbose_name='생성시간')),
                ('comment_updated_at', models.DateTimeField(auto_now=True, verbose_name='수정시간')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.article', verbose_name='게시글')),
                ('comment_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='사용자')),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote', models.BooleanField(verbose_name='투표여부')),
                ('vote_category', models.CharField(max_length=50, verbose_name='투표 종류')),
                ('vote_article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.article', verbose_name='투표한 게시글')),
                ('vote_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='투표한 유저')),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like', models.BooleanField(verbose_name='공감여부')),
                ('like_category', models.CharField(default='', max_length=50, verbose_name='공감종류')),
                ('like_article', models.ManyToManyField(related_name='article_likes', to='article.article')),
                ('like_comment', models.ManyToManyField(related_name='comment_likes', to='article.comment')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='article_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='article.category', verbose_name='카테고리 종류'),
        ),
        migrations.AddField(
            model_name='article',
            name='board',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.board', verbose_name='해당 게시판'),
        ),
    ]
