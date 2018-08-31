from GENERATOR import *
from datetime import datetime
from time import sleep
from bs4 import BeautifulSoup
from gtts import gTTS
from googletrans import Translator
from multiprocessing import Pool, Process
#from ffmpy import FFmpeg
import time, random, asyncio, timeit, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, urllib, urllib.parse, ast, pytz, wikipedia, pafy, youtube_dl, atexit

print ("\n\n============= HI =============\n")

#cl = RIDEN()
cl = RIDEN(authTokenRFU="EwjA7BGA87lPrc4L0zU9.grzYgOnTdKvSkrQ7FTsKMq.TmsMcUZV6F1pLmV4TxQ5RDSN8NwxUg/x9iFFmCoYF6s=")
cl.log("YOUR TOKEN : {}".format(str(cl.authToken)))
channel = RIDENChannel(cl,cl.server.CHANNEL_ID['LINE_TIMELINE'])
cl.log("CHANNEL TOKEN : " + str(channel.getChannelResult()))

print ("LOGIN SUCCESS")

clProfile = cl.getProfile()
clSettings = cl.getSettings()
RIDEN = RIDENPoll(cl)

Rfu = [cl]
mid = cl.profile.mid
RfuBot=[mid]
Owner=["uac8e3eaf1eb2a55770bf10c3b2357c33"]
RfuSekawan = RfuBot + Rfu + Owner

contact = cl.getProfile()
backup = cl.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

Squad = {
    "Contact":False,
    "GName":"PUYからコミュニティにシンプル",
    "AutoRespon":False,
    "KickRespon":False,
    "autoAdd":True,
    "PesanAdd":"",
    "ContactAdd":{},
    "autoJoin":True,
    "AutojoinTicket":True,
    "AutoReject":False,
    "autoRead":False,
    "Timeline":False,
    "Welcome":False,
    "WcText": "Selamat Datang",
    "Leave":False,
    "WvText": "Selamat Jalan",
    "Adminadd":False,
    "AdminDel":False,
    "readMember":{},
    "readPoint":{},
    "readTime":{},
    "ROM":{},
    "AddMention":True,
    "Admin": {
        "uac8e3eaf1eb2a55770bf10c3b2357c33":True,  #MID ADMIN HERE
        "uac8e3eaf1eb2a55770bf10c3b2357c33":True
    },
}

Mozilla = {
    "userAgent": [
        "Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
        "Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 FirePHP/0.5",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux ppc; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux AMD64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1.1; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; U; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; rv:5.0) Gecko/20100101 Firefox/5.0"
    ],
    "mimic": {
        "copy": False,
        "conpp": False,
        "status": False,
        "target": {}
    }
}

setTime = {}
setTime = Squad['readTime']
mulai = time.time()
msg_dict = {}

ProfileMe = {
    "displayName": "",
	"statusMessage": "",
	"pictureStatus": ""
}
ProfileMe["displayName"] = clProfile.displayName
ProfileMe["statusMessage"] = clProfile.statusMessage
ProfileMe["pictureStatus"] = clProfile.pictureStatus

RfuCctv={
    "Point1":{},
    "Point2":{},
    "Point3":{}
}

Helpz ="""    「 Favs 」
Tagall / Mentionall
Ceksider on/off
 'Ceksider' :
  Melihat Pembaca.
 'Recheck' :
  Mengulang titik Pembaca
Getsider on/off
Groupinfo
Url on/off
Geturl
@Me
Calendar
Wikipedia: [query]
Write [query]

  「 Token - OFFLINE 」
Tokenlist/offline

'''Once Again, An JUST FOR FUN!'''

『 @About : to See a Creator 』
『 @Bye : Bot Out 』"""

#------------------------------------------------ SCRIP DEF ----------------------------------------------------------#

def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)

def logError(text):
    client.log("[ ERROR ] {}".format(str(text)))
    tz = pytz.timezone("Asia/Jakarta")
    timeNow = datetime.now(tz=tz)
    timeHours = datetime.strftime(timeNow,"(%H:%M)")
    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
    inihari = datetime.now(tz=tz)
    hr = inihari.strftime('%A')
    bln = inihari.strftime('%m')
    for i in range(len(day)):
        if hr == day[i]: hasil = hari[i]
    for k in range(0, len(bulan)):
        if bln == str(k): bln = bulan[k-1]
    time = "{}, {} - {} - {} | {}".format(str(hasil), str(inihari.strftime('%d')), str(bln), str(inihari.strftime('%Y')), str(inihari.strftime('%H:%M:%S')))
    with open("errorLog.txt","a") as error:
        error.write("\n[{}] {}".format(str(time), text))

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def RIDEN_FAST_USER(fast):
    try:
        if fast.type == 0:
            return
        if fast.type == 5:
            if Squad["autoAdd"] == True:
                if (Squad["PesanAdd"] in [""," ","\n",None]):
                    pass
                else:
                    Squad["ContactAdd"][fast.param2] = True
                    usr = cl.getContact(op.param2)
                    cl.sendMessage(fast.param1, "Haii {} " + str(Squad["PesanAdd"]).format(usr.displayName))
                    cl.sendMessage(fast.param1, None, contentMetadata={'mid':mid}, contentType=13)
#--------------------------------------------- PARAM SCRIP AUTO JOIN BOT & AUTO REJECT ------------------------------------------------#
        if fast.type == 13:
            if mid in fast.param3:
              if Squad['autoJoin'] == True:
                if fast.param2 in RfuSekawan and fast.param2 in Squad["Admin"]:
                    cl.acceptGroupInvitation(fast.param1)
                    ginfo = cl.getGroup(fast.param1)
                    _session = requests.session()
                    image = "https://lh3.googleusercontent.com/proxy/-qcXIaVI5RPLI_rZgSi8T-QyHCDuVXRoFQUksJ2tzKKOGt8vGLQ6EW7yZBO9SIpQ0b5GlZgahj8S4lENJRr2PDK7jN-vPImkR628uGfvOlr3HpSjBCWrGfCGiOsj9pT7PjH8OuZ6bZ7_9RB7tTeUcmld8U5z=w256-h256-nc"
                    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                    headers = {
                        "Host": "game.linefriends.com",
                        "Content-Type": "application/json",
                        "User-Agent": "Mozilla/5.0",
                        "Referer": "https://game.linefriends.com/cdn/jbp-lcs/"
                    }
                    data = {
                        "cc": "UXfpO//D+K6TlqsIBX4AhlamXjhsCUtI1/lWa0zxvp3YA3BlQFwCS8cEKWXBtSJO2cwDtNmbXRA6QPIDBiHbvDOODNoaDQgv6Vno900RzrJ+orAi+vCx9BymUUoebOT3RRtTaJHTYL3AiHLB1MlUdOJvGf7QqPih3p1WUxvWG1v+Tol4W/zAEFdXld5bYneQI3YAZjUn8Ejekfh3qwEHu30f9IayoJs1IwU5C45QMS8Qfu73cln4qH90pgOiQ2Yq15ZJ68/0/Amwy46C5ugyoqookxI4/Oh+Iu+tjT0VtP2Fv5/YoNCKOwbrsw2jHAvL8ACR1qVJj2NesAHkB7fDzC6Ncb0mbxQ5/r1P8oQ1Gbk",
                        "to": fast.param1,
                        "messages": [
                            {
                                "type": "flex",
                                "altText": "Puy",
                                "contents": {
                                    "type": "bubble",
                                    "body": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "「 Joined Groups 」\n", #% (elapsed_time),
                                                "size": "md",
                                                "weight": "bold",
                                                "align": "center",
                                                "gravity": "top",
                                                "color": "#000000",
                                            },
                                            {
                                                "type": "text",
                                                #"text": "%s" % (elapsed_time),
                                                "text": "Terimakasih sudah mengundang saya ke group '{}' ketik Help untuk Bantuan!".format(str(ginfo.name)),
                                                #str(" "+ginfo.name+" ")
                                                "size": "md",
                                                "align": "center",
                                                "gravity": "top",
                                                "color": "#0000ff",
                                                "wrap": True
                                            }
                                        ]
                                    }
                                }
                            }
                        ]
                    }
                    data = json.dumps(data)
                    sendPost = _session.post(url, data=data, headers=headers)
                    print ("ANDA JOIN DI GRUP")

        if fast.type == 13:
            if mid in fast.param3:
              if Squad['AutoReject'] == True:
                if fast.param2 not in RfuSekawan and fast.param2 not in Squad["Admin"]:
                    gid = cl.getGroupIdsInvited()
                    for i in gid:
                        cl.rejectGroupInvitation(i)
#------------------- ( 1 ) ------------------------- PEMBATAS SCRIP SIDER & WC LV ------------------------------------------------#

        elif fast.type == 55:
            try:
                if RfuCctv['Point1'][fast.param1]==True:
                    if fast.param1 in RfuCctv['Point2']:
                        Name = cl.getContact(fast.param2).displayName
                        if Name in RfuCctv['Point3'][fast.param1]:
                            pass
                        else:
                            RfuCctv['Point3'][fast.param1] += "「" + Name + "」 \n"
                            if " " in Name:
                                nick = Name.split(' ')
                                if len(nick) == 2:
                                    cl.mentionWithRFU(fast.param1,fast.param2,"and the Reader Comes ","" + " ")
                                else:
                                    cl.mentionWithRFU(fast.param1,fast.param2,"Hei, ","" + "What are You doing There")
                            else:
                                cl.mentionWithRFU(fast.param1,fast.param2,"Hellooo, ","" + "Comeon Join the Conversation")
                    else:
                        cl.mentionWithRFU(fast.param1,fast.param2,"Hei, ","" + "How are you today?")
                else:
                    pass
            except:
                pass

        if fast.type == 55:
            try:
                if fast.param1 in Squad['readPoint']:
                    if fast.param2 in Squad['readMember'][fast.param1]:
                        pass
                    else:
                        Squad['readMember'][fast.param1] += fast.param2
                    Squad['ROM'][fast.param1][fast.param2] = fast.param2
                else:
                   pass
            except:
                pass

        if fast.type == 17:
            if Squad["Welcome"] == True:
                if fast.param2 not in Rfu:
                    #cl.sendText(kirim,"さようなら\n" + str(" "+ginfo.name+" "))
                    ginfo = cl.getGroup(fast.param1)
                    contact = cl.getContact(fast.param1)
                    _session = requests.session()
                    image = "https://lh3.googleusercontent.com/proxy/-qcXIaVI5RPLI_rZgSi8T-QyHCDuVXRoFQUksJ2tzKKOGt8vGLQ6EW7yZBO9SIpQ0b5GlZgahj8S4lENJRr2PDK7jN-vPImkR628uGfvOlr3HpSjBCWrGfCGiOsj9pT7PjH8OuZ6bZ7_9RB7tTeUcmld8U5z=w256-h256-nc"
                    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                    headers = {
                        "Host": "game.linefriends.com",
                        "Content-Type": "application/json",
                        "User-Agent": "Mozilla/5.0",
                        "Referer": "https://game.linefriends.com/cdn/jbp-lcs/"
                    }
                    data = {
                        "cc": "UXfpO//D+K6TlqsIBX4AhlamXjhsCUtI1/lWa0zxvp3YA3BlQFwCS8cEKWXBtSJO2cwDtNmbXRA6QPIDBiHbvDOODNoaDQgv6Vno900RzrJ+orAi+vCx9BymUUoebOT3RRtTaJHTYL3AiHLB1MlUdOJvGf7QqPih3p1WUxvWG1v+Tol4W/zAEFdXld5bYneQI3YAZjUn8Ejekfh3qwEHu30f9IayoJs1IwU5C45QMS8Qfu73cln4qH90pgOiQ2Yq15ZJ68/0/Amwy46C5ugyoqookxI4/Oh+Iu+tjT0VtP2Fv5/YoNCKOwbrsw2jHAvL8ACR1qVJj2NesAHkB7fDzC6Ncb0mbxQ5/r1P8oQ1Gbk",
                        "to": fast.param1,
                        "messages": [
                            {
                                "type": "flex",
                                "altText": "Puy",
                                "contents": {
                                    "type": "bubble",
                                    "body": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "   「 Member Joined 」\n", #% (elapsed_time),
                                                "size": "md",
                                                "weight": "bold",
                                                "align": "center",
                                                "gravity": "top",
                                                "color": "#000000",
                                            },
                                            {
                                                "type": "text",
                                                #"text": "%s" % (elapsed_time),
                                                "text": "Selamat Datang di {}{}".format(str(contact.displayName)),
                                                #.format(str(contact.displayName))
                                                #.format(str(ginfo.name)),
                                                "size": "md",
                                                "align": "center",
                                                "gravity": "top",
                                                "color": "#0000ff",
                                                "wrap": True
                                            }
                                        ]
                                    }
                                }
                            }
                        ]
                    }
                    data = json.dumps(data)
                    sendPost = _session.post(url, data=data, headers=headers)
                    #cl.mentionWithRFU(fast.param1,fast.param2," Hello","" + "\n " + str(Squad['WcText']))
                    #cl.sendMessage(fast.param1, None, contentMetadata={'mid':fast.param2}, contentType=13)
                    print ("MEMBER HAS JOIN THE GROUP")

        if fast.type == 15:
            if Squad["Leave"] == True:
                if fast.param2 not in Rfu:
                    ginfo = cl.getGroup(fast.param1)
                    cl.mentionWithRFU(fast.param1,fast.param2," Hello","" + "\n " + str(Squad['LvText']))
                    cl.sendMessage(fast.param1, None, contentMetadata={'mid':fast.param2}, contentType=13)
                    print ("MEMBER HAS LEFT THE GROUP")

