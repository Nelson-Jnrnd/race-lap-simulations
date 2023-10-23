def ms_to_kph(speed_ms):
    '''The function converts a speed in meters per second to kilometers per hour.
    
    Parameters
    ----------
    speed_ms
        The speed in meters per second.
    
    Returns
    -------
        the speed in kilometers per hour (kph) by converting the speed from meters per second (m/s) to
    kilometers per hour.
    
    '''
    return 3.6 * speed_ms

def kph_to_ms(speed_kph):
    return speed_kph / 3.6


def example_torque_curve(rpm):
    '''The function calculates the torque based on the given RPM using a quadratic equation.
    
    Parameters
    ----------
    rpm
        The "rpm" parameter represents the revolutions per minute of an engine.
    
    Returns
    -------
        the torque value at the given RPM.
    
    '''
    a = -0.00017 / 10
    b = 15 / 100
    c = 20000 / 100
    return max(0, a * rpm * rpm + b * rpm + c)

def plot_torque_curve(engine):
    '''The function `plot_torque_curve` takes an engine object as input and plots the torque curve of the
    engine.
    
    Parameters
    ----------
    engine
        The "engine" parameter is an object that represents an engine. It should have the following
    attributes and methods:
    
    Returns
    -------
        a tuple containing the figure and axis objects created by matplotlib.pyplot.subplots().
    
    '''
    import numpy as np
    import matplotlib.pyplot as plt

    rpms = np.arange(engine.min_rpm, engine.max_rpm)
    torque_values = [engine.torque_output(rpm) for rpm in rpms]

    fig, ax = plt.subplots()
    ax.plot(torque_values)
    ax.grid()
    ax.set_title('Engine Torque Curve')
    ax.set_xlabel('Speed (RPM)')
    ax.set_ylabel('Torque (Nm)')
    return fig, ax

# ---- Speed Fuzzy logic ----

def trapezoidal_membership(speed, start, rise_start, fall_start, end):
    """
    Calculates the membership value of a speed using a trapezoidal membership function.
    
    Parameters:
    - speed: The speed for which to calculate the membership value.
    - start: The start of the trapezoid where the membership is 0.
    - rise_start: The point at which the membership starts rising to 1.
    - fall_start: The point at which the membership starts falling from 1.
    - end: The end of the trapezoid where the membership is 0.
    
    Returns:
    - The membership value of the speed.
    """
    if speed <= start or speed >= end:
        return 0
    elif start < speed <= rise_start:
        return (speed - start) / (rise_start - start)
    elif rise_start < speed < fall_start:
        return 1
    elif fall_start <= speed < end:
        return (end - speed) / (end - fall_start)
    else:
        return 0

# Speed values (in kph) delimiting the speed bins
START = 0
START_MEDIUM = 75
END_SLOW = 125
START_HIGH = 150
END_MEDIUM = 200
END = 500

# Define membership functions for different speed categories
def low_speed(speed):
    return trapezoidal_membership(speed, START, START, START_MEDIUM, END_SLOW)

def medium_speed(speed):
    return trapezoidal_membership(speed, START_MEDIUM, END_SLOW, START_HIGH, END_MEDIUM)

def high_speed(speed):
    return trapezoidal_membership(speed, START_HIGH, END_MEDIUM, END, END)

def speed_membership(speed):
    """
    Returns the membership values for a given speed in the three sets: Low, Medium, and High.
    """
    return low_speed(speed), medium_speed(speed), high_speed(speed)