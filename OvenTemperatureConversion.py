
from core.base.model.AliceSkill import AliceSkill
from core.dialog.model.DialogSession import DialogSession
from core.util.Decorators import IntentHandler


class OvenTemperatureConversion(AliceSkill):
	"""
	Author: LazzaAU
	Description: Convert temperature between F and C and also inform of what oven Gas mark to use
	"""

	@IntentHandler('convert2Celsius')
	def f2cIntent(self, session: DialogSession, **_kwargs):

		if 'Number' not in session.slotsAsObjects:
			self.endDialog(session.sessionId, self.randomTalk(text='respondNoIdea'))
			return

		spokentemperature = session.slotValue('Number')
		temp1 = TempConversion(spokentemperature)
		temp2 = temp1.convert_to_celsius()
		self.endDialog(session.sessionId, self.randomTalk(text='respondCelsius', replace=[temp2]))

	@IntentHandler('convert2fahrenheit')
	def c2fIntent(self, session: DialogSession, **_kwargs):

		if 'Number' not in session.slotsAsObjects:
			self.endDialog(session.sessionId, self.randomTalk(text='respondNoIdea'))
			return

		spokentemperature = session.slotValue('Number')
		temp1 = TempConversion(spokentemperature)
		temp2 = temp1.convert_to_fahrenheit()
		self.endDialog(session.sessionId, self.randomTalk(text='respondFahrenheit', replace=[temp2]))

	@IntentHandler('informGasMark')
	def gasMarkIntent(self, session: DialogSession, **_kwargs):

		if 'Number' not in session.slotsAsObjects:
			self.endDialog(session.sessionId, self.randomTalk(text='respondNoIdea'))
			return
		
		spokeninput = session.slotValue('Number')

		if 'fahrenheit' not in session.slotsAsObjects:

			if spokeninput < 135:
				self.endDialog(session.sessionId, self.randomTalk(text='respondOutOfRange'))
			elif 135 <= spokeninput <= 148:
				_correctGasMark = 1
				self.endDialog(session.sessionId, self.randomTalk(text='respondGasMark', replace=[_correctGasMark]))
			elif 149 <= spokeninput <= 162:
				_correctGasMark = 2
				self.endDialog(session.sessionId, self.randomTalk(text='respondGasMark', replace=[_correctGasMark]))
			elif 163 <= spokeninput <= 176:
				_correctGasMark = 3
				self.endDialog(session.sessionId, self.randomTalk(text='respondGasMark', replace=[_correctGasMark]))
			elif 177 <= spokeninput <= 190:
				_correctGasMark = 4
				self.endDialog(session.sessionId, self.randomTalk(text='respondGasMark', replace=[_correctGasMark]))
			elif 191 <= spokeninput <= 203:
				_correctGasMark = 5
				self.endDialog(session.sessionId, self.randomTalk(text='respondGasMark', replace=[_correctGasMark]))
			elif 204 <= spokeninput <= 217:
				_correctGasMark = 6
				self.endDialog(session.sessionId, self.randomTalk(text='respondGasMark', replace=[_correctGasMark]))
			elif 218 <= spokeninput <= 231:
				_correctGasMark = 7
				self.endDialog(session.sessionId, self.randomTalk(text='respondGasMark', replace=[_correctGasMark]))
			elif 232 <= spokeninput <= 245:
				_correctGasMark = 8
				self.endDialog(session.sessionId, self.randomTalk(text='respondGasMark', replace=[_correctGasMark]))
			elif 246 <= spokeninput <= 269:
				_correctGasMark = 9
				self.endDialog(session.sessionId, self.randomTalk(text='respondGasMark', replace=[_correctGasMark]))
			elif 270 <= spokeninput <= 290:
				_correctGasMark = 10
				self.endDialog(session.sessionId, self.randomTalk(text='respondGasMark', replace=[_correctGasMark]))
			else:
				self.endDialog(session.sessionId, self.randomTalk(text='respondAboveRange'))
			return

		if 'celsius' not in session.slotsAsObjects:
			if spokeninput < 275:
				self.endDialog(session.sessionId, self.randomTalk(text='respondOutOfRange'))
			elif 275 <= spokeninput <= 291:
				_correctGasMark = 1
				self.endDialog(session.sessionId, self.randomTalk(text='respondGasMark', replace=[_correctGasMark]))
			elif 300 <= spokeninput <= 324:
				_correctGasMark = 2
				self.endDialog(session.sessionId, self.randomTalk(text='respondGasMark', replace=[_correctGasMark]))
			elif 325 <= spokeninput <= 349:
				_correctGasMark = 3
				self.endDialog(session.sessionId, self.randomTalk(text='respondGasMark', replace=[_correctGasMark]))
			elif 350 <= spokeninput <= 374:
				_correctGasMark = 4
				self.endDialog(session.sessionId, self.randomTalk(text='respondGasMark', replace=[_correctGasMark]))
			elif 375 <= spokeninput <= 399:
				_correctGasMark = 5
				self.endDialog(session.sessionId, self.randomTalk(text='respondGasMark', replace=[_correctGasMark]))
			elif 400 <= spokeninput <= 424:
				_correctGasMark = 6
				self.endDialog(session.sessionId, self.randomTalk(text='respondGasMark', replace=[_correctGasMark]))
			elif 425 <= spokeninput <= 449:
				_correctGasMark = 7
				self.endDialog(session.sessionId, self.randomTalk(text='respondGasMark', replace=[_correctGasMark]))
			elif 450 <= spokeninput <= 474:
				_correctGasMark = 8
				self.endDialog(session.sessionId, self.randomTalk(text='respondGasMark', replace=[_correctGasMark]))
			elif 475 <= spokeninput <= 499:
				_correctGasMark = 9
				self.endDialog(session.sessionId, self.randomTalk(text='respondGasMark', replace=[_correctGasMark]))
			elif 500 <= spokeninput <= 525:
				_correctGasMark = 10
				self.endDialog(session.sessionId, self.randomTalk(text='respondGasMark', replace=[_correctGasMark]))
			else:
				self.endDialog(session.sessionId, self.randomTalk(text='respondAboveRange'))


class TempConversion:
	# _requested_temp = 0

	def __init__(self, requestedtemp):
		self.requestedtemp = requestedtemp

	def convert_to_fahrenheit(self):
		result = int((9 * self.requestedtemp) / 5 + 32)
		return result

	def convert_to_celsius(self):
		result = int((self.requestedtemp - 32) * 5 / 9)
		return result
