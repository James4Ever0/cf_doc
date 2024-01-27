#!/bin/bash
# must pipe the data to the process.
cat xwd.dump | pypy3  pypy_xwd.py --raw | python3 unpickle.py 
