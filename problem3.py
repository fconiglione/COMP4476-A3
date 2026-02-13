"""
COMP4476 - Introduction to Cryptography
Francesco Coniglione (1206780)
Assignment 3 - Problem 3

Reference(s): https://www.geeksforgeeks.org/ethical-hacking/birthday-attack-in-cryptography/

Note(s): I could not figure out a way to do this with brute force so I found online that I could use a birthday attack to find two common plaintexts that produce the same hash.
"""

from problem1 import ALPHABET, hash
import random

def run_birthday_attack():
    seen_hashes = {} # blank dictionary to store seen hashes
    count = 0
        
    while True:
        # Count the number of attempts
        count += 1
        # Create random strings of length 25 to compare
        candidate = "".join(random.choice(ALPHABET) for _ in range(25))
        
        # Get the hash
        h_str, _ = hash(candidate)
        
        # Check if the hash has already been checked
        if h_str in seen_hashes:
            # We found two different strings with the same hash!
            text1 = seen_hashes[h_str]
            text2 = candidate # the new candidate that produced the same hash
            
            # Ensure they aren't the exact same string
            if text1 != text2:
                print(f"Attempts: {count}")
                print(f"Plaintext 1: '{text1}'")
                print(f"Plaintext 2: '{text2}'")
                print(f"Common Hash: '{h_str}'")
                break # Exit the loop once we find a collision
        
        # Store and return
        seen_hashes[h_str] = candidate

if __name__ == "__main__":
    run_birthday_attack()