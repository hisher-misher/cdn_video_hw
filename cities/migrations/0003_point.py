# Generated by Django 4.1.3 on 2022-11-25 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0002_alter_city_x_coord_alter_city_y_coord'),
    ]

    operations = [
        migrations.CreateModel(
            name='Point',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x_coord', models.FloatField(blank=True, null=True)),
                ('y_coord', models.FloatField(blank=True, null=True)),
            ],
        ),
    ]
