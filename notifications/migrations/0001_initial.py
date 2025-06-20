# Generated by Django 5.2.2 on 2025-06-11 18:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tickets', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='notifications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=255)),
                ('is_read', models.BooleanField(default=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user')),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tickets.tickets')),
            ],
        ),
    ]
