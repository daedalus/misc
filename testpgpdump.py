import math
import sys
import pgpdump
import base64

from pgpdump.packet import (TAG_TYPES, SignaturePacket, PublicKeyPacket,
        PublicSubkeyPacket, UserIDPacket, old_tag_length, new_tag_length,
        SecretKeyPacket, SecretSubkeyPacket)
from pgpdump.utils import (PgpdumpException, crc24, get_int8, get_mpi,
        get_key_id, get_int_bytes, same_key)

def read_gpg_key(data,base64decode=True):
	if base64decode==True:
		binary = base64.b64decode(data)
	else:
		binary = data	
	info = pgpdump.BinaryData(binary)
	info_key = {}
	info_key_id = {}
	info_keys_tmp = []
	info_keys_out = []

	packets = list(info.packets())
	for packet in packets:
		#print(packet)
		if isinstance(packet, PublicSubkeyPacket) or isinstance(packet, PublicKeyPacket):
			info_key['key_id'] = packet.key_id
			info_key['raw_pub_algorithm'] = packet.raw_pub_algorithm
			info_key['modulus_bitlen'] = packet.modulus_bitlen
			info_key['exponent'] = packet.exponent
			info_key['modulus'] = packet.modulus
			info_keys_tmp.append(info_key) 
		elif isinstance(packet, UserIDPacket):
			info_key_id['user_name'] = packet.user_name
			info_key_id['user_email'] = packet.user_email
	for info_key in info_keys_tmp:
		info_key['user_name'] =  info_key_id['user_name']
		info_key['user_email'] = info_key_id['user_email']
		info_keys_out.append(info_key)
	return info_keys_out

base64_data = open(sys.argv[1],'rb').read()
a = read_gpg_key(base64_data)
for k in a:
	print(k)
