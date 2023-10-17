# -*- coding: utf-8 -*- 
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
  print ('[*] Usage: python dokkebi_han.py <ASCII> <HAN> <KSG> <SPC>')
  exit()

ASCII_FONT  = argv[1]
HAN_FONT  = argv[2]
KSG_FONT  = argv[3]
SPC_FONT  = argv[4]
start = 0
width = 16
height = width


outFile = open(HAN_FONT.split("\\")[-1].replace(("."+HAN_FONT.split('.')[-1]),'.json'),'w',encoding='utf-8')

printf("{")
printf("	\"version\": 1,\n")
printf("	\"attr\": {")
printf("		\"name\": \""+HAN_FONT.split("\\")[-1]+"\",\n")
printf("		\"psname\": \""+HAN_FONT.split("\\")[-1]+"\",\n")
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

CP437_list = "\x00☺☻♥♦♣♠•◘○◙♂♀♪♫☼►◄↕‼¶§▬↨↑↓→←∟↔▲▼ !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\x5C]^_`abcdefghijklmnopqrstuvwxyz{|}~⌂ÇüéâäàåçêëèïîìÄÅÉæÆôöòûùÿÖÜ¢£¥₧ƒáíóúñÑªº¿⌐¬½¼¡«»░▒▓│┤╡╢╖╕╣║╗╝╜╛┐└┴┬├─┼╞╟╚╔╩╦╠═╬╧╨╤╥╙╘╒╓╫╪┘┌█▄▌▐▀αßΓπΣσµτΦΘΩδ∞φε∩≡±≥≤⌠⌡÷≈°∙·√ⁿ²■\xA0"
fp = open(ASCII_FONT , 'rb')
fp.seek(start)

for i in range(len(CP437_list)):
    printf("\t\t{\n")
    if (i<0x20 or i>0x7f):
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
fp.close()

# 한글조합

for i in range(44032,57363):
    printf("\t\t{\n")
    printf("\t\t\t\"unicode\": " + str(i) + ",\n")
    printf("\t\t\t\"components\": ")
    printf(str(UTF2CJJ(i))+"\n")
    printf("\t\t},\n")


# 한글자모
jamo_list2=[57345, 57346, 57595, 57347, 57597, 57598, 57348, 57349, 57350, 57601, 57602, 57603, 57604, 57605, 57606, 57607, 57351, 57352, 57353, 57610, 57354, 57355, 57356, 57357, 57358, 57359, 57360, 57361, 57362, 57363, 57505, 57506, 57507, 57508, 57509, 57510, 57511, 57512, 57513, 57514, 57515, 57516, 57517, 57518, 57519, 57520, 57521, 57522, 57523, 57524, 57525]
for i in range(12593,12643):
    printf("\t\t{\n")
    printf("\t\t\t\"unicode\": " + str(i) + ",\n")
    printf("\t\t\t\"components\": [")
    printf(str(jamo_list2[i-12593])+"],\n")
    printf("\t\t\t\"advanceWidth\":16\n")
    printf("\t\t},\n")



# 한글

fp = open(HAN_FONT , 'rb')
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


# KSG

