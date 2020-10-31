from typing import Any
from unittest import TestCase, mock
from unittest.mock import MagicMock, PropertyMock

from PublishedSkills.OvenTemperatureConversion.OvenTemperatureConversion import OvenTemperatureConversion


class TestOvenTemperatureConversion(TestCase):

	def test_converting_to_celcius_intent(self):
		pass # Nothing to test


	def test_converting_to_fahrenheit_intent(self):
		pass # Nothing to test


	def test_ready_to_convert(self):
		pass # Nothing to test


	def test_ask_to_repeat_with_number(self):
		pass # Nothing to test


	@mock.patch('core.base.SuperManager.SuperManager')
	def test_gas_mark_intent(self, mock_superManager):
		class DialogSession:

			def __init__(self, slotsAsObjects: dict):
				self.slotsAsObjects = slotsAsObjects


			@property
			def sessionId(self) -> str:
				return 'unittest'


			def slotValue(self, slotName: str, index: int = 0, defaultValue: Any = None) -> Any:
				try:
					return self.slotsAsObjects[slotName]
				except (KeyError, IndexError):
					return defaultValue


		class LanguageManager:

			@property
			def activeLanguage(self) -> str:
				return 'en'


			@property
			def supportedLanguages(self) -> list:
				return ['en']


		# mock SuperManager
		mock_superManagerInstance = MagicMock()
		mock_superManager.getInstance.return_value = mock_superManagerInstance
		mock_superManagerInstance.talkManager.randomTalk.return_value = 'unittest'

		mock_languageManager = PropertyMock(return_value=LanguageManager())
		type(mock_superManagerInstance).languageManager = mock_languageManager

		skill = OvenTemperatureConversion()

		# If slot is missing
		session = DialogSession({})
		skill.gasMarkIntent(session)
		mock_superManagerInstance.talkManager.randomTalk.assert_called_once_with(skill='OvenTemperatureConversion', talk='respondNoIdea')
		mock_superManagerInstance.reset_mock()

		# If slot is not upper first
		session = DialogSession({'number': 10})
		skill.gasMarkIntent(session)
		mock_superManagerInstance.talkManager.randomTalk.assert_called_once_with(skill='OvenTemperatureConversion', talk='respondNoIdea')
		mock_superManagerInstance.reset_mock()

		# the number is under range
		session = DialogSession({'Number': 75})
		skill.gasMarkIntent(session)
		mock_superManagerInstance.talkManager.randomTalk.assert_called_once_with(skill='OvenTemperatureConversion', talk='respondOutOfRange')
		mock_superManagerInstance.reset_mock()

		# the number is under range
		session = DialogSession({'Number': 300})
		skill.gasMarkIntent(session)
		mock_superManagerInstance.talkManager.randomTalk.assert_called_once_with(skill='OvenTemperatureConversion', talk='respondAboveRange')
		mock_superManagerInstance.reset_mock()

		# should be working correctly
		session = DialogSession({'Number': 155})
		skill.gasMarkIntent(session)
		mock_superManagerInstance.talkManager.randomTalk.assert_called_once_with(skill='OvenTemperatureConversion', talk='respondGasMark')
		mock_superManagerInstance.reset_mock()

		# if slot is present but empty
		session = DialogSession({'Number': ''})
		skill.gasMarkIntent(session)
		mock_superManagerInstance.talkManager.randomTalk.assert_called_once_with(skill='OvenTemperatureConversion', talk='respondNoIdea')
		mock_superManagerInstance.reset_mock()

		# if slot is present but not correct type, could be working if cast to int
		session = DialogSession({'Number': '155'})
		skill.gasMarkIntent(session)
		mock_superManagerInstance.talkManager.randomTalk.assert_called_once_with(skill='OvenTemperatureConversion', talk='respondGasMark')
		mock_superManagerInstance.reset_mock()

		# if slot is present but not correct type and above range, could be working if cast to int
		session = DialogSession({'Number': '300'})
		skill.gasMarkIntent(session)
		mock_superManagerInstance.talkManager.randomTalk.assert_called_once_with(skill='OvenTemperatureConversion', talk='respondAboveRange')
		mock_superManagerInstance.reset_mock()


	def test_convert_to_fahrenheit(self):
		pass # Nothing to test


	def test_convert_to_celsius(self):
		pass # Nothing to test
