#!/bin/bash
mkfifo {stdout,stderr}
./sdiff.sh 1> stdout 2> stderr
