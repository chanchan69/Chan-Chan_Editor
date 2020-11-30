import requests
from colorama import Fore, Style, init
from os import system
class Main():
  def __init__(self):
    self.start()

  def remove_bad_lines(self, wombo, outfile):
    outfile = open(outfile, "w+")
    for line in wombo:
      if '@' and ':' and '.' in line:
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

  def inputs(self):
      self.userinputfile = input(f'{cyan}[{magenta}1{cyan}] Combo File:{magenta} ')
      self.uoutput = input(f'{cyan}[{magenta}2{cyan}] Output File:{magenta} ')
      self.uinput = open(self.userinputfile, 'r+')

  def start(self):
    print(sign)
    print(main_menu)
    user_input = input(f'{cyan}>{magenta} ')
    system('cls')
    self.inputs()
    if user_input == '1':
      self.remove_bad_lines(self.uinput, self.uoutput)

    elif user_input == '2':
      self.remove_dupe_lines(self.uinput, self.uoutput)

    elif user_input == '3':
      self.email_to_user(self.uinput, self.uoutput)

    elif user_input == '4':
      addtext = input(f'{cyan}[{magenta}3{cyan}] Text to Add:{magenta} ')
      self.add_text_after_line(self.uinput, self.uoutput, addtext)

    elif user_input == '5':
      addtext = input(f'{cyan}[{magenta}3{cyan}] Text to Add:{magenta} ')
      self.add_text_before_line(self.uinput, self.uoutput, addtext)
    
    elif user_input == '6':
      segments = int(input(f'{cyan}[{magenta}3{cyan}] How Many Files:{magenta} '))
      self.file_spliter(self.userinputfile, self.uoutput, segments)

    elif user_input == '7':
      print(f'{cyan}Opening Link in Your Web Browser\n')
      import webbrowser
      new = 2
      url = "https://discord.gg/f32CZay9r3"
      webbrowser.open(url, new=new)
      print(f'{Fore.GREEN}Done opening link')
      print(f'{Fore.CYAN}')

if __name__ == '__main__':
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

{cyan}[{magenta}1{cyan}] Remove Bad Lines
[{magenta}2{cyan}] Remove Duplicate Lines
[{magenta}3{cyan}] Email:Pass to User:Pass
[{magenta}4{cyan}] Add Text After Lines
[{magenta}5{cyan}] Add Text Before Lines
[{magenta}6{cyan}] File Splitter
[{magenta}7{cyan}] Join the Discord{magenta}
  ''')
  Main()