
import phonenumbers
from metl.utils import *

@tarr.rule
def formatPhoneNumber( field ):

	if field.getValue() is None:
		return field

	prototype = phonenumbers.parse( field.getValue() )
	field.setValue(
		phonenumbers.format_number( 
			prototype, 
			phonenumbers.PhoneNumberFormat.NATIONAL 
		)
	)

	return field