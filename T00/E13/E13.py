import torch

def E13(x):
    # check: prevent division by 0
    if x[0] == 0 or x[1] == 0:
        print("Error")
        return None
    
    x = torch.tensor([x[0],x[1]], device="cpu",dtype=torch.float32)
    z = 1 / x # 5 -> 1/5
    return z

def main():
    x = [-9,6]
    z = E13(x)
    print(z, "\n")

if __name__ == "__main__":
    main()