# Generated by Django 3.2 on 2021-04-29 18:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mystore', '0008_auto_20210430_0006'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='authordb',
            unique_together=set(),
        ),
    ]