# Generated by Django 5.0.1 on 2024-02-01 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=100, null=True)),
                ('EmailId', models.CharField(blank=True, max_length=100, null=True)),
                ('Password', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]