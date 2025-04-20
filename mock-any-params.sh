#!/bin/bash

# this script can be invoked using any number of arguments
# and will return true and exit
# this can be used to speedup the execution time by substituing this for long running commands

echo "=== mock script called ==="
echo "params: $@"
echo "=== returning success ==="
