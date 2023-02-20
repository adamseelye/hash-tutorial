import random
import string
import hashlib
import time
import threading


def generate(alphabet, max_len):
    if max_len <= 0:
        return
    for c in alphabet:
        yield c
    for c in alphabet:
        for next in generate(alphabet, max_len - 1):
            yield c + next


upper = string.ascii_uppercase
lower = string.ascii_lowercase
letters = string.ascii_letters
printable = string.printable

user_pword = input("Please enter a password to crack: ")
start_time = time.perf_counter()
encoded = user_pword.encode("utf-8")
hashed = hashlib.md5(encoded).hexdigest()

# threads = threading.Thread(target=generate())
# threads.start()
# print("Threads started...")

i = 1
while i >= 1:
    i -= 1
    for c in generate(lower, 5):
        char_hash = hashlib.md5(c.encode("utf-8")).hexdigest()
        if char_hash == hashed:
            print("\nSuccess!")
            print("Cracked password: " + encoded.decode("utf-8") + "\n")
            print("MD5 password hash: " + char_hash + "\n")
            break
        else:
            # pass
            print("Not a match: " + c)

end_time = time.perf_counter()
total_time = end_time - start_time
rounded_time = round(total_time, 2)
print("Run time: " + str(rounded_time) + " seconds")
