# Generated by Django 2.2.1 on 2020-07-16 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0019_auto_20200716_2125'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='reply',
        ),
        migrations.AddField(
            model_name='reply',
            name='comment',
            field=models.ForeignKey(null=True, on_delete=True, to='user.Comment'),
        ),
    ]