from sys import argv, exit
import math

PUA_start=57344

def printf(temp):
    # print(temp, end="")
    outFile.write(temp)


chosung_list = [' ', 'ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
jungsung_list = [' ', 'ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ']
jongsung_list = [' ', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
chosung_len=len(chosung_list)
jungsung_len=len(jungsung_list)
jongsung_len=len(jongsung_list)

jamo_list = [chosung_list, jungsung_list, jongsung_list]
jamo_len = [chosung_len, jungsung_len, jongsung_len]

max_jamo = [8, 4, 4] #8x4x4벌
def HangulTemplate(cho, jung, jong):
    
    #                           ㅏ ㅐ ㅑ ㅒ ㅓ ㅔ ㅕ ㅖ ㅗ ㅘ ㅙ ㅚ ㅛ ㅜ ㅝ ㅞ ㅟ ㅠ ㅡ ㅢ ㅣ
    choTypesWithoutFinal = [0, 0, 0, 0, 0, 0, 0, 0, 1, 3, 3, 3, 1, 2, 4, 4, 4, 2, 1, 3, 0];
    choTypesWithFinal =    [5, 5, 5, 5, 5, 5, 5, 5, 6, 7, 7, 7, 6, 6, 7, 7, 7, 6, 6, 7, 5];
    jongTypes =            [0, 2, 0, 2, 1, 2, 1, 2, 3, 0, 2, 1, 3, 3, 1, 2, 1, 3, 3, 1, 1];

    return [
    choTypesWithoutFinal[jung] if jong == 0 else choTypesWithFinal[jung],
    (0 if jong == 0 else 2) + (0 if (cho == 0 or cho == 15) else 1),
    jongTypes[jung]
    ]


def UTF2CJJ(code):
    cho  = (code - ord('가'))//(21*28)
    jung = ((code - ord('가')) - ((21*28)*cho)) // 28
    jong = (code - ord('가')) - ((21*28)*cho) - 28*jung

    result = HangulTemplate(cho, jung, jong)

    if jong == 0:
        return [PUA_start + result[0] * chosung_len + cho + 1,#blank fix
            PUA_start + (max_jamo[0] * chosung_len) + (result[1] * jungsung_len) + jung + 1#blank fix
        ]
    else:
        return [PUA_start + result[0] * chosung_len + cho + 1,#blank fix
            PUA_start + (max_jamo[0] * chosung_len) + (result[1] * jungsung_len) + jung + 1,#blank fix
            PUA_start + (max_jamo[0] * chosung_len) + (max_jamo[1] * jungsung_len) + (result[2] * jongsung_len) + jong
        ]




if len(argv) < 2:
  print ('[*] Usage: python dokkebi_han.py <input_file> <start> [width] [height]')
  exit()

file  = argv[1]
start = int(argv[2], 16)
width = 16
height = width
if len(argv) > 2:
    width = int(argv[3])
    height = width
if len(argv) > 3:
    height = int(argv[4])

outFile = open(file.replace(("."+file.split('.')[-1]),'.json'),'w',encoding='utf-8')


for i in range(44032,55203):
    printf("\t\t{\n")
    printf("\t\t\t\"unicode\": " + str(i) + ",\n")
    printf("\t\t\t\"components\": ")
    printf(str(UTF2CJJ(i))+"\n")
    printf("\t\t},\n")

fp = open(file , 'rb')
fp.seek(start)
max_sybal=(max_jamo[0] * chosung_len) + (max_jamo[1] * jungsung_len) + (max_jamo[2] * jongsung_len)
for i in range(max_sybal):

    current = 0
    if i < (max_jamo[0] * chosung_len):
        current = 1
    elif i < (max_jamo[0] * chosung_len) + (max_jamo[1] * jungsung_len):
        current = 2
    elif i < max_sybal:
        current = 3
    
    printf("\t\t{\n")
    printf("\t\t\t\"unicode\": " + str(i + PUA_start) + ",\n")
    
    #name print
    printf("\t\t\t\"name\": \"DKB | ")
    if current == 1:
        temp = i
        printf("choseong | ")
    elif current == 2:
        temp = i - (max_jamo[0] * chosung_len)
        printf("jungseong | ")
    elif current == 3:
        temp = i - (max_jamo[0] * chosung_len) - (max_jamo[1] * jungsung_len)
        printf("jongseong | ")

    if current != 0:
        printf(str(temp//jamo_len[current-1] + 1) + " | " + jamo_list[current-1][temp%jamo_len[current-1]] + "\",\n")
    else:
        printf("\",\n")
    
    #data print        
    printf("\t\t\t\"data\": [\n")
    for h in range(height):
        printf("\t\t\t\t\"")
        # horizon
        for w in range(math.ceil(width/8)):
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
