# Generated by Django 2.1.1 on 2018-09-17 14:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apotek', '0003_auto_20180917_2309'),
        ('pendaftaran', '0003_kunjungan'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resep',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jumlah', models.PositiveSmallIntegerField()),
                ('aturan_pakai', models.CharField(max_length=10)),
                ('nama_obat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apotek.DataObat')),
            ],
        ),
        migrations.AlterModelOptions(
            name='kunjungan',
            options={'verbose_name_plural': 'Data Kunjungan'},
        ),
        migrations.AddField(
            model_name='resep',
            name='nama_pasien',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pendaftaran.Kunjungan'),
        ),
    ]