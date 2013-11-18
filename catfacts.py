from flask import Flask, request, redirect, url_for, render_template
from twilio.rest import TwilioRestClient
import sqlite3
import os
import random

app = Flask(__name__)

twilio_sid = 'AC7a648d772558bc3a02206c2a4b840ad8'
twilio_tok = '10e0cad3d72db9da836bddcc501b4587'
twilio_num = '+18324635638'

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/invalid/')
def invalid():
	return render_template('index_invalid.html')

@app.route('/success/')
def success():
	return render_template('success.html')

@app.errorhandler(404)
def whoops(error):
	return render_template('error.html')


@app.route('/submit/')
def submit():
	param = request.args.get('number')
	num = ''

	if '*.*sosa' in param:
		return redirect('http://youtu.be/94rvfF_Btzk')

	for char in param:
		if char.isdigit():
			num += char

	if (len(num) == 11) and (num[0] == '1'):
		num = '+' + num
	elif (len(num) == 10) and (num[0] != '1'):
		num = '+1' + num
	else:
		return redirect(url_for('invalid'))

	if send_text(num):
		return redirect(url_for('success'))
	else:
		return redirect(url_for('invalid'))


def add_db(num):
	if (num == '+17135059472') or (num == '+12818419207') or (num == '+18327909328') or (num == '+17137247774'):
		return False

	print 'adding number (%s) to database' % num

	client = TwilioRestClient(twilio_sid, twilio_tok) 
	message = client.messages.create(to=num, from_=twilio_num, body="#CATFACTS: \nCongratulations, you've been signed up for Catfacts.\nDid you know that there's more than one way to skin a cat.")

	con = sqlite3.connect('numbers.db')

	with con:
		cur = con.cursor()
		cur.execute("CREATE TABLE IF NOT EXISTS numbers(number TEXT);")
		str_y = "SELECT * FROM numbers WHERE number = %s" % num
		cur.execute(str_y)
		check = cur.fetchone()
		if not check:
			str_x = "INSERT INTO numbers(number) VALUES (%s)" % num
			cur.execute(str_x)

	str_ret = ''
	cur.execute("SELECT * FROM numbers")
	for row in cur.fetchall():
		str_ret + '\n' + row[0]

	return True


def send_text(num):
	if (num == '+17135059472') or (num == '+12818419207') or (num == '+18327909328') or (num == '+17137247774'):
		return False

	with open('string1.txt') as f:
		intros = f.readlines()
	with open('string2.txt') as b:
		body = b.readlines()
	with open('string3.txt') as t:
		thing = t.readlines()

	string = "#CATFACTS: " + random.choice(intros) + random.choice(body) + random.choice(thing)
	string.replace('\n', ' ')
	string.replace('\t', ' ')
	print string

	client = TwilioRestClient(twilio_sid, twilio_tok)
	message = client.messages.create(to=num, from_=twilio_num, body=string)

	return True


if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5000))

	if port == 5000:
		app.debug = True

	app.run(host='0.0.0.0', port=port)





