# -*- coding: utf-8 -*- 
from sys import argv, exit
from text_list import CP437_list,SPC_list,KSG_list, KANJI_list
import math

PUA_start=57344

KOR_FONT_LIST = [0xCEA22]
ENG_FONT_LIST = [0xCD954]

type_name = ["명조체"]
bbale_name = ["네모", "빨래"]
type_name_eng = ["Myeongjoche"]
bbale_name_eng = ["Nemo", "Ppallae"]

#명조체 -ROMAN
#고딕체 -BOLD
#보석체 -roman(작은 보석)
#가는체 -Thin
#필기체 -Hand
#둥근체 -Italic;일치하지 않음
#샘물체 -bold(작은볼드)
#바람체 -WIND
def printf(temp):
    # print(temp, end="")
    outFile.write(temp)


chosung_list = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
jungsung_list = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ']
jongsung_list = ['ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
chosung_len=len(chosung_list)
jungsung_len=len(jungsung_list)
jongsung_len=len(jongsung_list)

jamo_list = [chosung_list, jungsung_list, jongsung_list]
jamo_len = [chosung_len, jungsung_len, jongsung_len]

max_jamo = [5, 2, 3] #5x2x3벌
def HangulTemplate(cho, jung, jong):
    
    #                      ㅏ ㅐ ㅑ ㅒ ㅓ ㅔ ㅕ ㅖ ㅗ ㅘ ㅙ ㅚ ㅛ ㅜ ㅝ ㅞ ㅟ ㅠ ㅡ ㅢ ㅣ
    choTypes =             [0, 3, 0, 3, 0, 3, 0, 3, 2, 1, 4, 1, 2, 2, 1, 4, 1, 2, 2, 1, 0];
    jongTypes =            [0, 2, 0, 2, 0, 2, 0, 2, 1, 0, 2, 0, 1, 1, 0, 2, 0, 1, 1, 0, 0];

    return [
    choTypes[jung],
    (0 if jong == 0 else 1),
    jongTypes[jung]
    ]


def UTF2CJJ(code):
    cho  = (code - ord('가'))//(21*28)
    jung = ((code - ord('가')) - ((21*28)*cho)) // 28
    jong = (code - ord('가')) - ((21*28)*cho) - 28*jung

    result = HangulTemplate(cho, jung, jong)

    if jong == 0:
        return [PUA_start + result[0] * chosung_len + cho,
            PUA_start + (max_jamo[0] * chosung_len) + (result[1] * jungsung_len) + jung
        ]
    else:
        return [PUA_start + result[0] * chosung_len + cho,
            PUA_start + (max_jamo[0] * chosung_len) + (result[1] * jungsung_len) + jung,
            PUA_start + (max_jamo[0] * chosung_len) + (max_jamo[1] * jungsung_len) + (result[2] * jongsung_len) + jong - 1
        ]




if len(argv) < 2:
  print ('[*] Usage: python dokkebi_han.py <INPUT>')
  exit()

print(chosung_len)
print(jungsung_len)

input_data  = argv[1]
FONT_TYPE   = 0
FONT_BBALE  = 0

width = 16
height = width

font_name = "HEBaram"+bbale_name_eng[FONT_BBALE]+type_name_eng[FONT_TYPE]
font_name_kor = "HE바람"+bbale_name[FONT_BBALE]+type_name[FONT_TYPE]


outFile = open(font_name+".json",'w',encoding='utf-8')

fp = open(input_data , 'rb')

printf("{")
printf("	\"version\": 1.1,\n")
printf("	\"attr\": {")
printf("		\"name\": \""+font_name_kor+"\",\n")
printf("		\"psname\": \""+font_name+"\",\n")
printf("		\"style\": \"regular\",\n")
printf("		\"author\": \"Taeyun An (WindowsTiger)\",\n")
printf("		\"licence\": \"SIL Open Font License 1.1\",\n")
printf("		\"widthType\": \"monospace\",\n")
printf("		\"fixedWidth\": 8,\n")
printf("		\"spaceWidth\": 8,\n")
printf("		\"letterSpacing\": 1,\n")
printf("		\"descent\": 0,\n")
printf("		\"ascent\": 16,\n")
printf("		\"offsetX\": 0,\n")
printf("		\"lineGap\": 0,\n")
printf("		\"maxWidth\": 16\n")
printf("	},\n")
printf("	\"glyphs\": [\n")


# 영어

fp.seek(ENG_FONT_LIST[FONT_TYPE])

for i in range(len(CP437_list)):
    printf("\t\t{\n")
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

fp.seek(ENG_FONT_LIST[FONT_TYPE]+0x1000)

#원화기호 하드코딩
printf("\t\t{\n")
printf("\t\t\t\"unicode\": 8361,\n")
        
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

#전각띄어쓰기 하드코딩
printf("\t\t{\n")
printf("\t\t\t\"unicode\": 12288,\n") 
printf("\t\t\t\"advanceWidth\":16\n")
printf("\t\t},\n")

# 한글자모
            #ㄱ    ㄲ     ㄳ
jamo_list2=[57344, 57345, 57510,
            #ㄴ    ㄵ     ㄶ
            57346, 57512, 57513,
            #ㄷ    ㄸ
            57347, 57348,
            #ㄹ	   ㄺ	   ㄻ	   ㄼ	   ㄽ	   ㄾ	 ㄿ   ㅀ 
            57349, 57516, 57517, 57518, 57519, 57520, 57521, 57522,
            #ㅁ	   ㅂ	   ㅃ	   ㅄ	
            57350, 57351, 57352, 57525,
            #ㅅ	   ㅆ	  ㅇ 	  ㅈ	ㅉ	
            57353, 57354 57355, 57356, 57357,
            #ㅊ	   ㅋ	  ㅌ	  ㅍ	ㅎ
            57358, 57359, 573560, 573561, 573562]
for i in range(12593,12623):
    printf("\t\t{\n")
    printf("\t\t\t\"unicode\": " + str(i) + ",\n")
    printf("\t\t\t\"components\": [")
    printf(str(jamo_list2[i-12593])+"],\n")
    printf("\t\t\t\"advanceWidth\":16\n")
    printf("\t\t},\n")

moum_start=57785
for i in range(12623,12644):
    printf("\t\t{\n")
    printf("\t\t\t\"unicode\": " + str(i) + ",\n")
    printf("\t\t\t\"components\": [")
    printf(str(moum_start+i-12623 - (0 if FONT_BBALE == 0 else 440))+"],\n")
    printf("\t\t\t\"advanceWidth\":16\n")
    printf("\t\t},\n")


for i in range(44032,55204):
    printf("\t\t{\n")
    printf("\t\t\t\"unicode\": " + str(i) + ",\n")
    printf("\t\t\t\"components\": ")
    printf(str(UTF2CJJ(i))+"\n")
    printf("\t\t},\n")

# 한글
fp.seek(KOR_FONT_LIST[FONT_TYPE])
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


printf("		{\n")
printf("			\"name\": \".notdef\",\n")
printf("			\"unicode\": 0,\n")
printf("			\"data\": [\n")
printf("				\"################\",\n")
printf("				\"##............##\",\n")
printf("				\"#.#..........#.#\",\n")
printf("				\"#..#........#..#\",\n")
printf("				\"#...#......#...#\",\n")
printf("				\"#....#....#....#\",\n")
printf("				\"#.....#..#.....#\",\n")
printf("				\"#......##......#\",\n")
printf("				\"#......##......#\",\n")
printf("				\"#.....#..#.....#\",\n")
printf("				\"#....#....#....#\",\n")
printf("				\"#...#......#...#\",\n")
printf("				\"#..#........#..#\",\n")
printf("				\"#.#..........#.#\",\n")
printf("				\"##............##\",\n")
printf("				\"################\"\n")
printf("			]\n")
printf("		}\n")
printf("\t]\n")
printf("}\n")
