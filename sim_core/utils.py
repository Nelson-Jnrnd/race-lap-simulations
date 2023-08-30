def ms_to_kph(speed_ms):
    return 3.6 * speed_ms


def example_torque_curve(rpm):
    a = -0.00017 / 10
    b = 15 / 100
    c = 20000 / 100
    return max(0, a * rpm * rpm + b * rpm + c)

def plot_torque_curve(engine):
    import numpy as np
    import matplotlib.pyplot as plt

    rpms = np.arange(engine.min_rpm, engine.max_rpm)
    torque_values = [engine.torque_output(rpm) for rpm in rpms]

    fig, ax = plt.subplots()
    ax.plot(torque_values)
    ax.grid()
    #ax.set_xlim([1000, np.max(rpms)])
    ax.set_title('Engine Torque Curve')
    ax.set_xlabel('Speed (RPM)')
    ax.set_ylabel('Torque (Nm)')
    return fig, ax