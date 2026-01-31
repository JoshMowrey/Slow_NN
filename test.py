import slow_nn
import random

def main():
    nn = slow_nn.slow_nn(4, 1)
    trueVal = 0;
    x = 4;
    input = list()
    for _ in range(x):
        input.append(random.randint(0, 100));

    print(input)
    print(nn.Eval(input=input));

if __name__ == "__main__":
    main()
