# Generated by Django 4.0.5 on 2022-06-06 02:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0003_remove_doctor_user_doc_people_user_doc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='user_doc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.doctor'),
        ),
    ]