from sys import argv, exit
import math

PUA_start=57344

def printf(temp):
    # print(temp, end="")
    outFile.write(temp)


CP437_list = "\x00☺☻♥♦♣♠•◘○◙♂♀♪♫☼►◄↕‼¶§▬↨↑↓→←∟↔▲▼ !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\x5C]^_`abcdefghijklmnopqrstuvwxyz{|}~⌂ÇüéâäàåçêëèïîìÄÅÉæÆôöòûùÿÖÜ¢£¥₧ƒáíóúñÑªº¿⌐¬½¼¡«»░▒▓│┤╡╢╖╕╣║╗╝╜╛┐└┴┬├─┼╞╟╚╔╩╦╠═╬╧╨╤╥╙╘╒╓╫╪┘┌█▄▌▐▀αßΓπΣσµτΦΘΩδ∞φε∩≡±≥≤⌠⌡÷≈°∙·√ⁿ²■\xA0"

if len(argv) < 2:
  print ('[*] Usage: python dokkebi_eng.py <input_file> <start> [height]')
  exit()

file  = argv[1]
start = int(argv[2], 16)
height = 16
if len(argv) > 2:
    height = int(argv[3])

mode = 1

fp = open(file , 'rb')
fp.seek(start)

outFile = open(file.replace(("."+file.split('.')[-1]),'.json'),'w',encoding='utf-8')

for i in range(len(CP437_list)):
    printf("\t\t{\n")
    if (i<0x20 or i>0x7f) and mode == 1:
        printf("\t\t\t\"unicode\": " + str(0xF000+i) + ",\n")
    else:
        printf("\t\t\t\"unicode\": " + str(ord(CP437_list[i])) + ",\n")
    
    #data print        
    printf("\t\t\t\"data\": [\n")
    for h in range(height):
        printf("\t\t\t\t\"")
        # horizon
        for w in range(math.ceil(height/16)):
            value = fp.read(1)[0]
            bin_val = format(value, 'b').zfill(8).replace('1','#').replace('0','.')
            printf(bin_val)

        if h < height-1:
            printf("\",\n")
        else:
            printf("\"\n")

    printf("\t\t\t]\n")
    printf("\t\t},\n")
fp.close()
