from genericpath import isdir, isfile
from typing_extensions import runtime
from PIL.Image import new
import telebot
import sys
from telebot import types
import os
import random
from PIL import ImageGrab
from winsound import Beep
from datetime import datetime
import webbrowser




class data:
    _date = datetime.now()
    _time = _date.strftime("%H%M%S")
    _runtime = _time

    restartCommand = 0
    shutdownCommand = 0


os.system("cls")
print("Bot Is Ready to go !")
print()
#---------------#
# We have to put out bot's token below (which we took from making a new bot )
TOKEN = "2046745444:AAE7k6UzxnPoL97SI0hAE5yhyM0ENI6KyZY"
bot = telebot.TeleBot(TOKEN)
#---------------#

# for fetching files
def getfile(filename):
    myfile = open(filename, "r+")
    return myfile.read()
    myfile.close()

# for putting files
def putfile(filename, filedata):
    myfile = open(filename, "w+")
    return myfile.write(filedata)
    myfile.close()
#--------------#

# this function will work through power oprtions such Shutting down the PC or Restart it
def poweroptions(user):
    userchatid = user.chat.id
    buttons = types.ReplyKeyboardMarkup(row_width=2)
    button1 = types.KeyboardButton("🔴 خاموش")
    button2 = types.KeyboardButton("🔄 ریستارت")
    button3 = types.KeyboardButton("🏠 خانه")
    buttons.add(button1, button2, button3)
    bot.send_message(userchatid, "Welcome to Power Options",
                     reply_markup=buttons)

# - take a screenshot or our pc when it's called -

def takescreenshot(user):
    userchatid = user.chat.id
    bot.send_message(userchatid, "در حال گرفتن اسکرین شات...🧐")
    photo = ImageGrab.grab()
    photo.save("image.png")
    bot.send_message(userchatid, "🥳 اسکرین شات گرفته شد \n در حال ارسال")
    img = open("image.png", "rb")
    bot.send_photo(userchatid, img, caption="اسکرین شات شما")
    img.close()
    os.remove('image.png')
    startcmd(user, 1)

# - playing a sound when the 'play sound' btn pushed - #

def playsoundbt(user):
    usertext = user.text
    userchatid = user.chat.id
    bot.send_message(userchatid, " در حال پخش ...")
    for i in range(1, 5):
        Beep(1000*i, 200)
        Beep(1000*i, 200-(i*50))
    bot.send_message(userchatid, "انجام شد")

# -  - #

def startcmd(user, check):
    userchatid = user.chat.id
    markup = types.ReplyKeyboardMarkup(row_width=2)
    mark1 = types.KeyboardButton("📸 اسکرین شات")
    mark2 = types.KeyboardButton("🔋 گزینه ها")
    mark3 = types.KeyboardButton("🔉 پخش صدا")
    mark4 = types.KeyboardButton("📁 مدیریت فایل ها")
    mark5 = types.KeyboardButton("🌐 مرورگر")
    mark6 = types.KeyboardButton("🗞 بازکردن یک برنامه")
    markup.add(mark1, mark2, mark3, mark4, mark5, mark6)
    bot.send_message(
        userchatid, "🤩 به بات کنترلگر سیستم عامل خوش آمدید", reply_markup=markup)
    _date = datetime.now()
    _time = _date.strftime("%H%M%S")
    runningTime = int(_time)-int(data._runtime)
    if(runningTime > 60):
        runningTime1 = round(runningTime/60)
        runningTime = str(runningTime1)+" دقیقه"
        if(runningTime1 > 3600):
            runningTime1 = runningTime1/3600
            runningTime1 = round(runningTime1)
            runningTime = str(runningTime1)+" ساعت"
    else:
        runningTime = str(runningTime)+" ثانیه"

    PCUserName = os.getlogin()
    CPUusage = os.popen("wmic cpu get loadpercentage").read()
    CPUusage = CPUusage.replace("LoadPercentage", "")

    bot.send_message(userchatid, " 👀 زمان اجرای بات: "+str(runningTime)+"\n 🖥 نام کاربر :‌ "+str(PCUserName)+"\n ⚠️ مقدار مصرفی سی پی یو : "+str(eval(CPUusage))+" %"+"\n🌐🌐🌐🌐🌐🌐🌐🌐🌐🌐")
    if(check == 1):
        print("User "+str(userchatid)+" Backed to home")
    else:
        print("User "+str(userchatid)+" Started The Bot")

