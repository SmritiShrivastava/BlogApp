# Generated by Django 3.1 on 2020-09-27 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentsmodel',
            name='created',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='blogmodel',
            name='blogContent',
            field=models.CharField(max_length=50000),
        ),
        migrations.AlterField(
            model_name='blogmodel',
            name='blogDescription',
            field=models.CharField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='blogmodel',
            name='blogTitle',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='blogmodel',
            name='location',
            field=models.CharField(blank=True, max_length=4000, null=True),
        ),
    ]
