from fast_IO import input, print
from time import time

def main():
    start = time()
    for i in range(1,1000000):
        s = input()
    print(f"input took {time()-start:.4f}")
    
    start = time()

    for _ in range(1,1000000):
        print(end="")
    
    print(f"output took {time()-start:.4f}")

if __name__ == "__main__":
    main()
