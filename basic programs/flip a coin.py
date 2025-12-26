import random
def flip_coin(num_flips):
 
        heads_count=0
        tails_count=0
        for _ in range(num_flips):
            if random.random()<0.5:
                tails_count +=1
            else:
                heads_count +=1
        heads_percentage=(heads_count/num_flips)*100
        tails_percentage=(tails_count/num_flips)*100
        print(f"\n Total flips:{num_flips}")
        print(f"heads count:{heads_count:}")
        print(f"tails count:{tails_count:}")
        print(f" percentage of heads:{heads_percentage:.2f}%")
        print(f" percentage of tails:{tails_percentage:.2f}%")
if __name__=="__main__":
        try: 
            flips=int(input(" Enter a positive number for the number of flips."))
            if flips<=0:
                 print(" Please enter a positive number")
            else:
                flip_coin(flips)
        except ValueError:
          print("invalid number please enter a whole  number")

