  # -*- coding: utf-8 -*-

from LineAPI.linepy import *
from LineAPI.akad.ttypes import Message
from LineAPI.akad.ttypes import ContentType as Type
from gtts import gTTS
from time import sleep
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
from googletrans import Translator
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, six, ast, pytz, urllib, urllib3, urllib.parse, traceback, atexit

bot = LINE("EwpSg0TaKzo97PQbRYm0.bwkg+0EnhGaxzB5GWz4Sma.8aZahBFcR3w9u2jl7t+VSz76m9gqDEdjD7mNWDjKg9Y=")
botMid = bot.profile.mid
botProfile = bot.getProfile()
botSettings = bot.getSettings()
botPoll = OEPoll(bot)
botStart = time.time()

msg_dict = {}

settings = {
    "autoAdd": False,
    "autoJoin": True,
    "autoLeave": False,
    "autoRead": True,
    "autoRespon": False,
    "autoJoinTicket": False,
    "checkContact": False,
    "checkPost": False,
    "checkSticker": False,
    "changePictureProfile": False,
    "changeGroupPicture": [],
    "keyCommand": "",
    "myProfile": {
        "displayName": "",
        "coverId": "",
        "pictureStatus": "",
        "statusMessage": ""
    },
    "mimic": {
        "copy": False,
        "status": False,
        "target": {}
    },
    "setKey": False,
    "unsendMessage": False
}
sider = {}
alamat = {
    "linkimage": "",
    "linkvid": ""
}
read = {
    "ROM": {},
    "readPoint": {},
    "readMember": {},
    "readTime": {}
}

list_language = {
    "list_textToSpeech": {
        "id": "Indonesia",
        "af" : "Afrikaans",
        "sq" : "Albanian",
        "ar" : "Arabic",
        "hy" : "Armenian",
        "bn" : "Bengali",
        "ca" : "Catalan",
        "zh" : "Chinese",
        "zh-cn" : "Chinese (Mandarin/China)",
        "zh-tw" : "Chinese (Mandarin/Taiwan)",
        "zh-yue" : "Chinese (Cantonese)",
        "hr" : "Croatian",
        "cs" : "Czech",
        "da" : "Danish",
        "nl" : "Dutch",
        "en" : "English",
        "en-au" : "English (Australia)",
        "en-uk" : "English (United Kingdom)",
        "en-us" : "English (United States)",
        "eo" : "Esperanto",
        "fi" : "Finnish",
        "fr" : "French",
        "de" : "German",
        "el" : "Greek",
        "hi" : "Hindi",
        "hu" : "Hungarian",
        "is" : "Icelandic",
        "id" : "Indonesian",
        "it" : "Italian",
        "ja" : "Japanese",
        "km" : "Khmer (Cambodian)",
        "ko" : "Korean",
        "la" : "Latin",
        "lv" : "Latvian",
        "mk" : "Macedonian",
        "no" : "Norwegian",
        "pl" : "Polish",
        "pt" : "Portuguese",
        "ro" : "Romanian",
        "ru" : "Russian",
        "sr" : "Serbian",
        "si" : "Sinhala",
        "sk" : "Slovak",
        "es" : "Spanish",
        "es-es" : "Spanish (Spain)",
        "es-us" : "Spanish (United States)",
        "sw" : "Swahili",
        "sv" : "Swedish",
        "ta" : "Tamil",
        "th" : "Thai",
        "tr" : "Turkish",
        "uk" : "Ukrainian",
        "vi" : "Vietnamese",
        "cy" : "Welsh"
    },
    "list_translate": {
        "af": "afrikaans",
        "sq": "albanian",
        "am": "amharic",
        "ar": "arabic",
        "hy": "armenian",
        "az": "azerbaijani",
        "eu": "basque",
        "be": "belarusian",
        "bn": "bengali",
        "bs": "bosnian",
        "bg": "bulgarian",
        "ca": "catalan",
        "ceb": "cebuano",
        "ny": "chichewa",
        "zh-cn": "chinese (simplified)",
        "zh-tw": "chinese (traditional)",
        "co": "corsican",
        "hr": "croatian",
        "cs": "czech",
        "da": "danish",
        "nl": "dutch",
        "en": "english",
        "eo": "esperanto",
        "et": "estonian",
        "tl": "filipino",
        "fi": "finnish",
        "fr": "french",
        "fy": "frisian",
        "gl": "galician",
        "ka": "georgian",
        "de": "german",
        "el": "greek",
        "gu": "gujarati",
        "ht": "haitian creole",
        "ha": "hausa",
        "haw": "hawaiian",
        "iw": "hebrew",
        "hi": "hindi",
        "hmn": "hmong",
        "hu": "hungarian",
        "is": "icelandic",
        "ig": "igbo",
        "id": "indonesian",
        "ga": "irish",
        "it": "italian",
        "ja": "japanese",
        "jw": "javanese",
        "kn": "kannada",
        "kk": "kazakh",
        "km": "khmer",
        "ko": "korean",
        "ku": "kurdish (kurmanji)",
        "ky": "kyrgyz",
        "lo": "lao",
        "la": "latin",
        "lv": "latvian",
        "lt": "lithuanian",
        "lb": "luxembourgish",
        "mk": "macedonian",
        "mg": "malagasy",
        "ms": "malay",
        "ml": "malayalam",
        "mt": "maltese",
        "mi": "maori",
        "mr": "marathi",
        "mn": "mongolian",
        "my": "myanmar (burmese)",
        "ne": "nepali",
        "no": "norwegian",
        "ps": "pashto",
        "fa": "persian",
        "pl": "polish",
        "pt": "portuguese",
        "pa": "punjabi",
        "ro": "romanian",
        "ru": "russian",
        "sm": "samoan",
        "gd": "scots gaelic",
        "sr": "serbian",
        "st": "sesotho",
        "sn": "shona",
        "sd": "sindhi",
        "si": "sinhala",
        "sk": "slovak",
        "sl": "slovenian",
        "so": "somali",
        "es": "spanish",
        "su": "sundanese",
        "sw": "swahili",
        "sv": "swedish",
        "tg": "tajik",
        "ta": "tamil",
        "te": "telugu",
        "th": "thai",
        "tr": "turkish",
        "uk": "ukrainian",
        "ur": "urdu",
        "uz": "uzbek",
        "vi": "vietnamese",
        "cy": "welsh",
        "xh": "xhosa",
        "yi": "yiddish",
        "yo": "yoruba",
        "zu": "zulu",
        "fil": "Filipino",
        "he": "Hebrew"
    }
}

try:
    with open("Log_data.json","r",encoding="utf_8_sig") as f:
        msg_dict = json.loads(f.read())
except:
    print("Couldn't read Log data")

settings["myProfile"]["displayName"] = botProfile.displayName
settings["myProfile"]["statusMessage"] = botProfile.statusMessage
settings["myProfile"]["pictureStatus"] = botProfile.pictureStatus

def restartBot():
    print ("[ INFO ] BOT RESTART")
    python = sys.executable
    os.execl(python, python, *sys.argv)


def logError(text):
    bot.log("[ ERROR ] {}".format(str(text)))
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
    with open("logError.txt","a") as error:
        error.write("\n[ {} ] {}".format(str(time), text))

def cTime_to_datetime(unixtime):
    return datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
def dt_to_str(dt):
    return dt.strftime('%H:%M:%S')
def sendCarousel(data):
    data = json.dumps(data)
    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/SendMessage"
    headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0.1; Redmi 3S Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/68.0.3440.85 Mobile Safari/537.36 Line/8.11.0'}
    headers['Content-Type'] = 'application/json'
    headers['Accept-Encoding'] = 'gzip,deflate'
    headers['Accept-Language'] = 'id-ID,en-US;q=0.9'
    headers['Connection'] = 'keep-alive'
    return requests.post(url, data=data, headers=headers)
def delete_log():
    ndt = datetime.now()
    for data in msg_dict:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > timedelta(1):
            if "path" in msg_dict[data]:
                bot.deleteFile(msg_dict[data]["path"])
            del msg_dict[data]
def changeVideoAndPictureProfile(pict, vids):
    try:
        files = {'file': open(vids, 'rb')}
        obs_params = bot.genOBSParams({'oid': botMid, 'ver': '2.0', 'type': 'video', 'cat': 'vp.mp4', 'name': 'Hello_World.mp4'})
        data = {'params': obs_params}
        r_vp = bot.server.postContent('{}/talk/vp/upload.nhn'.format(str(bot.server.LINE_OBS_DOMAIN)), data=data, files=files)
        if r_vp.status_code != 201:
            return "Failed update profile"
        bot.updateProfilePicture(pict, 'vp')
        return "Success update profile"
    except Exception as e:
        raise Exception("Error change video and picture profile %s"%str(e))
def sendMention(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@zeroxyuuki "
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    bot.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)

def command(text):
    pesan = text.lower()
    if settings["setKey"] == True:
        if pesan.startswith(settings["keyCommand"]):
            cmd = pesan.replace(settings["keyCommand"],"")
        else:
            cmd = "Undefined command"
    else:
        cmd = text.lower()
    return cmd

