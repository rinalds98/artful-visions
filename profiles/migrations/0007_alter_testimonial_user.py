# Generated by Django 3.2.18 on 2023-06-07 21:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_testimonial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonial',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.userprofile'),
        ),
    ]
