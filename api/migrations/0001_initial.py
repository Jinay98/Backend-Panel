# Generated by Django 3.0.5 on 2020-04-27 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('shipment_info', models.CharField(default='', max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.IntegerField(default=0)),
            ],
        ),
    ]