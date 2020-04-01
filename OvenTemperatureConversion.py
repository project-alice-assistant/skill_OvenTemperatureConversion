
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

		input_temperature = session.slotValue('Number')
		temp1 = TempConversion(input_temperature)
		temp2 = temp1.convert_to_celsius()
		self.endDialog(session.sessionId, self.randomTalk(text='respondCelsius', replace=[temp2]))

	@IntentHandler('convert2fahrenheit')
	def c2fIntent(self, session: DialogSession, **_kwargs):

		if 'Number' not in session.slotsAsObjects:
			self.endDialog(session.sessionId, self.randomTalk(text='respondNoIdea'))
			return

		input_temperature = session.slotValue('Number')
		temp1 = TempConversion(input_temperature)
		temp2 = temp1.convert_to_fahrenheit()
		self.endDialog(session.sessionId, self.randomTalk(text='respondFahrenheit', replace=[temp2]))

	@IntentHandler('informGasMark')
	def gasMarkIntent(self, session: DialogSession, **_kwargs):

		if 'Number' not in session.slotsAsObjects:
			self.endDialog(session.sessionId, self.randomTalk(text='respondNoIdea'))
			return
		input_temp = session.slotValue('Number')

		if 'fahrenheit' not in session.slotsAsObjects:

			if input_temp < 135:
				self.endDialog(session.sessionId, self.randomTalk(text='respondOutOfRange'))
			elif 135 <= input_temp <= 148:
				correct_gas_mark = 1
				self.endDialog(session.sessionId, self.randomTalk(text='respondGasMark', replace=[correct_gas_mark]))
			elif 149 <= input_temp <= 162:
				correct_gas_mark = 2
				self.endDialog(session.sessionId, self.randomTalk(text='respondGasMark', replace=[correct_gas_mark]))
			elif 163 <= input_temp <= 176:
				correct_gas_mark = 3
				self.endDialog(session.sessionId, self.randomTalk(text='respondGasMark', replace=[correct_gas_mark]))
			elif 177 <= input_temp <= 190:
				correct_gas_mark = 4
				self.endDialog(session.sessionId, self.randomTalk(text='respondGasMark', replace=[correct_gas_mark]))
			elif 191 <= input_temp <= 203:
				correct_gas_mark = 5
				self.endDialog(session.sessionId, self.randomTalk(text='respondGasMark', replace=[correct_gas_mark]))
			elif 204 <= input_temp <= 217:
				correct_gas_mark = 6
				self.endDialog(session.sessionId, self.randomTalk(text='respondGasMark', replace=[correct_gas_mark]))
			elif 218 <= input_temp <= 231:
				correct_gas_mark = 7
				self.endDialog(session.sessionId, self.randomTalk(text='respondGasMark', replace=[correct_gas_mark]))
			elif 232 <= input_temp <= 245:
				correct_gas_mark = 8
				self.endDialog(session.sessionId, self.randomTalk(text='respondGasMark', replace=[correct_gas_mark]))
			elif 246 <= input_temp <= 269:
				correct_gas_mark = 9
				self.endDialog(session.sessionId, self.randomTalk(text='respondGasMark', replace=[correct_gas_mark]))
			elif 270 <= input_temp <= 290:
				correct_gas_mark = 10
				self.endDialog(session.sessionId, self.randomTalk(text='respondGasMark', replace=[correct_gas_mark]))
			else:
				self.endDialog(session.sessionId, self.randomTalk(text='respondAboveRange'))
			return

		if 'celsius' not in session.slotsAsObjects:
			if input_temp < 275:
				self.endDialog(session.sessionId, self.randomTalk(text='respondOutOfRange'))
			elif 275 <= input_temp <= 291:
				correct_gas_mark = 1
				self.endDialog(session.sessionId, self.randomTalk(text='respondGasMark', replace=[correct_gas_mark]))
			elif 300 <= input_temp <= 324:
				correct_gas_mark = 2
				self.endDialog(session.sessionId, self.randomTalk(text='respondGasMark', replace=[correct_gas_mark]))
			elif 325 <= input_temp <= 349:
				correct_gas_mark = 3
				self.endDialog(session.sessionId, self.randomTalk(text='respondGasMark', replace=[correct_gas_mark]))
			elif 350 <= input_temp <= 374:
				correct_gas_mark = 4
				self.endDialog(session.sessionId, self.randomTalk(text='respondGasMark', replace=[correct_gas_mark]))
			elif 375 <= input_temp <= 399:
				correct_gas_mark = 5
				self.endDialog(session.sessionId, self.randomTalk(text='respondGasMark', replace=[correct_gas_mark]))
			elif 400 <= input_temp <= 424:
				correct_gas_mark = 6
				self.endDialog(session.sessionId, self.randomTalk(text='respondGasMark', replace=[correct_gas_mark]))
			elif 425 <= input_temp <= 449:
				correct_gas_mark = 7
				self.endDialog(session.sessionId, self.randomTalk(text='respondGasMark', replace=[correct_gas_mark]))
			elif 450 <= input_temp <= 474:
				correct_gas_mark = 8
				self.endDialog(session.sessionId, self.randomTalk(text='respondGasMark', replace=[correct_gas_mark]))
			elif 475 <= input_temp <= 499:
				correct_gas_mark = 9
				self.endDialog(session.sessionId, self.randomTalk(text='respondGasMark', replace=[correct_gas_mark]))
			elif 500 <= input_temp <= 525:
				correct_gas_mark = 10
				self.endDialog(session.sessionId, self.randomTalk(text='respondGasMark', replace=[correct_gas_mark]))
			else:
				self.endDialog(session.sessionId, self.randomTalk(text='respondAboveRange'))


class TempConversion:
	requestedTemp = 0

	def __init__(self, requestedTemp):
		self.requestedTemp = requestedTemp

	def convert_to_fahrenheit(self):
		result = int((9 * self.requestedTemp) / 5 + 32)
		return result

	def convert_to_celsius(self):
		result = int((self.requestedTemp - 32) * 5 / 9)
		return result
