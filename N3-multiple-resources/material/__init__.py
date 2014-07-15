
import requests, codecs, json
from metl.utils import *

class DownloadVenue( Modifier ):

	"""
	Open in your browser:
	* https://developer.foursquare.com/docs/explore#req=venues/40a55d80f964a52020f31ee3

	Copy the oauth information and set the oath variable.
	"""

	oath = '3VHYKZDB4E5CAI4WZLBCEBTMBBILPTCAHIGTH1ON4SINN2EM'

	def modify( self, record ):

		content = requests.get('https://api.foursquare.com/v2/venues/%(id)s?oauth_token=%(oath)s&v=20140715' % {
			'id': record.getField('id').getValue(),
			'oath': self.oath
		}).json()

		fp = codecs.open( 'source/%s.json' % ( record.getField('id').getValue() ), 'w', 'utf-8' )
		json.dump( content, fp )
		fp.close()

		return record
