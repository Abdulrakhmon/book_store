# Generated by Django 4.0 on 2022-03-12 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_alter_rateofbook_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='number',
            field=models.CharField(max_length=10),
        ),
    ]