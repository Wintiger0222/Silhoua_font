from sys import argv, exit

if len(argv) < 2:
  print ('[*] Usage: python dokkebi_han.py <input_file> <start> [width]')
  exit()

file  = argv[1]
start = int(argv[2], 16)
width = 16
if len(argv) > 2:
    width = int(argv[3])

fp = open(file , 'rb')
fp.seek(start)
for i in range(1):
    for h in range(width):
        for w in range(width//8):
            value = fp.read(1)[0]
            bin_val = format(value, 'b').zfill(8).replace('1','#').replace('0','.')
            print(bin_val, end="")
        print("")
fp.close()
