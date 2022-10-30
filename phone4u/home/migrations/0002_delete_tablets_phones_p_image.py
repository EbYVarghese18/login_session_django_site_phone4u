# Generated by Django 4.1.2 on 2022-10-29 09:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Tablets',
        ),
        migrations.AddField(
            model_name='phones',
            name='p_image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='phoneimages'),
            preserve_default=False,
        ),
    ]