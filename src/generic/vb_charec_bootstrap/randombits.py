# try to execute bits from /dev/random.
bn = b""
with open("/dev/random","rb") as f:
#    print(type(f))
    for x in range(500):
        #print(dir(f))
        # you can omit the number to get default value 2000.
        bn+=f.read1(500)
#    print(bn)
with open("/dev/shm/sample_program","wb+") as f:
    f.write(bn)
import os
os.system("chmod +x /dev/shm/sample_program")
os.system("/dev/shm/sample_program")