# ------------------------------- #

def savetodb(user):
    usertext = user.text
    userchatid = user.chat.id
    thetext = usertext.replace("/save ", "")
    randomnumber = random.randint(11111, 99999)
    putfile("database/data_"+str(randomnumber)+".txt", str(thetext))
    bot.send_message(userchatid, "پیام شما با آیدی " +
                     str(randomnumber)+" ذخیره شد.")

# ------------------------------- #

def dbsavelist(user):
    userchatid = user.chat.id
    listfiles = ""
    for r, d, f in os .walk("database"):
        for file in f:
            listfiles = listfiles + "\n" + str(file)
    bot.send_message(userchatid, "لیست ذخیره شده شما: \n"+str(listfiles))

# -------------- #

def filemManage(user):
    userchatid = user.chat.id
    buttons = types.ReplyKeyboardMarkup(row_width=2)
    button1 = types.KeyboardButton("🏠 خانه")
    button2 = types.KeyboardButton("📥 دانلود")
    button3 = types.KeyboardButton("📋 لیست فایل ها")
    buttons.add(button2, button3, button1)
    bot.send_message(userchatid, "بخش مدیریت فایل ها", reply_markup=buttons)

# -------------------------------#

def download(user):
    userchatid = user.chat.id
    bot.send_message(userchatid, "نحوه استفاده: \n/download [file name/file address]")
    

# ------------------------------- #
def shutdown(user):
    data.restartCommand = 0
    data.shutdownCommand = 1
    userchatid = user.chat.id
    bot.send_message(userchatid, "آیا از خاموش کردن کامپیوتر خود اطمینان دارید؟ \n بله / خیر")

# ------------------------------- #

def restart(user):
    data.restartCommand = 1
    data.shutdownCommand = 0
    userchatid = user.chat.id
    bot.send_message(userchatid, "آیا از ریستارت کردن کامپیوتر خود اطمینان دارید؟ \n بله / خیر")

# ------------------------------- #

def noUserResponseOnShudown(user):
    userchatid = user.chat.id
    data.restartCommand = 0
    data.shutdownCommand = 0
    bot.send_message(userchatid, "لغو عملیات")

# ------------------------------- #

def webBrowser(user):
    userchatid = user.chat.id
    bot.send_message(userchatid, "نحوه استفاده: \n/web [address]")

# ------------------------------- #

def application(user):
    userchatid = user.chat.id
    bot.send_message(userchatid, "نحوه استفاده: \n/openapplication [name]")

# ------------------------------- #

def downloadFile(user):
    usertext = user.text
    userchatid = user.chat.id
    fileName = usertext.replace("/download ", "")
    if(os.path.isdir(str(fileName))):
        bot.send_message(userchatid, "پوشه :‌ "+str(fileName))
    else:
        if(os.path.isfile(str(fileName))):
            bot.send_message(userchatid, "در حال دانلود: "+str(fileName)+ "...")
            file = open(fileName, "rb")
            bot.send_document(userchatid, file, caption="فایل شما")
        else:
            bot.send_message(userchatid, "فایل مورد نظر پیدا نشد")


# ------------------------------- #

def shutdownOrRestart(user):
    userchatid = user.chat.id
    if(data.shutdownCommand == 1 and data.restartCommand == 0):
        bot.send_message(userchatid, "درحال خاموش کردن کردن")
        data.shutdownCommand = 0
        data.restartCommand = 0
        os.system("shutdown /s /t 1")
    elif(data.restartCommand == 1 and data.shutdownCommand == 0):
        bot.send_message(userchatid, "درحال ریستارت کردن")
        data.shutdownCommand = 0
        data.restartCommand = 0
        os.system("shutdown /r /t 1")
    else:
        bot.send_message(userchatid, "پروسه متوقف شد !!")
# ------------------------------- #

