# Generated by Django 3.0.3 on 2020-03-19 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=300)),
                ('author_name', models.CharField(max_length=300)),
                ('book_price', models.IntegerField()),
                ('book_quantity', models.IntegerField()),
            ],
        ),
    ]