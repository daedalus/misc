#!/bin/bash
# Autor Dario Clavijo 2017
set -x
for f in *; do
	sed $f -e 's/\s\{1,6\}$//g' > /tmp/$f
	mv /tmp/$f $f
done
