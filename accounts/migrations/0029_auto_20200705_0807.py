# Generated by Django 2.2.13 on 2020-07-05 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0028_auto_20200705_0732'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='pass1',
            field=models.CharField(blank=True, default='zero', max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='pass2',
            field=models.CharField(blank=True, default='zero', max_length=300, null=True),
        ),
    ]
