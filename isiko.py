from datetime import date
import json

#Global variables
users = {}
events = {}
advertisements = {}



class User:
	username = ''
	email = ''
	password = ''
	age = 0

	def __init__(self, username = '', email = '', password = '', age = 0):
		if age < 18:
			return False

		self.username = username
		self.email = email
		self.password = password
		self.age = age


class Event:
	id = 0
	user = ''
	name = ''
	type = ''
	when = ''
	where = ''
	time = ''
	information = ''
	corona_restrictions = ''
	contact = ''

	def __init__(self, id = '', user = '', name = '', type = '', when = '', where = '', time = '', information = '', corona_restrictions = '', contact = ''):
		self.id = id
		self.user = user
		self.name = name
		self.type = type
		self.when = when
		self.where = where
		self.time = time
		self.information = information
		self.corona_restrictions = corona_restrictions
		self.contact = contact

	@staticmethod
	def find_all():
		return list(events.values())

	@staticmethod
	def search(text):
		results = []

		for event in events.values():
			if text.lower() in event.name.lower():
				results.append(event)

		return results

	def toJSON(self):
		return json.dumps(self, default=lambda o: o.__dict__,
			sort_keys=True, indent=4)


class Advertisement:
	id = 0
	user = ''
	type = ''
	name = ''
	information = ''
	contact = ''

	def toJSON(self):
		return json.dumps(self, default=lambda o: o.__dict__,
			sort_keys=True, indent=4)

class JobAdvertisement(Advertisement):
	when = ''
	where = ''

	def __init__ (self, id = 0, user = '', type = '', name = '', information = '', contact = '', when = '', where = ''):
		self.id = id
		self.user = user
		self.type = type
		self.name = name
		self.information = information
		self.contact = contact
		self.when = when
		self.where = where


	@staticmethod
	def find_all():
		results = []

		for ad in advertisements.values():
			if ad.type == 'job':
				results.append(ad)

		return results

	@staticmethod
	def search(text):
		results = []

		for ad in advertisements.values():
			if ad.type == 'job' and text.lower() in ad.name.lower():
				results.append(ad)

		return results

class SkillAdvertisement(Advertisement):

	def __init__ (self, id = 0, user = '', type = '', name = '', information = '', contact = ''):
		self.id = id
		self.user = user
		self.type = type
		self.name = name
		self.information = information
		self.contact = contact

	@staticmethod
	def find_all():
		results = []

		for ad in advertisements.values():
			if ad.type == 'skill':
				results.append(ad)

		return results

	@staticmethod
	def search(text):
		results = []

		for ad in advertisements.values():
			if ad.type == 'skill' and text.lower() in ad.name.lower():
				results.append(ad)

		return results



# Reading the database and print results - an example

#databse example:

users = {
	'test_organizer': User(username = 'test_organizer', email = 'organizer@example.com', password = '', age = 18),
	'test_artist': User(username = 'test_artist', email = 'artist@example.com', password = '', age = 18),
	'test_user': User(username = 'test_user', email = 'user@example.com', password = '', age = 18),
	'campus2parties': User(username = 'campus2parties', email = 'campusparties@gmail.com', password = '', age = 21),
	'santos_collective': User(username = 'santos_collective', email = 'santos.collective@icloud.com', password = '', age = 26),
	'brianna23': User(username = 'brianna23', email = 'brianna.fuller@gmail.com', password = '', age = 36),
	'haydnart': User(username = 'haydnart', email = 'artbyhaydn@gmail.com', password = '', age = 42),
	'richiie32': User(username = 'richiie32', email = 'richardgh32@gmail.com', password = '', age = 19),
	'serbansand': User(username = 'serbansand', email = 'sand.soundengineer@gmail.com', password = '', age = 48),
}

