# Generated by Django 5.0.6 on 2024-06-12 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lead', '0002_lead_description_lead_email_lead_name_lead_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]