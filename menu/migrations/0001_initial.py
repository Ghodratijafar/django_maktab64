# Generated by Django 4.0.1 on 2022-01-20 19:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('catagory', '0001_initial'),
        ('cashier', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Receipts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_price', models.IntegerField(default=0)),
                ('final_price', models.IntegerField(default=0)),
                ('time_stamp', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(max_length=30)),
                ('table_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cashier.table')),
            ],
        ),
        migrations.CreateModel(
            name='Menuitem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('price', models.IntegerField()),
                ('description', models.CharField(max_length=50)),
                ('discount', models.IntegerField(default=0)),
                ('catagory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catagory.catagory')),
            ],
        ),
    ]
