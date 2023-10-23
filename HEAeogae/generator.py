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
    
    #                          ㄱ ㄲ ㄳ ㄴ ㄵ ㄶ ㄷ ㄹ ㄺ ㄻ ㄼ ㄽ ㄾ ㄿ ㅀ ㅁ ㅂ ㅄ ㅅ ㅆ ㅇ ㅈ ㅊ ㅋ ㅌ ㅍ ㅎ
    jongTypes =            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1];

    jungjong_t= jung*jongsung_len+jong
    cho_t= (cho*jungsung_len+jung) + jungsung_len*chosung_len*jongTypes[jong]
    
    return [cho_t, jungjong_t]


def UTF2CJJ(code):
    cho  = (code - ord('가'))//(21*28)
    jung = ((code - ord('가')) - ((21*28)*cho)) // 28
    jong = (code - ord('가')) - ((21*28)*cho) - 28*jung

    result = HangulTemplate(cho, jung, jong)

    return [PUA_start+jungsung_len*jongsung_len*2 + result[0], PUA_start+jungsung_len*jongsung_len + result[1]]




if len(argv) < 0:
  print ('[*] Usage: python dokkebi_han.py')
  exit()

outFile = open('output.json','w',encoding='utf-8')


for i in range(44032,55203):
    printf("\t\t{\n")
    printf("\t\t\t\"unicode\": " + str(i) + ",\n")
    printf("\t\t\t\"components\": ")
    printf(str(UTF2CJJ(i))+"\n")
    printf("\t\t},\n")

