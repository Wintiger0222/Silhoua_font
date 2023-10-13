from sys import argv, exit


PUA_start=57344

def printf(temp):
    print(temp, end="")

chosung_list = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
jungsung_list = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ']
jongsung_list = [' ', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
chosung_len=len(chosung_list)
jungsung_len=len(jungsung_list)
jongsung_len=len(jongsung_list)

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
    cho  = (code - ord('가'))//(jongsung_len*jungsung_len)
    jung = ((code - ord('가')) - ((jongsung_len*jungsung_len)*cho)) // jongsung_len
    jong = (code - ord('가')) - ((jongsung_len*jungsung_len)*cho) - jongsung_len*jung

    result = HangulTemplate(cho, jung, jong)

    return [PUA_start + result[0] * chosung_len + cho,
        PUA_start + (max_jamo[0] * chosung_len) + (result[1] * jungsung_len) + jung,
        PUA_start + (max_jamo[0] * chosung_len) + (max_jamo[1] * jungsung_len) + (result[2] * jongsung_len) + jong
    ]


print(UTF2CJJ(49395))


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
max_sybal=(max_jamo[0] * chosung_len) + (max_jamo[1] * jungsung_len) + (max_jamo[2] * jongsung_len)
for i in range(max_sybal):

    current = 0
    if i < (max_jamo[0] * chosung_len):
        current = 1
    elif i < (max_jamo[0] * chosung_len) + (max_jamo[1] * jungsung_len):
        current = 2
    elif i < max_sybal:
        current = 3
    
    printf("\t\t\t\t\"unicode\": " + str(i + PUA_start) + ",\n")
    
    #name print
    printf("\t\t\t\t\"name\": \"DKB | ")
    if current == 1:
        printf("choseong | " + str(i//chosung_len + 1) + " | " + chosung_list[i%chosung_len] + "\",\n")
    elif current == 2:
        temp = i - (max_jamo[0] * chosung_len)
        printf("jungseong | " + str(temp//jungsung_len + 1) + " | " + jungsung_list[temp%jungsung_len] + "\",\n")
    elif current == 3:
        temp = i - (max_jamo[0] * chosung_len) - (max_jamo[1] * jungsung_len)
        printf("jongseong | " + str(temp//jongsung_len + 1) + " | " + jongsung_list[temp%jongsung_len] + "\",\n")
    else:
        printf("\",\n")
    
    #data print        
    printf("\t\t\t\t\"data\": [\n")
    for h in range(width):
        printf("\t\t\t\t\t\"")
        # horizon
        for w in range(width//8):
            value = fp.read(1)[0]
            bin_val = format(value, 'b').zfill(8).replace('1','#').replace('0','.')
            printf(bin_val)

        if h < width-1:
            printf("\",\n")
        else:
            printf("\"\n")

    printf("\t\t\t\t]\n")
fp.close()
