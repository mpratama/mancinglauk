# Generated by Django 2.1.1 on 2018-09-17 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataPasien',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_bpjs', models.CharField(default='000', help_text='Bila belum ada kartu, masukkan 000', max_length=15)),
                ('nik', models.CharField(default='000', help_text='Bila belum ada kartu, masukkan 000', max_length=20)),
                ('nama_pasien', models.CharField(help_text='Masukkan Nama Sesuai Kartu', max_length=50)),
                ('tanggal_lahir', models.DateField(help_text='Wajib diisi')),
                ('golongan_darah', models.CharField(blank=True, choices=[('A', 'A'), ('A+', 'A+'), ('A-', 'A-'), ('AB', 'AB'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('B', 'B'), ('B+', 'B+'), ('B-', 'B-'), ('O', 'O'), ('O+', 'O+'), ('O-', 'O-')], max_length=3)),
                ('alamat', models.CharField(choices=[('GT', 'Ganteng'), ('ML', 'Melayu'), ('PL', 'Pelabuhan'), ('RL', 'Ralena'), ('LT', 'Luar Tayando')], max_length=2)),
                ('agama', models.CharField(blank=True, choices=[('IS', 'Islam'), ('KP', 'Kristen Protestan'), ('KK', 'Kristen Katholik'), ('HD', 'Hindu'), ('BU', 'Buddha'), ('KO', 'Konghucu')], max_length=2)),
                ('jenis_kelamin', models.CharField(blank=True, choices=[('L', 'Laki - Laki'), ('P', 'Perempuan')], max_length=1)),
                ('pekerjaan', models.CharField(blank=True, choices=[('0', 'Belum / Tidak Bekerja'), ('1', 'Pegawai Negeri'), ('2', 'Ibu Rumah Tangga'), ('3', 'Buruh'), ('4', 'Petani'), ('5', 'Nelayan'), ('6', 'Pedagang'), ('7', 'Karyawan Swasta'), ('8', 'ABRI'), ('9', 'Professional'), ('10', 'Wiraswasta'), ('11', 'Purnawirawan'), ('12', 'Pensiunan'), ('13', 'Pelajar'), ('14', 'Mahasiswa'), ('15', 'Lain - Lain')], max_length=2)),
                ('pendidikan_akhir', models.CharField(blank=True, choices=[('1', 'SD'), ('2', 'SMP'), ('3', 'SMA'), ('4', 'D3'), ('5', 'S1'), ('6', 'S2'), ('7', 'S3')], max_length=1)),
                ('status_nikah', models.CharField(blank=True, choices=[('0', 'Menikah'), ('1', 'Belum Menikah'), ('2', 'Janda'), ('3', 'Duda')], max_length=2)),
                ('no_hp', models.CharField(blank=True, max_length=20)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_edited', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Data Pasien',
            },
        ),
    ]
