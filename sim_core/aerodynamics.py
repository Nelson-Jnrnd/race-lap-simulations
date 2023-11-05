from typing import Callable
from sim_core.utils import speed_membership

class AerodynamicProfile:
    def __init__(self, baseline: Callable[[float], float], coef_low_speed: float = 1, coef_medium_speed: float = 1, coef_high_speed: float = 1):
        self.baseline = baseline
        self.coef_low_speed = coef_low_speed
        self.coef_medium_speed = coef_medium_speed
        self.coef_high_speed = coef_high_speed
    
    def output(self, speed):
        from sim_core.utils import kph_to_ms
        low_membership, medium_membership, high_membership = speed_membership(speed)
        out = self.baseline(kph_to_ms(speed))
        return out * self.coef_low_speed * low_membership + out * self.coef_medium_speed * medium_membership + out * self.coef_high_speed * high_membership

class FrontWing:
    class AerodynamicComponent:
        def __init__(self, downforce: AerodynamicProfile, drag: AerodynamicProfile, base_weight: float, coef_weight: float = 1):
            self.downforce = downforce
            self.drag = drag
            self.base_weight = base_weight
            self.coef_weight = coef_weight

        def get_downforce(self, speed: float):
            return self.downforce.output(speed)
        
        def get_drag(self, speed: float):
            return self.drag.output(speed)
    
    class MainPlane(AerodynamicComponent):
        def __init__(self, downforce: AerodynamicProfile, drag: AerodynamicProfile, base_weight: float, coef_weight: float = 1):
            super().__init__(downforce, drag, base_weight, coef_weight)
    
    class Flaps(AerodynamicComponent):
        stall_angle: float = 40
        def __init__(self, downforce: AerodynamicProfile, drag: AerodynamicProfile, base_weight: float, coef_weight: float = 1, angle_range: tuple = (0, 60)):
            super().__init__(downforce, drag, base_weight, coef_weight)
            self.angle_range = angle_range
            self.angle = angle_range[0]
        def set_angle(self, angle: float):
            if angle < self.angle_range[0] or angle > self.angle_range[1]:
                raise Exception(f"Angle must be between {self.angle_range[0]} and {self.angle_range[1]}")
            self.angle = angle
        def get_downforce(self, speed: float):
            if self.angle <= self.stall_angle:
                return super().get_downforce(speed) * (self.angle + 5) / self.angle_range[-1]
            else:
                return super().get_downforce(speed) * (self.stall_angle - 1.5 * (self.angle + 5 - self.stall_angle)) / self.angle_range[-1]
        def get_drag(self, speed: float):
            return super().get_drag(speed) * (self.angle + 5) / self.angle_range[-1]
    
    class EndPlates(AerodynamicComponent):
        def __init__(self, downforce: AerodynamicProfile, drag: AerodynamicProfile, drag_reduction_percent: float, tire_wear_reduction_percent: float, tire_temp_reduction_percent: float, base_weight: float, coef_weight: float = 1):
            super().__init__(downforce, drag, base_weight, coef_weight)
            self.drag_reduction_percent = drag_reduction_percent
            self.tire_wear_reduction_percent = tire_wear_reduction_percent
            self.tire_temp_reduction_percent = tire_temp_reduction_percent

        def get_downforce(self, speed: float):
            return super().get_downforce(speed)
        
        def get_drag(self, speed: float):
            return super().get_drag(speed)

    def __init__(self, mainplane: MainPlane, flaps: Flaps, endplates: EndPlates):
        self.mainplane = mainplane
        self.flaps = flaps
        self.endplates = endplates
    
    def get_downforce(self, speed: float):
        return self.mainplane.get_downforce(speed) + self.flaps.get_downforce(speed) + self.endplates.get_downforce(speed)
    
    def get_drag(self, speed: float):
        return (self.mainplane.get_drag(speed) + self.flaps.get_drag(speed) + self.endplates.get_drag(speed)) * (1 - self.endplates.drag_reduction_percent)