class AutoTransmission:
    def __init__(self, engine, shift_up_rpm, shift_down_rpm):
        '''Initializes the AutomaticTransmission class with an engine instance and RPM thresholds for shifting.
        
        Parameters
        ----------
        engine : Engine
            An instance of the Engine class.
        shift_up_rpm : int
            The RPM threshold at which the transmission will shift up a gear.
        shift_down_rpm : int
            The RPM threshold at which the transmission will shift down a gear.
        '''
        self.engine = engine
        self.shift_up_rpm = shift_up_rpm
        self.shift_down_rpm = shift_down_rpm

    def update(self):
        '''The function updates the gear of the engine based on the current and previous RPM values.
        
        '''
        if self.shift_up_rpm < self.engine._rpm:
            self.engine.upshift()
        elif self.shift_down_rpm > self.engine._rpm:
            self.engine.downshift()