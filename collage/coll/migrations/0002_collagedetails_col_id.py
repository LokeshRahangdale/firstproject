# Generated by Django 2.2.3 on 2019-08-27 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coll', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='collagedetails',
            name='col_id',
            field=models.IntegerField(auto_created=True, default=1),
            preserve_default=False,
        ),
    ]