def helpmessage():
    if settings['setKey'] == True:
        key = settings['keyCommand']
    else:
        key = ''
    helpMessage =   "╔══[ Help Message ]" + "\n" + \
                    "╠ " + key + "Help" + "\n" + \
                    "╠ " + key + "Translate" + "\n" + \
                    "╠ " + key + "TTS" + "\n" + \
                    "╠══[ Status Command ]" + "\n" + \
                    "╠ " + key + "Restart" + "\n" + \
                    "╠ " + key + "Runtime" + "\n" + \
                    "╠ " + key + "Speed" + "\n" + \
                    "╠ " + key + "Status" + "\n" + \
                    "╠ MyKey" + "\n" + \
                    "╠ SetKey「On/Off」" + "\n" + \
                    "╠══[ Settings Command ]" + "\n" + \
                    "╠ " + key + "AutoAdd「On/Off」" + "\n" + \
                    "╠ " + key + "AutoJoin「On/Off」" + "\n" + \
                    "╠ " + key + "AutoJoinTicket「On/Off」" + "\n" + \
                    "╠ " + key + "AutoLeave「On/Off」" + "\n" + \
                    "╠ " + key + "AutoRead「On/Off」" + "\n" + \
                    "╠ " + key + "AutoRespon「On/Off」" + "\n" + \
                    "╠ " + key + "CheckContact「On/Off」" + "\n" + \
                    "╠ " + key + "CheckPost「On/Off」" + "\n" + \
                    "╠ " + key + "CheckSticker「On/Off」" + "\n" + \
                    "╠ " + key + "UnsendChat「On/Off」" + "\n" + \
                    "╠══[ Self Command ]" + "\n" + \
                    "╠ " + key + "ChangeName:「Query」" + "\n" + \
                    "╠ " + key + "ChangeBio:「Query」" + "\n" + \
                    "╠ " + key + "Me" + "\n" + \
                    "╠ " + key + "MyMid" + "\n" + \
                    "╠ " + key + "MyName" + "\n" + \
                    "╠ " + key + "MyBio" + "\n" + \
                    "╠ " + key + "MyPicture" + "\n" + \
                    "╠ " + key + "MyVideoProfile" + "\n" + \
                    "╠ " + key + "MyCover" + "\n" + \
                    "╠ " + key + "StealContact「Mention」" + "\n" + \
                    "╠ " + key + "StealMid「Mention」" + "\n" + \
                    "╠ " + key + "StealName「Mention」" + "\n" + \
                    "╠ " + key + "StealBio「Mention」" + "\n" + \
                    "╠ " + key + "StealPicture「Mention」" + "\n" + \
                    "╠ " + key + "StealVideoProfile「Mention」" + "\n" + \
                    "╠ " + key + "StealCover「Mention」" + "\n" + \
                    "╠ " + key + "CloneProfile「Mention」" + "\n" + \
                    "╠ " + key + "RestoreProfile" + "\n" + \
                    "╠ " + key + "BackupProfile" + "\n" + \
                    "╠ " + key + "ChangePictureProfile" + "\n" + \
                    "╠══[ Group Command ]" + "\n" + \
                    "╠ " + key + "GroupCreator" + "\n" + \
                    "╠ " + key + "GroupId" + "\n" + \
                    "╠ " + key + "GroupName" + "\n" + \
                    "╠ " + key + "GroupPicture" + "\n" + \
                    "╠ " + key + "GroupTicket" + "\n" + \
                    "╠ " + key + "GroupTicket「On/Off」" + "\n" + \
                    "╠ " + key + "GroupList" + "\n" + \
                    "╠ " + key + "GroupMemberList" + "\n" + \
                    "╠ " + key + "GroupInfo" + "\n" + \
                    "╠ " + key + "ChangeGroupPicture" + "\n" + \
                    "╠══[ Special Command ]" + "\n" + \
                    "╠ " + key + "Mimic「On/Off」" + "\n" + \
                    "╠ " + key + "MimicList" + "\n" + \
                    "╠ " + key + "MimicAdd「Mention」" + "\n" + \
                    "╠ " + key + "MimicDel「Mention」" + "\n" + \
                    "╠ " + key + "Mention" + "\n" + \
                    "╠ " + key + "Lurking「On/Off/Reset」" + "\n" + \
                    "╠ " + key + "Lurking" + "\n" + \
                    "╠ " + key + "Crash" + "\n" + \
                    "╠══[ Media Command ]" + "\n" + \
                    "╠ " + key + "CheckDate「Date」" + "\n" + \
                    "╠ " + key + "CheckWebsite「url」" + "\n" + \
                    "╠ " + key + "CheckPraytime「Location」" + "\n" + \
                    "╠ " + key + "CheckWeather「Location」" + "\n" + \
                    "╠ " + key + "CheckLocation「Location」" + "\n" + \
                    "╠ " + key + "InstaInfo 「UserName」" + "\n" + \
                    "╠ " + key + "InstaPost 「UserName」|「Number」" + "\n" + \
                    "╠ " + key + "InstaStory 「UserName」|「Number」" + "\n" + \
                    "╠ " + key + "SearchYoutube「Search」" + "\n" + \
                    "╠ " + key + "SearchMusic 「Search」" + "\n" + \
                    "╠ " + key + "SearchLyric 「Search」" + "\n" + \
                    "╠ " + key + "SearchImage 「Search」" + "\n" + \
                    "╚══[ HELLO WORLD ]"
    return helpMessage

def helptexttospeech():
    if settings['setKey'] == True:
        key = settings['keyCommand']
    else:
        key = ''
    helpTextToSpeech =  "╔══[ Help TextToSpeech ]" + "\n" + \
                        "╠ " + key + "af : Afrikaans" + "\n" + \
                        "╠ " + key + "sq : Albanian" + "\n" + \
                        "╠ " + key + "ar : Arabic" + "\n" + \
                        "╠ " + key + "hy : Armenian" + "\n" + \
                        "╠ " + key + "bn : Bengali" + "\n" + \
                        "╠ " + key + "ca : Catalan" + "\n" + \
                        "╠ " + key + "zh : Chinese" + "\n" + \
                        "╠ " + key + "zhcn : Chinese (Mandarin/China)" + "\n" + \
                        "╠ " + key + "zhtw : Chinese (Mandarin/Taiwan)" + "\n" + \
                        "╠ " + key + "zhyue : Chinese (Cantonese)" + "\n" + \
                        "╠ " + key + "hr : Croatian" + "\n" + \
                        "╠ " + key + "cs : Czech" + "\n" + \
                        "╠ " + key + "da : Danish" + "\n" + \
                        "╠ " + key + "nl : Dutch" + "\n" + \
                        "╠ " + key + "en : English" + "\n" + \
                        "╠ " + key + "enau : English (Australia)" + "\n" + \
                        "╠ " + key + "enuk : English (United Kingdom)" + "\n" + \
                        "╠ " + key + "enus : English (United States)" + "\n" + \
                        "╠ " + key + "eo : Esperanto" + "\n" + \
                        "╠ " + key + "fi : Finnish" + "\n" + \
                        "╠ " + key + "fr : French" + "\n" + \
                        "╠ " + key + "de : German" + "\n" + \
                        "╠ " + key + "el : Greek" + "\n" + \
                        "╠ " + key + "hi : Hindi" + "\n" + \
                        "╠ " + key + "hu : Hungarian" + "\n" + \
                        "╠ " + key + "is : Icelandic" + "\n" + \
                        "╠ " + key + "id : Indonesian" + "\n" + \
                        "╠ " + key + "it : Italian" + "\n" + \
                        "╠ " + key + "ja : Japanese" + "\n" + \
                        "╠ " + key + "km : Khmer (Cambodian)" + "\n" + \
                        "╠ " + key + "ko : Korean" + "\n" + \
                        "╠ " + key + "la : Latin" + "\n" + \
                        "╠ " + key + "lv : Latvian" + "\n" + \
                        "╠ " + key + "mk : Macedonian" + "\n" + \
                        "╠ " + key + "no : Norwegian" + "\n" + \
                        "╠ " + key + "pl : Polish" + "\n" + \
                        "╠ " + key + "pt : Portuguese" + "\n" + \
                        "╠ " + key + "ro : Romanian" + "\n" + \
                        "╠ " + key + "ru : Russian" + "\n" + \
                        "╠ " + key + "sr : Serbian" + "\n" + \
                        "╠ " + key + "si : Sinhala" + "\n" + \
                        "╠ " + key + "sk : Slovak" + "\n" + \
                        "╠ " + key + "es : Spanish" + "\n" + \
                        "╠ " + key + "eses : Spanish (Spain)" + "\n" + \
                        "╠ " + key + "esus : Spanish (United States)" + "\n" + \
                        "╠ " + key + "sw : Swahili" + "\n" + \
                        "╠ " + key + "sv : Swedish" + "\n" + \
                        "╠ " + key + "ta : Tamil" + "\n" + \
                        "╠ " + key + "th : Thai" + "\n" + \
                        "╠ " + key + "tr : Turkish" + "\n" + \
                        "╠ " + key + "uk : Ukrainian" + "\n" + \
                        "╠ " + key + "vi : Vietnamese" + "\n" + \
                        "╠ " + key + "cy : Welsh" + "\n" + \
                        "╚══[ ----------------------- ]" + "\n" + "\n\n" + \
                        "Contoh : " + key + "say-id lol"
    return helpTextToSpeech

