# one file per user 
from enum import Enum
import datetime as dt
import json
from time import sleep
from os.path import isfile
from os import remove
#import urllib2
import netifaces

'''
def internet_on():
    try:
        response = urllib2.urlopen('http://74.125.228.100',timeout=1)
        return True
    except urllib2.URLError as err:
    	pass
    return False
'''

def eth0_is_up():
    addr = netifaces.ifaddresses('eth0')
    return netifaces.AF_INET in addr

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

class PiTrainerState(Enum):
	load_program = 1
	ready_for_exercise = 2
	doing_exercise = 3
	exercise_too_hard = 4
	paused_exercise = 5
	give_feedback = 6
	finished_workout = 7
	upload_results = 8
	ready_to_turn_off = 9

def shaken_twice():
	pass

def upload_results():
	pass

''' User instructions

1. When you are ready, shake the PiTrainer twice. The flashing green 'play'
arrow will appear. Once shaken twice again, The Pi will start. 2. Place the
PiTrainer in a secure position where it will not fall or be trodden on. It
will then scroll text telling you what apparatus you should use, whether it be
a mat or a rowing machine.

<When you are ready to start the exercise …>

<I think all exercises are timed, right?  When your exercise is coming to an
<end, the PiTrainer will …>

6. If the activity is too hard (over-straining you) then move the purple
square towards the red border one step over for a little too hard, or move
twice so the purple square touches the red for much too hard.

5.If you want to pause the Pi at any point during a timed exercise, move the
purple square towards the blue border with the joystick.

3. When a timed activity finishes, you can record how difficult or easy you
found it.  Move the purple square towards the red side if you found it
difficult or towards the green side if you found it easy.  Shake the Pi twice
to confirm your choice, and flashing green 'play' arrow will appear. Once
shaken twice again, the PiTrainer will tell you about your next exercise.

4. Continue as above.  When you have finished your last activity in the
workout, rather than showing a green arrow, the PiTrainer will flash a red
stop sign.

8. This should make the pi quit the activity and return to the home screen.
then pull the joystick up to shut down the pi, then return it to the pi bank.
alternatively, pull the joystick down 3 times - one to pause, one to return to
the menu, and one to shut down. if the pi falls, it will automatically pause,
because of the vibrations this will pause. two shakes can also be used to
pause and play.

'''

# If Pi Trainer is started and there is an old completed workout stored, we need to upload it.
if isfile('completed.json'):
	pi_trainer = PiTrainerState.upload_results
else:
	pi_trainer = PiTrainerState.load_program

program = []
exercise_index = 0
to_do = None
completed = []
loops_per_sec = 4

while True:
	sleep(1/loops_per_sec)

	if pi_trainer is PiTrainerState.load_program:

		# Display 'not ready' on screen
		sense.set_pixels(not_ready)
		try:
			with open('program.json','r') as f:
				try:
					program = json.loads(f.read())
					remove('program.json')
					pi_trainer = PiTrainerState.ready_for_exercise
				except ValueError:
					pass
		except FileNotFoundError:
			pass

	elif pi_trainer is PiTrainerState.ready_for_exercise:

		# Display 'play' on screen
		sense.set_pixels(play)
		if shaken_twice():
			to_do = program[exercise_index]
			exercise_index += 1
			pi_trainer = PiTrainerState.doing_exercise

	elif pi_trainer is PiTrainerState.doing_exercise:
		# Update the display

		# Check for user input and update the state
		if pause():
			pi_trainer = PiTrainerState.paused_exercise
		elif too_hard():
			pi_trainer = PiTrainerState.exercise_too_hard
		elif timer == 0:
			pi_trainer = PiTrainerState.give_feedback
		else:
			timer -= 1

	elif pi_trainer is PiTrainerState.exercise_too_hard:
		pass
	elif pi_trainer is PiTrainerState.paused_exercise:
		pass
	elif pi_trainer is PiTrainerState.give_feedback:
		# Get feedback from the user about how difficult or easy the exercise was

		if exercise_index == len(program):
			pi_trainer = PiTrainerState.finished_workout
		else:
			pi_trainer = PiTrainerState.ready_for_exercise

	elif pi_trainer is PiTrainerState.finished_workout:

		# Display 'plug in to a network' logo so results can be uploaded
		sense.set_pixels(plug_me_in)

		if not isfile('completed.json'):
			with open('completed.json', 'w') as f:
				f.write(json.dumps(completed,indent=0))

		# Wait for a network connection before trying to upload results
		if eth0_is_up():
			pi_trainer = PiTrainerState.upload_results

	elif pi_trainer is PiTrainerState.upload_results:

		sense.set_pixels(uploading)
		
		if isfile('completed.json'):
			# Display 'uploading' on screen
			upload_results()
			remove('completed.json')

		if isfile('program.json'):
			pi_trainer = PiTrainerState.load_program
		else:
			pi_trainer = PiTrainerState.ready_to_turn_off

	elif pi_trainer is PiTrainerState.ready_to_turn_off:
		sense.set_pixels(turn_off)
	else:
		pass

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
