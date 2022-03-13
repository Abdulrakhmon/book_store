# Generated by Django 4.0 on 2022-03-11 23:46

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('image', models.ImageField(upload_to='books/')),
                ('description', models.CharField(max_length=512)),
                ('author', models.CharField(max_length=128)),
                ('published_date', models.DateField(verbose_name='Published date')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.PositiveSmallIntegerField()),
                ('on_sale', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Book',
                'verbose_name_plural': 'Books',
                'db_table': 'book',
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=512)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Book Category',
                'verbose_name_plural': 'Book Categories',
                'db_table': 'book_category',
            },
        ),
        migrations.CreateModel(
            name='DiscountedBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=256, null=True)),
                ('description', models.CharField(blank=True, max_length=512, null=True)),
                ('percentage', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)])),
                ('beginning_time', models.DateTimeField()),
                ('ending_time', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Discounted Book',
                'verbose_name_plural': 'Discounted Books',
                'db_table': 'discounted_book',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='ExtraQuantityForExistBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveSmallIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Extra Quantity For Exist Book',
                'verbose_name_plural': 'Extra Quantity For Exist Books',
                'db_table': 'extra_quantity_for_exist_book',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveSmallIntegerField()),
                ('total_quantity_of_items', models.PositiveSmallIntegerField()),
                ('total_amount_of_purchase', models.DecimalField(decimal_places=2, max_digits=15)),
                ('status', models.IntegerField(choices=[(1, 'Created'), (2, 'In progress'), (3, 'Rejected'), (4, 'Completed')], default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
                'db_table': 'order',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='OrderedBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveSmallIntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=15)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Ordered Book',
                'verbose_name_plural': 'Ordered Books',
                'db_table': 'ordered_book',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='RateOfBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('description', models.CharField(blank=True, max_length=512, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='books.book')),
            ],
            options={
                'verbose_name': 'Rate of book',
                'verbose_name_plural': 'Rates of books',
                'db_table': 'rate_of_book',
                'ordering': ('-id',),
            },
        ),
    ]
