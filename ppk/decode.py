# module
import marshal, zlib, base64, os, sys

try:
    r = sys.argv[1]
except:
    exit("Masukkan : python2 ....py CONTOH : python2 namafilenya.py")

if not os.path.isfile(r):
    exit("File Tidak Ditemukan!")

a = open(r).read()
b = marshal.dumps(a)
c = zlib.compress(b)
d = base64.b64encode(c)

sv = 'import marshal, zlib, base64\nexec(marshal.loads(zlib.decompress(base64.b64decode("{}"))))'

open("ini_.py", "w").write(sv.format(d))
exit("berhasil : file tersimpan ini_.py")
