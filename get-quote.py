def main():
 
  print("Keep it logically awesome.")

  f = open("./quotes.txt")
  for lines in f:
    quotes = lines
    print(quotes)
  
  f.close()

  # print(quotes)

if __name__== "__main__":
  main()
