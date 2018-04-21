try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': "A program that uses a spreadsheet of people who've paid/not paid their member dues and email a reminder to those who haven't...",
	'author': 'Sunny Lam',
	'url': 'https://github.com/sunnylam13/send_dues_reminder_042118_1',
	'download_url': 'https://github.com/sunnylam13/send_dues_reminder_042118_1',
	'author_email': 'sunny.lam@gmail.com',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['NAME'],
	'scripts': [],
	'name': 'Sending Member Dues Reminder Emails'
}

setup(**config)