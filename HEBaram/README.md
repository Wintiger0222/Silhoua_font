# HE바람
1993년 DOS 한글 입출력 프로그램 한글 바람 3.0의 폰트입니다.
## 폰트 지원범위
* ASCII문자 + 한글11172자 + KS X 1001 한자 및 특수문자 + 한글바람 특수문자를 지원합니다.

## 사용 도구
* [Pixel Font Maker](https://github.com/wintiger0222/pixel-font-maker) : 폰트 제작
* CrystalTile2

## 참조 폰트
* [바람시스템 한글바람 카드 한글롬](https://github.com/ika-musume/HangulCard_dumps/tree/main/BaramSystem_HangulBaram)

## PUA영역
### 바람 특수문자

| U+   | 0  | 1  | 2   | 3  | 4                            | 5                            | 6                            | 7                            | 8                            | 9                            | A                            | B                            | C                            | D                            | E  | F                            |
|------|----|----|-----|----|------------------------------|------------------------------|------------------------------|------------------------------|------------------------------|------------------------------|------------------------------|------------------------------|------------------------------|------------------------------|----|------------------------------|
| F000 | 한 | 글 | 바  | 람 |                              |                              |                              | ⒈𝟬                           |                              |                              |                              | (주                          | 주)                          | 바                           | 람 | 시                           |
| F010 | 스 | 템 |     |    |                              |                              |                              |                              |                              |                              |                              |                              |                              |                              |    |                              |
| F020 |    |    |     |    |                              |                              | ■<sup>[1](#footnote_1)</sup> | ■<sup>[1](#footnote_1)</sup> | ■<sup>[1](#footnote_1)</sup> | ■<sup>[1](#footnote_1)</sup> | ■<sup>[1](#footnote_1)</sup> | ■<sup>[1](#footnote_1)</sup> | ■<sup>[1](#footnote_1)</sup> | ■<sup>[1](#footnote_1)</sup> | 𝙑  | 𝗩                            |
| F030 | 🄀  | ⒈  | ⒉   | ⒊  | ⒋                            | ⒌                            | ⒍                            | ⒎                            | ⒏                            | ⒐                            | A.                           | B.                           | C.                           | D.                           | E. | F.                           |
| F040 | 𝟬  | 𝟭  | 𝟮   | 𝟯  | 𝟰                            | 𝟱                            | 𝟲                            | 𝟳                            | 𝟴                            | 𝟵                            | 𝗔                            | 𝗕                            | 𝗖                            | 𝗗                            | 𝗘  | 𝗙                            |
| F050 | 𝝰  | 𝝱  | ｜■ | ｜ | [                            | ■｜                          | ⏮                            | ▶                            | ◀                            | ⏭                            | ▛                            | ▀                            | ▜                            | ▌                            | ▐  | ▙                            |
| F060 | ▅  | ▟  | ｜■ | ｜ | [                            | ■｜                          | ⏮                            | ▶                            | ◀                            | ⏭                            | ▛                            | ▀                            | ▜                            | ▌                            | ▐  | ▙                            |
| F070 | ▅  | ▟  | ╔   | ╦  | ═                            | ╦                            | ╗                            | ╠                            | ╬                            | ═                            | ╩                            | ╣                            | ╚                            | ╩                            | ═  | ╩                            |
| F080 | ╝  | ║  | ║   | 🐁  | 📱                            | ⚡                            | 🖶                            | ON                           | OFF                          | 💡<sup>[7](#footnote_7)</sup> | 💡<sup>[7](#footnote_7)</sup> | 🔍                            | 📧                            | ®                            | ✏  | □<sup>[8](#footnote_8)</sup> |
| F090 | 🛑  | ⚠  | ⌛   | ⏰  | ■<sup>[2](#footnote_2)</sup> | ■<sup>[3](#footnote_3)</sup> | ■<sup>[4](#footnote_4)</sup> | ■<sup>[5](#footnote_5)</sup> | ■<sup>[6](#footnote_6)</sup> |                              |                              |                              |                              |                              |    |                              |

### 키보드 글쇠 문자

| U+   | 9   | A  | B   | C   | D   | E   | F   | 0     | 1     | 2   | 3    | 4   | 5   | 6   | 7   | 8   |
|------|-----|----|-----|-----|-----|-----|-----|-------|-------|-----|------|-----|-----|-----|-----|-----|
| F099 | [ES | C] | [CT | RL] | [AL | t]  | [↑S | hift] | [shif | t↑] | [한/ | 영] | [한 | 자] | [s  | pa  |
| F0A9 | c   | e] | [Ta | b↹] | [RE | T]  | [F  | 1]    | [F    | 2]  | [F   | 3]  | [F  | 4]  | [F  | 5]  |
| F0B9 | [F  | 6] | [F  | 7]  | [F  | 8]  | [F  | 9]    | [F    | 10] | [F   | 11] | [F  | 12] | [`  | `]  |
| F0C9 | [=  | =] | [+  | +]  | [-  | -]  | [*  | *]    | [/    | /]  | [%   | %]  | [＼ | ＼] | [HO | ME] |
| F0D9 | [EN | D] | [PG | UP] | [PG | DN] | [IN | S]    | [DE   | L]  | [Prt | sc] |     |     |     |     |

| U+   | 0 | 1    | 2     | 3    | 4    | 5    | 6   | 7    | 8    | 9    | A    | B   | C    | D     | E     | F     | 10 | 11   | 12   | 13   | 14 | 15   | 16   | 17    | 18   | 19 |
|------|---|------|-------|------|------|------|-----|------|------|------|------|-----|------|-------|-------|-------|----|------|------|------|----|------|------|-------|------|----|
| F0E5 | ╔ | ═    | ═     | ═    | ═    | ═    | ═   | ═    | ═    | ═    | ═    | ═   | ═    | ═     | ═     | ═     | ═  | ═    | ═    | ═    | ═  | ═    | ═    | ═     | ═    | ╗  |
| F0FF | ║ | ■<sup>[1](#footnote_1)</sup>    | ■<sup>[1](#footnote_1)</sup>     |      |      |      |     |      |      |      |      |     |      |       |       |       |    |      |      |      |    |      |      |       |      | ║  |
| F119 | ║ | [Es] | [F1]  | [F2] | [F3] | [F4] |     | [F5] | [F6] | [F7] | [F8] |     | [F9] | [F10] | [F11] | [F12] |    | [Ps] | [Sl] | [Pb] |    | [Num | ICa | psIS | crt] | ║  |
| F133 | ║ |      |       |      |      |      |     |      |      |      |      |     |      |       |       |       |    |      |      |      |    |      |      |       |      | ║  |
| F14D | ║ | [`]  | [1]   | [2]  | [3]  | [4]  | [5] | [6]  | [7]  | [8]  | [9]  | [0] | [-]  | [=]   | [←    | ─]    |    | [In] | [Hm] | [Pu] |    | [Nl] | [/]  | [*]   | [-]  | ║  |
| F167 | ║ | [Ta  | b↹]   | 🅀    | 🅆    | 🄴    | 🅁   | 🅃    | 🅈    | 🅄    | 🄸    | 🄾   | 🄿    | [{]   | [}]   | Π     |    | [De] | [En] | [Pd] |    | [7]  | [8]  | [9]   | [+]  | ║  |
| F181 | ║ | [Ca  | ps]   | 🄰    | 🅂    | 🄳    | 🄵   | 🄶    | 🄷    | 🄹    | 🄺    | 🄻   | [:]  | [']   | [Re   | t]    |    |      |      |      |    | [4]  | [5]  | [6]   | Ц    | ║  |
| F19B | ║ | [↑S  | hift] | 🅉    | 🅇    | 🄲    | 🅅   | 🄱    | 🄽    | 🄼    | [,]  | [.] | [/]  | [＼]  | [shif | t↑]   |    |      | ⍐    |      |    | [1]  | [2]  | [3]   | Π    | ║  |
| F1B5 | ║ | [Cr  | rl]   | [Al  | t]   | [    | =   | =    | =    | =    | =    | ]   | [한/ | 영]   | [한   | 자]   |    | ⍇    | ⍗    | ⍈    |    | [0   | 0]   | [.]   | [↵]  | ║  |
| F1CF | ╚ | ═    | ═     | ═    | ═    | ═    | ═   | ═    | ═    | ═    | ═    | ═   | ═    | ═     | ═     | ═     | ═  | ═    | ═    | ═    | ═  | ═    | ═    | ═     | ═    | ╝  |

### 삼보특수문자

| U+   | 0  | 1  | 2  | 3  | 4  | 5  | 6  | 7  | 8 | 9 | A | B | C | D | E | F |
|------|----|----|----|----|----|----|----|----|---|---|---|---|---|---|---|---|
| F700 |    | ☺  | ☻  | ♥  | ♦  | ♣  | ♠  | •  | ◘  | ○ | ◙ | ♂ | ♀ | ♪ | ♫ | ☼ |
| F710 | ►  | ◄  | ↕  | ‼  | ¶  | §  | ▬  | ↨  | ↑ | ↓ | → | ← | ∟ | ↔ | ▲ | ▼ |

| U+   | 0  | 1  | 2  | 3  | 4  | 5  | 6  | 7  | 8 | 9 | A | B | C | D | E | F |
|------|----|----|----|----|----|----|----|----|---|---|---|---|---|---|---|---|
| F7A0 | 日 | 月 | 火 | 水 | 木 | 金 | 土 | 年 | ☏ | ⌐ | ¬ | ½ | ¼ | ¡ | ~ | ■<sup>[1](#footnote_1)</sup> |
| F7B0 | ░  | ▒  | ▓  | │  | ┤  | ╡  | ╢  | ╖  | ╕ | ╣ | ║ | ╗ | ╝ | ╜ | ╛ | ┐ |
| F7C0 | └  | ┴  | ┬  | ├  | ─  | ┼  | ╞  | ╟  | ╚ | ╔ | ╩ | ╦ | ╠ | ═ | ╬ | ╧ |
| F7D0 | ╨  | ╤  | ╥  | ╙  | ╘  | ╒  | ╓  | ╫  | ╪ | ┘ | ┌ | █ | ▄ | ▌ | ▐ | ▀ |
| F7E0 | α  | ß  | Γ  | π  | Σ  | σ  | µ  | τ  | Φ | Θ | Ω | δ | ∞ | φ | ε | ∩ |
| F7F0 | ≡  | ±  | ≥  | ≤  | ⌠  | ⌡  | ÷  | ≈  | ° | ∙ | · | √ | ⁿ | ² | ■ |   |

### 확장아스키 반각문자

| U+   | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | A | B | C | D | E | F |
|------|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| F800 |   | ☺ | ☻ | ♥ | ♦ | ♣ | ♠ | • | ◘ | ○ | ◙ | ♂ | ♀ | ♪ | ♫ | ☼ |
| F810 | ► | ◄ | ↕ | ‼ | ¶ | § | ▬ | ↨ | ↑ | ↓ | → | ← | ∟ | ↔ | ▲ | ▼ |
| F870 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | ⌂ |
| F880 | Ç | ü | é | â | ä | à | å | ç | ê | ë | è | ï | î | ì | Ä | Å |
| F890 | É | æ | Æ | ô | ö | ò | û | ù | ÿ | Ö | Ü | ¢ | £ | ¥ | ₧ | ƒ |
| F8A0 | á | í | ó | ú | ñ | Ñ | ª | º | ¿ | ⌐ | ¬ | ½ | ¼ | ¡ | « | » |
| F8B0 | ░ | ▒ | ▓ | │ | ┤ | ╡ | ╢ | ╖ | ╕ | ╣ | ║ | ╗ | ╝ | ╜ | ╛ | ┐ |
| F8C0 | └ | ┴ | ┬ | ├ | ─ | ┼ | ╞ | ╟ | ╚ | ╔ | ╩ | ╦ | ╠ | ═ | ╬ | ╧ |
| F8D0 | ╨ | ╤ | ╥ | ╙ | ╘ | ╒ | ╓ | ╫ | ╪ | ┘ | ┌ | █ | ▄ | ▌ | ▐ | ▀ |
| F8E0 | α | ß | Γ | π | Σ | σ | µ | τ | Φ | Θ | Ω | δ | ∞ | φ | ε | ∩ |
| F8F0 | ≡ | ± | ≥ | ≤ | ⌠ | ⌡ | ÷ | ≈ | ° | ∙ | · | √ | ⁿ | ² | ■ |   |


* <a name="footnote_1">1</a>: 한글바람 로고
* <a name="footnote_2">2</a>: 금성사 로고
* <a name="footnote_3">3</a>: 삼성전자 구로고
* <a name="footnote_4">4</a>: 대우전자 로고
* <a name="footnote_5">5</a>: 삼보컴퓨터 구로고
* <a name="footnote_6">6</a>: 현대전자 로고
* <a name="footnote_7">7</a>: U+F089 켜진발광다이오드 / U+F08A 꺼진발광다이오드 
* <a name="footnote_8">8</a>: 지우개 그림글자

## 다운로드 

| 폰트이름 | 자형 | TTF |  WOFF2 |  BDF |
| ------- | ---- | ---- | ---- | ---- |
| HE바람네모명조체 | [보기](https://lsfont.quiple.dev/#https://wintiger0222.github.io/Silhoua_font/HEBaram/HEBaramNemoMyeongjoche.ttf)  | [다운로드](https://wintiger0222.github.io/Silhoua_font/HEBaram/HEBaramNemoMyeongjoche.ttf)   | [다운로드](https://wintiger0222.github.io/Silhoua_font/HEBaram/HEBaramNemoMyeongjoche.woff2)    | [다운로드](https://wintiger0222.github.io/Silhoua_font/HEBaram/HEBaramNemoMyeongjoche.bdf)    |
| HE바람네모고딕체 | [보기](https://lsfont.quiple.dev/#https://wintiger0222.github.io/Silhoua_font/HEBaram/HEBaramNemoGodikche.ttf)     | [다운로드](https://wintiger0222.github.io/Silhoua_font/HEBaram/HEBaramNemoGodikche.ttf)      | [다운로드](https://wintiger0222.github.io/Silhoua_font/HEBaram/HEBaramNemoGodikche.woff2)       | [다운로드](https://wintiger0222.github.io/Silhoua_font/HEBaram/HEBaramNemoGodikche.bdf)       |
| HE바람네모보석체 | [보기](https://lsfont.quiple.dev/#https://wintiger0222.github.io/Silhoua_font/HEBaram/HEBaramNemoBoseokche.ttf)    | [다운로드](https://wintiger0222.github.io/Silhoua_font/HEBaram/HEBaramNemoBoseokche.ttf)     | [다운로드](https://wintiger0222.github.io/Silhoua_font/HEBaram/HEBaramNemoBoseokche.woff2)      | [다운로드](https://wintiger0222.github.io/Silhoua_font/HEBaram/HEBaramNemoBoseokche.bdf)      |
| HE바람네모가는체 | [보기](https://lsfont.quiple.dev/#https://wintiger0222.github.io/Silhoua_font/HEBaram/HEBaramNemoSaemmulche.ttf)   | [다운로드](https://wintiger0222.github.io/Silhoua_font/HEBaram/HEBaramNemoSaemmulche.ttf)    | [다운로드](https://wintiger0222.github.io/Silhoua_font/HEBaram/HEBaramNemoSaemmulche.woff2)     | [다운로드](https://wintiger0222.github.io/Silhoua_font/HEBaram/HEBaramNemoSaemmulche.bdf)     |
| HE바람네모필기체 | [보기](https://lsfont.quiple.dev/#https://wintiger0222.github.io/Silhoua_font/HEBaram/HEBaramNemoPilgiche.ttf)     | [다운로드](https://wintiger0222.github.io/Silhoua_font/HEBaram/HEBaramNemoPilgiche.ttf)      | [다운로드](https://wintiger0222.github.io/Silhoua_font/HEBaram/HEBaramNemoPilgiche.woff2)       | [다운로드](https://wintiger0222.github.io/Silhoua_font/HEBaram/HEBaramNemoPilgiche.bdf)       |
| HE바람네모둥근체 | [보기](https://lsfont.quiple.dev/#https://wintiger0222.github.io/Silhoua_font/HEBaram/HEBaramNemoDunggeunche.ttf)  | [다운로드](https://wintiger0222.github.io/Silhoua_font/HEBaram/HEBaramNemoDunggeunche.ttf)   | [다운로드](https://wintiger0222.github.io/Silhoua_font/HEBaram/HEBaramNemoDunggeunche.woff2)    | [다운로드](https://wintiger0222.github.io/Silhoua_font/HEBaram/HEBaramNemoDunggeunche.bdf)    |
| HE바람네모샘물체 | [보기](https://lsfont.quiple.dev/#https://wintiger0222.github.io/Silhoua_font/HEBaram/HEBaramPpallaeSaemmulche.ttf)| [다운로드](https://wintiger0222.github.io/Silhoua_font/HEBaram/HEBaramPpallaeSaemmulche.ttf) | [다운로드](https://wintiger0222.github.io/Silhoua_font/HEBaram/HEBaramPpallaeSaemmulche.woff2)  | [다운로드](https://wintiger0222.github.io/Silhoua_font/HEBaram/HEBaramPpallaeSaemmulche.bdf)  |
| HE바람네모바람체 | [보기](https://lsfont.quiple.dev/#https://wintiger0222.github.io/Silhoua_font/HEBaram/HEBaramNemoBaramche.ttf)     | [다운로드](https://wintiger0222.github.io/Silhoua_font/HEBaram/HEBaramNemoBaramche.ttf)      | [다운로드](https://wintiger0222.github.io/Silhoua_font/HEBaram/HEBaramNemoBaramche.woff2)       | [다운로드](https://wintiger0222.github.io/Silhoua_font/HEBaram/HEBaramNemoBaramche.bdf)       |
| HE바람빨래명조체 | [보기](https://lsfont.quiple.dev/#https://wintiger0222.github.io/Silhoua_font/HEBaram/HEBaramPpallaeMyeongjoche.ttf)  | [다운로드](https://wintiger0222.github.io/Silhoua_font/HEBaram/HEBaramPpallaeMyeongjoche.ttf)   | [다운로드](https://wintiger0222.github.io/Silhoua_font/HEBaram/HEBaramPpallaeMyeongjoche.woff2)    | [다운로드](https://wintiger0222.github.io/Silhoua_font/HEBaram/HEBaramPpallaeMyeongjoche.bdf)    |
| HE바람빨래고딕체 | [보기](https://lsfont.quiple.dev/#https://wintiger0222.github.io/Silhoua_font/HEBaram/HEBaramPpallaeGodikche.ttf)     | [다운로드](https://wintiger0222.github.io/Silhoua_font/HEBaram/HEBaramPpallaeGodikche.ttf)      | [다운로드](https://wintiger0222.github.io/Silhoua_font/HEBaram/HEBaramPpallaeGodikche.woff2)       | [다운로드](https://wintiger0222.github.io/Silhoua_font/HEBaram/HEBaramPpallaeGodikche.bdf)       |
| HE바람빨래보석체 | [보기](https://lsfont.quiple.dev/#https://wintiger0222.github.io/Silhoua_font/HEBaram/HEBaramPpallaeBoseokche.ttf)    | [다운로드](https://wintiger0222.github.io/Silhoua_font/HEBaram/HEBaramPpallaeBoseokche.ttf)     | [다운로드](https://wintiger0222.github.io/Silhoua_font/HEBaram/HEBaramPpallaeBoseokche.woff2)      | [다운로드](https://wintiger0222.github.io/Silhoua_font/HEBaram/HEBaramPpallaeBoseokche.bdf)      |
| HE바람빨래가는체 | [보기](https://lsfont.quiple.dev/#https://wintiger0222.github.io/Silhoua_font/HEBaram/HEBaramPpallaeSaemmulche.ttf)   | [다운로드](https://wintiger0222.github.io/Silhoua_font/HEBaram/HEBaramPpallaeSaemmulche.ttf)    | [다운로드](https://wintiger0222.github.io/Silhoua_font/HEBaram/HEBaramPpallaeSaemmulche.woff2)     | [다운로드](https://wintiger0222.github.io/Silhoua_font/HEBaram/HEBaramPpallaeSaemmulche.bdf)     |
| HE바람빨래필기체 | [보기](https://lsfont.quiple.dev/#https://wintiger0222.github.io/Silhoua_font/HEBaram/HEBaramPpallaePilgiche.ttf)     | [다운로드](https://wintiger0222.github.io/Silhoua_font/HEBaram/HEBaramPpallaePilgiche.ttf)      | [다운로드](https://wintiger0222.github.io/Silhoua_font/HEBaram/HEBaramPpallaePilgiche.woff2)       | [다운로드](https://wintiger0222.github.io/Silhoua_font/HEBaram/HEBaramPpallaePilgiche.bdf)       |
| HE바람빨래둥근체 | [보기](https://lsfont.quiple.dev/#https://wintiger0222.github.io/Silhoua_font/HEBaram/HEBaramPpallaeDunggeunche.ttf)  | [다운로드](https://wintiger0222.github.io/Silhoua_font/HEBaram/HEBaramPpallaeDunggeunche.ttf)   | [다운로드](https://wintiger0222.github.io/Silhoua_font/HEBaram/HEBaramPpallaeDunggeunche.woff2)    | [다운로드](https://wintiger0222.github.io/Silhoua_font/HEBaram/HEBaramPpallaeDunggeunche.bdf)    |
| HE바람빨래샘물체 | [보기](https://lsfont.quiple.dev/#https://wintiger0222.github.io/Silhoua_font/HEBaram/HEBaramPpallaeSaemmulche.ttf)| [다운로드](https://wintiger0222.github.io/Silhoua_font/HEBaram/HEBaramPpallaeSaemmulche.ttf) | [다운로드](https://wintiger0222.github.io/Silhoua_font/HEBaram/HEBaramPpallaeSaemmulche.woff2)  | [다운로드](https://wintiger0222.github.io/Silhoua_font/HEBaram/HEBaramPpallaeSaemmulche.bdf)  |
| HE바람빨래바람체 | [보기](https://lsfont.quiple.dev/#https://wintiger0222.github.io/Silhoua_font/HEBaram/HEBaramPpallaeBaramche.ttf)     | [다운로드](https://wintiger0222.github.io/Silhoua_font/HEBaram/HEBaramPpallaeBaramche.ttf)      | [다운로드](https://wintiger0222.github.io/Silhoua_font/HEBaram/HEBaramPpallaeBaramche.woff2)       | [다운로드](https://wintiger0222.github.io/Silhoua_font/HEBaram/HEBaramPpallaeBaramche.bdf)       |

## 법적 사항
I do not claim any rights to the original raster binary data charsets, which this work is based on. Credit for these goes to their respective designers.

At least in the US and South Korea, the font file and code are copyrighted, but the font design cannot be copyrighted. And likewise in both countries, bitmap fonts in general cannot be copyrighted. See also: [#](https://int10h.org/oldschool-pc-fonts/readme/#legal_stuff), [#](http://kasanlaw.com/bbs/board.php?bo_table=sub04_2&wr_id=226) Also, HESinimun's outline (scalable) font file is purely my creation for the first time, so I own the copyright, and I do not claim any rights to the "font design".

나는 이 작업의 기반이 되는 원본 비트맵 폰트에 대한 어떠한 권리도 주장하지 않습니다. 이에 대한 공로는 해당 디자이너에게 돌아갑니다.

적어도 미국과 대한민국에서는 폰트 파일 및 코드는 저작권을 갖지만 서체 디자인은 저작권을 갖지 못합니다. 그리고 마찬가지로 두 국가 모두에서 일반적으로 비트맵 폰트는 저작권을 갖지 못합니다. 윤곽선(스케일러블) 폰트가 아닌 비트맵 또는 그레이스케일 폰트 파일의 경우, 실질적으로 이미지 파일과 동일하므로 프로그램 저작물로서 보호되지 않습니다. 참조: [#](https://int10h.org/oldschool-pc-fonts/readme/#legal_stuff), [#](http://kasanlaw.com/bbs/board.php?bo_table=sub04_2&wr_id=226) 또한 HE바람의 윤곽선(스케일러블) 폰트 파일은 순전히 제가 처음 만든 것이기에 제게 저작권이 있고, 저는 ‘서체 디자인’에 대한 권리를 주장하지 않습니다.

## 이 프로젝트의 라이센스
Copyright © 2022 TaeYun An (WindowsTiger / 혜음우리말화연구소) (0xodbs02@naver.com), with reserved font name “HE바람” 시리즈.

HE바람 시리즈는 [SIL 오픈 폰트 라이선스 1.1](https://scripts.sil.org/cms/scripts/page.php?site_id=nrsi&id=OFL)에 따라 사용할 수 있으며, 폰트가 자체적으로 판매되지 않는 한 자유롭게 사용·연구·수정·재배포할 수 있습니다. 또한 어떠한 경우에도 저작권자는 계약·불법 행위 또는 기타 계약의 조치로 인한 일반·특수·간접·부수·결과적 손해를 포함하여 어떠한 청구·손해 또는 기타 책임도 지지 않습니다.

그리고 HE아현리를 수정하여 파생된 이차적 저작물 폰트는 이름에 ‘HE아현리’를 사용할 수 없으며, 다른 유형의 라이선스로 배포할 수 없습니다.

OFL 1.1을 한국어로 번역한 내용은 [이곳](LICENSE_ko.md)에서 확인할 수 있으며, 라이선스 원문은 [이곳](LICENSE.md)에서 확인할 수 있습니다.