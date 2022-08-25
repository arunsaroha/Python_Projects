alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text, shift):
  new = []
  for i in range(0,len(text)):
    for j in range(0,len(alphabet)):
      if alphabet[j] == text[i]:
        new_j = j+shift
        if new_j > 25:
          multiple = int(new_j/26)
          new_j = new_j - multiple*26
          new.insert(new_j,alphabet[new_j])
        else:
          new.insert(j+shift,alphabet[j+shift])
  new_text = ""
  new_text = new_text.join(new)
  print(f"The encoded text is {new_text}")


def decrypt(text, shift):
  new = []
  for i in range(0,len(text)):
    for j in range(0,len(alphabet)):
      if alphabet[j] == text[i]:
        new_j = j-shift
        if new_j < 0:
          multiple = int(new_j/26)
          new_j = new_j + multiple*26
          new.insert(new_j,alphabet[new_j])
        else:
          new.insert(j+shift,alphabet[j+shift])
  new_text = ""
  new_text = new_text.join(new)
  print(f"The encoded text is {new_text}")

  
if direction == "encode":
  encrypt(text, shift)
elif direction == "decode":
  decrypt(text, shift)