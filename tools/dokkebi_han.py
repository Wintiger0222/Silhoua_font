from sys import argv, exit

def printf(temp):
    print(temp, end="")

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
for i in range(2):
    printf("\"data\":[\n")
    #vertical
    for h in range(width):
        printf("\t\"")
        # horizon
        for w in range(width//8):
            value = fp.read(1)[0]
            bin_val = format(value, 'b').zfill(8).replace('1','#').replace('0','.')
            printf(bin_val)

        if h < width-1:
            printf("\",\n")
        else:
            printf("\"\n")

    printf("],\n")
fp.close()
