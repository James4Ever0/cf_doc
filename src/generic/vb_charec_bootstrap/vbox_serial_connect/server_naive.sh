#!/bin/bash
# again, this does not distinguish stdin&stdout. shall be deprecated.
cat /dev/ttyS0 | bash &>/dev/ttyS0
# on android:
# cat /dev/ttyS0 | sh &>/dev/ttyS0
# should we consider utilize other COM ports? or just use a single port to distinguish STDIN/OUT/ERR?
# shall you explore more. create fifo to utilize things.
# and filter out the echo problem. maybe?
# or just use it!