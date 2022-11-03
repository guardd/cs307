import uuid
import os,binascii
class IDCreation:

	def generate_ID():
		x = str(uuid.uuid4())
		return x
	def generate_color_hex():
		hexcode = binascii.b2a_hex(os.urandom(6))
		hexcode=hexcode.upper()
		hexcode= f'#{hexcode}'
		return hexcode