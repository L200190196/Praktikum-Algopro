Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> Nama = 'Royan Saifur Robbi'
>>> NIM = 196
>>> Tinggi = 1.64
>>> Berat = 50
>>> TahunLahir = 2000
>>> Aku = (TahunLahir, Berat, Tinggi, NIM, Nama)
>>> Data = [TahunLahir, Berat, Tinggi, NIM, Nama]
>>> type(Aku)
<class 'tuple'>
>>> # Data TahunLahir, Berat, Tinggi, NIM, dan Nama dikumpulkan dalam tuple dan disimpan di Aku
>>> Aku[0]
2000
>>> # 0 adalah data pertama didalam tuple Aku
>>> a = NIM % 4; Aku[a]
2000
>>> type(Aku[a])
<class 'int'>
>>> # Karena a adalah integer
>>> Aku[a:4]
(2000, 50, 1.64, 196)
>>> # Memanggil data dalam list dari data pertama sampai data keempat
>>> type(Aku[4])
<class 'str'>
>>> # Karena data kelima berisikan Nama yang mana bertipe string
>>> Aku[0] = 'ok'
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    Aku[0] = 'ok'
TypeError: 'tuple' object does not support item assignment
>>> # Tipe data tuple tidak dapat diubah datanya
>>> type(Data)
<class 'list'>
>>> # Data adalah tipe data list
>>> type(Data[4])
<class 'str'>
>>> # Karena data kelima yang berisikan Nama adalah bertipe string
>>> Data[4][5]
' '
>>> # Data yang dipanggil tidak ada atau kosong
>>> Data[4][a:6]
'Royan '
>>> # Daa yang dipanggil dididalam data Nama dari awal sampai data keenam
>>> Data[0] = 'ok'; Data
['ok', 50, 1.64, 196, 'Royan Saifur Robbi']
>>> # Data pertama didalam list Data diubah menjadi 'ok' dan list tersebut dipanggil
>>> Data[-a]
'ok'
>>> # Data pertama dalam lis Data dipanggil
>>> range(a)
range(0, 0)
>>> # Menyebutkan data yang berada dalam jangkauan a
>>> 
