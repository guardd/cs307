import uuid
import os,binascii
class IDCreation:

	def generate_ID():
		x = str(uuid.uuid4())
		return x
	def generate_color_hex():
		hexcode = binascii.b2a_hex(os.urandom(6))
		hexcode = str(hexcode).upper()
		hexcode = hexcode[2:8]
		hexcode= f'#{hexcode}'
		return hexcode