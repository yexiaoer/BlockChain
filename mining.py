import hashlib
import random
import binascii
import time
import datetime

##method to find the nounce for current target
def findNo(target):
	start_time = time.time()
	count = 0
	#the hash value for H("message"+nounce) need to be less than the target
	while True:
	    m = hashlib.sha256()
	    header = "message"
	    m.update(header.encode('utf-8'))
	    nonce = random.getrandbits(32)
	    m.update(str(nonce).encode('utf-8'));
	    #converting to hex string
	    hexdigest = m.hexdigest()
	    count += 1
	    #check if the hash value is less than the target
	    if(hexdigest < target):         
	        break
	end_time = time.time()
	print ("Target: ", target)
	print ("Number of hash calculated: ", count)
	print ("Time used to compute: ", end_time - start_time)
	print ("Nounce found: ", nonce)
	print ("Hash: ", hexdigest)

#Define target, I use hex here because it is easier 
#for me to calculate difficulty
#Difficulty value for the first block
first_block_diff_1 = 0x00000000ffff0000000000000000000000000000000000000000000000000000
target1 = 0x00ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
target2 = 0x000fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
target3 = 0x0000ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
target4 = 0x00000fffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
target5 = 0x000000ffffffffffffffffffffffffffffffffffffffffffffffffffffffffff

target1s = "00ffffff" + "ffffffff" + "ffffffff" + "ffffffff" + "ffffffff" + "ffffffff" + "ffffffff" + "ffffffff"
target2s = "000fffff" + "ffffffff" + "ffffffff" + "ffffffff" + "ffffffff" + "ffffffff" + "ffffffff" + "ffffffff"
target3s = "0000ffff" + "ffffffff" + "ffffffff" + "ffffffff" + "ffffffff" + "ffffffff" + "ffffffff" + "ffffffff"
target4s = "00000fff" + "ffffffff" + "ffffffff" + "ffffffff" + "ffffffff" + "ffffffff" + "ffffffff" + "ffffffff"
target5s = "000000ff" + "ffffffff" + "ffffffff" + "ffffffff" + "ffffffff" + "ffffffff" + "ffffffff" + "ffffffff"


#To calculate the difficulty, we need to use the following formula
#difficulty = difficulty_1_target / current_target
#I used float because without using it, it will
#print 0 since the result it very small
##finding the nounce of current target 
findNo(target1s)
print ("Difficulty for target: ", float(first_block_diff_1) / target1, "\n")

findNo(target2s)
print ("Difficulty for target: ", float(first_block_diff_1) / target2, "\n")

findNo(target3s)
print ("Difficulty for target: ", float(first_block_diff_1) / target3, "\n")

findNo(target4s)
print ("Difficulty for target: ", float(first_block_diff_1) / target4, "\n")

findNo(target5s)
print ("Difficulty for target: ", float(first_block_diff_1) / target5, "\n")
#After observing the result, I discovered that the target with more 
#leading zeros take longer time to find the nounce.The difficulty of the 
#target increase as the leading zero increse.


