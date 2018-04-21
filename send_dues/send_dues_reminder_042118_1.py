# -*- coding: utf-8 -*-

#! python3

# USAGE
# python3 send_dues_reminder_042118_1.py "PASSWORD"

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

unpaidMembers = {}

for r in range( 2,sheet.max_row + 1 ):
	payment = sheet.cell( row=r, column=lastCol ).value
	logging.debug( 'payment status is:  %s' % str(payment) )

	if payment != 'paid':
		name = sheet.cell(row=r,column=1).value
		logging.debug( 'name is:  %s' % str(name) )
		email = sheet.cell(row=r,column=2).value
		logging.debug( 'email is:  %s' % str(email) )
		unpaidMembers[name] = email
		logging.debug( 'email pushed into unpaidMembers dict' )

logging.debug( 'unpaidMembers dict is:  ' )
logging.debug( unpaidMembers )

# log into email account

smtpObj = smtplib.SMTP('smtp.gmail.com',587)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login( 'avatar.sage7@gmail.com', sys.argv[1] )

# send out reminder emails

