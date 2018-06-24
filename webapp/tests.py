from django.test import TestCase

# Create your tests here.
from webapp.forms import contains_all_letters


class SCheckerTestCase(TestCase):
	def setup(self):
		pass

	def test_lower_case(self):
		text = 'abcdefghijklmnopqrstuvwxyz'
		answer = contains_all_letters(text)
		self.assertEqual(answer,True)

	def test_upper_case(self):
		text = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
		answer = contains_all_letters(text)
		self.assertEqual(answer,True)

	def test_mixed_case(self):
		text = 'ABCDEFGHijkLMNOPQRSTUVWXYZ'
		answer = contains_all_letters(text)
		self.assertEqual(answer,True)

	def test_special_chars(self):
		text = 'abc...DEFGHIJK///LMNOP   QR2STU:V""WXYZ'
		answer = contains_all_letters(text)
		self.assertEqual(answer,True)

	def test_sentence(self):
		text = 'The quick brown fox jumps over the lazy dog'
		answer = contains_all_letters(text)
		self.assertEqual(answer,True)

	def test_missing_letter(self):
		#P is missing
		text = 'abc...DEFGHIJK///LMNO   QR2STU:V""WXYZ'
		answer = contains_all_letters(text)
		self.assertEqual(answer,False)

	def test_empty(self):
		#P is missing
		text = ''
		answer = contains_all_letters(text)
		self.assertEqual(answer,False)

	def test_just_special_chars(self):
		#P is missing
		text = '!@#$%^&*()-=<>?{}|;/.,78900-=<>?{}|;/.,78900'
		answer = contains_all_letters(text)
		self.assertEqual(answer,False)


