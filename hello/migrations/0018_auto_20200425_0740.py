# Generated by Django 3.0.5 on 2020-04-25 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0017_delete_industrytype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='subcategory',
            field=models.TextField(blank=True, null=True),
        ),
    ]