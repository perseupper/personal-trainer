# one file per user 
from enum import Enum
import datetime as dt
import json

timefmt = "%d/%m/%Y %H:%M:%S"

class MajorLevel(Enum):
	circuit = 1
	long_slow = 2
	interval = 3
	resistance = 4
	fartlek = 5

class Exercises(Enum):
	tricep_dips = 1
	tricep_extensions = 2
	tricep_pulldowns = 3
	shrugs = 4
	upright_rows = 5
	lateral_raises = 6
	pull_ups = 7
	reverse_curls = 8
	plank = 9
	# More exercises needed here

class BodyArea(Enum):
	upper = 1
	core = 2
	lower = 3

class MuscleGroup(Enum):
	lower_abs = 1
	upper_abs = 2
	deltoids = 3
	biceps = 4
	pectorals = 5
	obliques = 6
	abductors = 7
	quads = 8
	triceps = 9
	trapezius = 10
	forearms = 11
	gluteals = 12
	hamstrings = 13
	calves = 14
	latissimus_dorsi = 15

'''
body = {
	BodyArea.upper : [
		MuscleGroup.trapezius,
		MuscleGroup.triceps,
		MuscleGroup.forearms,
		MuscleGroup.deltoids,
		MuscleGroup.pectorals,
		MuscleGroup.biceps
	],
	BodyArea.core : [
		MuscleGroup.upper_abs,
		MuscleGroup.lower_abs,
		MuscleGroup.obliques,
		MuscleGroup.latissimus_dorsi
	],
	BodyArea.lower : [
		MuscleGroup.gluteals,
		MuscleGroup.hamstrings,
		MuscleGroup.calves,
		MuscleGroup.abductors,
		MuscleGroup.quads
	]
}
'''

exercises_to_muscles = {
	Exercises.tricep_dips : [
		MuscleGroup.triceps
	],
	Exercises.tricep_extensions : [
		MuscleGroup.triceps
	],
	Exercises.pull_ups : [
		MuscleGroup.biceps,
		MuscleGroup.latissimus_dorsi,
		MuscleGroup.forearms
	],
	# More exercises to add here
}

class Activity(Enum):
	work = 1
	rest = 2
	reps = 3
	kph  = 4
	slope = 5

class Time:
	def __init__(self,m,s):
		h = 0
		if s > 59:
			m += s // 60
			s %= 60
		if m > 59:
			h += m // 60
			m %= 60

		self.hr  = h
		self.min = m
		self.sec = s

	def str(self):
		result = []
		if self.hr > 0:
			result.append("{}h".format(self.hr))
		if self.min > 0:
			result.append("{}m".format(self.min))
		if self.sec > 0:
			result.append("{}s".format(self.sec))
		return " ".join(result)

levels = {
	MajorLevel.circuit : [
		{	# Level 0
			Activity.work : Time(0,45), 
			Activity.rest : Time(1,0),
			Activity.reps : 10
		},
		{	# Level 1
			Activity.work : Time(0,45), 
			Activity.rest : Time(0,30),
			Activity.reps : 10
		}
			# More levels needed for circuits 
	],
	MajorLevel.long_slow : [
		{	# Level 0
			Activity.work : Time(10,0), 
			Activity.kph : 10.0,
			Activity.slope : 3.0
		},
		{	# Level 1
			Activity.work : Time(13,0), 
			Activity.kph : 10.0,
			Activity.slope : 3.0
		},
		{	# Level 10
			Activity.work : Time(40,0), 
			Activity.kph : 10.0,
			Activity.slope : 3.0
		},
	],
	MajorLevel.interval : [
	]
}

class Workout:
	def __init__(self,jsontxt):
		if type(jsontxt) is str:
			try:
				data = json.loads(jsontxt)
			except:
				data = {}
		elif type(jsontxt) is dict:
			data = jsontxt
		else:
			data = {}

		if 'start' in data:
			self.start = dt.datetime.strptime(data['start'], timefmt)
		else:
			self.start = None

		if 'end' in data:
			self.end = dt.datetime.strptime(data['end'], timefmt)
		else:
			self.end = None

		if 'difficulty' in data:
			self.difficulty = data['difficulty']
		else:
			self.difficulty = None

		self.level = {
		'major':MajorLevel(data['majorlevel']),
		'minor':int(data['minorlevel'])
		}

	def set_start(self):
		self.start = dt.datetime.now()

	def set_end(self):
		self.end = dt.datetime.now()

	def set_difficulty(self,out_of_10):
		self.difficulty = out_of_10

	def dict(self):
		data = {}
		if self.start is not None:
			data['start'] = self.start.strftime(timefmt)
		if self.end is not None:
			data['end'] = self.end.strftime(timefmt)
		data['majorlevel'] = self.level['major'].value
		data['minorlevel'] = self.level['minor']
		if self.difficulty is not None:
			data['difficulty'] = self.difficulty
		return data

	def json(self):
		return json.dumps(self.dict(),indent=0)

	def str_major(self):
		return str(self.level['major']).replace('MajorLevel.','').replace('_',' ').title()

	def str_minor(self):
		return str(self.level['minor'])

	def str_description(self):
		data = levels[self.level['major']][self.level['minor']]
		work = data[Activity.work].str()
		kph = str(data[Activity.kph])
		slope = str(data[Activity.slope])
		description = "Running for {} at {}kph on a slope of {}".format(
			work,
			kph,
			slope)
		return description

class Circuit(Workout):
	def __init__(self,jsontxt):
		super().__init__(jsontxt)
		if type(jsontxt) is str:
			try:
				data = json.loads(jsontxt)
			except:
				data = {}
		elif type(jsontxt) is dict:
			data = jsontxt
		else:
			data = {}

		if 'exercise' in data:
			self.exercise = Exercises(data['exercise'])
		else:
			self.exercise = None

	def set_exercise(self,exercise):
		self.exercise = exercise

	def str_exercise(self):
		return str(self.exercise).replace("Exercises.","").replace("_"," ").title()

	def dict(self):
		try:
			data = super().dict()
		except:
			data = {}
		if self.exercise is not None:
			data['exercise'] = self.exercise.value
		return data

	def json(self):
		return json.dumps(self.dict(),indent=0)

	def str_description(self):
		data = levels[self.level['major']][self.level['minor']]
		work = data[Activity.work].str()
		rest = data[Activity.work].str()
		reps = str(data[Activity.reps])
		muscles = [str(m).replace("MuscleGroup.","").replace("_"," ").title() for m in exercises_to_muscles[self.exercise]]
		description = "{} reps of {} in {}, to target your {}.  Then rest for {}.".format(
			reps,
			self.str_exercise(),
			work,
			", ".join(muscles),
			rest)
		return description

completed = []
with open('program.json','r') as f:

	try:
		program = json.loads(f.read())
	except:
		program = []

	for to_do in program:
		if MajorLevel(to_do['majorlevel']) == MajorLevel.circuit:
			x = Circuit(to_do)
			print(x.str_description())
		elif MajorLevel(to_do['majorlevel']) == MajorLevel.long_slow:
			x = Workout(to_do)
			print(x.str_description())
		else:
			continue
		x.set_start()
		x.set_end()
		x.set_difficulty(4)
		completed.append(x.dict())

with open('completed.json', 'w') as f:
	f.write(json.dumps(completed,indent=0))
