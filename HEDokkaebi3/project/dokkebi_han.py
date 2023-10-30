# -*- coding: utf-8 -*- 
from sys import argv, exit
from text_list import CP437_list,CP437_list_2,SPC_list,KSG_list, KANJI_list
import math

PUA_start=57344

KOR_FONT_LIST = [0x30000, 0x35A30]
ENG_FONT_LIST = [0x3B460, 0x3CC60,0x3C460,0x3D460]
#3C220: 프린트 기호
#9D00:한자
#1000:KS특문
#20:삼보특문
type_name = ["명조체", "고딕체"]
bbale_name = ["네모", "빨래"]
type_name_eng = ["Myeongjoche", "Godikche"]
bbale_name_eng = ["Nemo", "Ppallae"]

#명조체
#고딕체
#세리프
#큰세리프
#고딕
#큰고딕

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

max_jamo = [1, 2, 2] #2x2벌
def HangulTemplate(cho, jung, jong):
    
                #    ㅏ ㅐ ㅑ ㅒ ㅓ ㅔ ㅕ ㅖ ㅗ ㅘ ㅙ ㅚ ㅛ ㅜ ㅝ ㅞ ㅟ ㅠ ㅡ ㅢ ㅣ
    jongTypes = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0];



    return [0 if (jong == 0 and FONT_BBALE != 1) else 1, jongTypes[jung]]


def UTF2CJJ(code):
    cho  = (code - ord('가'))//(21*28)
    jung = ((code - ord('가')) - ((21*28)*cho)) // 28
    jong = (code - ord('가')) - ((21*28)*cho) - 28*jung
    
    #공백포함
    cho = cho+1
    jung= jung+1

    result = HangulTemplate(cho, jung, jong)

    chojung = cho*jungsung_len+jung
    if jong != 0:
        return [PUA_start + chojung + (chosung_len-1)*jungsung_len,
            PUA_start + chosung_len*jungsung_len*2 - jungsung_len  + (jong-1) + result[1]*(jongsung_len-1)
        ]
    else:
        return [PUA_start + chojung]




if len(argv) < 2:
  print ('[*] Usage: python dokkebi_han.py <INPUT>')
  exit()

print(chosung_len)
print(jungsung_len)

input_data  = argv[1]
FONT_TYPE   = int(argv[2])
# FONT_BBALE  = int(argv[3])
FONT_BBALE  = 0

width = 16
height = width

font_name = "HEDokkaebi3"+bbale_name_eng[FONT_BBALE]+type_name_eng[FONT_TYPE]
font_name_kor = "HE도깨비3"+bbale_name[FONT_BBALE]+type_name[FONT_TYPE]


outFile = open(font_name+".json",'w',encoding='utf-8')

fp = open(input_data , 'rb')

printf("{")
printf("	\"version\": 10,\n")
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
    if (i<0x20 or i>=0x7f):
        printf("\t\t\t\"unicode\": " + str(0xF800+i) + ",\n")
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

# 확장 아스키 영역
## 사이에 쓰레기 문자열이 들어가 있어서 어쩔수 없이 분리함
## 또한 0x80부터는 하나가지고 전부 공유함
fp.seek(0x3BC60)
for i in range(len(CP437_list_2)):
    printf("\t\t{\n")
    if (CP437_list_2[i]=='!'):
        printf("\t\t\t\"unicode\": 0,\n")
    else:
        printf("\t\t\t\"unicode\": " + str(0xF880+i) + ",\n")
            
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


## 확장아스키 문자 링크
for i in range(len(CP437_list)):
    if (i<0x20 or i>=0x7f):
        printf("\t\t{\n")
        printf("\t\t\t\"unicode\": " + str(ord(CP437_list[i])) + ",\n")
        printf("\t\t\t\"components\": [" + str(0xF800+i) + "]\n")
        printf("\t\t},\n")
for i in range(len(CP437_list_2)):
    if(CP437_list_2[i]!='!'):
        printf("\t\t{\n")
        printf("\t\t\t\"unicode\": " + str(ord(CP437_list_2[i])) + ",\n")
        printf("\t\t\t\"components\": [" + str(0xF880+i) + "]\n")
        printf("\t\t},\n")

#전각띄어쓰기 하드코딩
printf("\t\t{\n")
printf("\t\t\t\"unicode\": 12288,\n") 
printf("\t\t\t\"advanceWidth\":16\n")
printf("\t\t},\n")

#삼보특수문자

fp.seek(0x20)
for i in range(len(SPC_list)):
    printf("\t\t{\n")
    if (i<0x20):
        printf("\t\t\t\"unicode\": " + str(0xF700+i) + ",\n")
    else:
        printf("\t\t\t\"unicode\": " + str(0xF780+i) + ",\n")
    
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

    printf("\t\t\t],\n")
    printf("\t\t\t\"advanceWidth\":16\n")
    printf("\t\t},\n")  

# 실제문자에 링크하기
for i in range(len(SPC_list)):
    if(SPC_list[i] == '!'):
        continue
    printf("\t\t{\n")
    printf("\t\t\t\"unicode\": " + str(ord(SPC_list[i])) + ",\n")
    if (i<0x20):
        printf("\t\t\t\"components\": [" + str(0xF700+i) + "],\n")
    else:
        printf("\t\t\t\"components\": [" + str(0xF780+i) + "],\n")
   
    printf("\t\t\t\"advanceWidth\":16\n")
    printf("\t\t},\n")