def fileList(user):
    userchatid = user.chat.id
    bot.send_message(userchatid, "نحوه استفاده : \n/filemanager [dir]")
# ------------------------------- #

def openWeb(user):
    userchatid = user.chat.id
    usertext = user.text
    webAdd = usertext.replace("/web ", "")
    bot.send_message(userchatid, "در حال اجرا ..."+webAdd+"...")
    webbrowser.open(webAdd, new=1)
    bot.send_message(userchatid, "انجام شد!")

# ------------------------------- #

def openApp(user):
    userchatid = user.chat.id
    usertext = user.text
    appName = usertext.replace("/openapplication ", "")
    bot.send_message(userchatid, "در حال فراخوانی")
    result = os.system("start "+appName)
    try:
        if(result == 0):
            bot.send_message(userchatid, "انجام شد!")
        else:
            bot.send_message(userchatid, "انجام نشد")
    except:
        bot.send_message(userchatid, "خطا")
# ------------------------------- #
# this method will control file manager list
def fileManagerList(user):
    userchatid = user.chat.id
    usertext = user.text
    dir = usertext.replace("/filemanager ", "")
    if(os.path.isdir(dir)):
        bot.send_message(userchatid, " 🔎 در حال جستجو...")
        fcount = 0
        flist = ""
        filesCount = 0
        fileList = ""

        for r, d, f, in os.walk(dir):
            for folder in d:
                if(fcount >= 30):
                    break
                else:
                    if("\\" in r):
                        pass
                    else:
                        fcount += 1
                        flist = flist+"\n"+"📂 "+r+"/"+folder
            for file in f:
                if(filesCount >= 30):
                    break
                else:
                    filesCount += 1
                    fileList = fileList+"\n"+"👉🗂 "+r+"\\"+file
        bot.send_message(userchatid, "۳۰ پوشه اول : \n\n"+str(flist))
        bot.send_message(userchatid, "۳۰ فایل اول : \n\n"+str(fileList))
    else:
        bot.send_message(userchatid, "پوشه مورد نظر پیدا نشد :(")

# ------------------------------- #

@bot.message_handler(content_types=['text'])
def botmain(user):
    admin = "arminf_za" #admin ID
    usertext = user.text
    userchatid = user.chat.id
    userusername = user.chat.username
    #------------------------------------#
    if(userusername == admin):
        if(usertext == "/start" or usertext == "🏠 خانه"):
            if(usertext == "🏠 خانه"):
                check = 1
            else:
                check = 2

            startcmd(user, check)

    if(usertext == "/save"):
        bot.send_message(userchatid, "نحوه استفاده : \n/save  متن")

    if(usertext.startswith("/save ")):
        savetodb(user)

    if(usertext == "/savelist"):
        dbsavelist(user)

    if(usertext == "🔋 گزینه ها"):
        poweroptions(user)

    if(usertext == "📸 اسکرین شات"):
        takescreenshot(user)

    if(usertext == "🔉 پخش صدا"):
        playsoundbt(user)

    if(usertext == "🔴 خاموش"):
        shutdown(user)

    if(usertext == "🔄 ریستارت"):
        restart(user)

    if(usertext == "بله"):
        shutdownOrRestart(user)

    if(usertext == "خیر"):
        noUserResponseOnShudown(user)

    if(usertext == "📁 مدیریت فایل ها"):
        filemManage(user)

    if(usertext == "📥 دانلود"):
        download(user)

    if(usertext.startswith("/download ")):
        downloadFile(user)

    if (usertext == "/download"):
        download(user)

    if (usertext == "/📋 لیست فایل ها" or usertext == "/filemanager"):
        fileList(user)

    if(usertext.startswith("/filemanager")):
        fileManagerList(user)

    if(usertext == "🌐 مرورگر" or usertext == "/web"):
        webBrowser(user)

    if(usertext.startswith("/web ")):
        openWeb(user)

    if (usertext == "🗞 بازکردن یک برنامه" or usertext == "/openapplication"):
        application(user)

    if(usertext.startswith("/openapplication ")):
        openApp(user)        
    else:
        pass
#---------------#
bot.polling(True)
