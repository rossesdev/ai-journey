def main():
  camel = input("camelCase: ")
  print(f"snake_case: {snake(camel)}")

def snake(str):
  str_list = list(str)

  for i,s in enumerate(str_list):
    if s.isupper() == True:
      str_list[i] = f"_{s.lower()}"

  return ''.join(str_list)

main()