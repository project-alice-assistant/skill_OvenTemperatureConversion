from core.base.model.AliceSkill import AliceSkill
from core.dialog.model.DialogSession import DialogSession
from core.util.Decorators import IntentHandler


class OvenTemperatureConversion(AliceSkill):
	"""
	Author: Lazza
	Description: Convert temperature between F and C and also inform of what
	oven Gas mark to use, The first two Intent handlers deal with converting
	between the two temperature types C and F.
	The third handler deals with outputting the oven gas Mark to use
	"""


	# Convert from fahrenheit to celcius
	@IntentHandler('convert2Celsius')
	def convertingToCelciusIntent(self, session: DialogSession):
		if 'Number' not in session.slotsAsObjects:
			self.askToRepeatWithNumber(session, intentFilta='convert2Celsius')
		else:
			self.readyToConvert(session, temperatureType='Celsius', converter=self.convertToCelsius)
		# Return value for unit testing
		return session.slotValue('Number')

	# Converting from celcius to fahrenheit
	@IntentHandler('convert2fahrenheit')
	def convertingToFahrenheitIntent(self, session: DialogSession):
		if 'Number' not in session.slotsAsObjects:
			self.askToRepeatWithNumber(session, intentFilta='convert2fahrenheit')
		else:
			self.readyToConvert(session, temperatureType='Fahrenheit', converter=self.convertToFahrenheit)
		# Return value for unit testing
		return session.slotValue('Number')

	# Convert and say the result
	def readyToConvert(self, session: DialogSession, converter, temperatureType: str):
		spokenTemperature: int = session.slotValue('Number')
		self.endDialog(session.sessionId, self.randomTalk(text='respondTemperature', replace=[converter(spokenTemperature), temperatureType]))


	# ask user to repeat what they said but with a number
	def askToRepeatWithNumber(self, session: DialogSession, intentFilta: str):
		self.continueDialog(
			sessionId=session.sessionId,
			text=self.randomTalk(text='respondNoIdea'),
			intentFilter=[intentFilta]
		)


	@IntentHandler('informGasMark')
	def gasMarkIntent(self, session: DialogSession, **_kwargs):

		if 'Number' not in session.slotsAsObjects:
			self.endDialog(session.sessionId, self.randomTalk(text='respondNoIdea'))
			return

		# Spokeninput is the users requested temperature
		spokenInput = session.slotValue('Number')

		if 'fahrenheit' in session.slotsAsObjects:
			spokenInput = self.convertToCelsius(spokenInput)

		if spokenInput < 135:
			self.endDialog(session.sessionId, self.randomTalk(text='respondOutOfRange'))
			return
		elif 135 <= spokenInput <= 148:
			correctGasMark = 1
		elif 149 <= spokenInput <= 162:
			correctGasMark = 2
		elif 163 <= spokenInput <= 176:
			correctGasMark = 3
		elif 177 <= spokenInput <= 190:
			correctGasMark = 4
		elif 191 <= spokenInput <= 203:
			correctGasMark = 5
		elif 204 <= spokenInput <= 217:
			correctGasMark = 6
		elif 218 <= spokenInput <= 231:
			correctGasMark = 7
		elif 232 <= spokenInput <= 245:
			correctGasMark = 8
		elif 246 <= spokenInput <= 269:
			correctGasMark = 9
		elif 270 <= spokenInput <= 290:
			correctGasMark = 10
		else:
			self.endDialog(session.sessionId, self.randomTalk(text='respondAboveRange'))
			return

		self.endDialog(session.sessionId, self.randomTalk(text='respondGasMark', replace=[correctGasMark]))
		# return local var for unit testing reasons
		return correctGasMark

	@staticmethod
	def convertToFahrenheit(temperature: int) -> int:
		return int((9 * temperature) / 5 + 32)


	@staticmethod
	def convertToCelsius(temperature: int) -> int:
		return int((temperature - 32) * 5 / 9)
