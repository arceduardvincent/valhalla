# Generated by Django 3.2.8 on 2022-04-12 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aws', '0002_alter_awsvirtualmachine_instance_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountID',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_id', models.CharField(max_length=30, verbose_name='Account ID')),
                ('pub_date', models.DateTimeField(verbose_name='Date published')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_name', models.CharField(max_length=30, verbose_name='Image Name')),
            ],
        ),
        migrations.CreateModel(
            name='InstanceID',
            fields=[
                ('instance_id', models.CharField(max_length=30, primary_key=True, serialize=False, verbose_name='Instance ID')),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(max_length=30, verbose_name='Region')),
            ],
        ),
    ]