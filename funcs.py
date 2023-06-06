# -*- coding: utf-8 -*-
"""
华为SDK接口"""
from huaweicloud_sis.client.asr_client import AsrCustomizationClient
from huaweicloud_sis.bean.asr_request import AsrCustomShortRequest
from huaweicloud_sis.bean.asr_request import AsrCustomLongRequest
from huaweicloud_sis.exception.exceptions import ClientException
from huaweicloud_sis.exception.exceptions import ServerException
from huaweicloud_sis.utils import io_utils
from huaweicloud_sis.bean.sis_config import SisConfig
"""
其他库"""
import webbrowser
import time
import subprocess
import wolframalpha
import json
import random
import operator
import datetime
import wikipedia
import json
import winshell
import pyjokes
import feedparser
import smtplib
import ctypes
import time
import requests
import shutil
import os
import sys
import tkinter
import tempfile
import pyttsx3
from twilio.rest import Client
from bs4 import BeautifulSoup
import win32com.client as wincl
import sounddevice as sd 
import speech_recognition as sr
import matplotlib.pyplot as plt
from scipy.io.wavfile import write
from urllib.request import urlopen
#from client.textui import progress
#from ecapture import ecapture as ec

# MacOS
#chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
# Windows
chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
# Linux
# chrome_path = '/usr/bin/google-chrome %s'

# 录音参数
freq = 44100  # 指定采样频率
duration = 5  # 指定持续时间

# 华为api参数
ak = 'xxx'
sk = 'xxx'
project_id = "xxx" 
region = "cn-north-4" 

# 识别参数
path = 'data/toSearch.wav'
#path_listen = 'data/toListen.wav'
path_audio_format = 'wav' # 音频格式，详见 api 文档
path_property = 'chinese_8k_common' # language_sampleRate_domain, 如 chinese_8k_common，详见 api 文档

#语音参数
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id) #男声
assname =("Jarvis")

def sayHello():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        speak("Good Morning !")
  
    elif hour>= 12 and hour<18:
        speak("Good Afternoon !")  
  
    else:
        speak("Good Evening !") 
    speak("I am your Assistant")
    speak(assname)
    speak("你好")


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def voiceWrite():
    #录制指定时长的音频，存为numpy array
    recording = sd.rec(int(duration * freq), samplerate=freq, channels=2)
    sd.wait()
    #把array存为wav文件“toSearch.wav”
    write("data/toSearch.wav", freq, recording)

def voiceRecog():
    config = SisConfig()
    config.set_connect_timeout(5) # 设置连接超时
    config.set_read_timeout(10) # 设置读取超时
    asr_client = AsrCustomizationClient(ak, sk, region, project_id, sis_config=config) # 初始化客户端
    data = io_utils.encode_file(path) #读入音频
    asr_request = AsrCustomShortRequest(path_audio_format, path_property, data) # 所有参数均可不设置，使用默认值
    asr_request.set_add_punc('yes')# 设置是否添加标点，yes or no，默认 no
    result = asr_client.get_short_response(asr_request)   #发送请求，打印、返回json结果
    recogResult = json.dumps(result, indent=2, ensure_ascii=False) #把json返回
    recogResultDict = json.loads(recogResult)
    keyword = recogResultDict['result']['text']
    #print(recogResult)
    return keyword

def txtSearch():
    #读取识别结果，访问搜索引擎并返回结果
    print("正在搜索:")
    print(voiceRecog())
    url = 'https://www.baidu.com/s?wd=' + voiceRecog()
    webbrowser.get(chrome_path).open(url)
    
def txtTranslate():
    print("查询中")
    print(voiceRecog())
    url = 'https://dict.youdao.com/search?q=' + voiceRecog()
    webbrowser.get(chrome_path).open(url)

def detectCommand():
    #简单检测口令，只支持英文
    r = sr.Recognizer()
    with sr.Microphone() as source:   
        print("语音助手正在运行")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        query = r.recognize_sphinx(audio, language ='en-us')
        query.lower()
        matches = ["hello","hi","there","good","jarvis"]
        # if any(x in query for x in matches):
        if True:
            print("我在！")
            speak("Heard That!")
            if 'wikipedia' in query:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences = 3)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            # elif "name" in query or "What is your name" in query:
            elif True:
                speak("My friends call me")
                print("我是：", assname)
                speak(assname)
            elif "translate" in query:
                print("请提供原句")
                speak("What do you wish to translate?")
                voiceWrite()
                speak("translating")
                txtTranslate()
            elif 'google' in query:
                speak("OK，opening google")
                print("正在打开谷歌搜索")
                url = 'google.com'
                webbrowser.get(chrome_path).open(url)
            elif "search" in query:
                speak("What is your keyword?")
                print("搜点什么呢？")
                voiceWrite()
                speak("Searching")
                txtSearch()
        else: 
            print("请详述您的指令")
    except Exception as e:
        print(e)
     
def detectLoop():
    while True:
        detectCommand()