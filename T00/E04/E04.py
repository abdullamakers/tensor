import torch

def E04(x1,y1):
    x = torch.tensor([x1[0], x1[1]], device= "cpu") # if need to using a GPU write "cuda"
    y = torch.tensor([y1[0], y1[1]], device = "cpu")
    z = x ** y
    return z

def main():
    x = [2.0,2.0]
    y = [3.0,4.0]
    z = E04(x,y)
    print(z,"\n")

if __name__ == "__main__":
    main()