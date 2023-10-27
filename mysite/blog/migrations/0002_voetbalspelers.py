# Generated by Django 3.2.22 on 2023-10-27 15:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Voetbalspelers',
            fields=[
                ('post_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='blog.post')),
                ('player_name', models.CharField(max_length=200)),
                ('current_club', models.CharField(max_length=200)),
            ],
            bases=('blog.post',),
        ),
    ]
