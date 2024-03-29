# Generated by Django 5.0.1 on 2024-02-03 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseapp', '0003_alter_donor_bloodgroup_alter_patient_bloodgroup'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donor',
            name='bloodgroup',
            field=models.CharField(choices=[("Don't know", "Don't know"), ('O positive', 'O positive'), ('O negative', 'O negative'), ('A positive', 'A positive'), ('A negative', 'A negative'), ('B positive', 'B positive'), ('B negative', 'B negative'), ('AB positive', 'AB positive'), ('AB negative', 'AB negative')], default="Don't know", max_length=20),
        ),
        migrations.AlterField(
            model_name='patient',
            name='bloodgroup',
            field=models.CharField(choices=[("Don't know", "Don't know"), ('O positive', 'O positive'), ('O negative', 'O negative'), ('A positive', 'A positive'), ('A negative', 'A negative'), ('B positive', 'B positive'), ('B negative', 'B negative'), ('AB positive', 'AB positive'), ('AB negative', 'AB negative')], default="Don't know", max_length=20),
        ),
    ]
