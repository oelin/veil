'''Tauveil, by Illuis <me.illuis@gmail.com>
 
Tauveil steganographically embeds an esoteric me with in a given cover text.
This is achived by placing non-printing characters at certain positions in
the cover. This effectively encodes where parts of the secret message are
located. As such the message may be extracted by locating these points; easy
for a computer, impossible for a human.'''
 
 
 
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
