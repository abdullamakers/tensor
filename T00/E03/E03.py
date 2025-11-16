import torch

def E03(x1,y1):
    x = torch.tensor([x1[0],x1[1]], device = "cpu")
    y = torch.tensor([y1[0],y1[1]], device = "cpu")
    z = x / y
    return z

def main():
    x = [12.0, 6.0]
    y = [4.0, 2.0]
    z = E03(x,y)
    print(z, "\n")

if __name__ == "__main__":
    main()