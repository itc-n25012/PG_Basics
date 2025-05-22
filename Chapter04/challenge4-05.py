def conv(string):
    try:
        return float(string)
    except ValueError:
        print("Could not convert")

s = float("3.14")
print(s)
