# -*- coding: utf-8 -*-
import configparser, os, sys

cur_dir = os.path.split(os.path.realpath(__file__))[0]
conf_file_dir = os.path.join(cur_dir, 'conf.ini')

parent_dir = os.path.dirname(cur_dir)

cf = configparser.ConfigParser()
cf.read(conf_file_dir)


def getIEPath():
    return cf.get('Brower','IEPath')   
def getChromePath():
    return cf.get('Brower','ChromePath')
def getCur_Browser():
    return cf.get('Brower','Cur_Browser')    
def getWinSecurity_Name():
    return cf.get('Brower','WinSecurity_Name')  
    
def getSite_url():
    return cf.get('Site','Site_url')  
def getHttps_user():
    return cf.get('Site','Https_user') 
def getHttps_psd():
    return cf.get('Site','Https_psd') 
    
def getData_targetDir():
    #return cf.get('Data','Data_targetDir')
    return os.path.join(parent_dir, 'data')
       

def getResult_Dir():
    return cf.get('Result','Result_Dir')
def getLog_file():
    return cf.get('Result','Log_file')

def get_APIGetdata():
    return os.path.join(cf.get('Data','Data_targetDir'), cf.get('Data','Get_data'))

'''
if __name__ == "__main__":
   print (getResult_Dir())
'''
