def patternMatching(text,pattern) :
    n = len(text)
    m = len(pattern)
    occurrences = []
    for i in range(n-m+1) :
        if text[i : i+m] == pattern :
            occurrences.append(i)
    if occurrences :
        return occurrences
    else :
        return 'Pattern Not Found'
    
text = input('Enter the text : ')
pattern = input("Enter the pattern which is to be searched : ")
if len(pattern) > len(text) :
    print("Pattern cannot be longer than text")
    quit()
    
result = patternMatching(text,pattern)

if result == 'Pattern Not Found' :
    print(f"'{pattern}' not found in the text")
    
else :
    print(f"'{pattern}' found at the following indices {result}")
