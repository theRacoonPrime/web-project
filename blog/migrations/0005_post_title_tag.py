# Generated by Django 4.0.4 on 2022-06-01 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_post_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default=' My awesome blog', max_length=255),
        ),
    ]
