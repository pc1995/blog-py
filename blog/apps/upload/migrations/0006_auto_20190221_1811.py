# Generated by Django 2.1.4 on 2019-02-21 18:11

from django.db import migrations, models
import upload.storage


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0005_auto_20190221_1810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='images',
            field=models.ImageField(max_length=500, storage=upload.storage.ImageStorage(), upload_to='article/'),
        ),
    ]