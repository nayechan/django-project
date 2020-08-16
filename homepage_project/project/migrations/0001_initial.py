# Generated by Django 3.0.8 on 2020-08-16 07:08

import datetime
from django.db import migrations, models
import markdownx.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projectName', models.CharField(max_length=100)),
                ('version', models.CharField(max_length=100)),
                ('pub_date', models.DateTimeField(default=datetime.datetime(2020, 8, 16, 16, 8, 39, 521300), editable=False)),
                ('context', markdownx.models.MarkdownxField(verbose_name='CONTENT')),
            ],
            options={
                'verbose_name': 'project',
                'verbose_name_plural': 'projects',
                'db_table': 'project_project',
                'ordering': ('-projectName', '-version', '-pub_date'),
            },
        ),
    ]