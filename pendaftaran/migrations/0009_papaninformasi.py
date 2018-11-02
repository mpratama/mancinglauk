# Generated by Django 2.1.1 on 2018-10-29 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pendaftaran', '0008_auto_20180929_0801'),
    ]

    operations = [
        migrations.CreateModel(
            name='PapanInformasi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tanggal_pengumuman', models.DateField(help_text='Tanggal Pengumuman Ditulis')),
                ('judul_pengumuman', models.CharField(max_length=20)),
                ('isi_pengumuman', models.TextField(help_text='Isi Pengumuman')),
            ],
        ),
    ]