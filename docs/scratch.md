# Scratch Notes and Log

## Saturday, April 21, 2018 10:14 AM

High level

* read data from Excel sheet

* find all members who've not paid dues for last month

* find email addresses and send them personalized reminders

Code level

* open and read cells of Excel sheet with `openpyxl`

* create a dict of members who are behind

* log into SMTP with `smtplib.SMTP()`, `ehlo()`, `starttls()`, `login()`

* for those behind on dues send personalized email using `sendmail()`

## Saturday, April 21, 2018 10:42 AM

	smtpObj.login( 'my_email', sys.argv[1] )

pass your email address and `sys.argv[1]`, which will store your password string. 

You’ll enter the password as a command line argument each time you run the program, to avoid saving your password in your source code.

## Saturday, April 21, 2018 10:58 AM

	MacBook-Air:send_dues sunnyair$ python3 send_dues_reminder_042118_1.py PWDHIDDEN
	>
	>
	>

every time I try to log in with the password I only get a prompt

if I remove the pwd it works however that's it

hit pwd statement

	Traceback (most recent call last):
	  File "send_dues_reminder_042118_1.py", line 63, in <module>
	    raise e
	  File "send_dues_reminder_042118_1.py", line 58, in <module>
	    logging.debug( 'pwd was:  %s' % str(sys.argv[1]) )

only works when hard coded

I realized the issue was that I forgot to pass `sys.argv[1]` through `str()` method to convert to string

Still won't work:

	smtpObj.login( 'avatar.sage7@gmail.com', str(sys.argv[1]) )

result

	MacBook-Air:send_dues sunnyair$ python3 send_dues_reminder_042118_1.py 'm$[QhWNB(d7~S28Y49q
	>
	>
	>

maybe try `optparse` to avoid this error where it can't read the password due to the single quote or other special characters

## Monday, April 23, 2018 11:10 AM

tried `optparse` and it still results in the same problem...

[Python argparse argument with quotes](https://stackoverflow.com/questions/13168666/python-argparse-argument-with-quotes)

even escape back slashes don't work in the shell - the error occurs in the shell when running the command line

this means that no password with quotes can be used

[How to escape single quotes within single quoted strings?](https://stackoverflow.com/questions/1250079/how-to-escape-single-quotes-within-single-quoted-strings)

