# -*- coding: utf-8 -*-

#! python3

# USAGE
# python3 send_dues_reminder_042118_1.py "PASSWORD"

import logging
logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")
# logging.disable(logging.CRITICAL)

import openpyxl,smtplib
import optparse
import pprint

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

try:
	# smtpObj = smtplib.SMTP('smtp.gmail.com',587)
	smtpObj = smtplib.SMTP_SSL('smtp.gmail.com',465)
	smtpObj.ehlo()
	logging.debug( 'ehlo() worked.' )
	# smtpObj.starttls() # disable if using SMTP_SSL()
	# logging.debug( 'starttls() worked.' )

	# logging.debug( 'pwd was:  %s' % str(sys.argv[1]) )
	smtpObj.login( 'avatar.sage7@gmail.com', str(sys.argv[1]) )
	logging.debug( 'Email provider login successful.' )
except Exception as e:
	logging.debug( "There was an exception:  %s" % str(e) )
	raise e

# optional test
# logging.debug( "Listing folders:  " )
# logging.debug( pprint.pprint(smtpObj.list_folders()) )

# send out reminder emails

