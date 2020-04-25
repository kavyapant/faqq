# Generated by Django 3.0.5 on 2020-04-25 08:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0019_auto_20200425_0745'),
    ]

    operations = [
        migrations.DeleteModel(
            name='QuestionType',
        ),
        migrations.AlterField(
            model_name='question',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category', to='hello.Service'),
        ),
        migrations.AlterField(
            model_name='question',
            name='subcategory',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subcategory', to='hello.Service'),
        ),
    ]
