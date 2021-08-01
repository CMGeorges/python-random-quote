def main():
 
  print("Keep it logically awesome.")

  f = open("./quotes.txt")
  for lines in f:
    print(lines)
  
  f.close()

  # print(quotes)

if __name__== "__main__":
  main()
