Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> Nama = 'Royan Saifur Robbi'
>>> NIM = 'L200190196'
>>> X = '1' + NIM[7:]
>>> a = int(X)
>>> b = len(Nama)
>>> type(a)
<class 'int'>
>>> # Data 'X' diubah menjadi integer kemudian disimpan di 'a'
>>> type(b)
<class 'int'>
>>> # Data yang disimpan didalam 'Nama' mempunyai instruksi len dan disimpan di 'b'
>>> a / b
66.44444444444444
>>> # Hasil dari  1196 dibagi 18 adalah 66.44444444444444
>>> a // b
66
>>> # Arti dari '//' adalah pembagian kemudian hasilnya dibulatkan
>>> 10 * (a - 999)
1970
>>> # Hasil dari 'a' dikurangi 999 adalah 197, kemudian dikalikan 10 dan menghasilkan 1970
>>> b ** 2
324
>>> # Makna dari '**' adalah menjadi pangkat, jadi b pangkat 2 menghasilkan 324
>>> a % b
8
>>> # '%' akan menunjukan sisa dari hasil a dibagi b
>>> c = 12.5
>>> type(c)
<class 'float'>
>>> # 12.5 adalah bilangan desimal
>>> a / c
95.68
>>> # Hasil dari 'a' dibagi 'c'
>>> a // c
95.0
>>> # Hasil dari 'a' dibagi 'c' kemudian dibulatkan
>>> a % c
8.5
>>> # Sisa dari 'a' dibagi 'c'
>>> c > b
False
>>> # Karna 'c' adalah 12.5 sedangkan 'b' adalah 18, jadi pernyataan dari c > b salah
>>> type(c > b)
<class 'bool'>
>>> # bool merupakan pernyataan yang mempunyai dua kemungkinan yaitu 'True' dan 'False'
>>> a > b and b > c
True
>>> # 'a' adalah 197, nilai 'b' adalah 18, dan 'c' adalah 12.5, jadi pernyataan diatas benar
>>> a > 1100 or b < 10
True
>>> # *ralat nilai 'a' adalah 1197 dan 'b' adalah 18. Pernyataan diatas menggunakan logika 'or'
>>> 
