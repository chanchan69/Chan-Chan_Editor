import requests
from colorama import Fore, Style, init
from os import system
import time
import random
from ctypes import windll
class Main():
  def __init__(self):
    self.start()

  def remove_bad_lines(self, wombo, outfile):
    outfile = open(outfile, "w+")
    for line in wombo:
      if '@' and ':' and '.' in line:
        outfile.write(line)
    outfile.close()

  def remove_bad_proxy_lines(self, wombo, outfile):
    outfile = open(outfile, "w+")
    for line in wombo:
      if '.' and ':' in line:
        outfile.write(line)
    outfile.close()

  def remove_dupe_lines(self, wombo, outfile):
    lines_seen = set()
    outfile = open(outfile, "w+")
    for line in wombo:
      if line not in lines_seen:
          outfile.write(line)
          lines_seen.add(line)
    outfile.close()

  def add_text_before_line(self, wombo, outfile, text):
    outfile = open(outfile, "w+")
    for line in wombo:
      outfile.write(f'{text}{line}')
    outfile.close()

  def add_text_after_line(self, wombo, outfile, text):
    outfile = open(outfile, "w+")
    for line in wombo:
      cleanline = line.rstrip("\n")
      outfile.write(f'{cleanline}{text}\n')
    outfile.close()
  
  def email_to_user(self, wombo, outfile):
    outfile = open(outfile, "w+")
    for line in wombo:
      #mayperhaps this can be cleaner....
      mail_pass_split = line.split(':')
      domain_user = mail_pass_split[0].split('@')
      outfile.write(f'{domain_user[0]}:{mail_pass_split[1]}')
    outfile.close()

  def file_spliter(self, womboname, outfile, segments):
    def file_len(fname):
      with open(fname) as f:
          for i, l in enumerate(f):
              pass
      return i + 1
    lines_in_file = file_len(womboname)
    lines_per_file = lines_in_file / segments
    smallfile = None
    with open(womboname) as bigfile:
        for lineno, line in enumerate(bigfile):
            if lineno % lines_per_file == 0:
                if smallfile:
                    smallfile.close()
                small_filename = '{}{}'.format(lineno + lines_per_file, outfile)
                smallfile = open(small_filename, "w")
            smallfile.write(line)
        if smallfile:
            smallfile.close()

  def combo_editor(self, wombo, outfile):
    outfile = open(outfile, "w+")
    for line in wombo:
      try:
        mail_pass_split = line.split(':')
        password = mail_pass_split[1].rstrip("\n")
        editedpasswordlist = [f'@{password}', f'!{password}', f'#{password}', f'%{password}', f'123{password}', f'{password}123', f'?{password}', f'69{password}', f'{password}69', f'?{password}', '123Password', 'Password123', 'password123', '!password123']
        editedpassword = random.choice(editedpasswordlist)
        email = mail_pass_split[0].rstrip("\n")
        outfile.write('{}:{}\n'.format(email, editedpassword))
      except:
        pass
  
  def authproxy_converter(self, wombo, outfile):
    outfile = open(outfile, "w+")
    for line in wombo:
      if '@' in line:
        cleanline = line.rstrip("\n")
        info_split = cleanline.split('@')
        ipport = info_split[1].rstrip("@")
        #in User:pass@Ip:port
        #outIP:port:user:pass
        outfile.write('{}:{}\n'.format(ipport, info_split[0]))
      else:
        pass
  
  def inputs(self):
      self.userinputfile = input(f'{cyan}[{magenta}1{cyan}] Combo File:{magenta} ')
      self.uoutput = input(f'{cyan}[{magenta}2{cyan}] Output File:{magenta} ')
      self.uinput = open(self.userinputfile, 'r+', errors='ignore')

  def start(self):
    print(sign)
    print(main_menu)
    user_input = input(f'> ')
    system('cls')
    print(sign)
    print(f'{magenta} > {cyan}{anouncement.text}{magenta} <\n\n')
    self.inputs()
    if user_input == '1':
      self.remove_bad_lines(self.uinput, self.uoutput)

    elif user_input == '2':
      self.remove_bad_proxy_lines(self.uinput, self.uoutput)

    elif user_input == '3':
      self.remove_dupe_lines(self.uinput, self.uoutput)

    elif user_input == '4':
      self.combo_editor(self.uinput, self.uoutput)

    elif user_input == '5':
      self.email_to_user(self.uinput, self.uoutput)

    elif user_input == '6':
      addtext = input(f'{cyan}[{magenta}3{cyan}] Text to Add:{magenta} ')
      self.add_text_after_line(self.uinput, self.uoutput, addtext)

    elif user_input == '7':
      addtext = input(f'{cyan}[{magenta}3{cyan}] Text to Add:{magenta} ')
      self.add_text_before_line(self.uinput, self.uoutput, addtext)
    
    elif user_input == '8':
      segments = int(input(f'{cyan}[{magenta}3{cyan}] How Many Files:{magenta} '))
      self.file_spliter(self.userinputfile, self.uoutput, segments)

    elif user_input == '9':
      self.authproxy_converter(self.uinput, self.uoutput)

    elif user_input == '10':
      print(f'{cyan}Opening Link in Your Web Browser\n')
      import webbrowser
      new = 2
      url = "https://discord.gg/f32CZay9r3"
      webbrowser.open(url, new=new)
      print(f'{Fore.GREEN}Done opening link')
      print(f'{Fore.CYAN}')

