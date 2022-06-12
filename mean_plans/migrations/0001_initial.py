# Generated by Django 4.0.5 on 2022-06-08 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cate', models.CharField(choices=[('BF', 'Breakfast'), ('LC', 'Lunch'), ('SP', 'Supper')], default='BF', max_length=2)),
                ('size', models.IntegerField(max_length=2)),
                ('cuisine', models.CharField(max_length=40)),
            ],
        ),
    ]