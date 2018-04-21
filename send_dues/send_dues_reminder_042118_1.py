# -*- coding: utf-8 -*-

#! python3

# USAGE
# python3 send_dues_reminder_042118_1.py

import logging
logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")
# logging.disable(logging.CRITICAL)

import openpyxl,smtplib,sys

# open the sheet and get latest due status

wb = openpyxl.load_workbook('duesRecords.xlsx')
logging.debug( 'Workbook opened' )

sheet = wb['Sheet1']
logging.debug( 'Sheet title is:  %s' % str(sheet.title) )

lastCol = sheet.max_column
logging.debug( 'Last column is:  %s' % str(lastCol) )

latestMonth = sheet.cell(row=1,column=lastCol).value
logging.debug( 'Latest month is:  %s' % str(latestMonth) )

# check each member's payment status



# log into email account

# send out reminder emails

