# Generated by Django 4.1.7 on 2023-03-02 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('counter', '0007_alter_counter_cur_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='counter',
            name='counter_number',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
