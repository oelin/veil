# veil.py, a textual steganography tool which uses non-printing
# spaces to embed esoteric messages with in a given mask text.



# The Unicode character at u+200b is a special non-printing
# (or zero width) space. It is invisible is most common text
# mediums. This allows information to be embedded with in a
# mask text while remaining visually identical.

noprint = '\u200b'



# A decorator which joins iterable function output into a single
# string.

def stringify(func):
    def _(*args):
        # Get the output of the given function. Call it with the
        # arguments given.
        
        output = func(*args)

        # Join the output into a string.
        
        string = ''.join(output)
 
        return string
 
    return _



# Embed (or hide) an esoteric message with in a given mask text.
# The mask text must contain the characters of the message in
# the same order, however they do not need to be adjacent.

@stringify 

def veil(text, mask):
    # Create an iterator from the given text. Python3 doesn't
    # really have C-style pointers, however, the `next()` method
    # can be used for similar purposes.
    
    text = iter(text + '\0')

    # Get the character at the current index in `text`. This
    # should be the first character initially.
    
    current = next(text)

    # Loop through each character in the given mask text.
 
    for char in mask:
        # Denote matching characters in `text` and `mask` with a
        # Unicode non-printing space (u+200b).
        
        if char == current:
            current = next(text)
 
            yield noprint
            
        yield char



# Reveal an esoteric message embedded within a given mask text.
# This function is essentially an inverse of `veil()`.

@stringify

def unveil(mask):
    # Create an iterator from the given mask text. Again, this
    # just helps avoid weird attempts to implement pointers.
    
    mask = iter(mask)

    for char in mask:
        # Check if the current character is a non-printing space.
        # If it is, we know the following character must be part
        # of the esoteric message.
        
        if (char == noprint):
            yield next(mask)
