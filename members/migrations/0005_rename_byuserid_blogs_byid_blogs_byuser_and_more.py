# Generated by Django 4.2.1 on 2023-10-24 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0004_blogs_heading'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogs',
            old_name='byuserid',
            new_name='byid',
        ),
        migrations.AddField(
            model_name='blogs',
            name='byuser',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='blogs',
            name='content',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
