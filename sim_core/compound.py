class Compound:
    def __init__(self, name, base_grip, initial_degradation_rate, degradation_rate_change):
        self.name = name
        self.base_grip = base_grip
        self.initial_degradation_rate = initial_degradation_rate
        self.degradation_rate_change = degradation_rate_change

soft_compound = Compound(name="Soft", base_grip=1.0, initial_degradation_rate=0.0005, degradation_rate_change=0.00002)
medium_compound = Compound(name="Medium", base_grip=0.9, initial_degradation_rate=0.0003, degradation_rate_change=0.00001)
hard_compound = Compound(name="Hard", base_grip=0.7, initial_degradation_rate=0.0001, degradation_rate_change=0.000005)
