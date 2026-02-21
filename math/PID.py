previous_error = 0
integral = 0

def pid(setpoint, measured_value, l=10, Kp, Ki, Kd):
    global previous_error
    global integral
    dt = 0.1

    i = 0
    while i < l:
        error = setpoint − measured_value
        proportional = error
        integral = integral + error × dt
        derivative = (error − previous_error) / dt
        output = Kp × proportional + Ki × integral + Kd × derivative
        previous_error = error
        #wait(dt)
        i += 1

    return output
