import torch

def E06(x):
    x = torch.tensor([x[0], x[1]], device="cpu", dtype=torch.float32)
    z = torch.abs(x)
    return z

def main():
    x = [1.0,-4.0]
    z = E06(x)
    print(z,"\n")

if __name__ == "__main__":
    main()