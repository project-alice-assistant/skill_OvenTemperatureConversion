from core.base.model.AliceSkill import AliceSkill
from core.dialog.model.DialogSession import DialogSession
from core.util.Decorators import IntentHandler


class OvenTemperatureConversion(AliceSkill):
	"""
	Author: LazzaAU
	Description: Convert temperature between F and C and also inform of what
	oven Gas mark to use, The first two Intent handlers deal with converting
	between the two temperature types C and F.
	The third handler deals with outputting the oven gas Mark to use
	"""

	@IntentHandler('convert2Celsius')
	def f2cIntent(self, session: DialogSession, **_kwargs):
		# Check if a temperature number was provided
		if 'Number' not in session.slotsAsObjects:
			self.endDialog(session.sessionId, self.randomTalk(text='respondNoIdea'))
			return

		# Grab the requested temperature and send it to TempConversion class for converting

		spokenTemperature = session.slotValue('Number')
		temp1 = TempConversion(spokenTemperature)
		temp2 = temp1.convertToCelsius()
		self.endDialog(session.sessionId, self.randomTalk(text='respondCelsius', replace=[temp2]))

	@IntentHandler('convert2fahrenheit')
	def c2fIntent(self, session: DialogSession, **_kwargs):

		if 'Number' not in session.slotsAsObjects:
			self.endDialog(session.sessionId, self.randomTalk(text='respondNoIdea'))
			return


		spokenTemperature = session.slotValue('Number')
		temp1 = TempConversion(spokenTemperature)
		temp2 = temp1.convertToFahrenheit()
		self.endDialog(session.sessionId, self.randomTalk(text='respondFahrenheit', replace=[temp2]))

	@IntentHandler('informGasMark')
	def gasMarkIntent(self, session: DialogSession, **_kwargs):

		if 'Number' not in session.slotsAsObjects:
			self.endDialog(session.sessionId, self.randomTalk(text='respondNoIdea'))
			return

		# Spokeninput is the users requested temperature
		spokenInput = session.slotValue('Number')

		# todo work out a way to condense the below 72 lines of code ?
		if 'fahrenheit' not in session.slotsAsObjects:

			if spokenInput < 135:
				self.endDialog(session.sessionId, self.randomTalk(text='respondOutOfRange'))
			elif 135 <= spokenInput <= 148:
				correctGasMark = 1
				self.endDialog(session.sessionId, self.randomTalk(text='respondGasMark', replace=[correctGasMark]))
			elif 149 <= spokenInput <= 162:
				correctGasMark = 2
				self.endDialog(session.sessionId, self.randomTalk(text='respondGasMark', replace=[correctGasMark]))
			elif 163 <= spokenInput <= 176:
				correctGasMark = 3
				self.endDialog(session.sessionId, self.randomTalk(text='respondGasMark', replace=[correctGasMark]))
			elif 177 <= spokenInput <= 190:
				correctGasMark = 4
				self.endDialog(session.sessionId, self.randomTalk(text='respondGasMark', replace=[correctGasMark]))
			elif 191 <= spokenInput <= 203:
				correctGasMark = 5
				self.endDialog(session.sessionId, self.randomTalk(text='respondGasMark', replace=[correctGasMark]))
			elif 204 <= spokenInput <= 217:
				correctGasMark = 6
				self.endDialog(session.sessionId, self.randomTalk(text='respondGasMark', replace=[correctGasMark]))
			elif 218 <= spokenInput <= 231:
				correctGasMark = 7
				self.endDialog(session.sessionId, self.randomTalk(text='respondGasMark', replace=[correctGasMark]))
			elif 232 <= spokenInput <= 245:
				correctGasMark = 8
				self.endDialog(session.sessionId, self.randomTalk(text='respondGasMark', replace=[correctGasMark]))
			elif 246 <= spokenInput <= 269:
				correctGasMark = 9
				self.endDialog(session.sessionId, self.randomTalk(text='respondGasMark', replace=[correctGasMark]))
			elif 270 <= spokenInput <= 290:
				correctGasMark = 10
				self.endDialog(session.sessionId, self.randomTalk(text='respondGasMark', replace=[correctGasMark]))
			else:
				self.endDialog(session.sessionId, self.randomTalk(text='respondAboveRange'))
			return

		if 'celsius' not in session.slotsAsObjects:
			if spokenInput < 275:
				self.endDialog(session.sessionId, self.randomTalk(text='respondOutOfRange'))
			elif 275 <= spokenInput <= 291:
				correctGasMark = 1
				self.endDialog(session.sessionId, self.randomTalk(text='respondGasMark', replace=[correctGasMark]))
			elif 300 <= spokenInput <= 324:
				correctGasMark = 2
				self.endDialog(session.sessionId, self.randomTalk(text='respondGasMark', replace=[correctGasMark]))
			elif 325 <= spokenInput <= 349:
				correctGasMark = 3
				self.endDialog(session.sessionId, self.randomTalk(text='respondGasMark', replace=[correctGasMark]))
			elif 350 <= spokenInput <= 374:
				correctGasMark = 4
				self.endDialog(session.sessionId, self.randomTalk(text='respondGasMark', replace=[correctGasMark]))
			elif 375 <= spokenInput <= 399:
				correctGasMark = 5
				self.endDialog(session.sessionId, self.randomTalk(text='respondGasMark', replace=[correctGasMark]))
			elif 400 <= spokenInput <= 424:
				correctGasMark = 6
				self.endDialog(session.sessionId, self.randomTalk(text='respondGasMark', replace=[correctGasMark]))
			elif 425 <= spokenInput <= 449:
				correctGasMark = 7
				self.endDialog(session.sessionId, self.randomTalk(text='respondGasMark', replace=[correctGasMark]))
			elif 450 <= spokenInput <= 474:
				correctGasMark = 8
				self.endDialog(session.sessionId, self.randomTalk(text='respondGasMark', replace=[correctGasMark]))
			elif 475 <= spokenInput <= 499:
				correctGasMark = 9
				self.endDialog(session.sessionId, self.randomTalk(text='respondGasMark', replace=[correctGasMark]))
			elif 500 <= spokenInput <= 525:
				correctGasMark = 10
				self.endDialog(session.sessionId, self.randomTalk(text='respondGasMark', replace=[correctGasMark]))
			else:
				self.endDialog(session.sessionId, self.randomTalk(text='respondAboveRange'))


# Below class is for converting between C and F


class TempConversion:

	def __init__(self, requestedTemp):
		self._requestedTemp = requestedTemp

	def convertToFahrenheit(self):
		result = int((9 * self._requestedTemp) / 5 + 32)
		return result

	def convertToCelsius(self):
		result = int((self._requestedTemp - 32) * 5 / 9)
		return result