def helptranslate():
    if settings['setKey'] == True:
        key = settings['keyCommand']
    else:
        key = ''
    helpTranslate = "╔══[ Help Translate ]" + "\n" + \
                    "╠ " + key + "af : afrikaans" + "\n" + \
                    "╠ " + key + "sq : albanian" + "\n" + \
                    "╠ " + key + "am : amharic" + "\n" + \
                    "╠ " + key + "ar : arabic" + "\n" + \
                    "╠ " + key + "hy : armenian" + "\n" + \
                    "╠ " + key + "az : azerbaijani" + "\n" + \
                    "╠ " + key + "eu : basque" + "\n" + \
                    "╠ " + key + "be : belarusian" + "\n" + \
                    "╠ " + key + "bn : bengali" + "\n" + \
                    "╠ " + key + "bs : bosnian" + "\n" + \
                    "╠ " + key + "bg : bulgarian" + "\n" + \
                    "╠ " + key + "ca : catalan" + "\n" + \
                    "╠ " + key + "ceb : cebuano" + "\n" + \
                    "╠ " + key + "ny : chichewa" + "\n" + \
                    "╠ " + key + "zhcn : chinese (simplified)" + "\n" + \
                    "╠ " + key + "zhtw : chinese (traditional)" + "\n" + \
                    "╠ " + key + "co : corsican" + "\n" + \
                    "╠ " + key + "hr : croatian" + "\n" + \
                    "╠ " + key + "cs : czech" + "\n" + \
                    "╠ " + key + "da : danish" + "\n" + \
                    "╠ " + key + "nl : dutch" + "\n" + \
                    "╠ " + key + "en : english" + "\n" + \
                    "╠ " + key + "eo : esperanto" + "\n" + \
                    "╠ " + key + "et : estonian" + "\n" + \
                    "╠ " + key + "tl : filipino" + "\n" + \
                    "╠ " + key + "fi : finnish" + "\n" + \
                    "╠ " + key + "fr : french" + "\n" + \
                    "╠ " + key + "fy : frisian" + "\n" + \
                    "╠ " + key + "gl : galician" + "\n" + \
                    "╠ " + key + "ka : georgian" + "\n" + \
                    "╠ " + key + "de : german" + "\n" + \
                    "╠ " + key + "el : greek" + "\n" + \
                    "╠ " + key + "gu : gujarati" + "\n" + \
                    "╠ " + key + "ht : haitian creole" + "\n" + \
                    "╠ " + key + "ha : hausa" + "\n" + \
                    "╠ " + key + "haw : hawaiian" + "\n" + \
                    "╠ " + key + "iw : hebrew" + "\n" + \
                    "╠ " + key + "hi : hindi" + "\n" + \
                    "╠ " + key + "hmn : hmong" + "\n" + \
                    "╠ " + key + "hu : hungarian" + "\n" + \
                    "╠ " + key + "is : icelandic" + "\n" + \
                    "╠ " + key + "ig : igbo" + "\n" + \
                    "╠ " + key + "id : indonesian" + "\n" + \
                    "╠ " + key + "ga : irish" + "\n" + \
                    "╠ " + key + "it : italian" + "\n" + \
                    "╠ " + key + "ja : japanese" + "\n" + \
                    "╠ " + key + "jw : javanese" + "\n" + \
                    "╠ " + key + "kn : kannada" + "\n" + \
                    "╠ " + key + "kk : kazakh" + "\n" + \
                    "╠ " + key + "km : khmer" + "\n" + \
                    "╠ " + key + "ko : korean" + "\n" + \
                    "╠ " + key + "ku : kurdish (kurmanji)" + "\n" + \
                    "╠ " + key + "ky : kyrgyz" + "\n" + \
                    "╠ " + key + "lo : lao" + "\n" + \
                    "╠ " + key + "la : latin" + "\n" + \
                    "╠ " + key + "lv : latvian" + "\n" + \
                    "╠ " + key + "lt : lithuanian" + "\n" + \
                    "╠ " + key + "lb : luxembourgish" + "\n" + \
                    "╠ " + key + "mk : macedonian" + "\n" + \
                    "╠ " + key + "mg : malagasy" + "\n" + \
                    "╠ " + key + "ms : malay" + "\n" + \
                    "╠ " + key + "ml : malayalam" + "\n" + \
                    "╠ " + key + "mt : maltese" + "\n" + \
                    "╠ " + key + "mi : maori" + "\n" + \
                    "╠ " + key + "mr : marathi" + "\n" + \
                    "╠ " + key + "mn : mongolian" + "\n" + \
                    "╠ " + key + "my : myanmar (burmese)" + "\n" + \
                    "╠ " + key + "ne : nepali" + "\n" + \
                    "╠ " + key + "no : norwegian" + "\n" + \
                    "╠ " + key + "ps : pashto" + "\n" + \
                    "╠ " + key + "fa : persian" + "\n" + \
                    "╠ " + key + "pl : polish" + "\n" + \
                    "╠ " + key + "pt : portuguese" + "\n" + \
                    "╠ " + key + "pa : punjabi" + "\n" + \
                    "╠ " + key + "ro : romanian" + "\n" + \
                    "╠ " + key + "ru : russian" + "\n" + \
                    "╠ " + key + "sm : samoan" + "\n" + \
                    "╠ " + key + "gd : scots gaelic" + "\n" + \
                    "╠ " + key + "sr : serbian" + "\n" + \
                    "╠ " + key + "st : sesotho" + "\n" + \
                    "╠ " + key + "sn : shona" + "\n" + \
                    "╠ " + key + "sd : sindhi" + "\n" + \
                    "╠ " + key + "si : sinhala" + "\n" + \
                    "╠ " + key + "sk : slovak" + "\n" + \
                    "╠ " + key + "sl : slovenian" + "\n" + \
                    "╠ " + key + "so : somali" + "\n" + \
                    "╠ " + key + "es : spanish" + "\n" + \
                    "╠ " + key + "su : sundanese" + "\n" + \
                    "╠ " + key + "sw : swahili" + "\n" + \
                    "╠ " + key + "sv : swedish" + "\n" + \
                    "╠ " + key + "tg : tajik" + "\n" + \
                    "╠ " + key + "ta : tamil" + "\n" + \
                    "╠ " + key + "te : telugu" + "\n" + \
                    "╠ " + key + "th : thai" + "\n" + \
                    "╠ " + key + "tr : turkish" + "\n" + \
                    "╠ " + key + "uk : ukrainian" + "\n" + \
                    "╠ " + key + "ur : urdu" + "\n" + \
                    "╠ " + key + "uz : uzbek" + "\n" + \
                    "╠ " + key + "vi : vietnamese" + "\n" + \
                    "╠ " + key + "cy : welsh" + "\n" + \
                    "╠ " + key + "xh : xhosa" + "\n" + \
                    "╠ " + key + "yi : yiddish" + "\n" + \
                    "╠ " + key + "yo : yoruba" + "\n" + \
                    "╠ " + key + "zu : zulu" + "\n" + \
                    "╠ " + key + "fil : Filipino" + "\n" + \
                    "╠ " + key + "he : Hebrew" + "\n" + \
                    "╚══[ --------------------]" + "\n" + "\n\n" + \
                    "Contoh : " + key + "tr-id Zero"
    return helpTranslate

def clientBot(op):
    try:
        if op.type == 0:
            print ("[ 0 ] END OF OPERATION")
            return

        if op.type == 5:
            print ("[ 5 ] NOTIFIED ADD CONTACT")
            if settings["autoAdd"] == True:
                bot.findAndAddContactsByMid(op.param1)
            sendMention(op.param1, "hai @! \ncie ngeadd v:", [op.param2])

        if op.type == 55:
            try:
                if op.param1 in read['readPoint']:
                    if op.param2 in read['readMember'][op.param1]:
                        pass
                    else:
                        read['readMember'][op.param1] += op.param2
                    read['ROM'][op.param1][op.param2] = op.param2
                if op.param1 in sider:
                    if op.param2 not in sider[op.param1]:
                        sendMention(op.param1, "hai @! \nJoin Sini Mhank", [op.param2])
                        sider[op.param1].append(op.param2)
            except Exception as error:
                logError(error)
                traceback.print_tb(error.__traceback__)
                
        if op.type == 13:
            print ("[ 13 ] NOTIFIED INVITE INTO GROUP")
            if botMid in op.param3:
                if settings["autoJoin"] == True:
                    bot.acceptGroupInvitation(op.param1)
                    sendMention(op.param1, "@! Thanks for your invitation",[op.param2])

        if op.type in [22, 24]:
            print ("[ 22 And 24 ] NOTIFIED INVITE INTO ROOM & NOTIFIED LEAVE ROOM")
            if settings["autoLeave"] == True:
                sendMention(op.param1, "@! Thanks for your invitation,\nbut im cannot join to your group",[op.param2])
                bot.leaveRoom(op.param1)

        if op.type == 25:
            try:
                print ("[ 25 ] SEND MESSAGE")
                msg = op.message
                text = msg.text
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                setKey = settings["keyCommand"].title()
                if settings["setKey"] == False:
                    setKey = ''
                if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                    if msg.toType == 0:
                        if sender != bot.profile.mid:
                            to = sender
                        else:
                            to = receiver
                    elif msg.toType == 1:
                        to = receiver
                    elif msg.toType == 2:
                        to = receiver
                    if msg.contentType == 0:
                        if text is None:
                            return
                        else:
                            cmd = command(text)
                            if cmd == "help":
                                helpMessage = helpmessage()
                                bot.sendMessage(to, str(helpMessage))
                            elif cmd.startswith ('cvp'):
                              url = alamat["linkimage"]
                              url2 = alamat["linkvid"]
                              bot.sendMessage(to, "sedang proses....")
                              video = bot.downloadFileURL(url2, saveAs="video.mp4")
                              bot.sendMessage(to, "sukses download video......\ntunggu beberapa saat..")
                              image = bot.downloadFileURL(url, saveAs="image.jpg")
                              changeVideoAndPictureProfile('image.jpg','video.mp4')
                              bot.sendMessage(to, "sukses......\ncek pp anda...")
                            elif 'linkvid: ' in msg.text:
                              spl = msg.text.replace('linkvid: ','')
                              if spl in [""," ","\n",None]:
                                bot.sendMessage(msg.to, "Gagal set link video")
                              else:
                                alamat["linkvid"] = spl
                                bot.sendMessage(msg.to, "link video telah diset :\n\n{}".format(str(spl)))
                            elif 'linkimage: ' in msg.text:
                              spl = msg.text.replace('linkimage: ','')
                              if spl in [""," ","\n",None]:
                                bot.sendMessage(msg.to, "Gagal set link foto")
                              else:
                                alamat["linkimage"] = spl
                                bot.sendMessage(msg.to, "link foto telah diset :\n\n{}".format(str(spl)))    
                            elif cmd == "tts":
                                helpTextToSpeech = helptexttospeech()
                                bot.sendMessage(to, str(helpTextToSpeech))
                            elif cmd =="memelist":
                                helpMemelist = helpmemelist()
                                bot.sendMessage(to, str(helpMemelist))
                            elif cmd == "translate":
                                helpTranslate = helptranslate()
                                bot.sendMessage(to, str(helpTranslate))
                            elif cmd.startswith("changekey:"):
                                sep = text.split(" ")
                                key = text.replace(sep[0] + " ","")
                                if " " in key:
                                    bot.sendMessage(to, "Key tidak bisa menggunakan spasi")
                                else:
                                    settings["keyCommand"] = str(key).lower()
                                    bot.sendMessage(to, "Berhasil mengubah key command menjadi [ {} ]".format(str(key).lower()))
                            elif cmd == "sp bot":
                              bot.sendMessage(to, '[ Speed ]\n0.0001')
                            elif cmd == "tiktok":
                              r=requests.get("https://farzain.com/api/tiktok.php?country=id&apikey=EmGasKDC9P2cuj8JivgAUHIxr&type=json")
                              data=r.text
                              data=json.loads(data)
                              print(data)
                              hasil = "「LINK」\n"
                              hasil += "\nLinkPicture : " +str(data["first_pict"])                                
                              hasil += "\nLinkVideo : " +str(data["first_video"])
                              hasil += "\nQuotes : \n" +str(data["quote"])                                
                              bot.sendMessage(msg.to, str(hasil))  
                              bot.sendImageWithURL(to, data["first_pict"])
                              bot.sendVideoWithURL(to, data["first_video"])
                            elif cmd == "runtime":
                                timeNow = time.time()
                                runtime = timeNow - botStart
                                runtime = format_timespan(runtime)
                                bot.sendMessage(to, "Bot Already Running {}".format(str(runtime)))
                            elif cmd == "restart":
                              bot.sendMessage(to, "Restarting...")
                              bot.sendMessage(to, "Success Restart Bot")
                              restartBot()
                            elif cmd == "cek error":
                              with open('errorLog.txt', 'r') as er:
                                error = er.read()
                                bot.sendFooter(to, str(error))
