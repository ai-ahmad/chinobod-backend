# Generated by Django 4.2.10 on 2024-06-26 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='adminsuser',
            name='type',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]