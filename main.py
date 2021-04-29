try:
    from googletrans import Translator
    error = False
except:
    print('Cannot import the module needed for random latin words; therefore, you can\'t use it. Try installimg it or just use the offline version.')
    error = True
from random import choice

abcd = 'abcdefghijklmnopqrstuvwxyz '
replace_list = {'a':'4',
                'b':'6',
                'c':'(',
                'd':'d',
                'e':'e',
                'f':'f',
                'g':'9',
                'h':'h',
                'i':'| 1 !',
                'j':']',
                'k':'k',
                'l':'7',
                'm':'m',
                'n':'^',
                'o':'0',
                'p':'p',
                'q':'q',
                'r':'r',
                's':'$',
                't':'t',
                'u':'u',
                'v':'v',
                'w':'w',
                'x':'8',
                'y':'y',
                'z':'2',
                '1':'1',
                '2':'2',
                '3':'3',
                '4':'4',
                '5':'5',
                '6':'6',
                '7':'7',
                '8':'8',
                '9':'9',
                '0':'0'}
def only_alphabet(string):
    res = ''
    for i in string:
        if i.lower() in abcd:
            res += i
    return res

def get_words(string):
    string = only_alphabet(string).split(' ')
    return string

def translate_to_latin(word):
    trans = Translator().translate(word,
                                   src='en',
                                   dest='latin')
    return trans.text

def rand_replace(word):
    word = word.lower()
    res = ''
    for i in word:
        replace = choice([True,False])
        if replace:
            res += choice(replace_list[i].split(' '))
        else:
            res += i
    return res

def rand_trans(words):
    res = ''
    for i in words:
        do = choice([True,True,False])
        if do:
            res += translate_to_latin(i)
        else:
            res += i
    return res

def offline_generate(string):
    words = get_words(string)
    string = ''
    for i in words:
        string += i
    string = rand_replace(string)
    return string

def online_generate(string):
    string = rand_replace(rand_trans(get_words(sentence)))
    return string

if __name__ == '__main__':
    opt = input('Offline/online> ').lower()
    inpt = 'Enter nickname(example: The dark adam)> '
    if error and opt == 'online':
        print('You cannot use the online version for now.')
        exit()

    if error or opt == 'offline':
        sentence = input(inpt)
        print(offline_generate(string))
    elif opt == 'online':
        sentence = input(inpt)
        print(online_generate(sentence))
    else:
        print('No valid option was selected.')
