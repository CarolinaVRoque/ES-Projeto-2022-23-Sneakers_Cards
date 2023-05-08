# Generated by Django 4.2 on 2023-04-16 13:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='images/')),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CardType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descript', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('value', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Collector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('nickname', models.CharField(max_length=100)),
                ('power', models.IntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Deck',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('cards', models.ManyToManyField(to='SneakerCards.cards')),
                ('collector', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SneakerCards.collector')),
            ],
        ),
        migrations.AddField(
            model_name='cards',
            name='card_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SneakerCards.cardtype'),
        ),
    ]
