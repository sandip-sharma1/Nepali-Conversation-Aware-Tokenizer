from NepaliTokenizer import tokenize_pronunciationaware
# Example
if __name__ == "__main__":
  
    # Test sentence
    test_sentence = "ॐ श्री गुरु॒ः क़ुरान–ख़ानाले फ़ज़ीलत, दुःखः, हँसिलो स्वभाव र त्र्यस्त ब्रह्माण्डलाई चाँडै बुझ्छ।"
    
    # Tokenize
    result = tokenize_pronunciationaware(test_sentence)
    print(f"Original: {test_sentence}")
    print(f"Tokenized: {result}")
    
"""

Original: नेपाली भाषामा योगदान गर्न चाहन्छु।
Tokenized: ['ने', 'पा', 'ली', ' ', 'भा', 'षा', 'मा', ' ', 'यो', 'ग', 'दा', 'न', ' ', 'ग', 'र्', 'न', ' ', 'चा', 'ह', 'न्', 'छु', '।']

"""