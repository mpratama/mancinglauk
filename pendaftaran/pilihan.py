from .variabelkonstan import *

KOMPLEKS_CHOICES = (
    (GANTENG, 'Ganteng'),
    (MELAYU, 'Melayu'),
    (PELABUHAN, 'Pelabuhan'),
    (RALENA, 'Ralena'),
    (LUAR_TAYANDO, 'Luar Tayando'),
    (BELUM_TAHU, 'Belum Diketahui'),
)

AGAMA_CHOICES = (
    (ISLAM, 'Islam'),
    (PROTESTAN, 'Kristen Protestan'),
    (KATHOLIK, 'Kristen Katholik'),
    (HINDU, 'Hindu'),
    (BUDDHA, 'Buddha'),
    (KONGHUCU, 'Konghucu'),
)

JENIS_KELAMIN_CHOICES = (
    (LAKILAKI, 'Laki - Laki'),
    (PEREMPUAN, 'Perempuan'),
)

GOLONGAN_DARAH_CHOICES = (
    (A, 'A'),
    (APLUS, 'A+'),
    (AMIN, 'A-'),
    (AB, 'AB'),
    (ABPLUS, 'AB+'),
    (ABMIN, 'AB-'),
    (B, 'B'),
    (BPLUS, 'B+'),
    (BMIN, 'B-'),
    (O, 'O'),
    (OPLUS, 'O+'),
    (OMIN, 'O-'),
)

PEKERJAAN_CHOICES = (
    (TDKBEKERJA, 'Belum / Tidak Bekerja'),
    (PEGNEGRI, 'Pegawai Negeri'),
    (IBURUMAHTANGGA, 'Ibu Rumah Tangga'),
    (BURUH, 'Buruh'),
    (PETANI, 'Petani'),
    (NELAYAN, 'Nelayan'),
    (PEDAGANG, 'Pedagang'),
    (KARYSWASTA, 'Karyawan Swasta'),
    (ABRI, 'ABRI'),
    (PROFESSIONAL, 'Professional'),
    (WIRASWASTA, 'Wiraswasta'),
    (PURNAWIRAWAN, 'Purnawirawan'),
    (PENSIUNAN, 'Pensiunan'),
    (PELAJAR, 'Pelajar'),
    (MAHASISWA, 'Mahasiswa'),
    (LAINNYA, 'Lain - Lain'),
)

STATUS_NIKAH_CHOICES = (
    (MENIKAH, 'Menikah'),
    (BELUM_MENIKAH, 'Belum Menikah'),
    (JANDA, 'Janda'),
    (DUDA, 'Duda'),
)

PENDIDIKAN_AKHIR_CHOICES = (
    (SD, 'SD'),
    (SMP, 'SMP'),
    (SMA, 'SMA'),
    (D3, 'D3'),
    (S1, 'S1'),
    (S2, 'S2'),
    (S3, 'S3'),
)

SAT_OBAT_CHOICES = (
    (TABLET, 'Tablet'),
    (KAPSUL, 'Kapsul'),
    (BOTOL, 'Botol'),
    (PCS, 'Pcs'),
    (BOX, 'Box'),
    (TUBE, 'Tube'),
    (PASANG, 'Pasang'),
)