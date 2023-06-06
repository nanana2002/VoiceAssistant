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
import pyttsx3
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
from twilio.rest import Client
from bs4 import BeautifulSoup
import win32com.client as wincl
import sounddevice as sd 
import speech_recognition as sr
import matplotlib.pyplot as plt
from scipy.io.wavfile import write
from urllib.request import urlopen
from funcs import *
import threading
#from client.textui import progress
#from ecapture import ecapture as ec


class detectStdout(): # 重定向类
    def __init__(self):
        self.stdoutbak = sys.stdout
        self.stderrbak = sys.stderr
        sys.stdout = self
        sys.stderr = self

    def write(self, info):
        t.insert('end', info) 
        t.update() 
        t.see(tkinter.END) 

    def restoreStd(self):
        sys.stdout = self.stdoutbak
        sys.stderr = self.stderrbak
        

def btn_func():
    threading.Thread(target=detectLoop).start()
    threading.Thread(target=sayHello).start()



mystd = detectStdout() 
window = tkinter.Tk() 
t = tkinter.Text(window) 
t.pack()
b = tkinter.Button(window, text='start', command=btn_func) 
b.pack()
window.mainloop() 
mystd.restoreStd()