# 도깨비 특수문자

fp.seek(0x3C220)
BRAM_list = "！！！！！！！！！！！！！！！！"

for i in range(len(BRAM_list)):
    printf("\t\t{\n")
    printf("\t\t\t\"unicode\": " + str(0xF000+i) + ",\n")

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

    printf("\t\t\t],\n")
    printf("\t\t\t\"advanceWidth\":16\n")
    printf("\t\t},\n")  


for i in range(len(BRAM_list)):
    if(BRAM_list[i] == '！'):
        continue
    printf("\t\t{\n")
    printf("\t\t\t\"unicode\": " + str(ord(BRAM_list[i])) + ",\n")
    printf("\t\t\t\"components\": [" + str(0xF000+i) + "],\n")
    
    printf("\t\t\t\"advanceWidth\":16\n")
    printf("\t\t},\n")


## KS특수문자
fp.seek(0x1000)

for i in range(len(KSG_list)):
    if(KSG_list[i] == '☺'):
        for h in range(height):
            for w in range(math.ceil(width/8)):
                fp.read(1)[0]
        continue
    printf("\t\t{\n")
    printf("\t\t\t\"unicode\": " + str(ord(KSG_list[i])) + ",\n")
    
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

    printf("\t\t\t],\n")
    printf("\t\t\t\"advanceWidth\":16\n")
    printf("\t\t},\n")
  
#한자
fp.seek(0x9D00)

for i in range(len(KANJI_list)):
    if(KANJI_list[i] == '!'):
        for h in range(height):
            for w in range(math.ceil(width/8)):
                fp.read(1)[0]
        continue
    printf("\t\t{\n")
    printf("\t\t\t\"unicode\": " + str(ord(KANJI_list[i])) + ",\n")
    
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

    printf("\t\t\t],\n")
    printf("\t\t\t\"advanceWidth\":16\n")
    printf("\t\t},\n")

# 한글조합

for i in range(44032,55204):
    printf("\t\t{\n")
    printf("\t\t\t\"unicode\": " + str(i) + ",\n")
    printf("\t\t\t\"components\": ")
    printf(str(UTF2CJJ(i))+"\n")
    printf("\t\t},\n")


# 한글자모
            #ㄱ    ㄲ     ㄳ
jamo_list2=[57366, 57388, 58204,
            #ㄴ    ㄵ     ㄶ
            57410, 58206, 58207,
            #ㄷ    ㄸ
            57432, 57454,
            #ㄹ	   ㄺ	   ㄻ	   ㄼ	   ㄽ	   ㄾ	 ㄿ   ㅀ 
            57476, 58210, 58211, 58212, 58213, 58214, 58215, 58216,
            #ㅁ	   ㅂ	   ㅃ	   ㅄ	
            57498, 57520, 57542, 58219,
            #ㅅ	   ㅆ	  ㅇ 	  ㅈ	ㅉ	
            57564, 57586, 57608, 57630, 57652,
            #ㅊ	   ㅋ	  ㅌ	  ㅍ	ㅎ
            57674, 57696, 57718, 57740, 57762]
for i in range(12593,12623):
    printf("\t\t{\n")
    printf("\t\t\t\"unicode\": " + str(i) + ",\n")
    printf("\t\t\t\"components\": [")
    printf(str(jamo_list2[i-12593])+"],\n")
    printf("\t\t\t\"advanceWidth\":16\n")
    printf("\t\t},\n")

moum_start=57345 
for i in range(12623,12644):
    printf("\t\t{\n")
    printf("\t\t\t\"unicode\": " + str(i) + ",\n")
    printf("\t\t\t\"components\": [")
    printf(str(moum_start+i-12623)+"],\n")
    printf("\t\t\t\"advanceWidth\":16\n")
    printf("\t\t},\n")


# 한글

fp.seek(KOR_FONT_LIST[FONT_TYPE])
max_sybal=(chosung_len*jungsung_len) + ((chosung_len-1)*jungsung_len) + ((jongsung_len-1)*2)
for i in range(max_sybal):

    current = 0
    if i < (chosung_len*jungsung_len):
        current = 1
    elif i < (chosung_len*jungsung_len) + ((chosung_len-1)*jungsung_len):
        current = 2
    elif i < max_sybal:
        current = 3
    
    printf("\t\t{\n")
    printf("\t\t\t\"unicode\": " + str(i + PUA_start) + ",\n")
    
    #data print        
    printf("\t\t\t\"data\": [\n")
    if current == 1:
        height_kor = 16
    elif current == 2:
        height_kor = 10
    elif current == 3:
        height_kor = 6
    for h in range(height_kor):
        printf("\t\t\t\t\"")
        # horizon
        for w in range(math.ceil(width/8)):
            value = fp.read(1)[0]
            bin_val = format(value, 'b').zfill(8).replace('1','#').replace('0','.')
            printf(bin_val)

        if h < height_kor-1:
            printf("\",\n")
        else:
            printf("\"\n")
    if current == 2:
        printf(",\".\",\".\",\".\",\".\",\".\",\".\"")
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