KSG_list = "☺、。·‥…¨〃­―∥＼∼‘’“”〔〕〈〉《》「」『』【】±×÷≠≤≥∞∴°′″℃Å￠￡￥♂♀∠⊥⌒∂∇≡≒§※☆★○●◎◇◆□■△▲▽▼→←↑↓↔〓≪≫√∽∝∵∫∬∈∋⊆⊇⊂⊃∪∩∧∨￢⇒⇔∀∃´～ˇ˘˝˚˙¸˛¡¿ː∮∑∏¤℉‰◁◀▷▶♤♠♡♥♧♣⊙◈▣◐◑▤▥▨▧▦▩♨☏☎☜☞¶†‡↕↗↙↖↘♭♩♪♬㉿㈜№㏇™㏂㏘℡！＂＃＄％＆＇（）＊＋，－．／０１２３４５６７８９：；＜＝＞？＠ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ［￦］＾＿｀ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ｛｜｝￣ﾡﾢﾣﾤﾥﾦﾧﾨﾩﾪﾫﾬﾭﾮﾯﾰﾱﾲﾳﾴﾵﾶﾷﾸﾹﾺﾻﾼﾽﾾￂￃￄￅￆￇￊￋￌￍￎￏￒￓￔￕￖￗￚￛￜㅤㅥㅦㅧㅨㅩㅪㅫㅬㅭㅮㅯㅰㅱㅲㅳㅴㅵㅶㅷㅸㅹㅺㅻㅼㅽㅾㅿㆀㆁㆂㆃㆄㆅㆆㆇㆈㆉㆊㆋㆌㆍㆎⅰⅱⅲⅳⅴⅵⅶⅷⅸⅹ☺☺☺☺☺ⅠⅡⅢⅣⅤⅥⅦⅧⅨⅩ☺☺☺☺☺☺☺ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ☺☺☺☺☺☺☺☺αβγδεζηθικλμνξοπρστυφχψω☺☺☺☺☺☺─│┌┐┘└├┬┤┴┼━┃┏┓┛┗┣┳┫┻╋┠┯┨┷┿┝┰┥┸╂┒┑┚┙┖┕┎┍┞┟┡┢┦┧┩┪┭┮┱┲┵┶┹┺┽┾╀╁╃╄╅╆╇╈╉╊㎕㎖㎗ℓ㎘㏄㎣㎤㎥㎦㎙㎚㎛㎜㎝㎞㎟㎠㎡㎢㏊㎍㎎㎏㏏㎈㎉㏈㎧㎨㎰㎱㎲㎳㎴㎵㎶㎷㎸㎹㎀㎁㎂㎃㎄㎺㎻㎼㎽㎾㎿㎐㎑㎒㎓㎔Ω㏀㏁㎊㎋㎌㏖㏅㎭㎮㎯㏛㎩㎪㎫㎬㏝㏐㏓㏃㏉㏜㏆☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺ÆÐªĦ☺Ĳ☺ĿŁØŒºÞŦŊ☺㉠㉡㉢㉣㉤㉥㉦㉧㉨㉩㉪㉫㉬㉭㉮㉯㉰㉱㉲㉳㉴㉵㉶㉷㉸㉹㉺㉻ⓐⓑⓒⓓⓔⓕⓖⓗⓘⓙⓚⓛⓜⓝⓞⓟⓠⓡⓢⓣⓤⓥⓦⓧⓨⓩ①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮½⅓⅔¼¾⅛⅜⅝⅞æđðħıĳĸŀłøœßþŧŋŉ㈀㈁㈂㈃㈄㈅㈆㈇㈈㈉㈊㈋㈌㈍㈎㈏㈐㈑㈒㈓㈔㈕㈖㈗㈘㈙㈚㈛⒜⒝⒞⒟⒠⒡⒢⒣⒤⒥⒦⒧⒨⒩⒪⒫⒬⒭⒮⒯⒰⒱⒲⒳⒴⒵⑴⑵⑶⑷⑸⑹⑺⑻⑼⑽⑾⑿⒀⒁⒂¹²³⁴ⁿ₁₂₃₄ぁあぃいぅうぇえぉおかがきぎくぐけげこごさざしじすずせぜそぞただちぢっつづてでとどなにぬねのはばぱひびぴふぶぷへべぺほぼぽまみむめもゃやゅゆょよらりるれろゎわゐゑをんァアィイゥウェエォオカガキギクグケゲコゴサザシジスズセゼソゾタダチヂッツヅテデトドナニヌネノハバパヒビピフブプヘベペホボポマミムメモャヤュユョヨラリルレロヮワヰヱヲンヴヵヶ☺☺☺☺☺☺☺☺☺☺☺АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ☺☺☺☺☺☺☺☺☺☺☺☺абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
fp = open(KSG_FONT , 'rb')
fp.seek(start)

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
fp.close()

# SPC

SPC_list = "!☺☻!♦!!•◘!◙!!!♫☼►◄!‼!!▬↨!!!!∟!!!!!!!!!!!!⌐¬!!!!!░▒▓!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!█▄▌▐▀!!!!!!!!!!!!!!!!!!!!⌠⌡!≈!∙!!!!!!"
fp = open(SPC_FONT , 'rb')
fp.seek(start)

for i in range(len(SPC_list)):
    if(SPC_list[i] == '!'):
        for h in range(height):
            for w in range(math.ceil(width/8)):
                fp.read(1)[0]
        continue
    printf("\t\t{\n")
    printf("\t\t\t\"unicode\": " + str(ord(SPC_list[i])) + ",\n")
    
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
fp.close()



# SPC2


fp = open(SPC_FONT , 'rb')
fp.seek(start)

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
    if(i<len(SPC_list)-1):
        printf("\t\t},\n")
    else:
        printf("\t\t}\n")

fp.close()

printf("\t]\n")
printf("}\n")
