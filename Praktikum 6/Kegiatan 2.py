## Program Akun
## Dibuat oleh Royan L200190196
import random
angka = random.randint(100,999)

Nama = 'Royan Saifur Robbi'
TanggalLahir = '08 Februari 2000'
print(Nama)
print(TanggalLahir)
NamaSingkat = Nama[:5] + '. ' + Nama[6] + '. ' + Nama[13]
print(NamaSingkat)
username = Nama[0] + TanggalLahir[:2] + TanggalLahir[12:]
print(username)
password = Nama[:3] + str(angka)
print(password)
