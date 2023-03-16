import requests

# Load the file
r = requests.get("https://raw.githubusercontent.com/itb-ie/contest/master/text.txt")

# Split the text into lines
lines = r.text.splitlines()

# Decode the message
decoded_message = ""

# Loop over each line
for line in lines:
    # Count the number of vowels
    vowel_count = 0
    for char in line:
        if char.lower() in "aeiou":
            vowel_count += 1

    # Decode the letter based on the vowel count
    if vowel_count == 0:
        decoded_message += " "
    elif vowel_count <= 26:
        decoded_message += chr(vowel_count + 96)

# Print the decoded message
print(decoded_message)
