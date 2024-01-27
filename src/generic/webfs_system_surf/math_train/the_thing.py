import subprocess
# how do you teach the files?
# list things. so we can do this.
from subprocess import PIPE
ik = subprocess.Popen(["./anytrain.sh"],stdout =PIPE, stderr=PIPE)
ik = ik.communicate()
print(ik)
import os
print(os.listdir(),len(os.listdir()))
