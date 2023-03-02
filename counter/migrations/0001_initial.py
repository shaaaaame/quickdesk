# Generated by Django 4.1.7 on 2023-03-01 19:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('ticket_number', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('complete', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Counter',
            fields=[
                ('counter_number', models.SmallIntegerField(default=1, primary_key=True, serialize=False)),
                ('is_online', models.BooleanField(default=False)),
                ('cur_num', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='counter.ticket')),
            ],
        ),
    ]