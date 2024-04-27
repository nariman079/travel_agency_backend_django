# Generated by Django 4.1.4 on 2024-04-27 19:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='img/')),
                ('title', models.CharField(max_length=60)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('img', models.ImageField(upload_to='img/')),
                ('tour_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='src.tour')),
            ],
        ),
        migrations.CreateModel(
            name='Attraction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('img_1', models.ImageField(upload_to='img/')),
                ('tour_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='src.tour')),
            ],
        ),
    ]