events = {
	0: Event(id = 0, user = 'test_organizer', name = 'Test Event', type = 'concert', when = date.today().isoformat(), where = 'concert hall', time = 'inlet: 6pm, start: 7pm, duration:2h 40min', information = 'More information on my website http://...', corona_restrictions = '2G', contact = 'https://konzerthalle.de'),
	1: Event(id = 1, user = 'campus2parties', name = 'Party in C2', type = 'private party', when = date(year=2021, month=10, day=23).isoformat(), where = 'Campus 2', time = 'starting at 20pm, open end', information = '', corona_restrictions = '2G+', contact = 'Contact us on instgram if you have any questions! @campus2partys'),
	2: Event(id = 2, user = 'kulturhausRS', name = 'Reading Brave New World', type = 'reading', when = date(year=2021, month=12, day=10).isoformat(), where = 'Kulturhaus Rote Strasse', time = 'inlet: 5pm, start: 5:30pm', information = 'More information at http://...', corona_restrictions = '3G and distancing rules', contact = 'https://KulturhausRS.de'),
	3: Event(id = 3, user = 'karina123', name = 'Summer exhibition by Karina K', type = 'art', when = date(year=2022, month=3, day=2).isoformat(), where = 'Exhibition Halls Hamburg', time = 'open from 01pm to 10pm', information = 'More info at http://...', corona_restrictions = '2G+', contact = 'https://karinak.de'),
	4: Event(id = 4, user = 'richiie32', name = 'New Years Eve Party at my garage', type = 'private party', when = date(year=2021, month=12, day=31).isoformat(), where = 'main street 23', time = 'starting at 10pm, open end', information = 'I have 100 extra invitations for my huge NYE party... ', corona_restrictions = '2G+, will be tested', contact = 'Write me an email: ...'),
	5: Event(id = 5, user = 'kulturhausRS', name = 'Classical christmas', type = 'concert', when = date(year=2021, month=12, day=20).isoformat(), where = 'Kulturhaus Rote Strasse', time = '7pm, duration: 2h', information = 'More information at http://...', corona_restrictions = '3G and distancing rules', contact = 'https://KulturhausRS.de'),
	6: Event(id = 6, user = 'brianna23', name = 'Poetry Slam competition 21', type = 'poetry', when = date(year=2022, month=1, day=4).isoformat(), where = 'Café Paulina, main street 2', time = 'starting at 4pm, until 8pm', information = 'More information at http://...', corona_restrictions = '2G', contact = 'https://poetryslamleuphana.de'),
}

advertisements = {
	0: JobAdvertisement(id = 0, type = 'job', user = 'test_organizer', name = 'Looking for an Audio Engineer', when = date.today().isoformat(), where = 'concert hall', information = 'We are looking for an Audio Engineer...', contact = 'https://konzerthalle.de'),
	1: JobAdvertisement(id = 1, type = 'job', user = 'brianna23', name = 'Looking for a presenter', when = date.today().isoformat(), where = 'Café Paulina, main street 2', information = 'We are hosting a Poetry Slam competition and are looking for a presenter / moderator...', contact = 'https://poetryslamleuphana.de'),
	2: JobAdvertisement(id = 2, type = 'job', user = 'kulturhausRS', name = 'Host your new exhibition at our place!', when = date(year=2022, month=1, day=1).isoformat(), where = 'Kulturhaus Rote Straße', information = 'From January first 2022, we are offering rooms...', contact = 'https://kukturhausRS.de'),
	3: SkillAdvertisement(id = 3, type = 'skill', user = 'test_artist', name = 'Audio Engineer', information = 'I have been an Audio Engineer since 2012...', contact = 'artist@example.com'),
	4: SkillAdvertisement(id = 4, type = 'skill', user = 'davidbarker', name = 'Drummer', information = 'As an experienced drummer I can...', contact = 'https://davidonthedrums.com'),
	5: SkillAdvertisement(id = 5, type = 'skill', user = 'nocevents', name = 'We organize your party!', information = 'We have been organizing parties since 2010 and now...', contact = 'nocevents@mail.com'),
	6: SkillAdvertisement(id = 6, type = 'skill', user = 'santos_collective', name = 'DJ Collective', information = 'We are a group of techno DJs...', contact = 'santos_collective@gmail.com')
}


# Reading and browsing the database

def pretty_print(x):
	print(json.dumps(list(map(lambda a: a.__dict__, x)), indent=2))


#output of all users
print('All Users')
pretty_print(users.values())


#output of events
print('\n\n\n\n\n\nEvents:\n===\n')
print('All events:')
pretty_print(Event.find_all())
#searching through database
print('\n\nSearch Events for "concert":')
pretty_print(Event.search('concert'))

print('\n\nSearch Events for "party":')
pretty_print(Event.search('party'))


#output of skill advertisements
print('\n\n\n\n\n\nJob Advertisements:\n===\n')
print('All jobs:')
pretty_print(JobAdvertisement.find_all())
#searching through database
print('\n\nSearch jobs for "guitarist":')
pretty_print(JobAdvertisement.search('guitarist'))

print('\n\nSearch jobs for "engineer":')
pretty_print(JobAdvertisement.search('engineer'))


#output of job advertisements
print('\n\n\n\n\n\nSkill Advertisements:\n===\n')
print('All skills:')
pretty_print(SkillAdvertisement.find_all())
#searching through database
print('\n\nSearch skills for "guitarist":')
pretty_print(SkillAdvertisement.search('guitarist'))

print('\n\nSearch skills for "engineer":')
pretty_print(SkillAdvertisement.search('engineer'))
