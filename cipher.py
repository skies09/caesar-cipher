alphabet = 'abcdefghijklmnopqrstuvwxyz'
key = 3
newMessage = ''


message = input('Please enter a message: ')

for character in message:
    position = alphabet.find(character)
    newPosition = (position + key) % 26
    newCharacter = alphabet[newPosition]
  #  print('The new character is:', newCharacter)
    newMessage += newCharacter
    print('Your new message is ', newMessage)