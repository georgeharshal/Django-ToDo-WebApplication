# Generated by Django 5.0.1 on 2024-02-01 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TaskDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EmployeeName', models.CharField(blank=True, max_length=100, null=True)),
                ('Task', models.CharField(blank=True, max_length=100, null=True)),
                ('TaskDescription', models.TextField(blank=True, max_length=100, null=True)),
                ('DeadLine', models.DateField(blank=True, null=True)),
                ('Status', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