#--------------------------------------------- PARAM SCRIP ------------------------------------------------#

        if fast.type == 46:
            if fast.param2 in RfuBot:
                cl.removeAllMessages()

#------------------- ( 2 ) ------------------------- PEMBATAS SCRIP ------------------------------------------------#

        if fast.type == 26:
            msg = fast.message
            text = msg.text
            rfuText = msg.text
            msg_id = msg.id
            kirim = msg.to
            user = msg._from
            if msg.toType == 0 or msg.toType == 2:
                if msg.toType == 0:
                    to = kirim
                elif msg.toType == 2:
                    to = kirim
                if msg.contentType == 0:
                    if Squad["autoRead"] == True:
                        cl.sendChatChecked(kirim, msg_id)
                    if kirim in Squad["readPoint"]:
                        if user not in Squad["ROM"][kirim]:
                            Squad["ROM"][kirim][user] = True
                    if user in Mozilla["mimic"]["target"] and Mozilla["mimic"]["status"] == True and Mozilla["mimic"]["target"][user] == True:
                        text = msg.text
                        if text is not None:
                            cl.sendMessage(kirim,text)
                    if Squad["Timeline"] == True:
                       if msg.contentType == 16:
                            ret_ = " ㄔPosting Infoㄔ\n"
                            if msg.contentMetadata["serviceType"] == "GB":
                                contact = cl.getContact(user)
                                auth = "\n Author : {}".format(str(contact.displayName))
                            else:
                                auth = "\n Author : {}".format(str(contact.displayName))
                                ret_ += auth
                            if "stickerId" in msg.contentMetadata:
                                stck = "\n Sticker : https://line.me/R/shop/detail/{}".format(str(msg.contentMetadata["packageId"]))
                                ret_ += stck
                            if "mediaOid" in msg.contentMetadata:
                                object_ = msg.contentMetadata["mediaOid"].replace("svc=myhome|sid=h|","")
                                if msg.contentMetadata["mediaType"] == "V":
                                    if msg.contentMetadata["serviceType"] == "GB":
                                        ourl = "\n Object Url : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                        murl = "\n Media Url : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(msg.contentMetadata["mediaOid"]))
                                    else:
                                        ourl = "\n Object Url : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                        murl = "\n Media Url : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(object_))
                                    ret_ += murl
                                else:
                                    if msg.contentMetadata["serviceType"] == "GB":
                                        ourl = "\n Object Url : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                    else:
                                        ourl = "\n Objek Url : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                ret_ += ourl
                            if "text" in msg.contentMetadata:
                                dia = cl.getContact(user)
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan = 'Pengirim: '
                                xteam = str(dia.displayName)
                                pesan = ''
                                pesan2 = pesan+"@ARDIAN_GANTENG\n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':dia.mid}
                                zx2.append(zx)
                                kata = "\n Text : {}".format(str(msg.contentMetadata["text"]))
                                purl = "\n Post Url : {}".format(str(msg.contentMetadata["postEndUrl"]).replace("line://","https://line.me/R/"))
                                ret_ += purl
                                ret_ += kata
                                zxc += pesan2
                                pesan = xpesan + zxc + ret_ + ""
                                cl.sendMessage(kirim, pesan, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)

        #if fast.type in [25,26]:
        #    msg = fast.message
        #    user = msg._from
        #    kirim = msg.to
        #    if msg.contentType == 7:
        #        if Squad['IDSticker'] == True:
        #            stk_id = msg.contentMetadata['STKID']
        #            stk_ver = msg.contentMetadata['STKVER']
        #            pkg_id = msg.contentMetadata['STKPKGID']
        #            filler = "┗ STICKER CHECK ┛\nSTKID : %s\nSTKPKGID : %s\nSTKVER : %s\n\nLink\n\nline://shop/detail/%s" % (stk_id,pkg_id,stk_ver,pkg_id)
        #            cl.mentionWithRFU(kirim,user," ┗ Sticker Code ┛\n","" + "\n\n" + str(filler))
        #        else:
        #            pass

        #if fast.type == 25 or fast.type == 26:
        #    msg = fast.message
        #    user = msg._from
        #    kirim = msg.to
        #    if msg.contentType == 1:
        #      if Squad['Upfoto'] == True:
        #        if user in Owner:
        #            path = cl.downloadObjectMsg(msg.id)
        #            cl.updateProfilePicture(path)
        #            cl.mentionWithRFU(kirim,user,"┗ Update Picture Success ┛","")
        #            Squad['Upfoto'] = False

#======= AUTO TAG & CHAT BATAS SCRIP ========#
        if fast.type == 26:
            msg = fast.message
            user = msg._from
            kirim = msg.to
            if msg.contentType == 0 and user not in mid and msg.toType == 2:
                if "MENTION" in msg.contentMetadata.keys() != None:
                    if Squad['AutoRespon'] == True:
                        contact = cl.getContact(user)
                        cName = contact.displayName
                        balas = [cName + "\n" + str(Squad['MentionText'])]
                        ret_ = "" + random.choice(balas)
                        name = re.findall(r'@(\w+)', msg.text)
                        mention = ast.literal_eval(msg.contentMetadata["MENTION"])
                        mentionees = mention['MENTIONEES']
                        for mention in mentionees:
                              if mention['M'] in mid:
                                  cl.mentionWithRFU(kirim,user,"","" +str(ret_))
                                  break

        if fast.type == 26:
            msg = fast.message
            user = msg._from
            kirim = msg.to
            if msg.contentType == 0 and user not in RfuSekawan or user not in Squad["Admin"]:
                if "MENTION" in msg.contentMetadata.keys() != None:
                    if Squad['KickRespon'] == True:
                        contact = cl.getContact(user)
                        cName = contact.displayName
                        balas = [cName + "   『 Auto Reply 』\nWhat's Important?","   『 Auto Reply 』\nWas Sleeping"]
                        ret_ = "" + random.choice(balas)
                        name = re.findall(r'@(\w+)', msg.text)
                        mention = ast.literal_eval(msg.contentMetadata["MENTION"])
                        mentionees = mention['MENTIONEES']
                        for mention in mentionees:
                              if mention['M'] in mid:
                                  cl.mentionWithRFU(kirim,user,"","" +str(ret_))
                                  cl.kickoutFromGroup(kirim,[user])
                                  break

