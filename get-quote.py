import random

def primary():
  


  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  
  rng = random.randint(0,len(quotes)-1)
  print(quotes[rng])

if __name__== "__main__":
  primary()
