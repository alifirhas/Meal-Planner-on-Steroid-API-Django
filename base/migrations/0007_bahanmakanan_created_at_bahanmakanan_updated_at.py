# Generated by Django 4.1 on 2022-08-15 01:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0006_makanan_rename_name_tingkataktivitas_nama_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="bahanmakanan",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="bahanmakanan",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