#------------------- ( 3 ) ------------------------- PEMBATAS SCRIP ------------------------------------------------#

        if fast.type == 25 or fast.type == 26:
            msg = fast.message
            text = msg.text
            rfuText = msg.text
            msg_id = msg.id
            kirim = msg.to
            user = msg._from
            if msg.toType == 0 or msg.toType == 2:
                if msg.toType == 0:
                    to = kirim
                elif msg.toType == 2:
                    to = kirim
                if msg.contentType == 0:
                    if Squad["autoRead"] == True:
                        cl.sendChatChecked(0, msg_id)

                    elif rfuText is None:
                        return
                    else:
                        if rfuText.lower() == 'PROSES TRANSISI':
                            cl.sendMessage(0, user)

                        elif rfuText.lower() == "help":
                            if user in RfuSekawan or user in Squad["Admin"]:
                                 cl.sendMessage(kirim, str(Helpz))

                        elif rfuText.lower() == "devlist":
                            if user in RfuSekawan or user in Squad["Admin"]:
                                rfu = ""
                                sekawan = ""
                                wa = 0
                                wi = 0
                                for m_id in Owner:
                                    wa = wa + 1
                                    end = '\n'
                                    rfu += str(wa) + ". " +cl.getContact(m_id).displayName + "\n"
                                for m_id in Squad["Admin"]:
                                    wi = wi + 1
                                    end = '\n'
                                    sekawan += str(wi) + ". " +cl.getContact(m_id).displayName + "\n"
                                cl.sendText(kirim,"     「 Devlist 」\nOwner :\n"+rfu+"\nAdmin :\n"+sekawan+" ") #+ str(len(Owner)+len(Squad["Admin"])))

                        elif rfuText.lower() == "@bye": #With INDUK
                                ginfo = cl.getGroup(kirim)
                                _session = requests.session()
                                image = "https://lh3.googleusercontent.com/proxy/-qcXIaVI5RPLI_rZgSi8T-QyHCDuVXRoFQUksJ2tzKKOGt8vGLQ6EW7yZBO9SIpQ0b5GlZgahj8S4lENJRr2PDK7jN-vPImkR628uGfvOlr3HpSjBCWrGfCGiOsj9pT7PjH8OuZ6bZ7_9RB7tTeUcmld8U5z=w256-h256-nc"
                                url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                headers = {
                                    "Host": "game.linefriends.com",
                                    "Content-Type": "application/json",
                                    "User-Agent": "Mozilla/5.0",
                                    "Referer": "https://game.linefriends.com/cdn/jbp-lcs/"
                                }
                                data = {
                                    "cc": "UXfpO//D+K6TlqsIBX4AhlamXjhsCUtI1/lWa0zxvp3YA3BlQFwCS8cEKWXBtSJO2cwDtNmbXRA6QPIDBiHbvDOODNoaDQgv6Vno900RzrJ+orAi+vCx9BymUUoebOT3RRtTaJHTYL3AiHLB1MlUdOJvGf7QqPih3p1WUxvWG1v+Tol4W/zAEFdXld5bYneQI3YAZjUn8Ejekfh3qwEHu30f9IayoJs1IwU5C45QMS8Qfu73cln4qH90pgOiQ2Yq15ZJ68/0/Amwy46C5ugyoqookxI4/Oh+Iu+tjT0VtP2Fv5/YoNCKOwbrsw2jHAvL8ACR1qVJj2NesAHkB7fDzC6Ncb0mbxQ5/r1P8oQ1Gbk",
                                    "to": to,
                                    "messages": [
                                        {
                                            "type": "flex",
                                            "altText": "Puy",
                                            "contents": {
                                                "type": "bubble",
                                                "body": {
                                                    "type": "box",
                                                    "layout": "vertical",
                                                    "contents": [
                                                        {
                                                            "type": "text",
                                                            "text": "   「 Out Group 」\n", #% (elapsed_time),
                                                            "size": "md",
                                                            "weight": "bold",
                                                            "align": "center",
                                                            "gravity": "top",
                                                            "color": "#000000",
                                                        },
                                                        {
                                                            "type": "text",
                                                            "text": "Dadah '{}' Invite kembali jika Perlu.".format(str(ginfo.name)),
                                                            "size": "sm",
                                                            "align": "center",
                                                            "gravity": "top",
                                                            "color": "#0000ff",
                                                            "wrap": True
                                                        }
                                                    ]
                                                }
                                            }
                                        }
                                    ]
                                }
                                data = json.dumps(data)
                                sendPost = _session.post(url, data=data, headers=headers)
                                #cl.sendText(kirim,"さようなら\n" + str(" "+ginfo.name+" "))
                                cl.leaveGroup(kirim)

                        elif rfuText.lower() == "leaveall grup":
                            if user in RfuSekawan or user in Squad["Admin"]:
                                gid = cl.getGroupIdsJoined()
                                for i in gid:
                                    cl.leaveGroup(i)
                                    print ("Leave All group")

                        elif rfuText.lower() == 'url on':
                            #if user in RfuSekawan or user in Squad["Admin"]:
                                if msg.toType == 2:
                                    group = cl.getGroup(kirim)
                                    group.preventedJoinByTicket = False
                                    cl.updateGroup(group)

                        #elif rfuText.lower() == '+user': #and msg._from in ["uac8e3eaf1eb2a55770bf10c3b2357c33"]:
                        #  if user in RfuSekawan or user in Squad["Admin"]:
                        #    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        #        key = eval(msg.contentMetadata["MENTION"])
                        #        key1 = key["MENTIONEES"][0]["M"]
                        #        if key1 not in wait['info']:
                        #            pay = time.time()
                        #            nama = str(cl.split(' ')[1])
                        #            wait['name'][nama] =  {"user":nama,"mid":key1,"pay":pay+60*60*24*120,"runtime":pay,"token":{}}
                        #            wait['info'][key1] =  '%s' % nama
                        #            sendMention(msg.to, '@!telah Ditambahkan.','「 ADD SERVICE 」', [key1])
                        #        else:
                        #            cl.sendMessage(msg.to, 'Gagal!','「 ADD SERVICE 」', [key1])
                        #elif rfuText.lower() == '-user': #and msg._from in ["uac8e3eaf1eb2a55770bf10c3b2357c33"]:
                        #  if user in RfuSekawan or user in Squad["Admin"]:
                        #    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        #        key = eval(msg.contentMetadata["MENTION"])
                        #        key1 = key["MENTIONEES"][0]["M"]
                        #        if key1 in wait['info']:
                        #            b = wait['info'][key1]
                        #            os.system('screen -S %s -X kill'%b)
                        #            h =  wait['name'][b]
                        #            try:subprocess.getoutput('rm {}.py protect/{}.json'.format(b,b))
                        #            except:pass
                        #            del wait['info'][key1]
                        #            del wait['name'][b]
                        #            sendMention(msg.to, '@!telah Dihapus dari servis.','「 DEL SERVICE 」', [key1])
                        #        else:
                        #            sendMention(msg.to, 'Maaf, @!tidak terdaftar.','「 DEL SERVICE 」', [key1])

                        elif rfuText.lower() == 'url off':
                            #if user in RfuSekawan or user in Squad["Admin"]:
                                if msg.toType == 2:
                                    group = cl.getGroup(kirim)
                                    group.preventedJoinByTicket = True
                                    cl.updateGroup(group)

                        elif rfuText.lower() == 'geturl':
                          #if user in RfuSekawan or user in Squad["Admin"]:
                            if msg.toType == 2:
                                grup = cl.getGroup(kirim)
                                if grup.preventedJoinByTicket == True:
                                   grup.preventedJoinByTicket == False
                                   cl.updateGroup(grup)
                                set = cl.reissueGroupTicket(kirim)
                                cl.sendMessage(kirim, "  Group Ticket : \nhttps://line.me/R/ti/g/{}".format(str(set)))
                                #else:
                                    #cl.sendMessage(kirim, "Ketik Link on Dulu kaka")

                        elif rfuText.lower() == 'groupinfo':
                                group = cl.getGroup(kirim)
                                try:
                                    gCreator = group.creator.displayName
                                except:
                                    gCreator = "Not found"
                                if group.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(group.invitee))
                                if group.preventedJoinByTicket == True:
                                    gQr = "Mati"
                                    gTicket = "Mati"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(line.reissueGroupTicket(group.id)))
                                cuki = " "
                                cuki += "Group Name : {}".format(str(group.name))
                                #cuki += "\nID Group : {}".format(group.id)
                                cuki += "\nGroup Creator : {}".format(str(gCreator))
                                cuki += "\nMembers : {}".format(str(len(group.members)))
                                cuki += "\nPendings Member : {}".format(gPending)
                                cuki += "\nGroup Ticket Status : {}".format(gTicket)
                                cuki += "\nGroup Qr : {}".format(gQr)
                                #cl.sendMessage(kirim, str(cuki))
                                _session = requests.session()
                                image = "https://lh3.googleusercontent.com/proxy/-qcXIaVI5RPLI_rZgSi8T-QyHCDuVXRoFQUksJ2tzKKOGt8vGLQ6EW7yZBO9SIpQ0b5GlZgahj8S4lENJRr2PDK7jN-vPImkR628uGfvOlr3HpSjBCWrGfCGiOsj9pT7PjH8OuZ6bZ7_9RB7tTeUcmld8U5z=w256-h256-nc"
                                url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                headers = {
                                    "Host": "game.linefriends.com",
                                    "Content-Type": "application/json",
                                    "User-Agent": "Mozilla/5.0",
                                    "Referer": "https://game.linefriends.com/cdn/jbp-lcs/"
                                }
                                data = {
                                    "cc": "UXfpO//D+K6TlqsIBX4AhlamXjhsCUtI1/lWa0zxvp3YA3BlQFwCS8cEKWXBtSJO2cwDtNmbXRA6QPIDBiHbvDOODNoaDQgv6Vno900RzrJ+orAi+vCx9BymUUoebOT3RRtTaJHTYL3AiHLB1MlUdOJvGf7QqPih3p1WUxvWG1v+Tol4W/zAEFdXld5bYneQI3YAZjUn8Ejekfh3qwEHu30f9IayoJs1IwU5C45QMS8Qfu73cln4qH90pgOiQ2Yq15ZJ68/0/Amwy46C5ugyoqookxI4/Oh+Iu+tjT0VtP2Fv5/YoNCKOwbrsw2jHAvL8ACR1qVJj2NesAHkB7fDzC6Ncb0mbxQ5/r1P8oQ1Gbk",
                                    "to": to,
                                    "messages": [
                                        {
                                            "type": "flex",
                                            "altText": "Puy",
                                            "contents": {
                                                "type": "bubble",
                                                "body": {
                                                    "type": "box",
                                                    "layout": "vertical",
                                                    "contents": [
                                                        {
                                                            "type": "text",
                                                            "text": "   「 Info Group 」\n", #% (elapsed_time),
                                                            "size": "md",
                                                            "weight": "bold",
                                                            "align": "center",
                                                            "gravity": "top",
                                                            "color": "#000000",
                                                        },
                                                        {
                                                            "type": "text",
                                                            "text": "{}".format(str(cuki)),
                                                            "size": "sm",
                                                            "align": "center",
                                                            "gravity": "top",
                                                            "color": "#0000ff",
                                                            "wrap": True
                                                        }
                                                    ]
                                                }
                                            }
                                        }
                                    ]
                                }
                                data = json.dumps(data)
                                sendPost = _session.post(url, data=data, headers=headers)

                        elif rfuText in ["Memberlist"]:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                kontak = cl.getGroup(kirim)
                                group = kontak.members
                                num=1
                                msgs="LIST MEMBER\n"
                                for ids in group:
                                    msgs+="\n%i. %s" % (num, ids.displayName)
                                    num=(num+1)
                                msgs+="\n\nTOTAL MEMBER ( %i )" % len(group)
                                cl.sendText(kirim, msgs)

                        elif rfuText.lower() == 'ceksider on':
                            #if user in RfuSekawan or user in Squad["Admin"]:
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
                                bulan = ["January", "February", "March", "April", "May", "June", "Juli", "August", "September", "October", "November", "December"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                readTime = " " + timeNow.strftime('%H:%M:%S') + " "
                                if kirim in Squad['readPoint']:
                                        try:
                                            del Squad['readPoint'][kirim]
                                            del Squad['readMember'][kirim]
                                            del Squad['readTime'][kirim]
                                        except:
                                            pass
                                        Squad['readPoint'][kirim] = msg.id
                                        Squad['readMember'][kirim] = ""
                                        Squad['readTime'][kirim] = datetime.now().strftime('%H:%M:%S')
                                        Squad['ROM'][kirim] = {}
                                        with open('sider.json', 'w') as fp:
                                            json.dump(Squad, fp, sort_keys=True, indent=4)
                                            cl.sendMessage(kirim,"  「 Reader Notify 」\nIs now Active!")
                                else:
                                    try:
                                        del read['readPoint'][kirim]
                                        del read['readMember'][kirim]
                                        del read['readTime'][kirim]
                                    except:
                                        pass
                                    Squad['readPoint'][kirim] = msg.id
                                    Squad['readMember'][kirim] = ""
                                    Squad['readTime'][kirim] = datetime.now().strftime('%H:%M:%S')
                                    Squad['ROM'][kirim] = {}
                                    with open('sider.json', 'w') as fp:
                                        json.dump(Squad, fp, sort_keys=True, indent=4)
                                        cl.sendMessage(kirim, "  「 Reader Notify 」\nSetting Reader Point!\n  At: " + readTime)

                        elif rfuText.lower() == 'ceksider off':
                            #if user in RfuSekawan or user in Squad["Admin"]:
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
                                bulan = ["January", "February", "March", "April", "May", "June", "Juli", "August", "September", "October", "November", "December"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                readTime = " " + timeNow.strftime('%H:%M:%S') + " "
                                if kirim not in Squad['readPoint']:
                                    cl.sendMessage(kirim,"  「 Reader Notify 」\nIs now Unactive!")
                                else:
                                    try:
                                            del Squad['readPoint'][kirim]
                                            del Squad['readMember'][kirim]
                                            del Squad['readTime'][kirim]
                                    except:
                                          pass
                                    cl.sendMessage(kirim, "  「 Reader Notify 」\nDeleting Reader Point!\n  At: " + readTime)

                        elif rfuText.lower() == 'recheck':
                            #if user in RfuSekawan or user in Squad["Admin"]:
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
                                bulan = ["January", "February", "March", "April", "May", "June", "Juli", "August", "September", "October", "November", "December"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                readTime = " " + timeNow.strftime('%H:%M:%S') + " "
                                if kirim in Squad["readPoint"]:
                                    try:
                                        Squad["readPoint"][kirim] = True
                                        Squad["readMember"][kirim] = {}
                                        Squad["readTime"][kirim] = readTime
                                        Squad["ROM"][kirim] = {}
                                    except:
                                        pass
                                    cl.sendMessage(kirim, "  「 Reader Notify 」\nResetting Readerchecker!\n  At: " + readTime)
                                else:
                                    cl.sendMessage(kirim, "  「 Reader Notify 」\nGot Invalid,\n  '''Checkread on''' first!")

                        elif rfuText.lower() == 'ceksider':
                            #if user in RfuSekawan or user in Squad["Admin"]:
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
                                bulan = ["January", "February", "March", "April", "May", "June", "Juli", "August", "September", "October", "November", "December"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                readTime = " " + timeNow.strftime('%H:%M:%S') + " "
                                if kirim in Squad['readPoint']:
                                    if Squad["ROM"][kirim].items() == []:
                                        cl.sendMessage(kirim,"  「 Reader 」:\nNone")
                                    else:
                                        chiya = []
                                        for rom in Squad["ROM"][kirim].items():
                                            chiya.append(rom[1])
                                        cmem = cl.getContacts(chiya)
                                        zx = ""
                                        zxc = ""
                                        zx2 = []
                                        xpesan = '   「 Pembaca 」\n'
                                    for x in range(len(cmem)):
                                        xname = str(cmem[x].displayName)
                                        pesan = ''
                                        pesan2 = pesan+"@ARDIAN_GANTENG\n"
                                        xlen = str(len(zxc)+len(xpesan))
                                        xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                        zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                                        zx2.append(zx)
                                        zxc += pesan2
                                    text = xpesan+ zxc + "  At: " + readTime
                                    try:
                                        cl.sendMessage(kirim, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                    except Exception as error:
                                        print (error)
                                    pass
                                else:
                                    cl.sendMessage(kirim,"  「 Reader Notify 」\nGot Invalid,\n  '''Checkread on''' first!")

                        elif rfuText.lower() == 'getsider on':
                            #if user in RfuSekawan or user in Squad["Admin"]:
                                try:
                                    del RfuCctv['Point2'][kirim]
                                    del RfuCctv['Point3'][kirim]
                                    del RfuCctv['Point1'][kirim]
                                except:
                                    pass
                                RfuCctv['Point2'][kirim] = msg.id
                                RfuCctv['Point3'][kirim] = ""
                                RfuCctv['Point1'][kirim]=True
                                cl.sendText(kirim,"  「 Reader Notify 」\nStarting get reader!")

                        elif rfuText.lower() == 'getsider off':
                            #if user in RfuSekawan or user in Squad["Admin"]:
                                if kirim in RfuCctv['Point2']:
                                    RfuCctv['Point1'][kirim]=False
                                    cl.sendText(kirim, RfuCctv['Point3'][kirim])
                                else:
                                    cl.sendText(kirim, "  「 Reader Notify 」\nIs now Unactive hee!")

                        elif rfuText.lower().startswith("tagall"):
                            #if user in RfuSekawan or user in Squad["Admin"]:
                                gname = cl.getGroup(kirim)
                                local = [contact.mid for contact in gname.members]
                                try:
                                    lur = len(local)//20
                                    for fu in range(lur+1):
                                        hdc = u''
                                        sell=0
                                        com=[]
                                        for rid in gname.members[fu*20 : (fu+1)*20]:
                                            com.append({"S":str(sell), "E" :str(sell+6), "M":rid.mid})
                                            sell += 7
                                            hdc += u'@A_RFU\n'
                                            atas = '\n In {} '.format(str(gname.name))
                                            atas += '\n Has {} Members'.format(str(len(local)))
                                        cl.sendMessage(kirim, text=hdc + str(atas), contentMetadata={u'MENTION': json.dumps({'MENTIONEES':com})}, contentType=0)
                                except Exception as error:
                                    cl.sendMessage(kirim, str(error))

                        elif rfuText.lower().startswith("mentionall"):
                            #if user in RfuSekawan or user in Squad["Admin"]:
                                gname = cl.getGroup(kirim)
                                local = [contact.mid for contact in gname.members]
                                try:
                                    lur = len(local)//20
                                    for fu in range(lur+1):
                                        hdc = u''
                                        sell=0
                                        com=[]
                                        for rid in gname.members[fu*20 : (fu+1)*20]:
                                            com.append({"S":str(sell), "E" :str(sell+6), "M":rid.mid})
                                            sell += 7
                                            hdc += u'@A_RFU\n'
                                            atas = '\n In {} '.format(str(gname.name))
                                            atas += '\n Has {} Members'.format(str(len(local)))
                                        cl.sendMessage(kirim, text=hdc + str(atas), contentMetadata={u'MENTION': json.dumps({'MENTIONEES':com})}, contentType=0)
                                except Exception as error:
                                    cl.sendMessage(kirim, str(error))

                        elif rfuText in ["Welcomsg on"]:
                          if user in RfuSekawan or user in Squad["Admin"]:
                            if user in RfuSekawan:
                                Squad['Welcome'] = True
                                cl.sendText(kirim,"Cek Welcome Already ON")
                        elif rfuText in ["Welcomsg off"]:
                          if user in RfuSekawan or user in Squad["Admin"]:
                            if user in RfuSekawan:
                                Squad['Welcome'] = False
                                cl.sendText(kirim,"Cek Welcome Already Off")

                        elif rfuText.lower().startswith("changewelcome: "):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                teks = rfuText.split(": ")
                                data = rfuText.replace(teks[0] + ": ","")
                                try:
                                    Squad["WcText"] = data
                                    cl.sendText(kirim,"Welcome Message Change to:\n" +str("(" +data+ ")"))
                                except:
                                    cl.sendText(kirim,"Error")

                        elif rfuText in ["Leave on"]:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad['Leave'] = True
                                cl.sendText(kirim,"Cek Leave Already ON")
                        elif rfuText in ["Leave off"]:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad['Leave'] = False
                                cl.sendText(kirim,"Cek Leave Already Off")

                        elif rfuText.lower().startswith("changeleave: "):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                teks = rfuText.split(": ")
                                data = rfuText.replace(teks[0] + ": ","")
                                try:
                                    Squad["LvText"] = data
                                    cl.sendText(kirim,"Leave Message Change to:\n" +str("(" +data+ ")"))
                                except:
                                    cl.sendText(kirim,"Error")

                        elif rfuText.lower() == "runtimez":
                            if user in Owner:
                                eltime = time.time() - mulai
                                opn = " "+waktu(eltime)
                                cl.sendText(kirim,"Active in :" + opn)

                        elif rfuText.lower().startswith("broadcast: "):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                bc = msg.text.replace("Teks: ","")
                                gid = cl.getGroupIdsJoined()
                                owner = "uac8e3eaf1eb2a55770bf10c3b2357c33"
                                for i in gid:
                                    cl.mentionWithRFU(i,owner," By","\n" + str(" "+bc+" "))

                        elif rfuText.lower().startswith("contactbc: "):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                bc = msg.text.replace("Teks: ","")
                                gid = cl.getAllContactIds()
                                owner = "uac8e3eaf1eb2a55770bf10c3b2357c33"
                                for i in gid:
                                    cl.mentionWithRFU(i,owner," By","\n" + str(" ("+bc+")"))

                        elif rfuText.lower().startswith("adminadd"):
                            if user in RfuSekawan:
                                key = eval(msg.contentMetadata["MENTION"])
                                key["MENTIONEES"][0]["M"]
                                targets = []
                                for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                                for target in targets:
                                    if target in Squad["Admin"]:
                                        cl.sendText(kirim, "User added to Admin")
                                    else:
                                        try:
                                            Squad["Admin"][target] = True
                                            cl.sendText(kirim, "User in Admin ")
                                        except Exception as e:
                                            cl.sendText(kirim, str(error))

                        elif rfuText.lower().startswith("admindel"):
                            if user in Owner:
                                key = eval(msg.contentMetadata["MENTION"])
                                key["MENTIONEES"][0]["M"]
                                targets = []
                                for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                                for target in targets:
                                    if target not in Squad["Admin"]:
                                        cl.sendText(kirim, "User not Registered as Admin")
                                    else:
                                        try:
                                            del Squad["Admin"][target]
                                            cl.sendText(kirim, "Success Deleted User as Admin")
                                        except Exception as e:
                                            cl.sendText(kirim, str(error))

                        elif rfuText.lower() == "remove chat":
                            if user in RfuSekawan or user in Squad["Admin"]:
                                try:
                                    cl.removeAllMessages(fast.param2)
                                    ginfo = cl.getGroup(kirim)
                                    #cl.mentionWithRFU(kirim,owner,"Remove Message Success ","\n In Grup" + str(" ("+ginfo.name+")"))
                                    cl.sendText(kirim, 'Remove Message Success in this Group!')
                                except:
                                    pass

                        elif rfuText.lower() == 'restart':
                            if user in RfuSekawan:
                                cl.sendText(kirim, 'Restarting...')
                                print ("Restarting Server")
                                restart_program()

                        elif rfuText.lower() == 'bot logout':
                            if user in RfuSekawan:
                                cl.mentionWithRFU(kirim,user,"!Exit","")
                                print ("Selfbot Off")
                                exit(1)

                        elif rfuText.lower() == 'my grup':
                            if user in RfuSekawan or user in Squad["Admin"]:
                                groups = cl.groups
                                ret_ = "GRUP JOIN"
                                no = 0 + 1
                                for gid in groups:
                                    group = cl.getGroup(gid)
                                    ret_ += "\n\n{}. {} ".format(str(no), str(group.name))
                                    no += 1
                                ret_ += "\n\nTOTAL {} GRUP JOIN".format(str(len(groups)))
                                cl.sendText(kirim, str(ret_))

                        elif rfuText.lower().startswith("rejectall grup"):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                ginvited = cl.getGroupIdsInvited()
                                if ginvited != [] and ginvited != None:
                                    for gid in ginvited:
                                        cl.rejectGroupInvitation(gid)
                                    cl.sendMessage(kirim, "Succes Cancell {} Invite Grup".format(str(len(ginvited))))
                                else:
                                    cl.sendMessage(kirim, "Nothing Invited")

                        elif rfuText.lower().startswith("status"):
                            if user in Owner:
                                try:
                                    hasil = "Status Bot\n"
                                    if Squad["autoAdd"] == True: hasil += "\nAuto Add ( on )"
                                    else: hasil += "\nAuto Add ( off )"
                                    if Squad["autoJoin"] == True: hasil += "\nAuto Join ( on )"
                                    else: hasil += "\nAuto Join ( off )"
                                    if Squad["AutoReject"] == True: hasil += "\nAuto Reject Room ( on )"
                                    else: hasil += "\nAuto Reject Room ( off )"
                                    if Squad["AutojoinTicket"] == True: hasil += "\nAuto Join Ticket ( on )"
                                    else: hasil += "\nAuto Join Ticket ( off )"
                                    if Squad["autoRead"] == True: hasil += "\nAuto Read ( on )"
                                    else: hasil += "\nAuto Read ( off )"
                                    if Squad["AutoRespon"] == True: hasil += "\nDetect Mention ( on )"
                                    else: hasil += "\nDetect Mention ( off )"
                                    if Squad["KickRespon"] == True: hasil += "\nDetect Mention ( on )"
                                    else: hasil += "\nDetect Kick Mention ( off )"
                                    if Squad["Timeline"] == True: hasil += "\nCheck Post Timeline ( on )"
                                    else: hasil += "\nCheck Post ( off )"
                                    hasil += "\n"
                                    cl.sendMessage(kirim, str(hasil))
                                except Exception as error:
                                    cl.sendMessage(kirim, str(error))

                        elif rfuText in ["Autojoin on"]:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad['autoJoin'] = True
                                cl.sendText(kirim,"Join Set To On..")
                        elif rfuText in ["Autojoin off"]:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad['autoJoin'] = False
                                cl.sendText(kirim,"Join Set To Off..")

                        elif rfuText in ["Autoreject on"]:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad['AutoReject'] = True
                                cl.sendText(msg.to,"Reject Set To On..")
                        elif rfuText in ["Autoreject off"]:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad['AutoReject'] = False
                                cl.sendText(msg.to,"Reject Set To Off..")

                        elif rfuText in ["Adminadd:on"]:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad["Adminadd"] = True
                                cl.sendText(kirim,"   「 Admin Notify 」\nSent Contact to Add!")
                        elif rfuText in ["Adminadd:off"]:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad["Adminadd"] = False
                                cl.sendText(kirim,"   「 Admin Notify 」\nAdding admin is now Off!")

                        elif rfuText in ["Adminrem:on"]:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad["AdminDel"] = True
                                cl.sendText(kirim,"   「 Admin Notify 」\nSent Contact to Remove!")
                        elif rfuText in ["Adminrem:off"]:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad["AdminDel"] = False
                                cl.sendText(kirim,"   「 Admin Notify 」\nRemoving admin is now Off!")

                        elif rfuText in ["jointicket on"]:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad["AutojoinTicket"] = True
                                cl.sendText(kirim,"Join Ticket Set To On")
                        elif rfuText in ["jointicket off"]:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad["AutojoinTicket"] = False
                                cl.sendText(kirim,"Join Ticket Set To Off")
                        elif '/ti/g/' in rfuText.lower():
                            if user in RfuSekawan or user in Squad["Admin"]:
                                link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                                links = link_re.findall(msg.text)
                                n_links=[]
                                for l in links:
                                    if l not in n_links:
                                        n_links.append(l)
                                for ticket_id in n_links:
                                    if Squad["AutojoinTicket"] == True:
                                        group=cl.findGroupByTicket(ticket_id)
                                        cl.acceptGroupInvitationByTicket(group.id,ticket_id)
                                        cl.sendText(kirim,"Success Masuk %s" % str(group.name))

                        elif rfuText.lower() == 'refreshprofile':
                            if user in RfuSekawan or user in Squad["Admin"]:
                                try:
                                    cl.sendMessage(kirim, "   「 Refresh Profile 」\nWaiting for 5s!")
                                    time.sleep(5.0)
                                    clProfile.displayName = str(ProfileMe["displayName"])
                                    clProfile.statusMessage = str(ProfileMe["statusMessage"])
                                    clProfile.pictureStatus = str(ProfileMe["pictureStatus"])
                                    cl.updateProfileAttribute(8, clProfile.pictureStatus)
                                    cl.updateProfile(clProfile)
                                    cl.sendMessage(kirim, "   「 Refresh Profile 」\nSuccessfully!")
                                except:
                                    cl.sendMessage(kirim, "Error")

                        elif rfuText.lower().startswith("refresh"):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                try:
                                    cl.sendText(kirim,"   「 Refresh 」\nWaiting for 5s!")
                                    time.sleep(5.0)
                                    Squad['autoJoin'] = False
                                    Squad['autoAdd'] = False
                                    Squad['AutojoinTicket'] = False
                                    Squad['AutoReject'] = False
                                    Squad['Upfoto'] = False
                                    Squad['UpfotoBot'] = False
                                    Squad['UpfotoGrup'] = False
                                    Squad['Adminadd'] = False
                                    Squad['AdminDel'] = False
                                    Squad['Welcome'] = False
                                    Squad['Leave'] = False
                                    cl.sendText(kirim,"   「 Refresh 」\nDone Refresh!")
                                except Exception as e:
                                    cl.sendText(kirim, str(error))
#------------ TEMPLATE ------------#
### Help ###
                        elif rfuText.lower().startswith("helpz"):
                            #Help = Help
                            _session = requests.session()
                            image = "https://lh3.googleusercontent.com/proxy/-qcXIaVI5RPLI_rZgSi8T-QyHCDuVXRoFQUksJ2tzKKOGt8vGLQ6EW7yZBO9SIpQ0b5GlZgahj8S4lENJRr2PDK7jN-vPImkR628uGfvOlr3HpSjBCWrGfCGiOsj9pT7PjH8OuZ6bZ7_9RB7tTeUcmld8U5z=w256-h256-nc"
                            url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                            headers = {
                                "Host": "game.linefriends.com",
                                "Content-Type": "application/json",
                                "User-Agent": "Mozilla/5.0",
                                "Referer": "https://game.linefriends.com/cdn/jbp-lcs/"
                            }
                            data = {
                                "cc": "UXfpO//D+K6TlqsIBX4AhlamXjhsCUtI1/lWa0zxvp3YA3BlQFwCS8cEKWXBtSJO2cwDtNmbXRA6QPIDBiHbvDOODNoaDQgv6Vno900RzrJ+orAi+vCx9BymUUoebOT3RRtTaJHTYL3AiHLB1MlUdOJvGf7QqPih3p1WUxvWG1v+Tol4W/zAEFdXld5bYneQI3YAZjUn8Ejekfh3qwEHu30f9IayoJs1IwU5C45QMS8Qfu73cln4qH90pgOiQ2Yq15ZJ68/0/Amwy46C5ugyoqookxI4/Oh+Iu+tjT0VtP2Fv5/YoNCKOwbrsw2jHAvL8ACR1qVJj2NesAHkB7fDzC6Ncb0mbxQ5/r1P8oQ1Gbk",
                                "to": to,
                                "messages": [
                                    {
                                        "type": "flex",
                                        "altText": "Puy",
                                        "contents": {
                                            "type": "bubble",
                                            "body": {
                                                "type": "box",
                                                "layout": "vertical",
                                                "contents": [
                                                    {
                                                        "type": "text",
                                                        "text": "「 MENU 」\n\n", #% (elapsed_time),
                                                        "size": "md",
                                                        "weight": "bold",
                                                        "align": "center",
                                                        "gravity": "top",
                                                        "color": "#000000",
                                                    },
                                                    {
                                                        "type": "text",
                                                        "text": " " + str(Helpz),
                                                        "size": "sm",
                                                        "align": "start",
                                                        "color": "#0000ff",
                                                        "wrap": True
                                                    }
                                                ]
                                            }
                                        }
                                    }
                                ]
                            }
                            data = json.dumps(data)
                            sendPost = _session.post(url, data=data, headers=headers)
### Help Ended ###
### Token ###
                        elif rfuText.lower().startswith("@iosipad"):
                            r = requests.get("https://rfutoken.herokuapp.com/iosipad/rfu")
                            data = r.text
                            data = json.loads(data)
                            contact = cl.getContact(user)
                            h = cl.getContact(user)
                            name = "{}".format(h.displayName)
                            _session = requests.session()
                            to = msg.to
                            image = "https://lh3.googleusercontent.com/proxy/-qcXIaVI5RPLI_rZgSi8T-QyHCDuVXRoFQUksJ2tzKKOGt8vGLQ6EW7yZBO9SIpQ0b5GlZgahj8S4lENJRr2PDK7jN-vPImkR628uGfvOlr3HpSjBCWrGfCGiOsj9pT7PjH8OuZ6bZ7_9RB7tTeUcmld8U5z=w256-h256-nc"
                            url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                            headers = {
                                "Host": "game.linefriends.com",
                                "Content-Type": "application/json",
                                "User-Agent": "Mozilla/5.0",
                                "Referer": "https://game.linefriends.com/cdn/jbp-lcs/"
                            }
                            data = {
                                "cc": "UXfpO//D+K6TlqsIBX4AhlamXjhsCUtI1/lWa0zxvp3YA3BlQFwCS8cEKWXBtSJO2cwDtNmbXRA6QPIDBiHbvDOODNoaDQgv6Vno900RzrJ+orAi+vCx9BymUUoebOT3RRtTaJHTYL3AiHLB1MlUdOJvGf7QqPih3p1WUxvWG1v+Tol4W/zAEFdXld5bYneQI3YAZjUn8Ejekfh3qwEHu30f9IayoJs1IwU5C45QMS8Qfu73cln4qH90pgOiQ2Yq15ZJ68/0/Amwy46C5ugyoqookxI4/Oh+Iu+tjT0VtP2Fv5/YoNCKOwbrsw2jHAvL8ACR1qVJj2NesAHkB7fDzC6Ncb0mbxQ5/r1P8oQ1Gbk",
                                "to": to,
                                "messages": [
                                    {
                                        "type": "template",
                                        "altText": "Puy",
                                        "template": {
                                            "type": "buttons",
                                            "actions": [
                                                {
                                                    "type": "uri",
                                                    "label": "LOGIN",
                                                    "uri": "{}".format(str(data["qr"]))
                                                },
                                                {
                                                    "type": "uri",
                                                    "label": "CREATOR",
                                                    "uri": "line://ti/p/~yapuy"
                                                }
                                            ],
                                            "thumbnailImageUrl": "https://media1.tenor.com/images/22dab68a24735564a964e68194d23ffb/tenor.gif",
                                            "title": "Iosipad",
                                            "text": "Link will burn in 2 minutes"
                                        }
                                    }
                                ]
                            }
                            data = json.dumps(data)
                            sendPost = _session.post(url, data=data, headers=headers)

                        elif rfuText.lower().startswith("@token chrome"):
                            r = requests.get("https://rfutoken.herokuapp.com/iosipad/chromeos")
                            data = r.text
                            data = json.loads(data)
                            contact = cl.getContact(user)
                            h = cl.getContact(user)
                            name = "{}".format(h.displayName)
                            _session = requests.session()
                            image = "https://lh3.googleusercontent.com/proxy/-qcXIaVI5RPLI_rZgSi8T-QyHCDuVXRoFQUksJ2tzKKOGt8vGLQ6EW7yZBO9SIpQ0b5GlZgahj8S4lENJRr2PDK7jN-vPImkR628uGfvOlr3HpSjBCWrGfCGiOsj9pT7PjH8OuZ6bZ7_9RB7tTeUcmld8U5z=w256-h256-nc"
                            url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                            headers = {
                                "Host": "game.linefriends.com",
                                "Content-Type": "application/json",
                                "User-Agent": "Mozilla/5.0",
                                "Referer": "https://game.linefriends.com/cdn/jbp-lcs/"
                            }
                            data = {
                                "cc": "UXfpO//D+K6TlqsIBX4AhlamXjhsCUtI1/lWa0zxvp3YA3BlQFwCS8cEKWXBtSJO2cwDtNmbXRA6QPIDBiHbvDOODNoaDQgv6Vno900RzrJ+orAi+vCx9BymUUoebOT3RRtTaJHTYL3AiHLB1MlUdOJvGf7QqPih3p1WUxvWG1v+Tol4W/zAEFdXld5bYneQI3YAZjUn8Ejekfh3qwEHu30f9IayoJs1IwU5C45QMS8Qfu73cln4qH90pgOiQ2Yq15ZJ68/0/Amwy46C5ugyoqookxI4/Oh+Iu+tjT0VtP2Fv5/YoNCKOwbrsw2jHAvL8ACR1qVJj2NesAHkB7fDzC6Ncb0mbxQ5/r1P8oQ1Gbk",
                                "to": to,
                                "messages": [
                                    {
                                        "type": "flex",
                                        "altText": "Puy",
                                        "contents": {
                                            "type": "bubble",
                                            "header": {
                                                "type": "box",
                                                #"align": "center",
                                                #"color": "#0000ff",
                                                "layout": "vertical",
                                                "contents": [
                                                  {
                                                    "type": "text",
                                                    "align": "center",
                                                    "color": "#000000",
                                                    "size": "xl",
                                                    "weight": "bold",
                                                    "text": "CHROMEOS"
                                                  }
                                                ]
                                              },
                                              "hero": {
                                                "type": "image",
                                                "url": "https://herencia.net/wp-content/uploads/2017/05/Que_estudiar.jpg",
                                                "size": "full",
                                                "aspectRatio": "20:13"
                                              },
                                              "body": {
                                                "type": "box",
                                                "layout": "vertical",
                                                "contents": [
                                                  {
                                                    "type": "text",
                                                    "align": "center",
                                                    #"weight": "bold",
                                                    "text": "Link will burn in 2 minutes",
                                                    #"margin": "sm",
                                                    "wrap": True
                                                  }
                                                ]
                                              },
                                              "footer": {
                                                "type": "box",
                                                "layout": "vertical",
                                                "contents": [
                                                  {
                                                    "type": "spacer",
                                                    "size": "xl"
                                                  },
                                                  {
                                                    "type": "button",
                                                    "action": {
                                                      "type": "uri",
                                                      "label": "Login",
                                                      "uri": "{}".format(str(data["qr"]))
                                                    },
                                                    "style": "link"
                                                    #"color": "#000000"
                                                  }
                                                ]
                                              }
                                        }
                                    }
                                ]
                            }
                            data = json.dumps(data)
                            sendPost = _session.post(url, data=data, headers=headers)
### Token Ended ###
### Speed ###
                        elif rfuText.lower().startswith("speed"):
                            no = time.time()
                            cl.sendText("uac8e3eaf1eb2a55770bf10c3b2357c33", ' ')
                            elapsed_time = time.time() - no
                            _session = requests.session()
                            image = "https://lh3.googleusercontent.com/proxy/-qcXIaVI5RPLI_rZgSi8T-QyHCDuVXRoFQUksJ2tzKKOGt8vGLQ6EW7yZBO9SIpQ0b5GlZgahj8S4lENJRr2PDK7jN-vPImkR628uGfvOlr3HpSjBCWrGfCGiOsj9pT7PjH8OuZ6bZ7_9RB7tTeUcmld8U5z=w256-h256-nc"
                            url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                            headers = {
                                "Host": "game.linefriends.com",
                                "Content-Type": "application/json",
                                "User-Agent": "Mozilla/5.0",
                                "Referer": "https://game.linefriends.com/cdn/jbp-lcs/"
                            }
                            data = {
                                "cc": "UXfpO//D+K6TlqsIBX4AhlamXjhsCUtI1/lWa0zxvp3YA3BlQFwCS8cEKWXBtSJO2cwDtNmbXRA6QPIDBiHbvDOODNoaDQgv6Vno900RzrJ+orAi+vCx9BymUUoebOT3RRtTaJHTYL3AiHLB1MlUdOJvGf7QqPih3p1WUxvWG1v+Tol4W/zAEFdXld5bYneQI3YAZjUn8Ejekfh3qwEHu30f9IayoJs1IwU5C45QMS8Qfu73cln4qH90pgOiQ2Yq15ZJ68/0/Amwy46C5ugyoqookxI4/Oh+Iu+tjT0VtP2Fv5/YoNCKOwbrsw2jHAvL8ACR1qVJj2NesAHkB7fDzC6Ncb0mbxQ5/r1P8oQ1Gbk",
                                "to": to,
                                "messages": [
                                    {
                                        "type": "flex",
                                        "altText": "Puy",
                                        "contents": {
                                            "type": "bubble",
                                            "body": {
                                                "type": "box",
                                                "layout": "vertical",
                                                "contents": [
                                                    {
                                                        "type": "text",
                                                        "text": "   「 Speed Sender Messages 」\n", #% (elapsed_time),
                                                        "size": "md",
                                                        "weight": "bold",
                                                        "align": "center",
                                                        "gravity": "top",
                                                        "color": "#000000",
                                                    },
                                                    {
                                                        "type": "text",
                                                        "text": "%s" % (elapsed_time),
                                                        #"text": "%s".format(str(elapsed_time)),
                                                        "size": "md",
                                                        "align": "center",
                                                        "gravity": "top",
                                                        "color": "#0000ff"
                                                    }
                                                ]
                                            }
                                        }
                                    }
                                ]
                            }
                            data = json.dumps(data)
                            sendPost = _session.post(url, data=data, headers=headers)
### Speed Ended ###
### Wikipedia ###
                        elif rfuText.lower().startswith("wikipedia: "):
                            wiki = rfuText.lower().replace("wikipedia: ","")
                            wikipedia.set_lang("id")
                            pesan=" 『 "
                            pesan+=wikipedia.page(wiki).title
                            pesan+=" 』\n"
                            pesan+=wikipedia.summary(wiki, sentences=1)
                            pesan+="\n"
                            pesanz="Tap tombol dibawah untuk mengunjungi situs tersebut."
                            pesanz+=" "
                            pesann=""
                            pesann+=wikipedia.page(wiki).url
                            _session = requests.session()
                            image = "https://lh3.googleusercontent.com/proxy/-qcXIaVI5RPLI_rZgSi8T-QyHCDuVXRoFQUksJ2tzKKOGt8vGLQ6EW7yZBO9SIpQ0b5GlZgahj8S4lENJRr2PDK7jN-vPImkR628uGfvOlr3HpSjBCWrGfCGiOsj9pT7PjH8OuZ6bZ7_9RB7tTeUcmld8U5z=w256-h256-nc"
                            url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                            headers = {
                                "Host": "game.linefriends.com",
                                "Content-Type": "application/json",
                                "User-Agent": "Mozilla/5.0",
                                "Referer": "https://game.linefriends.com/cdn/jbp-lcs/"
                            }
                            data = {
                                "cc": "UXfpO//D+K6TlqsIBX4AhlamXjhsCUtI1/lWa0zxvp3YA3BlQFwCS8cEKWXBtSJO2cwDtNmbXRA6QPIDBiHbvDOODNoaDQgv6Vno900RzrJ+orAi+vCx9BymUUoebOT3RRtTaJHTYL3AiHLB1MlUdOJvGf7QqPih3p1WUxvWG1v+Tol4W/zAEFdXld5bYneQI3YAZjUn8Ejekfh3qwEHu30f9IayoJs1IwU5C45QMS8Qfu73cln4qH90pgOiQ2Yq15ZJ68/0/Amwy46C5ugyoqookxI4/Oh+Iu+tjT0VtP2Fv5/YoNCKOwbrsw2jHAvL8ACR1qVJj2NesAHkB7fDzC6Ncb0mbxQ5/r1P8oQ1Gbk",
                                "to": to,
                                "messages": [
                                    {
                                        "type": "flex",
                                        "altText": "Puy",
                                        "contents": {
                                            "type": "bubble",
                                            "header": {
                                                "type": "box",
                                                #"align": "center",
                                                #"color": "#0000ff",
                                                "layout": "vertical",
                                                "contents": [
                                                  {
                                                    "type": "text",
                                                    "align": "start",
                                                    "color": "#000000",
                                                    "size": "md",
                                                    "weight": "bold",
                                                    "text": "WIKIPEDIA", #% (elapsed_time),
                                                  }
                                                ]
                                              },
                                              "body": {
                                                "type": "box",
                                                "layout": "vertical",
                                                "contents": [
                                                  {
                                                    "type": "text",
                                                    "align": "center",
                                                    "weight": "regular",
                                                    "text": "{}".format(str(pesan)),
                                                    #"margin": "sm",
                                                    "wrap": True
                                                 },
                                                 {
                                                    "type": "text",
                                                    "align": "center",
                                                    "weight": "regular",
                                                    "text": "{}".format(str(pesanz)),
                                                    #"margin": "sm",
                                                    "wrap": True
                                                  }
                                                ]
                                              },
                                              "footer": {
                                                "type": "box",
                                                "layout": "vertical",
                                                "contents": [
                                                  {
                                                    "type": "spacer",
                                                    "size": "sm"
                                                  },
                                                  {
                                                    "type": "button",
                                                    "action": {
                                                      "type": "uri",
                                                      "label": "Visit here",
                                                      "uri": "{}".format(str(pesann)),
                                                    },
                                                    "style": "link",
                                                    "height": "sm"
                                                    #"color": "#000000"
                                                  }
                                                ]
                                              }
                                        }
                                    }
                                ]
                            }
                            data = json.dumps(data)
                            sendPost = _session.post(url, data=data, headers=headers)
### Wikipedia Ended ###
                        elif rfuText.lower().startswith("write "):
                            bcd = rfuText.lower().replace("write ","")
                            _session = requests.session()
                            image = "https://lh3.googleusercontent.com/proxy/-qcXIaVI5RPLI_rZgSi8T-QyHCDuVXRoFQUksJ2tzKKOGt8vGLQ6EW7yZBO9SIpQ0b5GlZgahj8S4lENJRr2PDK7jN-vPImkR628uGfvOlr3HpSjBCWrGfCGiOsj9pT7PjH8OuZ6bZ7_9RB7tTeUcmld8U5z=w256-h256-nc"
                            url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                            headers = {
                                "Host": "game.linefriends.com",
                                "Content-Type": "application/json",
                                "User-Agent": "Mozilla/5.0",
                                "Referer": "https://game.linefriends.com/cdn/jbp-lcs/"
                            }
                            data = {
                                "cc": "UXfpO//D+K6TlqsIBX4AhlamXjhsCUtI1/lWa0zxvp3YA3BlQFwCS8cEKWXBtSJO2cwDtNmbXRA6QPIDBiHbvDOODNoaDQgv6Vno900RzrJ+orAi+vCx9BymUUoebOT3RRtTaJHTYL3AiHLB1MlUdOJvGf7QqPih3p1WUxvWG1v+Tol4W/zAEFdXld5bYneQI3YAZjUn8Ejekfh3qwEHu30f9IayoJs1IwU5C45QMS8Qfu73cln4qH90pgOiQ2Yq15ZJ68/0/Amwy46C5ugyoqookxI4/Oh+Iu+tjT0VtP2Fv5/YoNCKOwbrsw2jHAvL8ACR1qVJj2NesAHkB7fDzC6Ncb0mbxQ5/r1P8oQ1Gbk",
                                "to": to,
                                "messages": [
                                    {
                                        "type": "flex",
                                        "altText": "Puy",
                                        "contents": {
                                            "type": "bubble",
                                            "body": {
                                                "type": "box",
                                                "layout": "vertical",
                                                "contents": [
                                                    {
                                                        "type": "text",
                                                        "text": "{}".format(str(bcd)),
                                                        "size": "lg",
                                                        "weight": "regular",
                                                        "align": "start",
                                                        "gravity": "top",
                                                        "color": "#000000",
                                                    }
                                                ]
                                            }
                                        }
                                    }
                                ]
                            }
                            data = json.dumps(data)
                            sendPost = _session.post(url, data=data, headers=headers)
### Runtime ###
                        elif rfuText.lower().startswith("runtime"):
                            eltime = time.time() - mulai
                            opn = " "+waktu(eltime)
                            _session = requests.session()
                            image = "https://lh3.googleusercontent.com/proxy/-qcXIaVI5RPLI_rZgSi8T-QyHCDuVXRoFQUksJ2tzKKOGt8vGLQ6EW7yZBO9SIpQ0b5GlZgahj8S4lENJRr2PDK7jN-vPImkR628uGfvOlr3HpSjBCWrGfCGiOsj9pT7PjH8OuZ6bZ7_9RB7tTeUcmld8U5z=w256-h256-nc"
                            url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                            headers = {
                                "Host": "game.linefriends.com",
                                "Content-Type": "application/json",
                                "User-Agent": "Mozilla/5.0",
                                "Referer": "https://game.linefriends.com/cdn/jbp-lcs/"
                            }
                            data = {
                                "cc": "UXfpO//D+K6TlqsIBX4AhlamXjhsCUtI1/lWa0zxvp3YA3BlQFwCS8cEKWXBtSJO2cwDtNmbXRA6QPIDBiHbvDOODNoaDQgv6Vno900RzrJ+orAi+vCx9BymUUoebOT3RRtTaJHTYL3AiHLB1MlUdOJvGf7QqPih3p1WUxvWG1v+Tol4W/zAEFdXld5bYneQI3YAZjUn8Ejekfh3qwEHu30f9IayoJs1IwU5C45QMS8Qfu73cln4qH90pgOiQ2Yq15ZJ68/0/Amwy46C5ugyoqookxI4/Oh+Iu+tjT0VtP2Fv5/YoNCKOwbrsw2jHAvL8ACR1qVJj2NesAHkB7fDzC6Ncb0mbxQ5/r1P8oQ1Gbk",
                                "to": to,
                                "messages": [
                                    {
                                        "type": "flex",
                                        "altText": "Puy",
                                        "contents": {
                                            "type": "bubble",
                                            "body": {
                                                "type": "box",
                                                "layout": "vertical",
                                                "contents": [
                                                    {
                                                        "type": "text",
                                                        "text": "   「 Runtime 」\n", #% (elapsed_time),
                                                        "size": "md",
                                                        "weight": "bold",
                                                        "align": "center",
                                                        "gravity": "top",
                                                        "color": "#000000",
                                                    },
                                                    {
                                                        "type": "text",
                                                        "text": "{}".format(str(opn)),
                                                        "size": "md",
                                                        "align": "center",
                                                        "gravity": "top",
                                                        "color": "#0000ff",
                                                        "wrap": True
                                                    }
                                                ]
                                            }
                                        }
                                    }
                                ]
                            }
                            data = json.dumps(data)
                            sendPost = _session.post(url, data=data, headers=headers)
### Runtime Ended ###
### About ###
                        elif rfuText.lower().startswith("@about"):
                            _session = requests.session()
                            image = "https://lh3.googleusercontent.com/proxy/-qcXIaVI5RPLI_rZgSi8T-QyHCDuVXRoFQUksJ2tzKKOGt8vGLQ6EW7yZBO9SIpQ0b5GlZgahj8S4lENJRr2PDK7jN-vPImkR628uGfvOlr3HpSjBCWrGfCGiOsj9pT7PjH8OuZ6bZ7_9RB7tTeUcmld8U5z=w256-h256-nc"
                            url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                            headers = {
                                "Host": "game.linefriends.com",
                                "Content-Type": "application/json",
                                "User-Agent": "Mozilla/5.0",
                                "Referer": "https://game.linefriends.com/cdn/jbp-lcs/"
                            }
                            data = {
                                "cc": "UXfpO//D+K6TlqsIBX4AhlamXjhsCUtI1/lWa0zxvp3YA3BlQFwCS8cEKWXBtSJO2cwDtNmbXRA6QPIDBiHbvDOODNoaDQgv6Vno900RzrJ+orAi+vCx9BymUUoebOT3RRtTaJHTYL3AiHLB1MlUdOJvGf7QqPih3p1WUxvWG1v+Tol4W/zAEFdXld5bYneQI3YAZjUn8Ejekfh3qwEHu30f9IayoJs1IwU5C45QMS8Qfu73cln4qH90pgOiQ2Yq15ZJ68/0/Amwy46C5ugyoqookxI4/Oh+Iu+tjT0VtP2Fv5/YoNCKOwbrsw2jHAvL8ACR1qVJj2NesAHkB7fDzC6Ncb0mbxQ5/r1P8oQ1Gbk",
                                "to": to,
                                "messages": [
                                    {
                                        "type": "flex",
                                        "altText": "Puy",
                                        "contents": {
                                            "type": "bubble",
                                            "header": {
                                                "type": "box",
                                                #"align": "center",
                                                #"color": "#0000ff",
                                                "layout": "vertical",
                                                "contents": [
                                                  {
                                                    "type": "text",
                                                    "align": "start",
                                                    "color": "#000000",
                                                    "size": "md",
                                                    "weight": "bold",
                                                    "text": "ABOUT"
                                                  }
                                                ]
                                              },
                                              "hero": {
                                                "type": "image",
                                                "url": "https://media1.tenor.com/images/de138457dc01a05aa94fbbc054aae14c/tenor.gif",
                                                "size": "full",
                                                "aspectMode": "cover",
                                                "aspectRatio": "4:3" #20:13
                                              },
                                              "body": {
                                                "type": "box",
                                                "layout": "vertical",
                                                "contents": [
                                                  {
                                                    "type": "text",
                                                    "align": "center",
                                                    "weight": "bold",
                                                    "text": "Made by Puy",
                                                    "color": "#186A3B",
                                                    #"margin": "sm",
                                                    "wrap": True
                                                  },
                                                  {
                                                    "type": "text",
                                                    "align": "center",
                                                    "weight": "regular",
                                                    "color": "#aaaaaa",
                                                    "text": "Supported by È̶͟͏RR̡͜O̵͘͟͜Ŗ͟͏͠ T̶̨̢͠҉E̶̡̛͠Á̶͡͡M̀͢͠ and U",
                                                    "wrap": True
                                                  },
                                                  {
                                                    "type": "text",
                                                    "align": "center",
                                                    "weight": "regular",
                                                    "color": "#000000",
                                                    "text": "An Just for Fun Bot.",
                                                    "wrap": True
                                                  }
                                                ]
                                              },
                                              "footer": {
                                                "type": "box",
                                                "layout": "vertical",
                                                "spacing": "sm",
                                                "contents": [
                                                  {
                                                    "type": "spacer",
                                                    "size": "sm"
                                                  },
                                                  {
                                                    "type": "button",
                                                    "action": {
                                                      "type": "uri",
                                                      "label": "Add Creator",
                                                      "uri": "http://line.me/ti/p/~yapuy"
                                                    },
                                                    "style": "link",
                                                    "height": "sm"
                                                    #"color": "#000000"
                                                  }
                                                ]
                                              }
                                        }
                                    }
                                ]
                            }
                            data = json.dumps(data)
                            sendPost = _session.post(url, data=data, headers=headers)
### About Ended ###
### Calendar ###
                        elif rfuText.lower().startswith("calendar"):
                            tz = pytz.timezone("Asia/Jakarta")
                            timeNow = datetime.now(tz=tz)
                            day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                            hari = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
                            bulan = ["January", "February", "March", "April", "May", "June", "Juli", "August", "September", "October", "November", "December"]
                            hr = timeNow.strftime("%A")
                            bln = timeNow.strftime("%m")
                            for i in range(len(day)):
                                if hr == day[i]: hasil = hari[i]
                            for k in range(0, len(bulan)):
                                if bln == str(k): bln = bulan[k-1]
                            readTime = hasil + ", " + timeNow.strftime('%d') + "." + bln + "." + timeNow.strftime('%Y') + "\nWib : " + timeNow.strftime('%H:%M:%S') + " "
                            _session = requests.session()
                            image = "https://lh3.googleusercontent.com/proxy/-qcXIaVI5RPLI_rZgSi8T-QyHCDuVXRoFQUksJ2tzKKOGt8vGLQ6EW7yZBO9SIpQ0b5GlZgahj8S4lENJRr2PDK7jN-vPImkR628uGfvOlr3HpSjBCWrGfCGiOsj9pT7PjH8OuZ6bZ7_9RB7tTeUcmld8U5z=w256-h256-nc"
                            url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                            headers = {
                                "Host": "game.linefriends.com",
                                "Content-Type": "application/json",
                                "User-Agent": "Mozilla/5.0",
                                "Referer": "https://game.linefriends.com/cdn/jbp-lcs/"
                            }
                            data = {
                                "cc": "UXfpO//D+K6TlqsIBX4AhlamXjhsCUtI1/lWa0zxvp3YA3BlQFwCS8cEKWXBtSJO2cwDtNmbXRA6QPIDBiHbvDOODNoaDQgv6Vno900RzrJ+orAi+vCx9BymUUoebOT3RRtTaJHTYL3AiHLB1MlUdOJvGf7QqPih3p1WUxvWG1v+Tol4W/zAEFdXld5bYneQI3YAZjUn8Ejekfh3qwEHu30f9IayoJs1IwU5C45QMS8Qfu73cln4qH90pgOiQ2Yq15ZJ68/0/Amwy46C5ugyoqookxI4/Oh+Iu+tjT0VtP2Fv5/YoNCKOwbrsw2jHAvL8ACR1qVJj2NesAHkB7fDzC6Ncb0mbxQ5/r1P8oQ1Gbk",
                                "to": to,
                                "messages": [
                                    {
                                        "type": "flex",
                                        "altText": "Puy",
                                        "contents": {
                                            "type": "bubble",
                                            "header": {
                                                "type": "box",
                                                #"align": "center",
                                                #"color": "#0000ff",
                                                "layout": "vertical",
                                                "contents": [
                                                  {
                                                    "type": "text",
                                                    "align": "center",
                                                    "color": "#000000",
                                                    "size": "md",
                                                    "weight": "bold",
                                                    "text": "   「 Calendar 」\n", #% (elapsed_time),
                                                  }
                                                ]
                                              },
                                              "body": {
                                                "type": "box",
                                                "layout": "vertical",
                                                "contents": [
                                                  {
                                                    "type": "text",
                                                    "align": "center",
                                                    "weight": "regular",
                                                    "text": "{}".format(readTime),
                                                    #"margin": "sm",
                                                    "wrap": True
                                                  }
                                                ]
                                              },
                                              "footer": {
                                                "type": "box",
                                                "layout": "vertical",
                                                "contents": [
                                                  {
                                                    "type": "spacer",
                                                    "size": "md"
                                                  },
                                                  {
                                                    "type": "button",
                                                    "action": {
                                                      "type": "uri",
                                                      "label": "Creator",
                                                      "uri": "http://line.me/ti/p/~yapuy"
                                                    },
                                                    "style": "primary",
                                                    "height": "md"
                                                    #"color": "#000000"
                                                  }
                                                ]
                                              }
                                        }
                                    }
                                ]
                            }
                            data = json.dumps(data)
                            sendPost = _session.post(url, data=data, headers=headers)
### Calendar Ended ###
### Myinfo ###
                        elif rfuText.lower().startswith("@me"):
                            contact = cl.getContact(user)
                            _session = requests.session()
                            image = "https://lh3.googleusercontent.com/proxy/-qcXIaVI5RPLI_rZgSi8T-QyHCDuVXRoFQUksJ2tzKKOGt8vGLQ6EW7yZBO9SIpQ0b5GlZgahj8S4lENJRr2PDK7jN-vPImkR628uGfvOlr3HpSjBCWrGfCGiOsj9pT7PjH8OuZ6bZ7_9RB7tTeUcmld8U5z=w256-h256-nc"
                            url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                            headers = {
                                "Host": "game.linefriends.com",
                                "Content-Type": "application/json",
                                "User-Agent": "Mozilla/5.0",
                                "Referer": "https://game.linefriends.com/cdn/jbp-lcs/"
                            }
                            data = {
                                "cc": "UXfpO//D+K6TlqsIBX4AhlamXjhsCUtI1/lWa0zxvp3YA3BlQFwCS8cEKWXBtSJO2cwDtNmbXRA6QPIDBiHbvDOODNoaDQgv6Vno900RzrJ+orAi+vCx9BymUUoebOT3RRtTaJHTYL3AiHLB1MlUdOJvGf7QqPih3p1WUxvWG1v+Tol4W/zAEFdXld5bYneQI3YAZjUn8Ejekfh3qwEHu30f9IayoJs1IwU5C45QMS8Qfu73cln4qH90pgOiQ2Yq15ZJ68/0/Amwy46C5ugyoqookxI4/Oh+Iu+tjT0VtP2Fv5/YoNCKOwbrsw2jHAvL8ACR1qVJj2NesAHkB7fDzC6Ncb0mbxQ5/r1P8oQ1Gbk",
                                "to": to,
                                "messages": [
                                    {
                                        "type": "flex",
                                        "altText": "Puy",
                                        "contents": {
                                            "type": "bubble",
                                            "header": {
                                                "type": "box",
                                                "layout": "vertical",
                                                "contents": [
                                                  {
                                                    "type": "text",
                                                    "align": "start",
                                                    "color": "#000000",
                                                    "size": "md",
                                                    #"spacing": "sm",
                                                    "weight": "bold",
                                                    "text": "PROFILE"
                                                  }
                                                ]
                                              },
                                              "hero": {
                                                "type": "image",
                                                "url": "https://syadnysyz2.herokuapp.com/storage/img?url=http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus),
                                                "size": "full",
                                                "aspectMode": "cover",
                                                "aspectRatio": "4:3" #20:13
                                              },
                                              "body": {
                                                "type": "box",
                                                "layout": "vertical",
                                                "spacing": "sm",
                                                "contents": [
                                                  {
                                                    "type": "text",
                                                    "align": "center",
                                                    "weight": "regular",
                                                    "color": "#186A3B",
                                                    "text": "{}".format(contact.displayName)
                                                    #"flex": 3
                                                  },
                                                  {
                                                    "type": "text",
                                                    "weight": "regular",
                                                    "color": "#aaaaaa",
                                                    "align": "center",
                                                    "text": "{}".format(contact.statusMessage),
                                                    "wrap": True
                                                    #"flex": 5
                                                  }
                                                ]
                                              },
                                              "footer": {
                                                "type": "box",
                                                "layout": "vertical",
                                                "spacing": "sm",
                                                #"separator": True,
                                                "contents": [
                                                  {
                                                    "type": "spacer",
                                                    "size": "sm"
                                                  },
                                                  {
                                                    "type": "button",
                                                    "action": {
                                                      "type": "uri",
                                                      "label": "Set Profile",
                                                      "uri": "line://nv/profile"
                                                    },
                                                    "style": "link",
                                                    "height": "sm"
                                                    #"color": "#000000"
                                                  }
                                                ]
                                              }
                                        }
                                    }
                                ]
                            }
                            data = json.dumps(data)
                            sendPost = _session.post(url, data=data, headers=headers)
### Myinfo Ended ###
### Getname ###
                        elif rfuText.lower().startswith("myname"):
                            contact = cl.getContact(user)
                            _session = requests.session()
                            image = "https://lh3.googleusercontent.com/proxy/-qcXIaVI5RPLI_rZgSi8T-QyHCDuVXRoFQUksJ2tzKKOGt8vGLQ6EW7yZBO9SIpQ0b5GlZgahj8S4lENJRr2PDK7jN-vPImkR628uGfvOlr3HpSjBCWrGfCGiOsj9pT7PjH8OuZ6bZ7_9RB7tTeUcmld8U5z=w256-h256-nc"
                            url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                            headers = {
                                "Host": "game.linefriends.com",
                                "Content-Type": "application/json",
                                "User-Agent": "Mozilla/5.0",
                                "Referer": "https://game.linefriends.com/cdn/jbp-lcs/"
                            }
                            data = {
                                "cc": "UXfpO//D+K6TlqsIBX4AhlamXjhsCUtI1/lWa0zxvp3YA3BlQFwCS8cEKWXBtSJO2cwDtNmbXRA6QPIDBiHbvDOODNoaDQgv6Vno900RzrJ+orAi+vCx9BymUUoebOT3RRtTaJHTYL3AiHLB1MlUdOJvGf7QqPih3p1WUxvWG1v+Tol4W/zAEFdXld5bYneQI3YAZjUn8Ejekfh3qwEHu30f9IayoJs1IwU5C45QMS8Qfu73cln4qH90pgOiQ2Yq15ZJ68/0/Amwy46C5ugyoqookxI4/Oh+Iu+tjT0VtP2Fv5/YoNCKOwbrsw2jHAvL8ACR1qVJj2NesAHkB7fDzC6Ncb0mbxQ5/r1P8oQ1Gbk",
                                "to": to,
                                "messages": [
                                    {
                                        "type": "flex",
                                        "altText": "Puy",
                                        "contents": {
                                            "type": "bubble",
                                            "header": {
                                                "type": "box",
                                                #"align": "center",
                                                #"color": "#0000ff",
                                                "layout": "vertical",
                                                "contents": [
                                                  {
                                                    "type": "text",
                                                    "align": "center",
                                                    "color": "#000000",
                                                    "size": "md",
                                                    "weight": "bold",
                                                    "text": "   「 Getname 」\n", #% (elapsed_time),
                                                  }
                                                ]
                                              },
                                              "body": {
                                                "type": "box",
                                                "layout": "vertical",
                                                "contents": [
                                                  {
                                                    "type": "text",
                                                    "align": "center",
                                                    "weight": "regular",
                                                    "text": "Yourname : {}".format(contact.displayName),
                                                    #"margin": "sm",
                                                    "wrap": True
                                                  }
                                                ]
                                              },
                                              "footer": {
                                                "type": "box",
                                                "layout": "vertical",
                                                "contents": [
                                                  {
                                                    "type": "spacer",
                                                    "size": "xl"
                                                  },
                                                  {
                                                    "type": "button",
                                                    "action": {
                                                      "type": "uri",
                                                      "label": "Creator",
                                                      "uri": "http://line.me/ti/p/~yapuy"
                                                    },
                                                    "style": "primary"
                                                    #"color": "#000000"
                                                  }
                                                ]
                                              }
                                        }
                                    }
                                ]
                            }
                            data = json.dumps(data)
                            sendPost = _session.post(url, data=data, headers=headers)
### Getname Ended ###
#------------ TEMPLATE ENDED ------------#
#------------ SCRIPT PUY -----------#
                        elif 'Tokenlist' in msg.text:
                           if user in Owner:
                              cl.sendText(kirim,"1\n"+cl.authToken)
                              #cl.sendText(kirim,"2\n"+riden1.authToken)
                              #cl.sendText(kirim,"3\n"+riden2.authToken)
                              #cl.sendText(kirim,"4\n"+riden3.authToken)
                              #cl.sendText(kirim,"5\n"+riden4.authToken)
                              #cl.sendText(kirim,"6\n"+riden5.authToken)
                              #cl.sendText(kirim,"7\n"+riden6.authToken)
#------------ SCRIPT PUY ENDED -----------#

                        elif rfuText.lower().startswith("apakah: "):
                            #if user in RfuSekawan or user in Squad["Admin"]:
                                try:
                                    txt = ['iya','tidak','bisa jadi','mungkin saja','tidak mungkin','au ah gelap']
                                    isi = random.choice(txt)
                                    tts = gTTS(text=isi, lang='id', slow=False)
                                    tts.save('temp2.mp3')
                                    cl.sendAudio(kirim, 'temp2.mp3')
                                except Exception as e:
                                    cl.sendText(kirim, str(e))

                        elif rfuText.lower().startswith("kapan: "):
                            #if user in RfuSekawan or user in Squad["Admin"]:
                                try:
                                    txt = ['kapan kapan','besok','satu abad lagi','Hari ini','Tahun depan','Minggu depan','Bulan depan','Sebentar lagi']
                                    isi = random.choice(txt)
                                    tts = gTTS(text=isi, lang='id', slow=False)
                                    tts.save('temp2.mp3')
                                    cl.sendAudio(kirim, 'temp2.mp3')
                                except Exception as e:
                                    cl.sendText(kirim, str(e))

    except Exception as error:
        print (error)

#-------------------------------------------- FINNISHING SCRIP ------------------------------------------------#

while True:
    try:
        Operation = RIDEN.singleTrace(count=50)
        if Operation is not None:
            for fast in Operation:
                RIDEN.setRevision(fast.revision)
                thread1 = threading.Thread(target=RIDEN_FAST_USER, args=(fast,))#self.OpInterrupt[fast.type], args=(fast,)
                thread1.start()
                thread1.join()
    except Exception as error:
        print (error)
