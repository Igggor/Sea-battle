# Generated by Django 5.0 on 2024-01-06 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('battle', '0004_rename_awards_profile_json'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='json',
        ),
        migrations.CreateModel(
            name='Award',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=256)),
                ('user', models.ManyToManyField(to='battle.profile')),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='awards',
            field=models.ManyToManyField(to='battle.award'),
        ),
    ]
