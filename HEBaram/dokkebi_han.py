# -*- coding: utf-8 -*- 
from sys import argv, exit
from KS_hanja import KANJI_list
import math

PUA_start=57344

KOR_FONT_LIST = [0x40000, 0x47180, 0x4E300, 0x55480, 0x5C600, 0x63780, 0x6A900, 0x71A80]
ENG_FONT_LIST = [0x0, 0x1000, 0x2000, 0x3000, 0x4000, 0x5000, 0x6000, 0x7000]
FONT_TYPE=1

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



    return [1 if jong == 0 else 0, jongTypes[jung]]


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
        return [PUA_start + chojung + result[0]*chosung_len*jungsung_len,
            PUA_start + chosung_len*jungsung_len*2 + jong * 2 +result[1]
        ]
    else:
        return [PUA_start + chojung + result[0]*chosung_len*jungsung_len]




if len(argv) < 2:
  print ('[*] Usage: python dokkebi_han.py <INPUT>')
  exit()

print(chosung_len)
print(jungsung_len)

input_data  = argv[1]
width = 16
height = width

font_name = "HEBaram"
font_name_kor = "HE바람"


outFile = open(font_name+".json",'w',encoding='utf-8')

fp = open(input_data , 'rb')

printf("{")
printf("	\"version\": 1,\n")
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

CP437_list = "\x00☺☻♥♦♣♠•◘○◙♂♀♪♫☼►◄↕‼¶§▬↨↑↓→←∟↔▲▼ !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\x5C]^_`abcdefghijklmnopqrstuvwxyz{|}~⌂ÇüéâäàåçêëèïîìÄÅÉæÆôöòûùÿÖÜ¢£¥₧ƒáíóúñÑªº¿⌐¬½¼¡«»░▒▓│┤╡╢╖╕╣║╗╝╜╛┐└┴┬├─┼╞╟╚╔╩╦╠═╬╧╨╤╥╙╘╒╓╫╪┘┌█▄▌▐▀αßΓπΣσµτΦΘΩδ∞φε∩≡±≥≤⌠⌡÷≈°∙·√ⁿ²■\xA0"

fp.seek(ENG_FONT_LIST[FONT_TYPE])

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

fp.seek(ENG_FONT_LIST[FONT_TYPE]+0x85C0)

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
        
#data print   
printf("\t\t\t\"advanceWidth\":16\n")
printf("\t\t},\n")

# SPC1

fp.seek(0x10000)
SPC_list = "!☺☻!♦!!•◘!◙!!!♫☼►◄!‼!!▬↨!!!!∟!!!!!!!!!!!!⌐¬!!!!!░▒▓!!╡╢╖╕╣║╗╝╜╛!!!!!!!╞╟╚╔╩╦╠═╬╧╨╤╥╙╘╒╓╫╪!!█▄▌▐▀!!!!!!!!!!!!!!!!!!!!⌠⌡!≈!∙↵!!!!!"


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

#SPC2
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


# 바람특수문자

fp.seek(0x78C00)
BRAM_list = "！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！🄀⒈⒉⒊⒋⒌⒍⒎⒏⒐！！！！！！𝟬𝟭𝟮𝟯𝟰𝟱𝟲𝟳𝟴𝟵𝗔𝗕𝗖𝗗𝗘𝗙𝝰𝝱！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！🐁📱⚡🖶！！！💡🔍📧®✏！🛑⚠⌛⏰！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！🅀🅆🄴🅁🅃🅈🅄🄸🄾🄿！！！！！！！！！！！！！！！！🄰🅂🄳🄵🄶🄷🄹🄺🄻！！！！！！！！！！！！！！！！！🅉🅇🄲🅅🄱🄽🄼！！！！！！！！⍐！！！！！！！！！！！！！！！！！！！！！！！！⍇⍗⍈！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！"


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

        

