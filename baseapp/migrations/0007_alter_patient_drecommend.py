# Generated by Django 5.0.1 on 2024-01-16 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseapp', '0006_alter_doctor_hospital'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='drecommend',
            field=models.FileField(max_length=50, null=True, upload_to='drecommend'),
        ),
    ]
