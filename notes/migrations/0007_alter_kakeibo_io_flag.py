# Generated by Django 4.1.5 on 2023-01-22 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0006_alter_tag_tag_code_alter_tag_tag_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kakeibo',
            name='io_flag',
            field=models.CharField(choices=[('0', '出金'), ('1', '入金')], max_length=1, verbose_name='入払区分'),
        ),
    ]
