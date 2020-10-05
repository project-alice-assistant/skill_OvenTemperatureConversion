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
	def letsconvert2C(self, session: DialogSession):
		if 'Number' not in session.slotsAsObjects:
			self.askForNumberC(session)
		else:
			self.readyToConvert2C(session)


	def readyToConvert2C(self, session: DialogSession):
		spokenTemperature = session.slotValue('Number')
		self.endDialog(session.sessionId, self.randomTalk(text='respondCelsius', replace=[self.convertToCelsius(spokenTemperature)]))


	def askForNumberC(self, session: DialogSession):
		self.continueDialog(
			sessionId=session.sessionId,
			text=self.randomTalk(text='respondNoIdea'),
			intentFilter=['convert2Celsius'],
			currentDialogState='askingToConvertToC'
		)


	@IntentHandler(intent='convert2Celsius', requiredState='askingToConvertToC')
	def f2cIntent(self, session):
		self.letsconvert2C(session)


	@IntentHandler('convert2fahrenheit')
	def letsconvert2F(self, session: DialogSession):
		if 'Number' not in session.slotsAsObjects:
			self.askForNumberF(session)
		else:
			self.readyToConvert2F(session)


	def askForNumberF(self, session: DialogSession):
		self.continueDialog(
			sessionId=session.sessionId,
			text=self.randomTalk(text='respondNoIdea'),
			intentFilter=['convert2Celsius'],
			currentDialogState='askingToConvertToC'
		)


	def readyToConvert2F(self, session: DialogSession):
		# Grab the requested temperature and convert it to F
		spokenTemperature = session.slotValue('Number')
		self.endDialog(session.sessionId, self.randomTalk(text='respondFahrenheit', replace=[self.convertToFahrenheit(spokenTemperature)]))


	@IntentHandler(intent='convert2fahrenheit', requiredState='askingToConvertToF')
	def c2fIntent(self, session: DialogSession, **_kwargs):
		# Check if a temperature number was provided
		self.letsconvert2F(session)


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


	@staticmethod
	def convertToFahrenheit(temperature: int) -> int:
		return int((9 * temperature) / 5 + 32)


	@staticmethod
	def convertToCelsius(temperature: int) -> int:
		return int((temperature - 32) * 5 / 9)
