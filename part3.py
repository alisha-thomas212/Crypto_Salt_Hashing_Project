from os import urandom
import base64
import string

# n: Number of salts to generate
def generate_salts(n, length=16):
    print("Script2 is running...")
    salts = set()
    charset = string.ascii_lowercase + string.digits
    
    while len(salts) < n:
        random_bytes = urandom(length * 2)  # Get extra bytes to increase chance
        encoded = base64.b64encode(random_bytes).decode('utf-8')  # Encode in base64
        salt = ''.join(filter(lambda c: c in charset, encoded))[:length] 
        
        if len(salt) == length:
            salts.add(salt)
    
    return list(salts)

if __name__ == "__main__":
    salts = generate_salts(16)
    print(salts)