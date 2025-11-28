import torch

def E10(x):
    x = torch.tensor([x[0],x[1]], device="cpu", dtype=torch.float32)
    z = torch.round(x)
    return z

def main():
    x = [-1.5,10.22]
    z = E10(x)
    print(z, "\n")

if __name__ == "__main__":
    main()