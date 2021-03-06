# Generated by Django 2.0.1 on 2018-01-31 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ajax',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(blank=True, max_length=255)),
                ('search', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('telephone', models.IntegerField()),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
            ],
        ),
    ]
