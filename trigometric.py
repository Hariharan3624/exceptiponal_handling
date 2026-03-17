import math

def calc():
    try:
        a = float(input("Enter angle in degrees: "))
        
        
        b = math.radians(a)
        
        
        c = math.sin(b)
        d = math.cos(b)
        
        
        if a % 180 == 90:
            e = "Undefined (Infinity)"
        else:
            e = math.tan(b)
        
        print("Results for is ", b)
        print(f"  Sine:   {c:.4f}")
        print(f"  Cosine: {d:.4f}")
        print(f"  Tangent: {e}")
        
    except ValueError:
        print("Invalid input! Please enter a numerical value.")

if __name__ == "__main__":
    calc()