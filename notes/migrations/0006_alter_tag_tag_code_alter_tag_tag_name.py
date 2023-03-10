# Generated by Django 4.1.5 on 2023-01-21 12:17

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0005_alter_tag_tag_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='tag_code',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='タグUUID'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='tag_name',
            field=models.CharField(blank=True, max_length=30, unique=True, verbose_name='タグ名称'),
        ),
    ]
