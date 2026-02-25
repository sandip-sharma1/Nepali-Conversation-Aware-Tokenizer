# Nepali-Conversation-Aware-Tokenizer

This project is a simple rule-based tokenizer for Nepali text.
It breaks words into syllable-like units using a predefined list of valid Nepali symbols.
I built this while experimenting with pronunciation-aware text processing for Nepali. The goal was to split text in a way that better matches how words are actually pronounced — not just character-by-character splitting..


---Why This Exists---
Most basic tokenizers split text by whitespace or individual Unicode characters.
That doesn’t work well for Nepali because:
Many characters combine to form meaningful syllables.
Consonant + vowel signs should stay together.
Some clusters like क्ष, त्र, ज्ञ represent a single sound unit.
This tokenizer tries to handle that using a predefined syllable dataset.



---How It Works---
The core idea is simple:
-->Take the input text.
-->Look at a sliding window of characters (default size = 4).
-->Try matching the longest possible substring against a list of valid Nepali syllables.
-->If a match is found:
       Add it as a token
       Move forward by that length
-->If no match is found:
      Fall back to a single character
      Move forward by one
-->It always prefers the longest valid syllable first.