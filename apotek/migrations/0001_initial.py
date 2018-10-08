# Generated by Django 2.1.1 on 2018-09-17 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataObat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_obat', models.CharField(help_text='Masukkan nama obat dan dosisnya', max_length=50)),
                ('satuan', models.CharField(blank=True, choices=[('TAB', 'Tablet'), ('CAP', 'Kapsul'), ('BTL', 'Botol'), ('PCS', 'Pcs'), ('BOX', 'Box'), ('TUB', 'Tube')], help_text='Satuan pemakaian obat', max_length=3)),
                ('jumlah', models.PositiveIntegerField(help_text='Jumlah')),
                ('tanggal_kadaluwarsa', models.DateField(help_text='Masukkan tanggal ED produk yang paling dekat')),
                ('no_batch', models.CharField(blank=True, help_text='Pisahkan dengan ";" bila lebih dari 1', max_length=30)),
                ('generik', models.BooleanField(default=True, help_text='Tandai bila termasuk obat generik')),
            ],
            options={
                'verbose_name_plural': 'Daftar Obat & Bahan Habis Pakai',
            },
        ),
    ]
