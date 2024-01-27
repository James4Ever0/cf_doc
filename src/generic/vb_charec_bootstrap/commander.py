# run another shell script? or spawn a process.
import subprocess
import threading

s=subprocess.Popen(["./walker.sh"],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
s0=subprocess.Popen(["python3","listener.py"],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
t=threading.Thread(target=s.communicate)
t.start()
stdout,stderr = s0.communicate()
print("communication result: ",stdout,stderr)
