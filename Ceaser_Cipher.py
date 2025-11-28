"""def caesar_cipher(string, offset):
    alphabet = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' ]
    
    encoded_string = ''

    for character in string:
        position = alphabet.index(character)
        offset_position = position - offset
    
        encoded_character =  alphabet[offset_position]
        encoded_string += encoded_character
    
    return encoded_string
        
    """
    
def caesar_cipher(string, offset, mode="encrypt"):
    
    alphabet = [
        'a','b','c','d','e','f','g','h','i','j','k','l','m',
        'n','o','p','q','r','s','t','u','v','w','x','y','z'
    ]
    
    encoded_string = ''

   
    if mode == "decrypt":
        offset = -offset

    for character in string:

    
        if character in alphabet:
            position = alphabet.index(character)
            offset_position = (position + offset) % 26
            encoded_character = alphabet[offset_position]
            encoded_string += encoded_character
        
        
        elif character.lower() in alphabet:
            position = alphabet.index(character.lower())
            offset_position = (position + offset) % 26
           
            encoded_character = alphabet[offset_position].upper()
            encoded_string += encoded_character

        
        else:
            encoded_string += character  

    return encoded_string
