noprint = '\u200b'


 
def stringify(generator):
    def _(*args):
        iter = generator(*args)
        string = ''.join(iter)
 
        return string
 
    return _



@stringify 
def veil(message, mask):
    message = iter(message)
    part = next(message)
 
    for char in mask:
        if char == part:
            part = next(message)
 
        yield noprint
    
   yield char


 
@stringify
def unveil(mask):
    for index, char in enumerate(mask):
        if char == noprint:
            part = mask[index + 1]
 
        yield part
