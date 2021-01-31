import  re



def normalize(text):
    text = re.sub(r"(\W)", '_', text)
    alphabet = {ord('а'): 'a', ord('A'): 'A',
            ord('б'): 'b', ord('Б'): 'B',
            ord('в'): 'v', ord('В'): 'V',
            ord('г'): 'g', ord('Г'): 'G',
            ord('д'): 'd', ord('Д'): 'D',
            ord('е'): 'e', ord('Е'): 'E',
            ord('ё'): 'yo', ord('Ё'): 'Yo',
            ord('ж'): 'zh', ord('Ж'): 'Zh',
            ord('з'): 'z', ord('З'): 'Z',
            ord('и'): 'i', ord('И'): 'I',
            ord('й'): 'j', ord('Й'): 'J',
            ord('к'): 'k', ord('К'): 'K',
            ord('л'): 'l', ord('Л'): 'L',
            ord('м'): 'm', ord('М'): 'M',
            ord('н'): 'n', ord('Н'): 'N',
            ord('о'): 'o', ord('О'): 'O',
            ord('п'): 'p', ord('П'): 'P',
            ord('р'): 'r', ord('Р'): 'R',
            ord('с'): 's', ord('С'): 'S',
            ord('т'): 't', ord('Т'): 'T',
            ord('у'): 'u', ord('У'): 'U',
            ord('ф'): 'f', ord('Ф'): 'F',
            ord('х'): 'h', ord('Х'): 'H',
            ord('ц'): 'c', ord('Ц'): 'C',
            ord('ч'): 'ch', ord('Ч'): 'Ch',
            ord('ш'): 'sh',  ord('Ш'): 'Sh',
            ord('щ'): 'shch', ord('Щ'): 'Shch',
            ord('ъ'): "'", ord('ь'): '`',
            ord('ы'): 'y', ord('Ы'): 'Y',
            ord('э'): 'e', ord('Э'): 'E',
            ord('ю'): 'ju', ord('Ю'): 'Ju',
            ord('я'): 'ja', ord('Я'): 'Ja'}
    new_text = ''
    for letter in text:
        letter = letter.translate(alphabet)
        new_text += letter
    return new_text
