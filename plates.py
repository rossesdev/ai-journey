def main():
  # numbers just at the end. NEVER in the middle
  # the first number used cannot be 0
  # No periods, spaces, or punctuation marks 

  plate = input("Plate: ")
  if is_valid(plate):
    print("Valid")
  else:
    print("Invalid")

def is_valid(plate):
  v = True

  if len(plate) < 2 or len(plate) > 6:
    v = False
  elif plate[0].isdigit() == True or plate[1].isdigit() == True:
    v = False
  
  

  for p in plate:
    if p.isdigit() and p == '0':
      v = False
      break
    print(p)



  return v

main()