# Pembatas Script #
                            elif cmd == "memberlist":
                              if msg.toType == 2:
                                group = bot.getGroup(to)
                                num = 0
                                ret_ = "╔══[ List Member ]"
                                for contact in group.members:
                                  num += 1
                                  ret_ += "\n╠ {}. {}".format(num, contact.displayName)
                                  ret_ += "\n╚══[ Total {} Members]".format(len(group.members))
                                  bot.sendMessage(to, ret_)
                            elif cmd == "pendinglist":
                              if msg.toType == 2:
                                group = bot.getGroup(to)
                                ret_ = "╔══[ Pending List ]"
                                no = 0
                                if group.invitee is None or group.invitee == []:
                                  return bot.sendMessage(to, "Tidak ada pendingan")
                                else:
                                  for pending in group.invitee:
                                    no += 1
                                    ret_ += "\n╠ {}. {}".format(str(no), str(pending.displayName))
                                    ret_ += "\n╚══[ Total {} Pending]".format(str(len(group.invitee)))
                                    bot.sendMessage(to, str(ret_))
                            elif cmd == "speed":
                                start = time.time()
                                bot.sendMessage(to, "Benchmarking...")
                                elapsed_time = time.time() - start
                                bot.sendMessage(to, "[ Speed ]\nKecepatan mengirim pesan {} detik".format(str(elapsed_time)))
                            elif cmd == "autoadd on":
                                settings["autoAdd"] = True
                                bot.sendMessage(to, "Berhasil mengaktifkan auto add")
                            elif cmd == "autoadd off":
                                settings["autoAdd"] = False
                                bot.sendMessage(to, "Berhasil menonaktifkan auto add")
                            elif cmd == "autojoin on":
                                settings["autoJoin"] = True
                                bot.sendMessage(to, "Berhasil mengaktifkan auto join")
                            elif cmd == "autojoin off":
                                settings["autoJoin"] = False
                                bot.sendMessage(to, "Berhasil menonaktifkan auto join")
                            elif cmd == "autoleave on":
                                settings["autoLeave"] = True
                                bot.sendMessage(to, "Berhasil mengaktifkan auto leave")
                            elif cmd == "autoleave off":
                                settings["autoLeave"] = False
                                bot.sendMessage(to, "Berhasil menonaktifkan auto leave")
                            elif cmd == "autorespon on":
                                settings["autoRespon"] = True
                                bot.sendMessage(to, "Berhasil mengaktifkan auto respon")
                            elif cmd == "autorespon off":
                                settings["autoRespon"] = False
                                bot.sendMessage(to, "Berhasil menonaktifkan auto respon")
                            elif cmd == "autoread on":
                                settings["autoRead"] = True
                                bot.sendMessage(to, "Berhasil mengaktifkan auto read")
                            elif cmd == "autoread off":
                                settings["autoRead"] = False
                                bot.sendMessage(to, "Berhasil menonaktifkan auto read")
                            elif cmd == "autojointicket on":
                                settings["autoJoinTicket"] = True
                                bot.sendMessage(to, "Berhasil mengaktifkan auto join by ticket")
                            elif cmd == "autoJoinTicket off":
                                settings["autoJoin"] = False
                                bot.sendMessage(to, "Berhasil menonaktifkan auto join by ticket")
                            elif cmd == "checkcontact on":
                                settings["checkContact"] = True
                                bot.sendMessage(to, "Berhasil mengaktifkan check details contact")
                            elif cmd == "checkcontact off":
                                settings["checkContact"] = False
                                bot.sendMessage(to, "Berhasil menonaktifkan check details contact")
                            elif cmd == "checkpost on":
                                settings["checkPost"] = True
                                bot.sendMessage(to, "Berhasil mengaktifkan check details post")
                            elif cmd == "checkpost off":
                                settings["checkPost"] = False
                                bot.sendMessage(to, "Berhasil menonaktifkan check details post")
                            elif cmd == "checksticker on":
                                settings["checkSticker"] = True
                                bot.sendMessage(to, "Berhasil mengaktifkan check details sticker")
                            elif cmd == "checksticker off":
                                settings["checkSticker"] = False
                                bot.sendMessage(to, "Berhasil menonaktifkan check details sticker")
                            elif cmd == "unsendchat on":
                                settings["unsendMessage"] = True
                                bot.sendMessage(to, "Berhasil mengaktifkan unsend message")
                            elif cmd == "unsendchat off":
                                settings["unsendMessage"] = False
                                bot.sendMessage(to, "Berhasil menonaktifkan unsend message")
                            elif cmd == "status" or cmd == "help status":
                                try:
                                    ret_ = "╔══[ Status ]"
                                    if settings["autoAdd"] == True: ret_ += "\n╠══[ ✅ ] Auto Add"
                                    else: ret_ += "\n╠══[ ❌ ] Auto Add"
                                    if settings["autoJoin"] == True: ret_ += "\n╠══[ ✅ ] Auto Join"
                                    else: ret_ += "\n╠══[ ❌ ] Auto Join"
                                    if settings["autoLeave"] == True: ret_ += "\n╠══[ ✅ ] Auto Leave Room"
                                    else: ret_ += "\n╠══[ ❌ ] Auto Leave Room"
                                    if settings["autoJoinTicket"] == True: ret_ += "\n╠══[ ✅ ] Auto Join Ticket"
                                    else: ret_ += "\n╠══[ ❌ ] Auto Join Ticket"
                                    if settings["autoRead"] == True: ret_ += "\n╠══[ ✅ ] Auto Read"
                                    else: ret_ += "\n╠══[ ❌ ] Auto Read"
                                    if settings["autoRespon"] == True: ret_ += "\n╠══[ ✅ ] Detect Mention"
                                    else: ret_ += "\n╠══[ ❌ ] Detect Mention"
                                    if settings["checkContact"] == True: ret_ += "\n╠══[ ✅ ] Check Contact"
                                    else: ret_ += "\n╠══[ ❌ ] Check Contact"
                                    if settings["checkPost"] == True: ret_ += "\n╠══[ ✅ ] Check Post"
                                    else: ret_ += "\n╠══[ ❌ ] Check Post"
                                    if settings["checkSticker"] == True: ret_ += "\n╠══[ ✅ ] Check Sticker"
                                    else: ret_ += "\n╠══[ ❌ ] Check Sticker"
                                    if settings["setKey"] == True: ret_ += "\n╠══[ ✅ ] Set Key"
                                    else: ret_ += "\n╠══[ ❌ ] Set Key"
                                    if settings["unsendMessage"] == True: ret_ += "\n╠══[ ✅ ] Unsend Message"
                                    else: ret_ += "\n╠══[ ❌ ] Unsend Message"
                                    ret_ += "\n╚══[ Status ]"
                                    bot.sendMessage(to, str(ret_))
                                except Exception as e:
                                    bot.sendMessage(msg.to, str(e))
