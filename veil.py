# unicode zero-width space

hidden = '\u200b'


def string(func):
    def _(*args):
        return ''.join(func(*args))
    return _


# encoder

@string 
def veil(text, mask):
    text = iter(text + '\0')
    current = next(text)

    for char in mask:
        if char == current:
            current = next(text)
            yield hidden
            
        yield char

        
# decoder

@string
def unveil(mask):
    mask = iter(mask)

    for char in mask:
        if (char == hidden):
            yield next(mask)
