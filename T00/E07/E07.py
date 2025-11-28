import torch

def E07(x):
    x = torch.tensor([x[0], x[1]], device = "cpu", dtype=torch.float32)
    z = -x
    return z

def main():
    x = [25,-25]
    z = E07(x)
    print(z,"\n")

if __name__ == "__main__":
    main()