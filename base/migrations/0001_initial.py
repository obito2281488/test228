# Generated by Django 3.0.8 on 2020-07-20 13:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/category/')),
                ('is_visible', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('is_visible', models.BooleanField(default=True)),
                ('price', models.FloatField()),
                ('weight', models.IntegerField()),
                ('main_image', models.ImageField(upload_to='media/product/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.Category')),
            ],
        ),
        migrations.CreateModel(
            name='OrderProducts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_amount', models.IntegerField(default=1)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='base.Order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='base.Product')),
            ],
        ),
    ]