# Generated by Django 5.1 on 2024-08-10 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AudioAttachmet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('src', models.TextField()),
            ],
            options={
                'db_table': 'audio_attachments',
            },
        ),
        migrations.CreateModel(
            name='FileAttachment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=90)),
                ('extension', models.CharField(max_length=15)),
                ('size', models.FloatField()),
                ('src', models.TextField()),
                ('content_type', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'file_attachments',
            },
        ),
    ]
