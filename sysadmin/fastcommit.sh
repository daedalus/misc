#!/bin/bash
# autor Dario Clavijo 2017
set -x
git pull; git add $1; git commit $1 -m $2 ; git push