#----------------------#
                            elif cmd == "# ls":
                              nub = os.popen('ls')
                              programmer = nub.read()
                              bot.sendMessage(to, "{}".format(programmer))
                              programmer.close()
                            elif cmd == "ciduk on":
                              sider[to] = []
                              bot.sendMessage(to, "cek sider diaktifkan")
                            elif cmd == "ciduk off":
                              if to in sider:
                                del sider[to]
                                bot.sendMessage(to, "cek sider dinonaktifkan")
                              else:
                                bot.sendMessage(to, "cek sider belum diaktifkan")
                            elif cmd == "ciduk reset":
                              if to in sider:
                                sider[to] = []
                                bot.sendMessage(to, "cek sider telah di reset")
                              else:
                                bot.sendMessage(to, "cek sider belum diaktifkan")
                            elif cmd.startswith("instainfo"):
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                url = requests.get("http://rahandiapi.herokuapp.com/instainfo/{}?key=betakey".format(txt))
                                data = url.json()
                                icon = "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Instagram_icon.png/599px-Instagram_icon.png"
                                name = "Instagram"
                                link = "https://www.instagram.com/{}".format(data["result"]["username"])
                                result = "╔══[ Instagram Info ]"
                                result += "\n╠ Name : {}".format(data["result"]["name"])
                                result += "\n╠ Username: {}".format(data["result"]["username"])
                                result += "\n╠ Bio : {}".format(data["result"]["bio"])
                                result += "\n╠ Follower : {}".format(data["result"]["follower"])
                                result += "\n╠ Following : {}".format(data["result"]["following"])
                                result += "\n╠ Private : {}".format(data["result"]["private"])
                                result += "\n╠ Post : {}".format(data["result"]["mediacount"])
                                result += "\n╚══[ Finish ]"
                                bot.sendImageWithURL(to, data["result"]["url"])
                                bot.sendFooter(to, str(result, icon, name, link))
                            elif cmd.startswith("changename:"):
                                sep = text.split(" ")
                                string = text.replace(sep[0] + " ","")
                                if len(string) <= 20:
                                    profile = bot.getProfile()
                                    profile.displayName = string
                                    bot.updateProfile(profile)
                                    bot.sendMessage(to,"Berhasil mengganti display name menjadi {}".format(str(string)))
                            elif cmd.startswith("changebio"):
                                sep = text.split(" ")
                                string = text.replace(sep[0] + " ","")
                                if len(string) <= 500:
                                    profile = bot.getProfile()
                                    profile.statusMessage = string
                                    bot.updateProfile(profile)
                                    bot.sendMessage(to,"Berhasil mengganti status message menjadi{}".format(str(string)))
                            elif cmd.startswith("out "):
                                    botMID = bot.profile.mid
                                    targets = []
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key["MENTIONEES"] [0] ["M"]
                                    for x in key["MENTIONEES"]:
                                        targets.append(x["M"])
                                    for target in targets:
                                        try:
                                            bot.kickoutFromGroup(to,[target])
                                            time.sleep(1)
                                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                              names = re.findall(r'@(\w+)', text)
                                              mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                              mentionees = mention['MENTIONEES']
                                              lists = []
                                            for mention in mentionees:
                                              if mention["M"] not in lists:
                                                lists.append(mention["M"])
                                            for ls in lists:
                                                contact = bot.getContact(ls)
                                                bot.sendMessage(to, "「Success Kick」\n{}".format(str(contact.displayName)))
                                        except Exception as e:
                                            bot.sendMessage(to, str(e))  
                            elif cmd.startswith("graffiti"):
                                try:
                                    sep = msg.text.split(" ")
                                    tai = text.replace(sep[0] + " ","")
                                    r = requests.get('http://corrykalam.pw/api/graffiti.php?text={}'.format(tai))
                                    data = r.text
                                    data = json.loads(data)
                                    bot.sendImageWithURL(msg.to, str(data["image"]))
                                except Exception as error:
                                    logError(error)
                            elif cmd.startswith('downloadyt: '):
                              url = msg.text.replace('downloadyt: ','')
                              r = requests.get("http://corrykalam.pw/api/yt.php?url=" + url)
                              data = r.text
                              data = json.loads(data)
                              ret_ = "Your Link Download Video\n{}".format(str(data["mp4"]["720"]))
                              bot.sendMessage(to, str(ret_))
                            elif cmd == "me":
                                sendMention(to, "@!", [sender])
                                bot.sendContact(to, sender)
                            elif cmd == "mymid":
                                bot.sendMessage(to, "[ MID ]\n{}".format(sender))
                            elif cmd == "myname":
                                contact = bot.getContact(sender)
                                bot.sendMessage(to, "[ Display Name ]\n{}".format(contact.displayName))
                            elif cmd == "mybio":
                                contact = bot.getContact(sender)
                                bot.sendMessage(to, "[ Status Message ]\n{}".format(contact.statusMessage))
                            elif cmd == "mypicture":
                                contact = bot.getContact(sender)
                                bot.sendImageWithURL(to,"http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus))
                            elif cmd == "myvideoprofile":
                                contact = bot.getContact(sender)
                                bot.sendVideoWithURL(to,"http://dl.profile.line-cdn.net/{}/vp".format(contact.pictureStatus))
                            elif cmd == "mycover":
                                channel = bot.getProfileCoverURL(sender)
                                path = str(channel)
                                bot.sendImageWithURL(to, path)
                            elif cmd.startswith("cloneprofile "):
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        contact = bot.getContact(ls)
                                        bot.cloneContactProfile(ls)
                                        bot.sendMessage(to, "Berhasil mengclone profile {}".format(contact.displayName))
                            elif cmd == "restoreprofile":
                                try:
                                    botProfile = bot.getProfile()
                                    botProfile.displayName = str(settings["myProfile"]["displayName"])
                                    botProfile.statusMessage = str(settings["myProfile"]["statusMessage"])
                                    botProfile.pictureStatus = str(settings["myProfile"]["pictureStatus"])
                                    bot.updateProfileAttribute(8, botProfile.pictureStatus)
                                    bot.updateProfile(botProfile)
                                    coverId = str(settings["myProfile"]["coverId"])
                                    bot.updateProfileCoverById(coverId)
                                    bot.sendMessage(to, "Berhasil restore profile tunggu beberapa saat sampai profile berubah")
                                except Exception as e:
                                    bot.sendMessage(to, "Gagal restore profile")
                                    logError(error)
                            elif cmd == "backupprofile":
                                try:
                                    profile = bot.getProfile()
                                    settings["myProfile"]["displayName"] = str(profile.displayName)
                                    settings["myProfile"]["statusMessage"] = str(profile.statusMessage)
                                    settings["myProfile"]["pictureStatus"] = str(profile.pictureStatus)
                                    coverId = bot.getProfileDetail()["result"]["objectId"]
                                    settings["myProfile"]["coverId"] = str(coverId)
                                    bot.sendMessage(to, "Berhasil backup profile")
                                except Exception as e:
                                    bot.sendMessage(to, "Gagal backup profile")
                                    logError(error)
                            elif cmd.startswith("stealmid "):
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    ret_ = "[ Mid User ]"
                                    for ls in lists:
                                        ret_ += "\n{}".format(str(ls))
                                    bot.sendMessage(to, str(ret_))
                            elif cmd.startswith("stealname "):
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        contact = bot.getContact(ls)
                                        bot.sendMessage(to, "[ Display Name ]\n{}".format(str(contact.displayName)))
                            elif cmd.startswith("stealbio "):
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        contact = bot.getContact(ls)
                                        bot.sendMessage(to, "[ Status Message ]\n{}".format(str(contact.statusMessage)))
                            elif cmd.startswith("stealpicture"):
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        contact = bot.getContact(ls)
                                        path = "http://dl.profile.line.naver.jp/{}".format(contact.pictureStatus)
                                        bot.sendImageWithURL(to, str(path))
                            elif cmd.startswith("stealvideoprofile "):
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        contact = bot.getContact(ls)
                                        path = "http://dl.profile.line.naver.jp/{}/vp".format(contact.pictureStatus)
                                        bot.sendVideoWithURL(to, str(path))
                            elif cmd.startswith("stealcover "):
                                if bot != None:
                                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                                        names = re.findall(r'@(\w+)', text)
                                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                        mentionees = mention['MENTIONEES']
                                        lists = []
                                        for mention in mentionees:
                                            if mention["M"] not in lists:
                                                lists.append(mention["M"])
                                        for ls in lists:
                                            channel = bot.getProfileCoverURL(ls)
                                            path = str(channel)
                                            bot.sendImageWithURL(to, str(path))
                            elif cmd == 'Crash':
                                 bot.sendContact(to, "ue10de0a302f521d008e7b4efa9abd842,'")
# Pembatas Script
                            elif cmd == 'groupcreator':
                                group = bot.getGroup(to)
                                GS = group.creator.mid
                                bot.sendContact(to, GS)
                            elif cmd == 'groupid':
                                gid = bot.getGroup(to)
                                bot.sendMessage(to, "[ID Group : ]\n" + gid.id)
                            elif cmd == 'grouppicture':
                                group = bot.getGroup(to)
                                path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                                bot.sendImageWithURL(to, path)
                            elif cmd == 'groupname':
                                gid = bot.getGroup(to)
                                bot.sendMessage(to, "[Nama Group : ]\n" + gid.name)
                            elif cmd == 'groupticket':
                                if msg.toType == 2:
                                    group = bot.getGroup(to)
                                    if group.preventedJoinByTicket == False:
                                        ticket = bot.reissueGroupTicket(to)
                                        bot.sendMessage(to, "[ Group Ticket ]\nhttps://line.me/R/ti/g/{}".format(str(ticket)))
                                    else:
                                        bot.sendMessage(to, "Grup qr tidak terbuka silahkan buka terlebih dahulu dengan perintah {}openqr".format(str(settings["keyCommand"])))
                            elif cmd == 'groupticket on':
                                if msg.toType == 2:
                                    group = bot.getGroup(to)
                                    if group.preventedJoinByTicket == False:
                                        bot.sendMessage(to, "Grup qr sudah terbuka")
                                    else:
                                        group.preventedJoinByTicket = False
                                        bot.updateGroup(group)
                                        bot.sendMessage(to, "Berhasil membuka grup qr")
                            elif cmd == 'groupticket off':
                                if msg.toType == 2:
                                    group = bot.getGroup(to)
                                    if group.preventedJoinByTicket == True:
                                        bot.sendMessage(to, "Grup qr sudah tertutup")
                                    else:
                                        group.preventedJoinByTicket = True
                                        bot.updateGroup(group)
                                        bot.sendMessage(to, "Berhasil menutup grup qr")
                            elif cmd == 'groupinfo':
                                group = bot.getGroup(to)
                                try:
                                    gCreator = group.creator.displayName
                                except:
                                    gCreator = "Tidak ditemukan"
                                if group.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(group.invitee))
                                if group.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(bot.reissueGroupTicket(group.id)))
                                path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                                ret_ = "╔══[ Group Info ]"
                                ret_ += "\n╠ Nama Group : {}".format(str(group.name))
                                ret_ += "\n╠ ID Group : {}".format(group.id)
                                ret_ += "\n╠ Pembuat : {}".format(str(gCreator))
                                ret_ += "\n╠ Jumlah Member : {}".format(str(len(group.members)))
                                ret_ += "\n╠ Jumlah Pending : {}".format(gPending)
                                ret_ += "\n╠ Group Qr : {}".format(gQr)
                                ret_ += "\n╠ Group Ticket : {}".format(gTicket)
                                ret_ += "\n╚══[ Finish ]"
                                bot.sendMessage(to, str(ret_))
                                bot.sendImageWithURL(to, path)
                            elif cmd == 'kam':
                                group = bot.getGroup(to)
                                path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                                bot.sendImageWithURL(to, path)
                                bot.sendMessage(to, "welcome to {}".format(str(group.name)))
                            elif cmd == 'groupmemberlist':
                                if msg.toType == 2:
                                    group = bot.getGroup(to)
                                    ret_ = "╔══[ Member List ]"
                                    no = 0 + 1
                                    for mem in group.members:
                                        ret_ += "\n╠ {}. {}".format(str(no), str(mem.displayName))
                                        no += 1
                                    ret_ += "\n╚══[ Total {} ]".format(str(len(group.members)))
                                    bot.sendMessage(to, str(ret_))
                            elif cmd == 'grouplist':
                                    groups = bot.groups
                                    ret_ = "╔══[ Group List ]"
                                    no = 0 + 1
                                    for gid in groups:
                                        group = bot.getGroup(gid)
                                        ret_ += "\n╠ {}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                                        no += 1
                                    ret_ += "\n╚══[ Total {} Groups ]".format(str(len(groups)))
                                    bot.sendMessage(to, ret_)
                            elif cmd.startswith("changegroupname"):
                                if msg.toType == 2:
                                    X = bot.getGroup(to)
                                    sep = msg.text.split(" ")
                                    X.name = msg.text.replace(sep[0] + " ","")
                                    bot.updateGroup(X)
