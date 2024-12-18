# Generated by Django 5.1.1 on 2024-11-17 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('olmsapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='acopies',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='book',
            name='issued_copies',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='issuedbookdetails',
            name='fine',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='issuedbookdetails',
            name='return_status',
            field=models.CharField(choices=[('returned', 'Returned'), ('not_returned', 'Not Returned')], default='not_returned', max_length=12),
        ),
    ]
