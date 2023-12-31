from math import pi

class Engine:

    def __init__(self, ratio_gears, ratio_differential, torque_output, min_rpm, max_rpm, idle_rpm):
        '''The function initializes the attributes of a class instance, including gear ratios, torque output,
        and RPM limits.
        
        Parameters
        ----------
        ratio_gears
            The ratio_gears parameter represents the gear ratios of the transmission. It is a list or array of
        numbers, where each number represents the gear ratio for a specific gear. For example, if the
        vehicle has 5 gears, the ratio_gears parameter could be [3.5, 2.5, 2, 1.5, 1].
        ratio_differential
            The ratio of the differential is a measure of how the torque from the engine is distributed to the
        wheels. It determines the speed at which the wheels rotate relative to the engine speed. A higher
        ratio means the wheels rotate at a slower speed compared to the engine speed.
        torque_output
            The torque output is a measure of the rotational force generated by the engine. It is 
            measured in units of Newton-meters (Nm). The torque output determines the engine's ability
            to accelerate the vehicle and overcome resistance.
        min_rpm
            The `min_rpm` parameter represents the minimum allowed RPM (revolutions per minute) for the engine.
        It is the lowest value that the RPM can be set to.
        max_rpm
            The maximum RPM (revolutions per minute) that the engine can reach.
        idle_rpm
            The idle_rpm parameter represents the idle speed of the engine, which is the minimum speed at which
        the engine can operate without stalling.
        
        '''
        self.ratio_gears = ratio_gears
        self.ratio_differential = ratio_differential
        self.torque_output = torque_output
        self.idle_rpm = idle_rpm
        self.max_rpm = max_rpm
        self.min_rpm = min_rpm

        self.reset()

    def reset(self):
        '''The `reset` function sets the RPM to the idle RPM and sets the gear to 1.
        
        '''
        self._set_rpm(self.idle_rpm)
        self.gear = 1

    def _set_rpm(self, value):
        '''The function `_set_rpm` sets the value of `_rpm` within the range of `min_rpm` and `max_rpm`.
        
        Parameters
        ----------
        value
            The `value` parameter represents the desired RPM (revolutions per minute) value that we want to set
        for a certain object.
        
        '''
        value = max(self.min_rpm, min(self.max_rpm, value))
        self._rpm = round(value)
        
    def torque_wheel(self, throttle):
        '''The function calculates the torque at the wheel based on the given RPM and the gear ratio.
        throttle
            The throttle parameters represent the pressure on the throttle pedal between 0 and 1.
        Returns
        -------
            the torque of the wheel.
        
        '''
        return self.torque_output(self._rpm) * self.ratio_gears[self.gear - 1] * throttle
    
    def force_wheel(self, radius_wheel, throttle):
        '''The function calculates the force exerted by a wheel given its RPM and radius.
        
        Parameters
        ----------
        radius_wheel
            The radius of the wheel.
        throttle
            The throttle parameters represent the pressure on the throttle pedal between 0 and 1.
        
        Returns
        -------
            the force exerted by the wheel, which is calculated by dividing the torque of the wheel by the
        radius of the wheel.
        
        '''
        return self.torque_wheel(throttle) / radius_wheel
    
    def update_rpm(self, radius_wheel, speed):
        '''The function calculates and updates the RPM (revolutions per minute) based on the given radius
        of the wheel and speed.
        
        Parameters
        ----------
        radius_wheel
            The radius of the wheel in meters.
        speed
            The speed parameter represents the speed of the vehicle in meters per second.
        
        '''
        self._set_rpm((speed * self.ratio_gears[self.gear - 1] * self.ratio_differential * 60) / (2 * pi * radius_wheel))
    
    def upshift(self):
        '''The function "upshift" increases the gear value by 1 if it is less than the length of the
        ratio_gears list.
        
        '''
        if self.gear < len(self.ratio_gears):
            self.gear += 1
    
    def downshift(self):
        '''The function decreases the gear value by 1 if it is greater than 1.
        
        '''
        if self.gear > 1:
            self.gear -= 1