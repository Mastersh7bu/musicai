# Generated by Django 4.2.2 on 2023-07-07 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AI_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_name', models.CharField(max_length=100)),
                ('model_name', models.CharField(max_length=250)),
            ],
            options={
                'verbose_name': 'AI Models',
                'verbose_name_plural': 'AI Models',
            },
        ),
    ]
