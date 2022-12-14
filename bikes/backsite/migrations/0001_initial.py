# Generated by Django 4.1 on 2022-08-07 06:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='brand',
            fields=[
                ('brandId', models.AutoField(primary_key=True, serialize=False)),
                ('brand_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='bike_model',
            fields=[
                ('modelId', models.AutoField(primary_key=True, serialize=False)),
                ('model_name', models.CharField(max_length=30)),
                ('brandId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backsite.brand')),
            ],
        ),
        migrations.CreateModel(
            name='bike',
            fields=[
                ('bikeId', models.AutoField(primary_key=True, serialize=False)),
                ('bikename', models.CharField(max_length=30)),
                ('bike_picture', models.ImageField(null=True, upload_to='')),
                ('modelId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backsite.bike_model')),
            ],
        ),
    ]
