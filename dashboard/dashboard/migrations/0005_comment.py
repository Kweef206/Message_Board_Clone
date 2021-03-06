# Generated by Django 2.2 on 2020-07-16 23:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('log_reg_app', '0005_auto_20200716_1300'),
        ('dashboard', '0004_auto_20200716_1415'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=255)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_comments', to='log_reg_app.User')),
                ('message_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_comments', to='dashboard.Post')),
            ],
        ),
    ]
