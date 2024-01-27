from dogtail import tree
from time import sleep
import subprocess
p=subprocess.Popen(["gnome-terminal","--wait"])
print(p.pid,"pid")
app = tree.root.application("gnome-terminal-server")
app.dump()
