# Generated by Django 4.1.3 on 2022-11-29 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0002_alter_services_text_alter_services_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feddback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('text', models.CharField(max_length=100)),
            ],
        ),
    ]
