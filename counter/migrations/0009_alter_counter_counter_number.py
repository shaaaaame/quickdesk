# Generated by Django 4.1.7 on 2023-03-02 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('counter', '0008_alter_counter_counter_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='counter',
            name='counter_number',
            field=models.SmallIntegerField(primary_key=True, serialize=False),
        ),
    ]