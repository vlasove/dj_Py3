def add(a:int, b:int) -> int:
    """
    this func for a + b 
    """
    return a + b


def sub(a:int, b:int) -> int:
    """
    this func for a - b
    """
    return a - b

def mult(a:int, b:int) -> int:
    """
    this func for a * b
    """
    return a * b

if __name__ == "__main__":
    res = add(10, 20) + sub(20, 30) + mult(30, 40)
    print(res)
