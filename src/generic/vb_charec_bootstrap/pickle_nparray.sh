#!/bin/bash
python3 genparr.py | pypy3 getslice.py
# no np module. pickle will fail.
