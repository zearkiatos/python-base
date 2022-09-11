CHARACTER_NOT_ALLOW = [".", ","]
def clear_not_allow_text(text:str)->str:
    if text != '':
        for character in CHARACTER_NOT_ALLOW:
            text = text.replace(character, '')
    return text
def text_analyzer (text:str, allow_characters:list)->dict:
    text = clear_not_allow_text(text)
    if (text!=''):
        textArray = text.split(" ")
    else:
        textArray = ['']

    text_analyzed = []

    for word in textArray:
        for character in allow_characters:
            if character in list(word) and not word in text_analyzed:
                text_analyzed.append(word)
                break
    
    return sort(text_analyzed)

def sort(array:list, ascending:bool = True)->list:
    temp = ''
    for i in range(0, len(array)):
        for j in range(i, len(array)):
            if (ascending):
                if (array[i] > array[j]):
                    temp = array[i]
                    array[i] = array[j]
                    array[j] = temp
            else:
                if (array[i] < array[j]):
                    temp = array[i]
                    array[i] = array[j]
                    array[j] = temp
        
    return array




def get_characters ()->list:
    characters = ['ñ', 'á', 'é', 'í', 'ó', 'ú']
    for i in range(97, 122):
        characters.append(chr(i))
    
    return characters


allow_characters = []



text = ''
print(text_analyzer(text, allow_characters))