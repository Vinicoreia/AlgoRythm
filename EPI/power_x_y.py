
def power_x_y(x:float, y:int) -> float:
    result, power = 1.0, y
    if(y < 0):
        power, x = -power, 1.0/x
    while power:
        if(power & 1):
            result *= x
        x, power = x*x, power >> 1
    return result

