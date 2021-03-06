# Generated by Django 4.0.2 on 2022-02-05 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description_short', models.CharField(max_length=100)),
                ('description_long', models.TextField()),
                ('lng', models.DecimalField(decimal_places=16, max_digits=20)),
                ('lat', models.DecimalField(decimal_places=16, max_digits=20)),
            ],
        ),
    ]
