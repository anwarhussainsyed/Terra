# Generated by Django 4.1.7 on 2023-09-09 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('terra', '0002_submit_blog_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact_us',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('subject', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=500)),
            ],
        ),
    ]
