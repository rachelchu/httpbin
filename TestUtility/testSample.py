# -*- coding: utf-8 -*-
import unittest, time, re
import os
import logging
import csv,chardet
import sys
import requests,json,glob

par_dir = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)),os.path.pardir))
#par_dir = os.path.dirname(os.getcwd())
sys.path.append(par_dir)
from CommonUtility import baseConfig
from CommonUtility import baseTestRunnerWithHTML
from CommonUtility import baseHandle


class APIGet(unittest.TestCase):

    def getAPI(self,arg):
        endpoint = "get"
        host = baseConfig.getSite_url()
        endpoint = arg.get("sub_url")
        url = ''.join([host,endpoint])
        headers = {"User-Agent":"test request headers"}
        params = {"show_env":"1"}
        r = requests.get(url=url,headers=headers,params=params)
        

    @staticmethod
    def getTestFunc(arg):
        def func_get(self):
            self.getAPI(arg)
        return func_get
    
def __generateTestCases():
    with open(baseConfig.get_APIGetdata(), newline='') as csvfile:
        arglists = csv.DictReader(csvfile)
        for arg in arglists:
            case='test_get_%s_%s'%(arg["result"],arg["method"])		
            setattr(APIGet,case,APIGet.getTestFunc(arg))

if __name__ == "__main__":
    #unittest.main()
    
    __generateTestCases()
    filename = r"API_Get_result"
    fp = baseHandle.openfile(filename)
    htmlrunner = baseTestRunnerWithHTML.TestRunner(stream=fp,title=u"API_Get_result",description=u"test for Get API")
    unittest.main(testRunner = htmlrunner)
    unittest.main()