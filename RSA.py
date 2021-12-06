import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Cipher import PKCS1_OAEP
import ast

random_generator = Random.new().read
key = RSA.generate(1024, random_generator) #mengenerate kunci publik dan kunci private

publickey = key.publickey() #ekspor kunci publik untuk ditukarkan

# ENKRIPSI
encryptor = PKCS1_OAEP.new(publickey) #gunakan instansi dari PKCS1_OAEP
encrypted = encryptor.encrypt(b'Zulfi Masyita Resia, V3920063, D3 Teknik Informatika, zulfimasyita@student.uns.ac.id') #pesan untuk dienkripsi

print('Hasil Enkripsi:', encrypted)

# Menambahkan teks pada file .txt
f = open ('enkripsi-alert.txt', 'a') #append file
f.write('File telah memiliki content!') #tambahkan isi teks alert ini ke file enkripsi-alert.txt
f.close()

# Update file .txt
f = open ('enkripsi.txt', 'w') #buka file txt, 'w' adalah write
f.write('Isi file hasil enkripsi telah diupdate!') #teks alert untuk menampilkan update dari file enkripsi.txt, namun membuat file lagi (enkripsi-alert.txt) untuk pembeda
f.write(str(encrypted)) #menambahkan hasil enkripsi di samping teks alert
f.close()

f = open('enkripsi.txt', 'r') #'r' adalah read
message = f.read()

# Dekripsi
decryptor = PKCS1_OAEP.new(key)
decrypted = decryptor.decrypt(ast.literal_eval(str(encrypted)))

print('Hasil Dekripsi:', decrypted)

f = open ('dekripsi.txt', 'w')
f.write('Isi file hasil dekripsi:') #tambahkan isi teks ini ke file dekripsi.txt
f.write(str(decrypted)) #hasil dekripsi akan ditampilkan di samping teks line 39
f.close()
