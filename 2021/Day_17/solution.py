from time import time
        
        
def main():
    t1 = time()

    with open("2021/Day_17/input") as f:
        lines = f.read().splitlines()
        
    print("Time:", time() - t1)
    
main()
