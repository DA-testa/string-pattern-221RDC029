def read_input():
    ievade = input().strip()
    if ievade == "I":
        pattern = input().strip()
        text = input().strip()
    elif ievade == "F":
        mape = 'test/06'
        with open(mape, 'r') as fails:
            pattern = fails.readline().strip()
            text = fails.readline().strip()
    else:
        print("Nepareiza ievade!")
    return pattern, text

def print_occurrences(output):
    print(' '.join(map(str, output)))

def hash_aprekins(s, length, base_cipars, prime_cipars):
    result = 0
    for i in range(length):
        result = (base_cipars * result + ord(s[i])) % prime_cipars
    return result

def get_occurrences(pattern, text, base_cipars = 13, prime_cipars = 256):
    pattern_garums = len(pattern)
    teksta_garums = len(text)
    pattern_hash = hash_aprekins(pattern, pattern_garums, base_cipars, prime_cipars)
    text_hash = hash_aprekins(text, pattern_garums, base_cipars, prime_cipars)
    occurrences = []
    for i in range(teksta_garums - pattern_garums + 1):
        if pattern_hash == text_hash:
            if pattern == text[i : i + pattern_garums]:
                occurrences.append(i)
        if i < teksta_garums - pattern_garums:
            text_hash = ((text_hash - ord(text[i]) * pow(base_cipars, pattern_garums-1, prime_cipars)) * base_cipars + ord(text[i+pattern_garums])) % prime_cipars
            if text_hash < 0:
                text_hash += prime_cipars
    return occurrences

if __name__ == '__main__':
    pattern, text = read_input()
    print_occurrences(get_occurrences(pattern, text))