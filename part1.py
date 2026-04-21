import hashlib
import random
import string

# generate random password
def generate_random_password(length=10):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))

# generate SHA256 hash
def generate_hash(password, salt):
    hash_input = password + salt
    hash_object = hashlib.sha256(hash_input.encode())
    return hash_object.hexdigest()

def main():
    student_number = "101299511"  
    last_two_digits = student_number[-2:]
    print("Script is running...")

    while True:
        password = generate_random_password()
        salt = student_number
        hash_value = generate_hash(password, salt)

        # Check if the hash starts with 'c0ffee11' 
        if hash_value[:6] == "c0ffee" and hash_value[6:8] == last_two_digits:
            break 

    print(f"Generated hash: {hash_value}")
    print(f"Password used: {password}")
    
if __name__ == "__main__":
    main()