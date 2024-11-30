def identify_verbs():
    # Input: Request a sentence with at least 7 words
    sentence = input("Enter a sentence with at least 7 words: ").split()
    
    # Check if input has at least 7 words
    if len(sentence) < 7:
        print("Please enter at least 7 words.")
        return

    # Basic list of common verbs for identification
    common_verbs = ['am', 'is', 'are', 'was', 'were', 'be', 'been', 'being',
                    'have', 'has', 'had', 'do', 'does', 'did', 'will', 'shall',
                    'go', 'going', 'enjoy', 'enjoying', 'see', 'seeing', 'make', 'making']

    # Identify verbs from the input sentence
    verbs_list = []
    for word in sentence:
        if word.lower() in common_verbs:
            verbs_list.append(word)
        

      


  #  verbs_list = [word for word in sentence if word.lower() in common_verbs]

    # Reverse each verb
    reversed_list = [verb[::-1] for verb in verbs_list]

    # Output
    print("verbsList:", verbs_list)
    print("reversedList:", reversed_list)

# Sample usage
identify_verbs()
