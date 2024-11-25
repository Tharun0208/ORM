# Generated by Django 4.2.16 on 2024-11-25 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eid', models.CharField(help_text='Employee', max_length=20)),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('salary', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]