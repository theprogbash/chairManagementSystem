# Generated by Django 2.2.6 on 2019-10-31 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('individualworkapp', '0003_specialization'),
    ]

    operations = [
        migrations.AddField(
            model_name='specialization',
            name='specialization_code',
            field=models.IntegerField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='specialty',
            name='specialty_code',
            field=models.IntegerField(max_length=20, null=True),
        ),
    ]