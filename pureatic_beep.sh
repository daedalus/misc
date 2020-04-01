#!/bin/bash
# Pureactiv vacum cleaner beep locator
# Author Dario Clavijo 2020
# GPlv3
echo AABVqgAAAAIAAAANAAAANzMuMwAAAAAAAAAFAAwpiutUqzD0zSgGLblvut3RUS0n4gGj8AvruF0l19JSD38sBJK/UgAAqlU= | base64 -d | nc $1 6668 | xxd
