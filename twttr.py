def main():  
  msg = input("Input: ")
  print(searchVowels(msg))

def searchVowels(msg):
  vowels = ['a', 'e', 'i', 'o', 'u']
  msg_list = list(msg)

  for letter in msg_list:
    if letter in vowels:
      msg_list.remove(letter)
  
  return ''.join(msg_list)

main()
