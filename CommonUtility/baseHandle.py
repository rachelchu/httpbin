# -*- coding: utf-8 -*-
# baseHandle.py
#
# Version 1.0 by rachel 2014/12/01

'''
#how to use:

import baseHandle

#Screenshot
baseScreenshot.screen_shot(driver,'name')

#Open result html to write.
filename = r"pfizer-register-result"
fp = baseHandle.openfile(filename)
'''
import os,sys
import time, os, logging, chardet

from . import baseConfig

_targetDir = baseConfig.getResult_Dir()

logger = logging.getLogger()

def openfile(name):
    filename = "%s\%s" % (_targetDir,time.strftime('%Y%m%d_%H%M%S',time.localtime(time.time())))
    fp = open(filename + "_"+ str(name) + ".html",'w')
    print ('[ HTML_RESULT: ]', filename + "_"+ str(name) + ".html")
    logging.info('[ HTML_RESULT: ]'+ filename + "_"+ str(name) + ".html")
    return fp

'''
Form normal operation
'''
### Start:Form normal operation
#check all checkbox in page
def check_checkbox(driver,csspath):
    checkBtns = driver.find_elements_by_css_selector(csspath)
    for checkBtn in checkBtns:
        selectBtn.click()

#fill all selector        
def check_selectlist(driver,csspath):
    pass
    
### End: Form normal operation

'''
switch window
'''
def switch_window(self):
    driver = self.driver
    nowhandle = self.driver.current_window_handle
    allhandles=driver.window_handles
    for handle in allhandles:
        if handle!=nowhandle:                
            driver.switch_to_window(handle)
'''
End:switch window
'''


'''
Chinese Coding
'''
def changeToChinese(message):
    if isinstance(message, unicode): 
        #message=u"中文"
        return message.encode('gb2312') 
    else: 
        #message="中文"
        return message.decode('utf-8').encode('gb2312')
'''
End:Chinese Coding
''' 

'''
Chinese Coding
'''
def GetCoding(message):
    return chardet.detect(message).get("encoding")
'''
End:Chinese Coding
'''         


'''
Time
'''
# format: "%Y/%m/%d" , "%Y-%m-%d"
def is_valid_date(str,format):
    try:
        _time = time.strptime(str, format)
        return _time
    except:
        return False
'''
End Time
'''

'''
Current path of script
'''
#获取脚本文件的当前路径
def cur_file_dir():
     #获取脚本路径
     path = sys.path[0]
     #判断为脚本文件还是py2exe编译后的文件，如果是脚本文件，则返回的是脚本的目录，如果是py2exe编译后的文件，则返回的是编译后的文件路径
     if os.path.isdir(path):
         return path
     elif os.path.isfile(path):
         return os.path.dirname(path)
         
#以下方法比较好
#os.path.split(os.path.realpath(__file__))[0]

#1） 获得脚本文件目录绝对路径
#os.path.abspath(os.path.dirname(__file__))

#2）获得上级目录
#os.path.dirname(fileOrDir)

#3）获得脚本文件名
#os.path.basename(__file__)

#4）获得当前工作目录
#os.getcwd()

#5) 目录连接
#os.path.join(dir1, file1)       
'''
End Current path of script
'''         
