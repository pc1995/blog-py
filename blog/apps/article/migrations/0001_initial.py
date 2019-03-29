# Generated by Django 2.1.4 on 2019-03-24 19:19

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, help_text='文章标题', max_length=100, verbose_name='文章标题')),
                ('img_src', models.CharField(blank=True, help_text='文章图片', max_length=300, null=True, verbose_name='文章图片')),
                ('content', models.TextField(default='', help_text='文章内容', verbose_name='文章内容')),
                ('markdown', models.TextField(default='', help_text='文章Markdown内容', verbose_name='文章Markdown内容')),
                ('desc', models.CharField(blank=True, help_text='文章简介', max_length=500, null=True, verbose_name='文章简介')),
                ('thumbs_up_count', models.IntegerField(blank=True, default=10, help_text='点赞人数', null=True, verbose_name='点赞人数')),
                ('share_count', models.IntegerField(blank=True, default=10, help_text='分享次数', null=True, verbose_name='分享次数')),
                ('look_count', models.IntegerField(blank=True, default=10, help_text='已看人数', null=True, verbose_name='已看人数')),
                ('comment_count', models.IntegerField(blank=True, default=10, help_text='评论条数', null=True, verbose_name='评论条数')),
                ('is_hot', models.IntegerField(blank=True, default=0, help_text='是否热门', null=True, verbose_name='是否热门')),
                ('category_type', models.CharField(blank=True, help_text='文章分类', max_length=100, null=True, verbose_name='文章分类')),
                ('add_time', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True, verbose_name='更新时间')),
                ('article_type', models.IntegerField(choices=[(1, '技术'), (2, '随记')], default=1, help_text='文章类型', verbose_name='文章类型')),
                ('original', models.BooleanField(default=True, help_text='是否原创', verbose_name='是否原创')),
            ],
            options={
                'verbose_name': '博客文章',
                'verbose_name_plural': '博客文章',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, help_text='分类名称', max_length=20, null=True, verbose_name='分类名称')),
                ('add_time', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True, verbose_name='创建时间')),
                ('category_type', models.IntegerField(choices=[(1, '一级类目'), (2, '二级类目'), (3, '三级类目')], help_text='类目级别', verbose_name='类目级别')),
                ('parent_category', models.ForeignKey(blank=True, help_text='父目录', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_category', to='article.Category', verbose_name='父类目级别')),
            ],
            options={
                'verbose_name': '分类',
                'verbose_name_plural': '分类',
            },
        ),
    ]
