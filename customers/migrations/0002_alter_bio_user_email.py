# Generated by Django 4.0.5 on 2022-06-06 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bio',
            name='user_email',
            field=models.EmailField(max_length=200),
        ),
    ]