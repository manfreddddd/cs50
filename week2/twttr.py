def twttr():
    user_input = input("Input: ")
    outputs = ""
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    for char in user_input:
        if char not in vowels:
            outputs += char

    print(f"Output: {outputs}")

       

twttr()
user_input = input("Input: ")
vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

# Initialize the output with the original input
outputs = user_input

# Replace each vowel in the original string
for vowel in vowels:
    outputs = outputs.replace(vowel, "")

print(f"Output: {outputs}")