# Pembatas Script #
                            elif cmd.startswith("window: "):
                                sep = text.split(" ")
                                r = request.get("http://corrykalam.pw/api/fwindow.php?text=" + sep[1] + "&btype=" + sep[2])
                            elif cmd.startswith("spam"):
                                sep = text.split(" ")
                                for i in range(int(sep[1])):
                                  bot.sendMessage(to, str(text.replace(sep[0] + " " + sep[1] + " ", ""))) 
                            elif cmd == "changepicture":
                               settings["changePictureProfile"] = True
                               bot.sendMessage(to, "Insert The Picture")
                            elif cmd == "changegrouppicture":
                                if msg.toType == 2:
                                    if to not in settings["changeGroupPicture"]:
                                        settings["changeGroupPicture"].append(to)
                                    bot.sendMessage(to, "Insert The Picture")

                            elif cmd == 'mention':
                              group = bot.getGroup(msg.to)
                              nama = [contact.mid for contact in group.members]
                              k = len(nama)//20
                              for a in range(k+1):
                                txt = u''
                                s=0
                                b=[]
                                for i in group.members[a*20 : (a+1)*20]:
                                  b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                                  s += 7
                                  txt += u'@babio \n'
                                sendMention(to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
                                sendMention(to, "Total {} Mention".format(str(len(nama))))  
                            elif cmd == 'mentionall':
                                group = bot.getGroup(msg.to)
                                nama = [contact.mid for contact in group.members]
                                k = len(nama)//20
                                for a in range(k+1):
                                    txt = u''
                                    s=0
                                    b=[]
                                    for i in group.members[a*20 : (a+1)*20]:
                                        b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                                        s += 7
                                        txt += u'@Rian \n'
                                    bot.sendMessage(to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
                                    bot.sendMessage(to, "Total {} Mention".format(str(len(nama))))
                            elif cmd == "lurking on":
                                tz = pytz.timezone("Asia/Makassar")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                if receiver in read['readPoint']:
                                    try:
                                        del read['readPoint'][receiver]
                                        del read['readMember'][receiver]
                                        del read['readTime'][receiver]
                                    except:
                                        pass
                                    read['readPoint'][receiver] = msg_id
                                    read['readMember'][receiver] = ""
                                    read['readTime'][receiver] = readTime
                                    read['ROM'][receiver] = {}
                                    bot.sendMessage(receiver,"Lurking telah diaktifkan")
                                else:
                                    try:
                                        del read['readPoint'][receiver]
                                        del read['readMember'][receiver]
                                        del read['readTime'][receiver]
                                    except:
                                        pass
                                    read['readPoint'][receiver] = msg_id
                                    read['readMember'][receiver] = ""
                                    read['readTime'][receiver] = readTime
                                    read['ROM'][receiver] = {}
                                    bot.sendMessage(receiver,"Set reading point : \n" + readTime)
                            elif cmd == "lurking off":
                                tz = pytz.timezone("Asia/Makassar")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                if receiver not in read['readPoint']:
                                    bot.sendMessage(receiver,"Lurking telah dinonaktifkan")
                                else:
                                    try:
                                        del read['readPoint'][receiver]
                                        del read['readMember'][receiver]
                                        del read['readTime'][receiver]
                                    except:
                                        pass
                                    bot.sendMessage(receiver,"Delete reading point : \n" + readTime)

                            elif cmd == "lurking reset":
                                tz = pytz.timezone("Asia/Makassar")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                if msg.to in read["readPoint"]:
                                    try:
                                        del read["readPoint"][msg.to]
                                        del read["readMember"][msg.to]
                                        del read["readTime"][msg.to]
                                        del read["ROM"][msg.to]
                                    except:
                                        pass
                                    read['readPoint'][receiver] = msg_id
                                    read['readMember'][receiver] = ""
                                    read['readTime'][receiver] = readTime
                                    read['ROM'][receiver] = {}
                                    bot.sendMessage(msg.to, "Reset reading point : \n" + readTime)
                                else:
                                    bot.sendMessage(msg.to, "Lurking belum diaktifkan ngapain di reset?")

                            elif cmd == "lurking":
                                tz = pytz.timezone("Asia/Makassar")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                if receiver in read['readPoint']:
                                    if read["ROM"][receiver].items() == []:
                                        bot.sendMessage(receiver,"Tidak Ada Sider")
                                    else:
                                        chiya = []
                                        for rom in read["ROM"][receiver].items():
                                            chiya.append(rom[1])
                                        cmem = bot.getContacts(chiya)
                                        zx = ""
                                        zxc = ""
                                        zx2 = []
                                        xpesan = '[Lurkers]\n'
                                    for x in range(len(cmem)):
                                        xname = str(cmem[x].displayName)
                                        pesan = ''
                                        pesan2 = pesan+"@c\n"
                                        xlen = str(len(zxc)+len(xpesan))
                                        xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                        zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                                        zx2.append(zx)
                                        zxc += pesan2
                                    text = xpesan+ zxc + "\n" + readTime
                                    try:
                                        bot.sendMessage(receiver, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                    except Exception as error:
                                        print (error)
                                    pass
                                else:
                                    bot.sendMessage(receiver,"Lurking belum diaktifkan")
                            elif cmd.startswith("mimicadd"):
                                targets = []
                                key = eval(msg.contentMetadata["MENTION"])
                                key["MENTIONEES"][0]["M"]
                                for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                                for target in targets:
                                    try:
                                        settings["mimic"]["target"][target] = True
                                        bot.sendMessage(msg.to,"Target Added")
                                        break
                                    except:
                                        bot.sendMessage(msg.to,"Failed To Add Target")
                                        break
                            elif cmd.startswith("mimicdel"):
                                targets = []
                                key = eval(msg.contentMetadata["MENTION"])
                                key["MENTIONEES"][0]["M"]
                                for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                                for target in targets:
                                    try:
                                        del settings["mimic"]["target"][target]
                                        bot.sendMessage(msg.to,"Success Delete Target")
                                        break
                                    except:
                                        bot.sendMessage(msg.to,"Failed Delete Target")
                                        break

                            elif cmd == "mimiclist":
                                if settings["mimic"]["target"] == {}:
                                    bot.sendMessage(msg.to,"Nothing Target")
                                else:
                                    mc = "╔══[ Mimic List ]"
                                    for mi_d in settings["mimic"]["target"]:
                                        mc += "\n╠ "+bot.getContact(mi_d).displayName
                                    mc += "\n╚══[ Finish ]"
                                    bot.sendMessage(msg.to,mc)

                            elif cmd.startswith("mimic"):
                                sep = text.split(" ")
                                mic = text.replace(sep[0] + " ","")
                                if mic == "on":
                                    if settings["mimic"]["status"] == False:
                                        settings["mimic"]["status"] = True
                                        bot.sendMessage(msg.to,"Reply Message on")
                                elif mic == "off":
                                    if settings["mimic"]["status"] == True:
                                        settings["mimic"]["status"] = False
                                        bot.sendMessage(msg.to,"Reply Message off")
# Pembatas Script #
                            elif cmd.startswith("checkwebsite"):
                                try:
                                    sep = text.split(" ")
                                    query = text.replace(sep[0] + " ","")
                                    r = requests.get("http://rahandiapi.herokuapp.com/sswebAPI?key=betakey&link={}".format(urllib.parse.quote(query)))
                                    data = r.text
                                    data = json.loads(data)
                                    bot.sendImageWithURL(to, data["result"])
                                except Exception as error:
                                    logError(error)
                            elif cmd.startswith("checkdate"):
                                try:
                                    sep = msg.text.split(" ")
                                    tanggal = msg.text.replace(sep[0] + " ","")
                                    r = requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                                    data=r.text
                                    data=json.loads(data)
                                    ret_ = "[ D A T E ]"
                                    ret_ += "\nDate Of Birth : {}".format(str(data["data"]["lahir"]))
                                    ret_ += "\nAge : {}".format(str(data["data"]["usia"]))
                                    ret_ += "\nBirthday : {}".format(str(data["data"]["ultah"]))
                                    ret_ += "\nZodiak : {}".format(str(data["data"]["zodiak"]))
                                    bot.sendMessage(to, str(ret_))
                                except Exception as error:
                                    logError(error)
                            elif cmd.startswith("checkpraytime "):
                                separate = msg.text.split(" ")
                                location = msg.text.replace(separate[0] + " ","")
                                r = requests.get("http://api.corrykalam.net/apisholat.php?lokasi={}".format(location))
                                data = r.text
                                data = json.loads(data)
                                tz = pytz.timezone("Asia/Makassar")
                                timeNow = datetime.now(tz=tz)
                                if data[1] != "Subuh : " and data[2] != "Dzuhur : " and data[3] != "Ashar : " and data[4] != "Maghrib : " and data[5] != "Isya : ":
                                    ret_ = "╔══[ Jadwal Sholat Sekitar " + data[0] + " ]"
                                    ret_ += "\n╠ Tanggal : " + datetime.strftime(timeNow,'%Y-%m-%d')
                                    ret_ += "\n╠ Jam : " + datetime.strftime(timeNow,'%H:%M:%S')
                                    ret_ += "\n╠ " + data[1]
                                    ret_ += "\n╠ " + data[2]
                                    ret_ += "\n╠ " + data[3]
                                    ret_ += "\n╠ " + data[4]
                                    ret_ += "\n╠ " + data[5]
                                    ret_ += "\n╚══[ Success ]"
                                    bot.sendMessage(msg.to, str(ret_))
                            elif cmd.startswith("checkweather "):
                                try:
                                    sep = text.split(" ")
                                    location = text.replace(sep[0] + " ","")
                                    r = requests.get("http://api.corrykalam.net/apicuaca.php?kota={}".format(location))
                                    data = r.text
                                    data = json.loads(data)
                                    tz = pytz.timezone("Asia/Makassar")
                                    timeNow = datetime.now(tz=tz)
                                    if "result" not in data:
                                        ret_ = "╔══[ Weather Status ]"
                                        ret_ += "\n╠ Location : " + data[0].replace("Temperatur di kota ","")
                                        ret_ += "\n╠ Suhu : " + data[1].replace("Suhu : ","") + "°C"
                                        ret_ += "\n╠ Kelembaban : " + data[2].replace("Kelembaban : ","") + "%"
                                        ret_ += "\n╠ Tekanan udara : " + data[3].replace("Tekanan udara : ","") + "HPa"
                                        ret_ += "\n╠ Kecepatan angin : " + data[4].replace("Kecepatan angin : ","") + "m/s"
                                        ret_ += "\n╠══[ Time Status ]"
                                        ret_ += "\n╠ Tanggal : " + datetime.strftime(timeNow,'%Y-%m-%d')
                                        ret_ += "\n╠ Jam : " + datetime.strftime(timeNow,'%H:%M:%S') + " WIB"
                                        ret_ += "\n╚══[ Success ]"
                                        bot.sendMessage(to, str(ret_))
                                except Exception as error:
                                    logError(error)
                            elif cmd.startswith("checklocation "):
                                try:
                                    sep = text.split(" ")
                                    location = text.replace(sep[0] + " ","")
                                    r = requests.get("http://leert.corrykalam.gq/location.php?location=".format(location))
                                    data = r.text
                                    data = json.loads(data)
                                    if data[0] != "" and data[1] != "" and data[2] != "":
                                        try:
                                            bot.sendLocation(to, data[1], data[2], data[0], location)
                                        except Exception as error:
                                            bot.sendMessage(to, "error\n"+str(error))
                                        link = "https://www.google.co.id/maps/@{},{},15z".format(str(data[1]), str(data[2]))
                                        ret_ = "╔══[ Location Status ]"
                                        ret_ += "\n╠ Location : " + data[0]
                                        ret_ += "\n╠ Google Maps : " + link
                                        ret_ += "\n╚══[ Waiting For Satelite View ]"
                                        bot.sendMessage(to, str(ret_))
                                        try:
                                            image = "https://maps.googleapis.com/maps/api/staticmap?center={},{}&zoom=15&size=400x400&maptype=hybrid&key=AIzaSyDfW1ccqljxklR44fgcg8OqxPUKVxj4qUg".format(str(data[1]), str(data[2]))
                                            bot.sendImageWithURL(to, image)
                                        except Exception as error:
                                            bot.sendMessage(to, "error\n"+str(error))
                                except Exception as error:
                                    bot.sendMessage(to, "error\n"+str(error))
                                    logError(error)

                            elif cmd.startswith("instapost"):
                                try:
                                    sep = text.split(" ")
                                    text = text.replace(sep[0] + " ","")
                                    cond = text.split("|")
                                    username = cond[0]
                                    no = cond[1]
                                    r = requests.get("https://farzain.com/api/ig_post.php?id=https://www.instagram.com/p/BXIFPLwArJp/?_a=1&XLXqULlSisCJLtUgj4MCW1HkQ=beta".format(str(username), str(no)))
                                    data = r.text
                                    data = json.loads(data)
                                    if data["find"] == True:
                                        if data["media"]["mediatype"] == 1:
                                            bot.sendImageWithURL(msg.to, str(data["pict_url"]["1"]))
                                        if data["media"]["mediatype"] == 2:
                                            bot.sendVideoWithURL(msg.to, str(data["video_url"]["1"]))
                                        ret_ = "╔══[ Info Post ]"
                                        ret_ += "\n╠ Jumlah Like : {}".format(str(data["like"]))
                                        ret_ += "\n╠ Comment : {}".format(str(data["comment"]))
                                        ret_ += "\n╚══[ Caption ]\n{}".format(str(data["caption"]))
                                        bot.sendMessage(to, str(ret_))
                                except Exception as error:
                                    logError(error)
                            elif cmd.startswith("instastory"):
                                try:
                                    sep = text.split(" ")
                                    text = text.replace(sep[0] + " ","")
                                    cond = text.split("|")
                                    search = str(cond[0])
                                    if len(cond) == 2:
                                        r = requests.get("https://farzain.com/api/ig_story.php?id={}&apikey=XLXqULlSisCJLtUgj4MCW1HkQ".format(search))
                                        data = r.text
                                        data = json.loads(data)
                                        if data["url"] != []:
                                            num = int(cond[1])
                                            if num <= len(data["url"]):
                                                search = data["url"][num - 1]
                                                if search["tipe"] == 1:
                                                    bot.sendImageWithURL(to, str(search["link"]))
                                                if search["tipe"] == 2:
                                                    bot.sendVideoWithURL(to, str(search["link"]))
                                except Exception as error:
                                    logError(error)
                            elif cmd.startswith("image"):
                                try:
                                    separate = msg.text.split(" ")
                                    search = msg.text.replace(separate[0] + " ","")
                                    r = requests.get("http://rahandiapi.herokuapp.com/imageapi?key=betakey&q={}".format(search))
                                    data = r.text
                                    data = json.loads(data)
                                    if data["result"] != []:
                                        items = data["result"]
                                        path = random.choice(items)
                                        a = items.index(path)
                                        b = len(items)
                                        bot.sendImageWithURL(to, str(path))
                                except Exception as error:
                                    logError(error)
                            elif cmd.startswith("music "):
                                sep = msg.text.split(" ")
                                query = msg.text.replace(sep[0] + " ","")
                                cond = query.split("|")
                                search = str(cond[0])
                                result = requests.get("http://api.ntcorp.us/joox/search?q={}".format(str(search)))
                                data = result.text
                                data = json.loads(data)
                                if len(cond) == 1:
                                    num = 0
                                    ret_ = "╔══[ Result Music ]"
                                    for music in data["result"]:
                                        num += 1
                                        ret_ += "\n╠ {}. {}".format(str(num), str(music["single"]))
                                    ret_ += "\n╚══[ Total {} Music ]".format(str(len(data["result"])))
                                    ret_ += "\n\nUntuk Melihat Details Music, silahkan gunakan command {}SearchMusic {}|「number」".format(str(setKey), str(search))
                                    bot.sendMessage(to, str(ret_))
                                elif len(cond) == 2:
                                    num = int(cond[1])
                                    if num <= len(data["result"]):
                                        music = data["result"][num - 1]
                                        result = requests.get("http://api.ntcorp.us/joox/song_info?sid={}".format(str(music["sid"])))
                                        data = result.text
                                        data = json.loads(data)
                                        if data["result"] != []:
                                            ret_ = "╔══[ Music ]"
                                            ret_ += "\n╠ Title : {}".format(str(data["result"]["song"]))
                                            ret_ += "\n╠ Album : {}".format(str(data["result"]["album"]))
                                            ret_ += "\n╠ Size : {}".format(str(data["result"]["size"]))
                                            ret_ += "\n╠ Link : {}".format(str(data["result"]["mp3"][0]))
                                            ret_ += "\n╚══[ Finish ]"
                                            bot.sendImageWithURL(to, str(data["result"]["img"]))
                                            bot.sendMessage(to, str(ret_))
                                            bot.sendAudioWithURL(to, str(data["result"]["mp3"][0]))
                            elif cmd.startswith("lyric "):
                                sep = msg.text.split(" ")
                                query = msg.text.replace(sep[0] + " ","")
                                r = requests.get('http://leert.corrykalam.gq/joox.php?song='+query)
                                data = r.text
                                data=json.loads(data)
                                ret_ = "[ RESULT ]"
                                ret_ += "\nJudul : {}".format(str(data["title"]))
                                ret_ += "\nPenyanyi : {}".format(str(data["singer"]))
                                ret_ += "\nLyric : "
                                ret_ += "\n {}".format(str(data["lyric"]))
                                bot.sendMessage(to, str(ret_))
                            elif cmd.startswith("youtube: "):
                                sep = text.split(" ")
                                search = text.replace(sep[0] + " ","")
                                params = {"search_query": search}
                                r = requests.get("https://www.youtube.com/results", params = params)
                                soup = BeautifulSoup(r.content, "html5lib")
                                ret_ = "╔══[ Youtube Result ]"
                                datas = []
                                for data in soup.select(".yt-lockup-title > a[title]"):
                                    if "&lists" not in data["href"]:
                                        datas.append(data)
                                for data in datas:
                                    ret_ += "\n╠══[ {} ]".format(str(data["title"]))
                                    ret_ += "\n╠ https://www.youtube.com{}".format(str(data["href"]))
                                ret_ += "\n╚══[ Total {} ]".format(len(datas))
                                bot.sendMessage(to, str(ret_))
                            elif cmd.startswith("tr-"):
                                sep = text.split("-")
                                sep = sep[1].split(" ")
                                lang = sep[0]
                                say = text.replace("tr-" + lang + " ","")
                                if lang not in list_language["list_translate"]:
                                    return bot.sendMessage(to, "Language not found")
                                translator = Translator()
                                hasil = translator.translate(say, dest=lang)
                                A = hasil.text
                                bot.sendMessage(to, str(A))
# Pembatas Script #
# Pembatas Script #
                        if text.lower() == "mykey":
                            bot.sendMessage(to, "KeyCommand Saat ini adalah [ {} ]".format(str(settings["keyCommand"])))
                        elif text.lower() == "setkey on":
                            settings["setKey"] = True
                            bot.sendMessage(to, "Berhasil mengaktifkan setkey")
                        elif text.lower() == "setkey off":
                            settings["setKey"] = False
                            bot.sendMessage(to, "Berhasil menonaktifkan setkey")
# Pembatas Script #
                    elif msg.contentType == 1:
                        if settings["changePictureProfile"] == True:
                            path = bot.downloadObjectMsg(msg_id)
                            settings["changePictureProfile"] = False
                            bot.updateProfilePicture(path)
                            bot.sendMessage(to, "Success change pict profile")
                        if msg.toType == 2:
                            if to in settings["changeGroupPicture"]:
                                path = bot.downloadObjectMsg(msg_id)
                                settings["changeGroupPicture"].remove(to)
                                bot.updateGroupPicture(to, path)
                                bot.sendMessage(to, "Success change pict group :)")
                    elif msg.contentType == 7:
                        if settings["checkSticker"] == True:
                            stk_id = msg.contentMetadata['STKID']
                            stk_ver = msg.contentMetadata['STKVER']
                            pkg_id = msg.contentMetadata['STKPKGID']
                            ret_ = "╔══[ Sticker Info ]"
                            ret_ += "\n╠ STICKER ID : {}".format(stk_id)
                            ret_ += "\n╠ STICKER PACKAGES ID : {}".format(pkg_id)
                            ret_ += "\n╠ STICKER VERSION : {}".format(stk_ver)
                            ret_ += "\n╠ STICKER URL : line://shop/detail/{}".format(pkg_id)
                            ret_ += "\n╚══[ Finish ]"
                            bot.sendMessage(to, str(ret_))
                    elif msg.contentType == 13:
                        if settings["checkContact"] == True:
                            try:
                                contact = bot.getContact(msg.contentMetadata["mid"])
                                if bot != None:
                                    cover = bot.getProfileCoverURL(msg.contentMetadata["mid"])
                                else:
                                    cover = "Tidak dapat masuk di line channel"
                                path = "http://dl.profile.line-cdn.net/{}".format(str(contact.pictureStatus))
                                try:
                                    bot.sendImageWithURL(to, str(path))
                                except:
                                    pass
                                ret_ = "╔══[ Details Contact ]"
                                ret_ += "\n╠ Nama : {}".format(str(contact.displayName))
                                ret_ += "\n╠ MID : {}".format(str(msg.contentMetadata["mid"]))
                                ret_ += "\n╠ Bio : {}".format(str(contact.statusMessage))
                                ret_ += "\n╠ Gambar Profile : http://dl.profile.line-cdn.net/{}".format(str(contact.pictureStatus))
                                ret_ += "\n╠ Gambar Cover : {}".format(str(cover))
                                ret_ += "\n╚══[ Finish ]"
                                bot.sendMessage(to, str(ret_))
                            except:
                                bot.sendMessage(to, "Kontak tidak valid")
                    elif msg.contentType == 16:
                        if settings["checkPost"] == True:
                            try:
                                ret_ = "╔══[ Details Post ]"
                                if msg.contentMetadata["serviceType"] == "GB":
                                    contact = bot.getContact(sender)
                                    auth = "\n╠ Penulis : {}".format(str(contact.displayName))
                                else:
                                    auth = "\n╠ Penulis : {}".format(str(msg.contentMetadata["serviceName"]))
                                purl = "\n╠ URL : {}".format(str(msg.contentMetadata["postEndUrl"]).replace("line://","https://line.me/R/"))
                                ret_ += auth
                                ret_ += purl
                                if "mediaOid" in msg.contentMetadata:
                                    object_ = msg.contentMetadata["mediaOid"].replace("svc=myhome|sid=h|","")
                                    if msg.contentMetadata["mediaType"] == "V":
                                        if msg.contentMetadata["serviceType"] == "GB":
                                            ourl = "\n╠ Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                            murl = "\n╠ Media URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(msg.contentMetadata["mediaOid"]))
                                        else:
                                            ourl = "\n╠ Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                            murl = "\n╠ Media URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(object_))
                                        ret_ += murl
                                    else:
                                        if msg.contentMetadata["serviceType"] == "GB":
                                            ourl = "\n╠ Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                        else:
                                            ourl = "\n╠ Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                    ret_ += ourl
                                if "stickerId" in msg.contentMetadata:
                                    stck = "\n╠ Stiker : https://line.me/R/shop/detail/{}".format(str(msg.contentMetadata["packageId"]))
                                    ret_ += stck
                                if "text" in msg.contentMetadata:
                                    text = "\n╠ Tulisan : {}".format(str(msg.contentMetadata["text"]))
                                    ret_ += text
                                ret_ += "\n╚══[ Finish ]"
                                bot.sendMessage(to, str(ret_))
                            except:
                                bot.sendMessage(to, "Post tidak valid")
            except Exception as error:
                logError(error)
                traceback.print_tb(error.__traceback__)
#------------

#untuk ganti link

#-----------
        if op.type == 25:
            try:
                print ("[ 25 ] RECIEVE MESSAGE")
                msg = op.message
                text = msg.text
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                    if msg.toType == 0:
                        if sender != bot.profile.mid:
                            to = sender
                        else:
                            to = receiver
                    elif msg.toType == 1:
                        to = receiver
                    elif msg.toType == 2:
                        to = receiver
                    if settings["autoRead"] == True:
                        bot.sendChatChecked(to, msg_id)
                    if to in read["readPoint"]:
                        if sender not in read["ROM"][to]:
                            read["ROM"][to][sender] = True
                    if sender in settings["mimic"]["target"] and settings["mimic"]["status"] == True and settings["mimic"]["target"][sender] == True:
                        text = msg.text
                        if text is not None:
                            bot.sendMessage(msg.to,text)
                    if settings["unsendMessage"] == True:
                        try:
                            msg = op.message
                            if msg.toType == 0:
                                bot.log("[{} : {}]".format(str(msg._from), str(msg.text)))
                            else:
                                bot.log("[{} : {}]".format(str(msg.to), str(msg.text)))
                                msg_dict[msg.id] = {"text": msg.text, "from": msg._from, "createdTime": msg.createdTime, "contentType": msg.contentType, "contentMetadata": msg.contentMetadata}
                        except Exception as error:
                            logError(error)
                    if msg.contentType == 0:
                        if text is None:
                            return
                        if "/ti/g/" in msg.text.lower():
                            if settings["autoJoinTicket"] == True:
                                link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                                links = link_re.findall(text)
                                n_links = []
                                for l in links:
                                    if l not in n_links:
                                        n_links.append(l)
                                for ticket_id in n_links:
                                    group = bot.findGroupByTicket(ticket_id)
                                    bot.acceptGroupInvitationByTicket(group.id,ticket_id)
                                    bot.sendMessage(to, "Berhasil masuk ke group %s" % str(group.name))
                        if 'MENTION' in msg.contentMetadata.keys()!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if botMid in mention["M"]:
                                    if settings["autoRespon"] == True:
                                        sendMention(sender, " Saya hanyalah bot @!", [sender])
                                    break
            except Exception as error:
                logError(error)
                traceback.print_tb(error.__traceback__)
        if op.type == 65:
            print ("[ 65 ] NOTIFIED DESTROY MESSAGE")
            if settings["unsendMessage"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict:
                        if msg_dict[msg_id]["from"]:
                            contact = bot.getContact(msg_dict[msg_id]["from"])
                            if contact.displayNameOverridden != None:
                                name_ = contact.displayNameOverridden
                            else:
                                name_ = contact.displayName
                                ret_ = "Send Message cancelled."
                                ret_ += "\nSender : @!"
                                ret_ += "\nSend At : {}".format(str(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"]))))
                                ret_ += "\nType : {}".format(str(Type._VALUES_TO_NAMES[msg_dict[msg_id]["contentType"]]))
                                ret_ += "\nText : {}".format(str(msg_dict[msg_id]["text"]))
                                sendMention(at, str(ret_), [contact.mid])
                            del msg_dict[msg_id]
                        else:
                            bot.sendMessage(at,"SentMessage cancelled,But I didn't have log data.\nSorry > <")
                except Exception as error:
                    logError(error)
                    traceback.print_tb(error.__traceback__)

        if op.type == 55:
            print ("[ 55 ] NOTIFIED READ MESSAGE")
            try:
                if op.param1 in read['readPoint']:
                    if op.param2 in read['readMember'][op.param1]:
                        pass
                    else:
                        read['readMember'][op.param1] += op.param2
                    read['ROM'][op.param1][op.param2] = op.param2
                else:
                   pass
            except Exception as error:
                logError(error)
                traceback.print_tb(error.__traceback__)
    except Exception as error:
        logError(error)
        traceback.print_tb(error.__traceback__)

while True:
    try:
        delete_log()
        ops = botPoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                botBot(op)
                botPoll.setRevision(op.revision)
    except Exception as error:
        logError(error)

def atend():
    print("Saving")
    with open("Log_data.json","w",encoding='utf8') as f:
        json.dump(msg_dict, f, ensure_ascii=False, indent=4,separators=(',', ': '))
    print("BYE")
atexit.register(atend)