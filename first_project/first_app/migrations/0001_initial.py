# Generated by Django 4.1.6 on 2023-02-14 10:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('top_name', models.CharField(max_length=64, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='webpage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('url', models.URLField(unique=True)),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='first_app.topic')),
            ],
        ),
        migrations.CreateModel(
            name='Accessrecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='first_app.webpage')),
            ],
        ),
    ]
