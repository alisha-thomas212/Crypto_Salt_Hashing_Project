Hashing and Salt Generation Scripts
===================================

--------------------------------------------------
part1.py
--------------------------------------------------
Description:
This code generates random passwords until it finds one whose SHA-256 hash (combined with my student number as salt) starts with "c0ffee" followed by the last two digits of the student number.
part1.txt: The generated hash

Features:
- Password Hashing using SHA-256
- static salt
- brute force approach based on hash prefix matching

--------------------------------------------------
part2.py
--------------------------------------------------
Description: 
This code performs a  brute-force attack to find an 8-character lowercase salt that, when appended to the given password ("comp2108"), produces the specified SHA-256 hash.
part2.txt: The generated answer

Features:
- Brute-force attack on hash
- Exhaustive search 
- SHA-256 hash matching

--------------------------------------------------
part3.py
--------------------------------------------------
Description: 
This code generates 16 unique random salts, each 16 characters long, using base64-encoded random bytes
part3.txt: The generated answer

Features:
- Secure random byte generation using os.urandom
- Base64 encoding and character filtering
- Salt uniqueness and format enforcement
