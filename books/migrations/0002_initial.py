# Generated by Django 4.0 on 2022-03-11 23:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rateofbook',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.user'),
        ),
        migrations.AddField(
            model_name='orderedbook',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='books.book'),
        ),
        migrations.AddField(
            model_name='orderedbook',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='books', to='books.order'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.user'),
        ),
        migrations.AddField(
            model_name='extraquantityforexistbook',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='books.book'),
        ),
        migrations.AddField(
            model_name='extraquantityforexistbook',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.user'),
        ),
        migrations.AddField(
            model_name='discountedbook',
            name='books',
            field=models.ManyToManyField(to='books.Book'),
        ),
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='books', to='books.category'),
        ),
        migrations.AddField(
            model_name='book',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.user'),
        ),
    ]
