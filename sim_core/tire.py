class Tire:
    def __init__(self, compound):
        self.compound = compound
        self.current_grip = compound.base_grip
        self.cumulative_stress = 0  # Cumulative stress the tire has experienced

    def get_grip(self):
        # Calculate the current grip based on cumulative stress and degradation rates from the compound
        degradation = (self.compound.initial_degradation_rate * self.cumulative_stress + 
                       0.5 * self.compound.degradation_rate_change * self.cumulative_stress**2)
        self.current_grip = max(self.compound.base_grip - degradation, 0)  # Ensure grip doesn't go negative
        return self.current_grip

    def __apply_stress(self, stress):
        # Increase the cumulative stress based on the stress applied during a simulation step
        self.cumulative_stress += stress / 100

    def __calculate_stress(self, longitudinal_force, lateral_force, vertical_force, temperature, surface_grip):
        # Constants for each force type
        k_longitudinal = 0.1
        k_lateral = 0.2
        k_vertical = 0.05

        # Temperature effect (assuming optimal_temperature is the ideal tire temperature)
        optimal_temperature = 90  # in Celsius, for example
        temperature_factor = 1 + (temperature - optimal_temperature)**2 * 0.001

        # Surface grip effect
        grip_factor = 1 + surface_grip  # assuming surface_grip is a value between 0 (low grip) and 1 (high grip)

        # Calculate stress from each force
        stress_longitudinal = k_longitudinal * longitudinal_force
        stress_lateral = k_lateral * lateral_force
        stress_vertical = k_vertical * vertical_force

        # Combine stresses
        total_stress = (stress_longitudinal + stress_lateral + stress_vertical) * temperature_factor * grip_factor

        return total_stress / 100
    
    def update(self, longitudinal_force, lateral_force, vertical_force, temperature, surface_grip):
        stress = self.__calculate_stress(
            longitudinal_force,
            lateral_force,
            vertical_force,
            temperature,
            surface_grip
        )
        self.__apply_stress(stress)
        

    def reset(self):
        # Reset the tire to its initial state (useful for simulations with new tires)
        self.current_grip = self.compound.base_grip
        self.cumulative_stress = 0