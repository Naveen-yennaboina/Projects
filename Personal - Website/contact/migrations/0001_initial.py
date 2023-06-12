# Generated by Django 3.1.5 on 2021-09-09 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('email', models.EmailField(max_length=300, unique=True)),
                ('contact_number', models.CharField(max_length=100, unique=True)),
                ('company_name', models.CharField(max_length=300)),
                ('description', models.TextField(max_length=5000, null=True)),
            ],
        ),
    ]
