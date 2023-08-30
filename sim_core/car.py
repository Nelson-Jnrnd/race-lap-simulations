class Car:
    def __init__(self, mass, radius_wheel, engine):
        self.mass = mass
        self.radius_wheel = radius_wheel
        self.engine = engine
        self.reset()

    def reset(self):
        self.speed = 0
        self.engine.reset()

    def accelerate(self, delta_t):
        force_engine = self.engine.force_wheel(self.radius_wheel)
        acceleration = force_engine / self.mass
        self.speed += acceleration * delta_t
        self.engine.update_rpm(self.radius_wheel, self.speed)