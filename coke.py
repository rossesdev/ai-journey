def main():
  amount_due = 50
  insertCoint = 0

  while amount_due > insertCoint:
    print(f"Amount Due: {amount_due}")
    insertCoint = int(input("Insert Coint: "))
    if insertCoint % 5 == 0:
      amount_due -= insertCoint
      insertCoint = 0

  print(f"Change Owed: {abs(amount_due)}")


main()