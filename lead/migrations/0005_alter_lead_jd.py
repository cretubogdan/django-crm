# Generated by Django 3.2.3 on 2021-06-07 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lead', '0004_alter_lead_jd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='jd',
            field=models.FileField(blank=True, upload_to=''),
        ),
    ]
