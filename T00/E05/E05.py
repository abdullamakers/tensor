import torch

def E05(x):
    if x[0] < 0 or x[1] < 0:
        return "error"
    x = torch.tensor([x[0], x[1]], device= "cpu") # if need to using a GPU write "cuda"
    z = x ** 0.5
    return z

def main():
    x1 = [125, 25]
    z1 = E05(x1)
    print(z1,"\n")

    x2 = [-125, 25]
    z2 = E05(x2)
    print(z2,"\n")


if __name__ == "__main__":
    main()