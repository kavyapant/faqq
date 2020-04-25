# Generated by Django 3.0.5 on 2020-04-25 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0018_auto_20200425_0740'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.TextField(max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='question',
            name='subcategory',
            field=models.TextField(blank=True, choices=[('Web Development', 'Web Development')], null=True),
        ),
    ]
