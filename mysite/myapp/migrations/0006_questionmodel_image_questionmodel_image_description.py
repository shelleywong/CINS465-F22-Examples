# Generated by Django 4.1 on 2022-10-11 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_answermodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionmodel',
            name='image',
            field=models.ImageField(max_length=144, null=True, upload_to='uploads/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='questionmodel',
            name='image_description',
            field=models.CharField(max_length=280, null=True),
        ),
    ]