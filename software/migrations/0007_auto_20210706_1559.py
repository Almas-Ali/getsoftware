# Generated by Django 3.2.1 on 2021-07-06 09:59

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('software', '0006_software_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catagory',
            name='short_dsc',
            field=ckeditor.fields.RichTextField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='image',
            name='short_dsc',
            field=ckeditor.fields.RichTextField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='software',
            name='dsc',
            field=ckeditor.fields.RichTextField(default='', max_length=10000),
        ),
        migrations.AlterField(
            model_name='software',
            name='short_dsc',
            field=ckeditor.fields.RichTextField(default='', max_length=500),
        ),
    ]
