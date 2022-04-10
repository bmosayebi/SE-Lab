def search(hash_patterns, text, len_pattern):
    counter = 0
    len_patterns = len(hash_patterns)
    len_text = len(text)
    m = 999999937
    b = 30
    hash_text = 0
    power = 1

    for i in range(len_pattern):
        hash_text = (hash_text * b + (ord(text[i])-96)) % m
        
        for hp in hash_patterns:
            hash_patterns[hp] = (hash_patterns[hp] * b + (ord(hp[i])-96)) % m
            
        if i < len_pattern - 1:
            power = (power*b) % m
    
  
    for hp in hash_patterns: 
        if hash_patterns[hp] == hash_text:
            counter += 1
            hash_patterns[hp] = -1

    for i in range(1, len_text - len_pattern + 1):
        hash_text = ( hash_text - power * (ord(text[i - 1])-96)) % m
        hash_text = (hash_text + m) % m
        hash_text = (hash_text * b + (ord(text[i + len_pattern - 1])-96)) % m
        for hp in hash_patterns: 
            if hash_patterns[hp] == hash_text:
                counter += 1
                hash_patterns[hp] = -1

        
    return counter

def main():
    text = input()
    n = int(input())
    patterns = input().split()
    patterns_1 = {}
    patterns_2 = {}
    patterns_3 = {}
    patterns_4 = {}
    counter = 0
    
    for i in range(n):
        if len(patterns[i]) == 1:
            patterns_1[patterns[i]] = 0
        elif len(patterns[i]) == 2:
            patterns_2[patterns[i]] = 0
        elif len(patterns[i]) == 3:
            patterns_3[patterns[i]] = 0
        else:
            patterns_4[patterns[i]] = 0
    
    if patterns_1:
        counter += search(patterns_1, text, 1)
    if patterns_2:
        counter += search(patterns_2, text, 2)
    if patterns_3:
        counter += search(patterns_3, text, 3)
    if patterns_4:
        counter += search(patterns_4, text, 4)
        
    print(counter)

if __name__ == '__main__':
    main()




    
