# Generated by Django 4.2 on 2023-04-04 11:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bloghere', '0002_post_thumbnail_alter_post_author_alter_post_slug_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='timeStamp',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 4, 4, 16, 42, 21, 564744), null=True),
        ),
    ]
