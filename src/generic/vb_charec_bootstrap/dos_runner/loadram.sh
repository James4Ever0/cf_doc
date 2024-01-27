#!/bin/bash
./unloadram.sh
sudo mkdir ramdisk
sudo chmod 777 ramdisk
sudo mount -t tmpfs -o size=10m myramdisk ramdisk
