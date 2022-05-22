import subprocess
import platform
import socket
import time
import signal
import os
from colorama import Fore
import readline

class MyCompleter(object):  # Custom completer

    def __init__(self, options):
        self.options = sorted(options)

    def complete(self, text, state):
        if state == 0:  # on first trigger, build possible matches
            if text:  # cache matches (entries that start with entered text)
                self.matches = [s for s in self.options 
                                    if s and s.startswith(text)]
            else:  
                self.matches = self.options[:]
        try: 
            return self.matches[state]
        except IndexError:
            return None

completer = MyCompleter(["komutlar", "ping", "scri", "tarih", "list", "list -a", "clear", "sys", "exit", "oku", "git", "dd", "hesap-makinesi"])
readline.set_completer(completer.complete)
readline.parse_and_bind('tab: complete')
path = '/root/'
hostname = socket.gethostname()
hostip = socket.gethostbyname(hostname)
print(chr(27)+'[2j')
print('\033c')
print('\x1bc')
print(Fore.RED+"""
 ____   ____ ____ _____ _____ ____  __  __ 
/ ___| / ___|  _ \_   _| ____|  _ \|  \/  |
\___ \| |   | |_) || | |  _| | |_) | |\/| |
 ___) | |___|  _ < | | | |___|  _ <| |  | |
|____/ \____|_| \_\|_| |_____|_| \_\_|  |_|
"""+Fore.RESET)
print("""

SCRTERM'e Hoş Geldiniz!

Web Site: https://colaxtiy.rf.gd/scrterm

Komutları Öğrenmek İçin:

    * komutlar [Bu Komudu Yazarak ScrTerm İçindeki Komutları Öğrenebilirsiniz!]

Sosyal Medya:

    * İnstagram [https://www.instagram.com/colaxtiy/]
    * Github [https://github.com/colaxtiy/]
    * Papara [1190971123]
    * ScrTerm Geliştirici Kanalı [t.me/scrterm]
""")
while True:
    dzn = os.getcwd()
    code = input(f'''\033[31m┌──[scr\033[33m@\033[34mscr\033[31m]-[\033[34m{dzn}\033[31m]
└─\033[33m#\033[39m ''')
    def sigint_handler(signum, frame):
        print('CTRL+C Çıkış Yapıldı!')
    signal.signal(signal.SIGINT, sigint_handler)
    if code == "ping":
        host = input("Ping Atılacak Web Sitesini Girin >>> ")
        number = input("Kaç Kez Pinglemek İstediğinizi Yazın >>> ")

        def ping(host):
            param = '-n' if platform.system().lower() == 'windows' else '-c'
            command = ['ping', param, number, host]
            return subprocess.call(command)
        print(ping(host))
    if code == 'scri':
        print("Yerel İp Adresin : "+Fore.RED + hostip)
        print(Fore.RESET+"Masaüstü Adınız : "+Fore.RED + hostname+Fore.RESET)
    if code == 'tarih':
        print("Yerel Tarihiniz : " + time.strftime("%m/%d/%Y"))
    if code == 'list':
        dir_list = os.listdir(dzn)
        print("Dizinler Ve Dosyalar '", dzn,"' :")
        print(dir_list)
    if code == 'list -a':
        file = input("Dosya Veya Dizin Yolu >>> ")
        dir_list2 = os.listdir(file)
        print("Dizinler Ve Dosyalar'", file, "':")
        print(dir_list2)
    if code == 'clear':
        print(chr(27)+'[2j')
        print('\033c')
        print('\x1bc')
    if code == 'sys':
        print("Sistem: "+Fore.RED+platform.system()+Fore.RESET)
        print("Node İsmi: "+Fore.RED+platform.node()+Fore.RESET)
        print("Release: "+Fore.RED+platform.release()+Fore.RESET)
        print("Versiyon: "+Fore.RED+platform.version()+Fore.RESET)
        print("Makine: "+Fore.RED+platform.machine()+Fore.RESET)
        print("İşlemci: "+Fore.RED+platform.processor()+Fore.RESET)
    if code == 'exit':
        exit()
    if code == 'komutlar':
        print("""
ping >>> Verilen Siteye Verilen Adette Ping Paketi Yollar.

scri >>> Yerel İp Adresinizi Ve Bilgisayarınızın İsmini Gösterir.

tarih >>> Bulunduğunuz Yerdeki Tarihi Gösterir.

list >>> Root Dizini Ve Altındaki Dizinleri Listeler.

list -a >>> Belirttiğiniz Dizini Listeler.

clear / ctrl+l >>> Ekranı Temizler.

sys >>> Sistem Hakkında Bilgiler Verir.

exit >>> Sistemden Çıkış Yapar.

ctrl+c >>> Yapılan İşlemi Durdurur.

komutlar >>> Komutların Kullanımını Anlatır. 

oku >>> Verdiğiniz Dosyanın İçeriğini Gösterir.

git >>> Github İşlemleri İçin Eklendi.

dd >>> Dizin Değiştirmek İçin Kullanılır.

hesap-makinesi >>> Toplama Çıkarma Çarpma İşleri İçin Hesap Makinesi.

""")
    if code == "oku":
        dos = input("Okumak İstediğiniz Dosyayı Girin >>> ")
        with open(dos)as f:
            contents = f.read()
            print(contents)
    if code == "git":
        os.system("./git")
    if code == "git clone":
        gt = input("Url girin >>> ")
        os.system("./git clone "+gt)
    if code == "dd":
        dz = input("Gitmek İstediğiniz Dizin >>> ")
        os.chdir(dz)
    if code == "hesap-makinesi":
        print(Fore.RED+"""
Toplama için + yazın

Çıkarma için - yazın

Çarpma için * yazın

Bölme için / yazın
""")
        hp = input(Fore.CYAN+"\nYapmak İstediğiniz İşlemi Seçin >>> "+Fore.RESET)
        sayi1 = int(input(Fore.GREEN+"\n1. Sayıyı Girin >>>"+Fore.RESET))
        sayi2 = int(input(Fore.GREEN + "\n2. Sayıyı Girin >>>" + Fore.RESET))
        if hp == "+":
            print(Fore.RED+"\nSonuç : "+Fore.RESET, sayi1 + sayi2)
        elif hp == "-":
            print(Fore.RED+"\nSonuç : "+Fore.RESET, sayi1 - sayi2)
        elif hp == "*":
            print(Fore.RED+"\nSonuç : "+Fore.RESET, sayi1 * sayi2)
        elif hp == "/":
            print(Fore.RED + "\nSonuç : " + Fore.RESET, sayi1 / sayi2)
