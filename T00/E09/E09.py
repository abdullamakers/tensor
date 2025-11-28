import torch

def E09(x,a,b):
    x = torch.tensor([x[0],x[1]], device="cpu", dtype=torch.float32)
    z = torch.clamp(x,min=a,max=b)
    return z

def main():
    x = [10000, -216]
    a = 0
    b = 5
    z = E09(x,a,b)
    print(z, "\n")


if __name__ == "__main__":
    main()