import random


def main():
    a = get_level()
    b = generate_integer(a)
    
    score = 0
    for k, v in b.items():
        t = 3
        while t > 0:
            try:
                ans = int(input(f"{k} = "))
                if ans == v:
                    score = score + 1
                    break
                else:
                    print("EEE")
                    t = t - 1
                        
            except ValueError:
                print("Invalid Entry. Enter a number")  
        if t == 0:
            print(f"Correct answer is {v}") 
                                                           
    print(f"Scores: {score}/10")    
    


def get_level():
    while True:
        try:
            level = int(input("Enter Level (1, 2 or 3): "))
            if level in [1, 2, 3]:
                return level
            else:
                continue
        except ValueError:
            print("Invalid Input. Enter a number")
     


def generate_integer(level):
    i = 10
    probs = {}
   

    while i > 0:
        if level == 1:
            x = random.randint(0, 9)
            y = random.randint(0, 9)
        elif level == 2:
            x = random.randint(10,99)
            y = random.randint(10,99)
        else:
            x = random.randint(100, 999)
            y = random.randint(100, 999)
        
  
        probs[f"{x} + {y}"] = x + y
        i = i - 1
           
    return probs

if __name__ == "__main__":
    main()
