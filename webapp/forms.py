from django import forms
import string


def contains_all_letters(text):
	
	""" Checks if a string contains all of the letters of the alphabet.

	Args:
	    text: the string to be evaluated
	Returns:
	    True if the string contains all of the letters of the alphabet.
	    False otherwise
	Raises:
	    None

	"""
	
	# use a flag to hold our return value, to support having only one return
	return_value = True
    
    # use a set to get the unique values from the input text into a 
    # quickly searchable data structure, force everything to be lowercase
    # so that we don't have to search for upper and lower
	s = set(text.lower())

	# if the number of unique characters in the string is less than the
    # size of the alphabet, it cannot contain the full alphabet
	if len(s) >= 26:
		
	    # the .ascii_lowercase method returns a string containing the lowercase
	    # alphabet, iterate through looking for each of the letters
		for a in string.ascii_lowercase:
			# if at any time we cannot find a letter, we can stop searching
			if not a in s:
				return_value = False
				break

	else:
		return_value = False

	return return_value


class SForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)

    def check_string(self):

    	text = self.cleaned_data['text']
    	return contains_all_letters(text)

