# Generated by Django 2.1.4 on 2019-02-25 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0012_auto_20190225_1606'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogarticle',
            name='look_count',
            field=models.IntegerField(blank=True, default=10, help_text='已看人数', null=True, verbose_name='已看人数'),
        ),
    ]