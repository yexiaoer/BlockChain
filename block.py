from datetime import datetime
import hashlib
import binascii

##swap function use to convert data in to endian format
##we are using big Endian
##The most significant byte (the "big end") of the data is 
##placed at the byte with the lowest address. The rest of 
##the data is placed in order in the next three bytes in memory.
def swap_endianess(h):
	if h[:2] == "0x":
		h = h[2:]
	return str.join("", [h[i:i+2] for i in range(len(h), -1, -2)])

print('Block number: #563226')
print('Block Hash Value: 0000000000000000001e0f3ccaa4b1cf87d9e655c89da0ed9f66946753f9b1ca')
print('a. Previous block hash:(Hash value for previous block)')
print('000000000000000000106cf93319ba33fc96b102527edb684e71b0113c76dc9a')
print('')
print('b. Merkle root:(Cotains the hash of all the transacitons) ')
print('98b9af57794720cb720e89cd124bd23c21a4c0b4014e73bcadf9d608bd448e3c')
print('')
print('c. Time: (The exact moment of this block hash discovery)')
print('2019-02-10 13:22:21')
print('')
print('d. Version: (Signal the network)')
print('0x20000000')
print('')
print('e. Bit:(Mining difficulty)')
print('389048373')
print('')
print('f. Nonce:(Random number added to the combination of transacitons,')
print('their data, the Merkle root, and other bits of information')
print('in order to make the proof of work algorithm come up with a ')
print('hash that matches the difficulty)')
print('498948828')
print('')

version = 0x2000E000
bits = 388919176
nonce = 2764423286
version = swap_endianess("{0:0{1}x}".format(version,8))
bits = swap_endianess("{0:0{1}x}".format(bits,8))
nonce = swap_endianess("{0:0{1}x}".format(nonce,8))

date_time_str = "2019-02-16 05:16:22" 
##converting time to time object
date_time_obj = datetime.strptime(date_time_str, "%Y-%m-%d %H:%M:%S")
##converting time into seconds
timestamp_as_int = int((date_time_obj - datetime(1970,1,1)).total_seconds())
##converting time into endian formate
time = swap_endianess("{0:0{1}x}".format(timestamp_as_int,8))

##previous block hash and current block merkle root copied from website
previous_block_hash = "000000000000000000106cf93319ba33fc96b102527edb684e71b0113c76dc9a"
merkle_root = "98b9af57794720cb720e89cd124bd23c21a4c0b4014e73bcadf9d608bd448e3c"
#converting into endian format
previous_block_hash = swap_endianess(previous_block_hash)
merkle_root = swap_endianess(merkle_root)

#encoding the data from string to ascii
version = version.encode("ascii")
previous_block_hash = previous_block_hash.encode("ascii")
merkle_root = merkle_root.encode("ascii")
time = time.encode("ascii")
bits = bits.encode("ascii")
nonce = nonce.encode("ascii") 

#print('Version: ', version)
#print('Previous block has', previous_block_hash)
#print('Merkle root', merkle_root)
#print('Time', time)
#print('Bit: ', bits)
#print('Nonce:', nonce)

#Add all the ascii data together
header_as_bytes = version + previous_block_hash + merkle_root + time + bits + nonce
#Return the binary data represented by the hexadecimal string header_as_bytes
block = binascii.unhexlify(header_as_bytes)
#use sha256 to hash 
#the digest of the concatenation of the strings fed to it so far 
#may contain non-ASCII characters, including null bytes.
round1 = hashlib.sha256(block).digest()
#containing only hexadecimal digits
round2 = hashlib.sha256(round1).hexdigest()
##converting into endian formate
verify = swap_endianess(round2) 
printt('hash = H(previous hash, Version + Merkle_root + Time + Bits, nonce)')
print('Hash Value calculated for this block: ')
print(verify)