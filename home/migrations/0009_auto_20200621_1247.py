# Generated by Django 3.0.7 on 2020-06-21 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20200621_1039'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='sub_total',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stock',
            name='total',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]