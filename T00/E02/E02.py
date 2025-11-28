import torch

def E02(x1,y1):
    x = torch.tensor([x1[0], x1[1]], device= "cpu", dtype=torch.float32) #if need to using a GPU write "cuda"
    y = torch.tensor([y1[0], y1[1]], device= "cpu", dtype=torch.float32)
    z = x * y
    return z

def main():
    x = [1.2, 4.5]
    y = [3.0, 2.2]
    z = E02(x,y)
    print(z,"\n")

if __name__ == "__main__":
    main()