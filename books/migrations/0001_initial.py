# Generated by Django 4.2.10 on 2024-06-25 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('author', models.CharField(max_length=300)),
                ('pdf_url', models.CharField(max_length=300)),
                ('image_url', models.CharField(max_length=300)),
                ('type', models.CharField(max_length=300)),
            ],
        ),
    ]