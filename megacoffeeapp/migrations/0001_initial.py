# Generated by Django 3.1.2 on 2023-09-22 18:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='megacoffeeapp.menu')),
                ('option', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='megacoffeeapp.option')),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(default='megacoffee', max_length=50)),
                ('name', models.CharField(default='menu', max_length=50)),
                ('using_page', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Quantity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('method', models.CharField(max_length=100)),
                ('packing', models.CharField(max_length=50)),
                ('orders', models.ManyToManyField(to='megacoffeeapp.Order')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='quantity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='megacoffeeapp.quantity'),
        ),
        migrations.CreateModel(
            name='Button',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('button_name', models.CharField(max_length=50)),
                ('click_time', models.DateTimeField()),
                ('is_right', models.BooleanField()),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='megacoffeeapp.page')),
            ],
        ),
    ]
