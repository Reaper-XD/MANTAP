# module
import marshal, zlib, base64, os, sys, time
os.system("clear")
os.system("git pull")
REAPER = """
╔═══╗╔═══╗╔═══╗╔═══╗╔═══╗╔═══╗────╔═══╗╔══╗╔╗───╔═══╗
╚╗╔╗║║╔══╝║╔═╗║║╔═╗║╚╗╔╗║║╔══╝────║╔══╝╚╣─╝║║───║╔══╝
─║║║║║╚══╗║║─╚╝║║─║║─║║║║║╚══╗────║╚══╗─║║─║║───║╚══╗
─║║║║║╔══╝║║─╔╗║║─║║─║║║║║╔══╝────║╔══╝─║║─║║─╔╗║╔══╝
╔╝╚╝║║╚══╗║╚═╝║║╚═╝║╔╝╚╝║║╚══╗────║║───╔╣─╗║╚═╝║║╚══╗
╚═══╝╚═══╝╚═══╝╚═══╝╚═══╝╚═══╝────╚╝───╚══╝╚═══╝╚═══╝
"""
print REAPER
def auto(z):
    for e in z + "\n":
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.05)
try:
    r = sys.argv[1]
except:
    auto("Masukkan : python2 ini....py CONTOH : python2 ini namafilenya.py")

if not os.path.isfile(r):
    auto("File Tidak Ditemukan!")

a = open(r).read()
b = marshal.dumps(a)
c = zlib.compress(b)
d = base64.b64encode(c)

sv = 'import marshal, zlib, base64\nexec(marshal.loads(zlib.decompress(base64.b64decode("{}"))))'

open("ini_.py", "w").write(sv.format(d))
auto("berhasil : file tersimpan ini_.py")
