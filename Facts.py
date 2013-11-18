import random
import time
import twilio
import sqlite3
from twilio.rest import TwilioRestClient

twilio_sid = 'AC7a648d772558bc3a02206c2a4b840ad8'
twilio_tok = '10e0cad3d72db9da836bddcc501b4587'
twilio_num = '+18324635638'

def main():
	con = sqlite3.connect('numbers.db')
	cur = con.cursor()
	cur.execute("CREATE TABLE IF NOT EXISTS numbers(number TEXT);")

	while 1 == 1:
		with open('string1.txt') as f:
			Intros = f.readlines()
		f.close()
		with open('string2.txt') as b:
			Body = b.readlines()
		f.close()
		with open('string3.txt') as t:
			Thing = t.readlines()
		f.close()
		#with open('Fact.txt') as fa:
		#	Facts = fa.readlines()

		s1 = random.choice(Intros)
		s2 = random.choice(Body)
		s3 = random.choice(Thing)
		#s4 = random.choice(Facts)

		sfinal = "#CATFACTS: " + s1 + s2 + s3 #+ s4
		sfinal = sfinal.replace("\n", " ")
		print sfinal

		time.sleep(5)
		with con:
			cur = con.cursor()
			cur.execute("SELECT * FROM numbers")

			rows = cur.fetchall()

		for row in rows:
			try:
				client = TwilioRestClient(account_sid, auth_token) 
				message = client.messages.create(to= ('+'+row[0]), from_= myNum, body= sfinal)
			except twilio.TwilioRestException as e:
				print e
				fileout = open('output.txt', 'w')
				fileout.write(i)
				fileout.close()

if __name__ == '__main__':
	main()
