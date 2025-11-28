import torch

def E11(x):
    x = torch.tensor([x[0],x[1]], device="cpu", dtype=torch.float32)
    z = torch.ceil(x) # 3.2 -> 4     3.9 -> 4
    return z

def main():
    x = [-12.4,12.9]
    z = E11(x)
    print(z ,"\n")

if __name__ == "__main__":
    main()