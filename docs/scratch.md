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

