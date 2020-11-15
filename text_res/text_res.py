def dev():
    print("Stub for developing applications")
    input()

def transcript():
    word=input("Enter your word to transcript: ")
    input_lang=input("Enter input language (ru or en): ")
    output_lang=input("Enter output language (ru or en): ")
    if input_lang=="en" and output_lang=="ru":
        print("In future.")
    if input_lang=="ru" and output_lang=="en":
        ru_to_en={
                'а':'a',
                'б':'b',
                'в':'v',
                'г':'g',
                'д':'d',
                'е':'e',
                'ё':'jo',
                'ж':'zh',
                'з':'z',
                'и':'i',
                'й':'i',
                'к':'k',
                'л':'l',
                'м':'m',
                'н':'n',
                'о':'o',
                'п':'p',
                'р':'r',
                'с':'s',
                'т':'t',
                'у':'u',
                'ф':'f',
                'х':'x',
                'ц':'c',
                'ч':'ch',
                'ш':'sh',
                'щ':'sh',
                'ъ':'"',
                'ы':'i',
                'ь':"'",
                'э':'e',
                'ю':'ju',
                'я':'ja',
                ' ':' '
                }
        def encrypt(word):
            cipher = ''
            for letter in word:
                if letter != ' ':
                    cipher += ru_to_en[letter]
                else:
                    cipher += ' '
            return cipher
        print(encrypt(word))
        input()
