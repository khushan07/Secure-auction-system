import emoji

# Taking user input
user_input = input("Enter a text with emojis: ")

# Converting emojis to text
text_without_emojis = emoji.demojize(user_input)

# Printing the result
print("Text without emojis:", text_without_emojis)
