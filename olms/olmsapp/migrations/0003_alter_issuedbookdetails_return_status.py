# Generated by Django 5.1.1 on 2024-11-17 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('olmsapp', '0002_book_acopies_book_issued_copies_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issuedbookdetails',
            name='return_status',
            field=models.CharField(choices=[('returned', 'Returned'), ('not_returned', 'Not Returned')], default='not_returned', max_length=50),
        ),
    ]