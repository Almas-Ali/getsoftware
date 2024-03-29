# Generated by Django 3.2.1 on 2021-07-09 13:38

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('software', '0008_catagory_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='ip',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='comment',
            name='value',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='contact',
            name='ip',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='contact',
            name='value',
            field=models.TextField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='like',
            name='ip',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='newsletter',
            name='ip',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='userdetail',
            name='ip',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='newsletter',
            name='value',
            field=models.TextField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='value',
            field=models.TextField(default='', max_length=200),
        ),
        migrations.CreateModel(
            name='Download_Monitor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user', models.CharField(default='', max_length=30)),
                ('ip', models.CharField(default='', max_length=20)),
                ('value', models.TextField(default='', max_length=200)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('catagory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='software.catagory')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='software.software')),
            ],
        ),
    ]
