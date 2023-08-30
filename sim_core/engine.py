from math import pi

class Engine:
    def __init__(self, ratio_gears, ratio_differential, torque_output):
        self.ratio_gears = ratio_gears
        self.ratio_differential = ratio_differential
        self.torque_output = torque_output

        self.gear = 1
        self.rpm = 2000
        self.max_rpm = 10000
        self.min_rpm = 100

    def step(self, delta_t):
        force_engine = self.force_wheel(self.rpm)
        net_force = force_engine
        car_mass = 550  # kg, this can be an attribute of the class
        acceleration = net_force / car_mass
        self.speed += acceleration * delta_t
        self.rpm = self.calc_rpm(self.speed)
        
    def torque_wheel(self, rpm):
        return self.torque_output(rpm) * self.ratio_gears[self.gear - 1]
    
    def force_wheel(self, rpm):
        return self.torque_wheel(rpm) / self.radius_wheel