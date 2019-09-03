#! /opt/conda/bin/python 
# -*- coding: utf-8 -*- 
import requests
import common.readConfig as readConfig
import os
from xlrd import open_workbook
from xml.etree import ElementTree as ElementTree
from common.Log import MyLog as Log
import json

localReadConfig = readConfig.ReadConfig()
proDir = readConfig.proDir
log = Log.get_log()
logger = log.get_logger()

caseNo = 0

def get_xls(xls_name, sheet_name):
    """
    get interface data from xls file
    :return:
    """
    cls = []
    # get xls file's path
    xlsPath = os.path.join(proDir, "../testFile", 'xlsx', xls_name)
    # open xls file
    file = open_workbook(xlsPath)
    # get sheet by name
    sheet = file.sheet_by_name(sheet_name)
    # get one sheet's rows
    nrows = sheet.nrows
   
    for i in range(nrows):
        if sheet.row_values(i)[0] != u'case_name':
            cls.append(sheet.row_values(i))
    return cls
