# Generated by Django 4.0.3 on 2022-03-08 05:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0004_remove_product_limited_at_product_is_limited'),
    ]

    operations = [
        migrations.RenameField(
            model_name='brand',
            old_name='category',
            new_name='categories',
        ),
        migrations.RemoveField(
            model_name='product',
            name='hot_size',
        ),
        migrations.RemoveField(
            model_name='product',
            name='ice_size',
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('capacity', models.IntegerField()),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cafe.brand')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='hot_size',
            field=models.ManyToManyField(blank=True, related_name='hot_size', to='cafe.size'),
        ),
        migrations.AddField(
            model_name='product',
            name='ice_size',
            field=models.ManyToManyField(blank=True, related_name='ice_size', to='cafe.size'),
        ),
    ]
