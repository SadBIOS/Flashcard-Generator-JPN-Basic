import os
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

BASE_SIZE = 1000
MARGIN = 100
FONT_SIZE = 700

FONT_SANS_PATH = "your_sans_serif_font_of_choice.ttf"
FONT_SERIF_PATH = "your_serif_font_of_choice.ttf"

hiragana_char_array = [
    "あ", "い", "う", "え", "お",
    "か", "き", "く", "け", "こ",
    "さ", "し", "す", "せ", "そ",
    "た", "ち", "つ", "て", "と",
    "な", "に", "ぬ", "ね", "の",
    "は", "ひ", "ふ", "へ", "ほ",
    "ま", "み", "む", "め", "も",
    "や", "ゆ", "よ",
    "ら", "り", "る", "れ", "ろ",
    "わ", "を", "ん",
    "が", "ぎ", "ぐ", "げ", "ご",
    "ざ", "じ", "ず", "ぜ", "ぞ",
    "だ", "ぢ", "づ", "で", "ど",
    "ば", "び", "ぶ", "べ", "ぼ",
    "ぱ", "ぴ", "ぷ", "ぺ", "ぽ",
    "きゃ", "しゃ", "ちゃ", "にゃ", "ひゃ", "みゃ", "りゃ", "ぎゃ", "じゃ", "ぢゃ", "びゃ", "ぴゃ",
    "きゅ", "しゅ", "ちゅ", "にゅ", "ひゅ", "みゅ", "りゅ", "ぎゅ", "じゅ", "ぢゅ", "びゅ", "ぴゅ",
    "きょ", "しょ", "ちょ", "にょ", "ひょ", "みょ", "りょ", "ぎょ", "じょ", "ぢょ", "びょ", "ぴょ"
]

katakana_char_array = [
    "ア", "イ", "ウ", "エ", "オ",
    "カ", "キ", "ク", "ケ", "コ",
    "サ", "シ", "ス", "セ", "ソ",
    "タ", "チ", "ツ", "テ", "ト",
    "ナ", "ニ", "ヌ", "ネ", "ノ",
    "ハ", "ヒ", "フ", "ヘ", "ホ",
    "マ", "ミ", "ム", "メ", "モ",
    "ヤ", "ユ", "ヨ",
    "ラ", "リ", "ル", "レ", "ロ",
    "ワ", "ヲ", "ン",
    "ガ", "ギ", "グ", "ゲ", "ゴ",
    "ザ", "ジ", "ズ", "ゼ", "ゾ",
    "ダ", "ヂ", "ヅ", "デ", "ド",
    "バ", "ビ", "ブ", "ベ", "ボ",
    "パ", "ピ", "プ", "ペ", "ポ",
    "キャ", "シャ", "チャ", "ニャ", "ヒャ", "ミャ", "リャ", "ギャ", "ジャ", "ヂャ", "ビャ", "ピャ",
    "キュ", "シュ", "チュ", "ニュ", "ヒュ", "ミュ", "リュ", "ギュ", "ジュ", "ヂュ", "ビュ", "ピュ",
    "キョ", "ショ", "チョ", "ニョ", "ヒョ", "ミョ", "リョ", "ギョ", "ジョ", "ヂョ", "ビョ", "ピョ",
    "ヴ",
    "ヴァ", "ヴィ", "ヴェ", "ヴォ",
    "ウィ", "ウェ", "ウォ",
    "ファ", "フィ", "フェ", "フォ",
    "ツァ", "ツィ", "ツェ", "ツォ",
    "ティ", "ディ", "トゥ", "ドゥ",
    "ジェ", "チェ", "シェ"
]

folders = {
    "sans_serif_hiragana": "sans_serif_hiragana",
    "serif_hiragana": "serif_hiragana",
    "sans_serif_katakana": "sans_serif_katakana",
    "serif_katakana": "serif_katakana",
    "hiragana_combined": "hiragana_combined",
    "katakana_combined": "katakana_combined",
}

for folder in folders.values():
    os.makedirs(folder, exist_ok=True)

font_sans = ImageFont.truetype(FONT_SANS_PATH, FONT_SIZE)
font_serif = ImageFont.truetype(FONT_SERIF_PATH, FONT_SIZE)

def create_image(char, font, output_path):
    temp = Image.new("RGB", (BASE_SIZE, BASE_SIZE), "white")
    draw = ImageDraw.Draw(temp)

    bbox = draw.textbbox((0, 0), char, font=font)
    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]

    final_w = max(BASE_SIZE, text_w + 2 * MARGIN)
    final_h = BASE_SIZE

    img = Image.new("RGB", (final_w, final_h), "white")
    draw = ImageDraw.Draw(img)

    x = (final_w - text_w) // 2 - bbox[0]
    y = (final_h - text_h) // 2 - bbox[1]

    draw.text((x, y), char, fill="black", font=font)

    img.save(output_path)
    return img

def generate_set(char_array, prefix, folder, font):
    images = []
    for i, char in enumerate(char_array, start=1):
        path = os.path.join(folder, f"{i}_{prefix}.png")
        img = create_image(char, font, path)
        images.append(img)
    return images

def combine_images(img_list_1, img_list_2, folder, prefix):
    for i, (img1, img2) in enumerate(zip(img_list_1, img_list_2), start=1):
        w = img1.width + img2.width
        h = max(img1.height, img2.height)

        combined = Image.new("RGB", (w, h), "white")
        combined.paste(img1, (0, 0))
        combined.paste(img2, (img1.width, 0))

        combined.save(os.path.join(folder, f"{i}_{prefix}_com.png"))

hir_sans = generate_set(
    hiragana_char_array,
    "hir_san",
    folders["sans_serif_hiragana"],
    font_sans
)

hir_serif = generate_set(
    hiragana_char_array,
    "hir_ser",
    folders["serif_hiragana"],
    font_serif
)

combine_images(
    hir_serif,
    hir_sans,
    folders["hiragana_combined"],
    "hir"
)

kat_sans = generate_set(
    katakana_char_array,
    "kat_san",
    folders["sans_serif_katakana"],
    font_sans
)

kat_serif = generate_set(
    katakana_char_array,
    "kat_ser",
    folders["serif_katakana"],
    font_serif
)

combine_images(
    kat_serif,
    kat_sans,
    folders["katakana_combined"],
    "kat"
)

print("Done generating all images.")