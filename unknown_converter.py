import pykakasi
from PIL import Image

u_table = {
    'a': "./static/material/unknown_A.jpg",
    'A': "./static/material/unknown_A.jpg",
    'b': "./static/material/unknown_B.jpg",
    'B': "./static/material/unknown_B.jpg",
    'c': "./static/material/unknown_C.jpg",
    'C': "./static/material/unknown_C.jpg",
    'd': "./static/material/unknown_D.jpg",
    'D': "./static/material/unknown_D.jpg",
    'e': "./static/material/unknown_E.jpg",
    'E': "./static/material/unknown_E.jpg",
    'f': "./static/material/unknown_F.jpg",
    'F': "./static/material/unknown_F.jpg",
    'g': "./static/material/unknown_G.jpg",
    'G': "./static/material/unknown_G.jpg",
    'h': "./static/material/unknown_H.jpg",
    'H': "./static/material/unknown_H.jpg",
    'i': "./static/material/unknown_I.jpg",
    'I': "./static/material/unknown_I.jpg",
    'j': "./static/material/unknown_J.jpg",
    'J': "./static/material/unknown_J.jpg",
    'k': "./static/material/unknown_K.jpg",
    'K': "./static/material/unknown_K.jpg",
    'l': "./static/material/unknown_L.jpg",
    'L': "./static/material/unknown_L.jpg",
    'm': "./static/material/unknown_M.jpg",
    'M': "./static/material/unknown_M.jpg",
    'n': "./static/material/unknown_N.jpg",
    'N': "./static/material/unknown_N.jpg",
    'o': "./static/material/unknown_O.jpg",
    'O': "./static/material/unknown_O.jpg",
    'p': "./static/material/unknown_P.jpg",
    'P': "./static/material/unknown_P.jpg",
    'q': "./static/material/unknown_Q.jpg",
    'Q': "./static/material/unknown_Qjpg",
    'r': "./static/material/unknown_R.jpg",
    'R': "./static/material/unknown_R.jpg",
    's': "./static/material/unknown_S.jpg",
    'S': "./static/material/unknown_S.jpg",
    't': "./static/material/unknown_T.jpg",
    'T': "./static/material/unknown_T.jpg",
    'u': "./static/material/unknown_U.jpg",
    'U': "./static/material/unknown_U.jpg",
    'v': "./static/material/unknown_V.jpg",
    'V': "./static/material/unknown_V.jpg",
    'w': "./static/material/unknown_W.jpg",
    'W': "./static/material/unknown_W.jpg",
    'x': "./static/material/unknown_X.jpg",
    'X': "./static/material/unknown_X.jpg",
    'y': "./static/material/unknown_Y.jpg",
    'Y': "./static/material/unknown_Y.jpg",
    'z': "./static/material/unknown_Z.jpg",
    'Z': "./static/material/unknown_Z.jpg",
    '!': "./static/material/unknown_!.jpg",
    '?': "./static/material/unknown_?.jpg",
    ' ': "./static/material/space.jpg",
    '　': "./static/material/space.jpg"
}
def mean(a):
    return u_table[a]
    
def convert(text):
    kakasi = pykakasi.kakasi()
    kakasi.setMode('H','a')
    kakasi.setMode('K','a')
    kakasi.setMode('J','a')
    #kakasi.setMode('s',True)

    conv = kakasi.getConverter()
    result = conv.do(text) #変換された文字を格納

    img = Image.open('./static/material/space.jpg')
    width,height = img.size
    img = None #ガベコレ
    whole_width = width * len(result)
    whole_height = height * 1
    unknown_img = Image.new('RGB',(whole_width,whole_height))
    #とりあえず１行で出力
    count = 0
    for a in result:
        path = mean(a)
        img = Image.open(path)
        for y in range(height):
            for x in range(width):
                unknown_img.putpixel((x + count * width,y),img.getpixel((x,y)))
        count += 1
    return unknown_img
