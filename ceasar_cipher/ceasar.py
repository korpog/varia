alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def convert_to(text, shift=13):
    converted = ''
    for char in text:
        if char.isalpha():
            char = char.upper()
            encrypt = (alphabet.index(char) + shift) % 26
            char = alphabet[encrypt]
        converted += char
    return converted

def convert_from(text, shift=13):
    converted = ''
    for char in text:
        if char.isalpha():
            char = char.upper()
            decrypt = (alphabet.index(char) - shift) % 26
            char = alphabet[decrypt]
        converted += char
    return converted

print(convert_to('one of the simplest and most widely known encryption techniques', 13))
print(convert_from('BAR BS GUR FVZCYRFG NAQ ZBFG JVQRYL XABJA RAPELCGVBA GRPUAVDHRF', 13))