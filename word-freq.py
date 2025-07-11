word = input("Enter the word you wanna look for: ")
freq = 0
#M1
#with open("testing.txt", "a") as file:
#    file.write("Hi there everyone, i am writing this to test some file basics, you know cuz i have been trying to learn python recently and now i am trying to apply the concepts on everything, so yeah, have a nice day and good bye!")



with open("testing.txt", "r") as file:
    content = file.read().lower()  # Read entire content and make lowercase
    freq = content.split().count(word)
print(freq)


#M2
word = input("Enter the word you're looking for:").lower()
freq = 0

with open("trying.txt", "a+") as file:
    file.write("Hi, i am attempting to try this again! ")
    #it moves the pointer to the begenning of the file so that we read from the begening 
    file.seek(0)
    content = file.read().lower()
    freq = content.split().count(word)
print(freq)

