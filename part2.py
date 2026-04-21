import hashlib
import itertools
import string

def find_salt(password, target_hash):
    charset = string.ascii_lowercase
    
    for salt in itertools.product(charset, repeat=8):
        salt = ''.join(salt)
        hashed_value = hashlib.sha256((password + salt).encode()).hexdigest()
        
        if hashed_value == target_hash:
            return salt

    return None

if __name__ == "__main__":
    print("Script is running...")
    password = "comp2108"
    target_hash = "9f02b0fd48e9211a5a33ae3321b942896e4ebb0cb267fdfff53fa58cf8c56f24"
    
    salt = find_salt(password, target_hash)
    
    if salt:
        print(f"Salt found: {salt}")
    else:
        print("Salt not found.")