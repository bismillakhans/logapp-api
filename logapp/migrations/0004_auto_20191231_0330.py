# Generated by Django 2.2.8 on 2019-12-31 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logapp', '0003_auto_20191231_0329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='mobile_number',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='vehicle_type',
            field=models.CharField(choices=[('two_wheeler', 'Two Wheeler'), ('three_wheeler', 'Three Wheeler'), ('four_wheeler', 'Four Wheeler'), ('heavy', 'Heavy Vehicle')], default='two_wheeler', max_length=120),
        ),
    ]
