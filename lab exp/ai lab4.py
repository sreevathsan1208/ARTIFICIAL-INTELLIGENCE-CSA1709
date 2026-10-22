from itertools import permutations

def solve_cryptarithmetic(word1, word2, result):
    # Combine all words to find the set of unique characters
    all_words = [word1, word2, result]
    unique_chars = set("".join(all_words))
    
    # A base-10 system can only map a maximum of 10 unique letters (0-9)
    if len(unique_chars) > 10:
        print("Invalid puzzle: More than 10 unique letters.")
        return None

    # Track the leading characters because they cannot be zero
    leading_chars = {word[0] for word in all_words}
    
    # Convert unique characters to a stable list format
    chars_list = list(unique_chars)
    
    # Generate all unique permutations of length len(chars_list) from digits 0-9
    for perm in permutations(range(10), len(chars_list)):
        # Map each character to a digit
        char_to_digit = dict(zip(chars_list, perm))
        
        # Rule: Leading characters cannot be zero
        if any(char_to_digit[char] == 0 for char in leading_chars):
            continue
            
        # Helper function to convert a word into its assigned numerical value
        def get_value(word):
            return int("".join(str(char_to_digit[char]) for char in word))
        
        val1 = get_value(word1)
        val2 = get_value(word2)
        val_result = get_value(result)
        
        # Check if the digit assignment satisfies the equation
        if val1 + val2 == val_result:
            return char_to_digit, val1, val2, val_result

    return None

# --- Example Usage ---
if __name__ == "__main__":
    # Define the puzzle words (e.g., SEND + MORE = MONEY)
    w1, w2, res = "SEND", "MORE", "MONEY"
    
    print(f"Solving puzzle: {w1} + {w2} = {res}...")
    solution = solve_cryptarithmetic(w1, w2, res)
    
    if solution:
        mapping, v1, v2, vr = solution
        print("\nSolution Found!")
        print(f"Letter Mapping: {sorted(mapping.items())}")
        print(f"Equation: {v1} + {v2} = {vr}")
    else:
        print("\nNo solution exists for this puzzle.")
