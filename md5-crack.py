import hashlib
from english_words import english_words_set

HASH = ''
SALT = ''
def main():
        for word in english_words_set:
                guess = hashlib.md5(word.encode('utf-8') + SALT.encode('utf-8')).hexdigest()
                if guess.upper() == HASH or guess.lower() == HASH:
                        print(f'[+] Password found: {word}')
                        exit(0)
                else:
                        print(f'')
        print(f'Password not found in wordlist...')
if __name__ == '__main__':
        main()