KSG_list = "☺、。·‥…¨〃­―∥＼∼‘’“”〔〕〈〉《》「」『』【】±×÷≠≤≥∞∴°′″℃Å￠￡￥♂♀∠⊥⌒∂∇≡≒§※☆★○●◎◇◆□■△▲▽▼→←↑↓↔〓≪≫√∽∝∵∫∬∈∋⊆⊇⊂⊃∪∩∧∨￢⇒⇔∀∃´～ˇ˘˝˚˙¸˛¡¿ː∮∑∏¤℉‰◁◀▷▶♤♠♡♥♧♣⊙◈▣◐◑▤▥▨▧▦▩♨☏☎☜☞¶†‡↕↗↙↖↘♭♩♪♬㉿㈜№㏇™㏂㏘℡☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺！＂＃＄％＆＇（）＊＋，－．／０１２３４５６７８９：；＜＝＞？＠ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ［￦］＾＿｀ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ｛｜｝￣ﾡﾢﾣﾤﾥﾦﾧﾨﾩﾪﾫﾬﾭﾮﾯﾰﾱﾲﾳﾴﾵﾶﾷﾸﾹﾺﾻﾼﾽﾾￂￃￄￅￆￇￊￋￌￍￎￏￒￓￔￕￖￗￚￛￜㅤㅥㅦㅧㅨㅩㅪㅫㅬㅭㅮㅯㅰㅱㅲㅳㅴㅵㅶㅷㅸㅹㅺㅻㅼㅽㅾㅿㆀㆁㆂㆃㆄㆅㆆㆇㆈㆉㆊㆋㆌㆍㆎⅰⅱⅲⅳⅴⅵⅶⅷⅸⅹ☺☺☺☺☺ⅠⅡⅢⅣⅤⅥⅦⅧⅨⅩ☺☺☺☺☺☺☺ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ☺☺☺☺☺☺☺☺αβγδεζηθικλμνξοπρστυφχψω☺☺☺☺☺☺─│┌┐┘└├┬┤┴┼━┃┏┓┛┗┣┳┫┻╋┠┯┨┷┿┝┰┥┸╂┒┑┚┙┖┕┎┍┞┟┡┢┦┧┩┪┭┮┱┲┵┶┹┺┽┾╀╁╃╄╅╆╇╈╉╊☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺㎕㎖㎗ℓ㎘㏄㎣㎤㎥㎦㎙㎚㎛㎜㎝㎞㎟㎠㎡㎢㏊㎍㎎㎏㏏㎈㎉㏈㎧㎨㎰㎱㎲㎳㎴㎵㎶㎷㎸㎹㎀㎁㎂㎃㎄㎺㎻㎼㎽㎾㎿㎐㎑㎒㎓㎔Ω㏀㏁㎊㎋㎌㏖㏅㎭㎮㎯㏛㎩㎪㎫㎬㏝㏐㏓㏃㏉㏜㏆☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺ÆÐªĦ☺Ĳ☺ĿŁØŒºÞŦŊ☺㉠㉡㉢㉣㉤㉥㉦㉧㉨㉩㉪㉫㉬㉭㉮㉯㉰㉱㉲㉳㉴㉵㉶㉷㉸㉹㉺㉻ⓐⓑⓒⓓⓔⓕⓖⓗⓘⓙⓚⓛⓜⓝⓞⓟⓠⓡⓢⓣⓤⓥⓦⓧⓨⓩ①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮½⅓⅔¼¾⅛⅜⅝⅞æđðħıĳĸŀłøœßþŧŋŉ㈀㈁㈂㈃㈄㈅㈆㈇㈈㈉㈊㈋㈌㈍㈎㈏㈐㈑㈒㈓㈔㈕㈖㈗㈘㈙㈚㈛⒜⒝⒞⒟⒠⒡⒢⒣⒤⒥⒦⒧⒨⒩⒪⒫⒬⒭⒮⒯⒰⒱⒲⒳⒴⒵⑴⑵⑶⑷⑸⑹⑺⑻⑼⑽⑾⑿⒀⒁⒂¹²³⁴ⁿ₁₂₃₄ぁあぃいぅうぇえぉおかがきぎくぐけげこごさざしじすずせぜそぞただちぢっつづてでとどなにぬねのはばぱひびぴふぶぷへべぺほぼぽまみむめもゃやゅゆょよらりるれろゎわゐゑをん☺☺☺☺☺☺☺☺☺☺☺ァアィイゥウェエォオカガキギクグケゲコゴサザシジスズセゼソゾタダチヂッツヅテデトドナニヌネノハバパヒビピフブプヘベペホボポマミムメモャヤュユョヨラリルレロヮワヰヱヲンヴヵヶ☺☺☺☺☺☺☺☺АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
fp.seek(0x11000)

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
fp.seek(0x19D00)

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
jamo_list2=[57806, 57828, 58230,
            #ㄴ    ㄵ     ㄶ
            57850, 58234, 58236,
            #ㄷ    ㄸ
            57872, 57894,
            #ㄹ	   ㄺ	   ㄻ	   ㄼ	   ㄽ	   ㄾ	 ㄿ   ㅀ 
            57916, 58242, 58244, 58246, 58248, 58250, 58252, 58254,
            #ㅁ	   ㅂ	   ㅃ	   ㅄ	
            57938, 57960, 57982, 58260,
            #ㅅ	   ㅆ	  ㅇ 	  ㅈ	ㅉ	
            58004, 58026, 58048, 58070, 58092,
            #ㅊ	   ㅋ	  ㅌ	  ㅍ	ㅎ
            58114, 58136, 58158, 58180, 58202]
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
    printf(str(moum_start+i-12623)+"],\n")
    printf("\t\t\t\"advanceWidth\":16\n")
    printf("\t\t},\n")


# 한글

fp.seek(KOR_FONT_LIST[FONT_TYPE])
max_sybal=(chosung_len*jungsung_len*2) + (jongsung_len*2)
for i in range(max_sybal):

    current = 0
    if i < (chosung_len*jungsung_len*2):
        current = 1
    elif i < max_sybal:
        current = 3
    
    printf("\t\t{\n")
    printf("\t\t\t\"unicode\": " + str(i + PUA_start) + ",\n")
    
    #data print        
    printf("\t\t\t\"data\": [\n")
    height_kor = 8 if current == 3 else 16
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
