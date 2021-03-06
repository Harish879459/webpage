# Generated by Django 3.0.8 on 2020-08-05 06:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customer', '0002_remove_customer_email'),
        ('cab', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('book_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('time', models.CharField(max_length=20)),
                ('date', models.CharField(max_length=10)),
                ('cab', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cab.Cab')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.Customer')),
            ],
            options={
                'db_table': 'book',
            },
        ),
    ]
