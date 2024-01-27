#!/bin/bash
mkdir /dev/shm/xvfb
Xvfb -pixdepths 3 27 -fbdir /dev/shm/xvfb :3
