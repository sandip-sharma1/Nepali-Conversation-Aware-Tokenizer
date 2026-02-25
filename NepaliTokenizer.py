from NepaliSyllables import valid_symbols

def tokenize_pronunciationaware(sentence, win_size=4):
    """
    Tokenize a Nepali word/sentence into syllables based on the provided syllable dataset.
    
    Args:
        sentence (str): The Nepali text to tokenize
        win_size (int): Maximum window size to consider for syllables, default is 4
        
    Returns:
        list: A list of syllable tokens
    """
    # Final tokens list
    FT = []
    
    # Ordered list of all characters in the sentence
    T = list(sentence)
    
    # Current window position
    current_win_pos = 0
    
    # Process until we reach the end of the input word or sentence
    while current_win_pos < len(T):
        # Get window of characters starting from current position
        t_window = T[current_win_pos:current_win_pos + win_size]
            
        # Flag to check if a valid syllable is found
        found_valid_syllable = False
        
        # Generate all possible syllables from the window starting at position 0
        # And start with the longest possible syllable (all chars in window)
        for length in range(len(t_window), 0, -1): # length: 4 3 2 1
            # Create potential syllable of current length
            # In First loop, Syllable is created using 4 chars
            # In Second loop, Syllable is created using 3 chars and so on
            potential_syllable = ''.join(t_window[:length]) 
            
            # Check if created potential syllable exists in the syllable dataset
            if potential_syllable in valid_symbols:
                # If exists add to final tokens
                FT.append(potential_syllable)
                
                # Move window position forward
                current_win_pos += length
                
                found_valid_syllable = True
                break
        
        # If no valid syllable was found, move forward by one character
        # To handle cases where individual characters are not in the dataset
        if not found_valid_syllable:
            # Add the single character as a token
            FT.append(T[current_win_pos])
            current_win_pos += 1
    
    return FT
