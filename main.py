lst_paragraph = []
paragraph = input("Enter a paragraph: ")
lst_paragraph = paragraph.split(" ")
print(lst_paragraph)

search = input("Enter a search string: ")
j = 0
for word in lst_paragraph:
    if word == search:
        j += 1
print('There are', j, 'occurrences')

reply = input("Do you want to replace the text [Y/N]: ")
if reply.lower() == "y":
    replacement = input("Enter a replacement string: ")
    for i in range(len(lst_paragraph)):  # Iterate over indices
        if lst_paragraph[i] == search:
            lst_paragraph[i] = replacement  # Replace word at index i
    print(lst_paragraph)
elif reply.lower() == "n":
    replyTwo = input("Oh! you don't like to replace, DO you want to check again[Y/N]")
    if replyTwo.lower() == 'y':
        print(lst_paragraph)
    else:
        print("Goodbye")
else:
    print("Invalid Key")


