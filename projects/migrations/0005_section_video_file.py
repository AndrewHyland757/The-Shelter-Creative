# Generated by Django 4.2 on 2024-10-18 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_section_new_header_color_hover_mobile_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='video_file',
            field=models.FileField(blank=True, null=True, upload_to='project_videos'),
        ),
    ]