if __name__ == '__main__':
  version = '1.2'
  windll.kernel32.SetConsoleTitleW(f'Chan-Chan Editor {version} | by SirChanChan | Main Menu')
  version1 = requests.get('https://pastebin.com/raw/g8nE8B7u').text
  if version == version1:
      pass
  else:
      print(f"{Fore.LIGHTRED_EX}Your version is outdated \nCurrent: {version1}{Fore.RESET}")
      time.sleep(3)
  init()
  cyan = Fore.LIGHTCYAN_EX
  magenta = Fore.MAGENTA; Style.BRIGHT
  anouncement = requests.get('https://pastebin.com/raw/Gkk7maxm')
  sign = f'''{magenta}
                     ▄▀▄▄▄▄   ▄▀▀▄ ▄▄   ▄▀▀█▄   ▄▀▀▄ ▀▄  ▄▀▄▄▄▄   ▄▀▀▄ ▄▄   ▄▀▀█▄   ▄▀▀▄ ▀▄ 
                    █ █    ▌ █  █   ▄▀ ▐ ▄▀ ▀▄ █  █ █ █ █ █    ▌ █  █   ▄▀ ▐ ▄▀ ▀▄ █  █ █ █ 
                    ▐ █      ▐  █▄▄▄█    █▄▄▄█ ▐  █  ▀█ ▐ █      ▐  █▄▄▄█    █▄▄▄█ ▐  █  ▀█ 
                      █         █   █   ▄▀   █   █   █    █         █   █   ▄▀   █   █   █  
                     ▄▀▄▄▄▄▀   ▄▀  ▄▀  █   ▄▀  ▄▀   █    ▄▀▄▄▄▄▀   ▄▀  ▄▀  █   ▄▀  ▄▀   █   
                    █     ▐   █   █    ▐   ▐   █    ▐   █     ▐   █   █    ▐   ▐   █    ▐   
                    ▐         ▐   ▐            ▐        ▐         ▐   ▐            ▐        
\n'''
  main_menu = (f'''
{magenta} > {cyan}{anouncement.text}{magenta} <
{magenta} > {cyan}Select an Option From Below{magenta} < {cyan}

{cyan}[{magenta}1{cyan}] Remove Bad Combo Lines
[{magenta}2{cyan}] Remove Bad Proxy Lines
[{magenta}3{cyan}] Remove Duplicate Lines
[{magenta}4{cyan}] Combo Editor
[{magenta}5{cyan}] Email:Pass -> User:Pass
[{magenta}6{cyan}] Add Text After Lines
[{magenta}7{cyan}] Add Text Before Lines
[{magenta}8{cyan}] File Splitter
[{magenta}9{cyan}] User:Pass@Ip:Port -> Ip:Port:User:Pass
[{magenta}10{cyan}] Join the Discord{magenta}
  ''')
  Main()
