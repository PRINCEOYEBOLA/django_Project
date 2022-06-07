# Generated by Django 4.0.5 on 2022-06-06 02:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0002_alter_bio_user_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='user_doc',
        ),
        migrations.AddField(
            model_name='people',
            name='user_doc',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='customers.doctor'),
        ),
    ]