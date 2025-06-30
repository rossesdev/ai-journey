name  = input("What's your name? ")

GRYFFINDOR = "Gryffindor"
SLYTHERIN = "Slytherin"

match name: 
  case "Harry" | "Hermione" | "Ron":
    print(GRYFFINDOR)
  case "Draco":
    print(SLYTHERIN)
  case _:
    print("Who?")