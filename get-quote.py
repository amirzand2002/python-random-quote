import random
def asli():
  #print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  print("fisrt line:",quotes[0].splitlines())
  last = len(quotes) - 1
  rnd = random.randint(0,last)
  print(quotes[rnd])

if __name__== "__main__":
  asli()

