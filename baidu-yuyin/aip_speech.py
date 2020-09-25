# coding=utf-8
from aip import AipSpeech


APP_ID = '22699268'
API_KEY = 'hQfPIHnylYzAMV6a5ywunl0O'
SECRET_KEY = 'WFkE6D1bK7Rx2GmipGpsw34MsDrTk7Nt'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
res = client.synthesis("hello")

with open("audio.mp3", "wb") as f:
	f.write(res)
