# Generated by Django 4.1.1 on 2022-09-29 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsdashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='record_delete',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField(blank=True)),
            ],
        ),
    ]
