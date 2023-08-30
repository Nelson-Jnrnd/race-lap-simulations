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