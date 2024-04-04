# Generated by Django 5.0.3 on 2024-04-04 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='prd',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('prd_name', models.CharField(blank=True, max_length=100, null=True)),
                ('pri', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('prd_pic', models.ImageField(blank=True, null=True, upload_to='media/')),
            ],
        ),
        migrations.CreateModel(
            name='sulu',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('passsword', models.CharField(blank=True, max_length=100, null=True)),
                ('Email', models.EmailField(blank=True, max_length=254, null=True)),
                ('ph', models.CharField(blank=True, max_length=10, null=True)),
                ('add', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
