# Generated by Django 4.0.5 on 2022-07-17 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('FatherName', models.CharField(max_length=100)),
                ('Roll', models.CharField(max_length=10)),
                ('phn_no', models.CharField(max_length=12)),
            ],
        ),
    ]
