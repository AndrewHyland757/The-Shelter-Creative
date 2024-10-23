# Generated by Django 4.2 on 2024-10-23 13:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_section_video_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectpage',
            name='section_10',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='section_10', to='projects.section'),
        ),
        migrations.AddField(
            model_name='projectpage',
            name='section_9',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='section_9', to='projects.section'),
        ),
    ]