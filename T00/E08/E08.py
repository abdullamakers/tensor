import torch

def E08(x):
    x = torch.tensor([x[0],x[1]], device="cpu", dtype=torch.float32)
    z = torch.sign(x)
    return z

def main():
    x = [25, -25]
    z = E08(x)
    print(z, "\n")

if __name__ == "__main__":
    main()