# Generated by Django 4.2.5 on 2023-10-12 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0014_alter_comment_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=70),
        ),
    ]
