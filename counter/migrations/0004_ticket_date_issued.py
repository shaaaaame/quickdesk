# Generated by Django 4.1.7 on 2023-03-01 22:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('counter', '0003_counter_is_serving_alter_counter_is_online'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='date_issued',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]