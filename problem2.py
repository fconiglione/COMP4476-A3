"""
COMP4476 - Introduction to Cryptography
Francesco Coniglione (1206780)
Assignment 3 - Problem 2
"""

from problem1 import hash

def mac(key, plaintext):
    # Ensure the key is 15 characters long
    if len(key) != 15:
        raise ValueError("The secret key must be 15 English characters.")
    
    # Inner hash (h(K || x))
    inner = key + plaintext
    inner_str, _ = hash(inner)

    # Outer hash (h(K || h(K || x)))
    outer = key + inner_str
    mac_result_str, mac_result_nums = hash(outer)

    return mac_result_str, mac_result_nums

# Testing the MAC function
if __name__ == "__main__":

    secret_key = "This is example"
    plaintext = "the birthday attack can be performed for any hash functions including sha three"

    mac_str, mac_nums = mac(secret_key, plaintext)

    print(f"Secret Key: '{secret_key}'")
    print(f"MAC Value (String): '{mac_str}'")
    print(f"MAC Value (Numbers): {mac_nums}")