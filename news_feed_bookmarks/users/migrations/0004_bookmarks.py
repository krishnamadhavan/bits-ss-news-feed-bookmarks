# Generated by Django 3.2.15 on 2023-11-15 13:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0003_auto_20231115_1308'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookmarks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Created Date and Time', verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Updated Date and Time', verbose_name='Updated At')),
                ('content', models.IntegerField(verbose_name='Content Primary Key')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User Primary Key')),
            ],
            options={
                'verbose_name': 'Bookmark',
                'verbose_name_plural': 'Bookmarks',
                'db_table': 'bookmarks',
                'unique_together': {('content', 'user')},
            },
        ),
    ]
