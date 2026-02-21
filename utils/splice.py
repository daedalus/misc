import sys
if len(sys.argv) == 1:
  print('usage: <"string"< <offset> <length>')
else:
  string = sys.argv[1]
  offset = int(sys.argv[2])
  length = int(sys.argv[3])
  print(string[offset: offset + length])
