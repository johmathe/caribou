#TODO(Mathilde): remove '_in_j'

class Agent:
    def __init__(self, agent_id):
        self.agent_id = agent_id
        self.power_load = 0
        self.power_gen = 0
        self.accum_power_load = 0  # accumulated power load in kWH
        self.accum_power_gen = 0  # accumulated power generation in kWH

    def get_id(self):
        return self.agent_id

    def get_instant_power_gen(self):
        return self.power_gen

    def get_instant_power_load(self):
        return self.power_load

    def set_instant_power_load(self, power_load):
        self.power_load = power_load

    def update_accum_power_load(self):
        self.accum_power_load += self.power_load

    def set_instant_power_gen(self, power_gen):
        self.power_gen = power_gen

    def update_accum_power_gen(self):
        self.accum_power_gen += self.power_gen

    def get_accum_power_load(self):
        return self.accum_power_load

    def get_accum_power_gen(self):
        return self.accum_power_gen

class PV(Agent):
    def __init__(self, agent_id):
        super().__init__(agent_id)
        self.angle = 180
        self.efficiency = 1

    def set_angle(self, angle):
        self.angle = angle

    def get_angle(self):
        return self.angle

    def set_efficiency(self, efficiency):
        self.efficiency = efficiency

    def get_efficiency(self):
        return self.efficiency

    def compute_instant_power_gen(self, irradiance):
        self.power_gen = self.efficiency*self.angle*irradiance



class EV(Agent):
    def __init__(self, agent_id):
        super().__init__(agent_id)
        self.capacity_kwh = 24
        self.soc = 0
        self.status = 0

    def set_capacity(self, capacity):
        """
        NOTE: this might be useful for dynamic battery size, e.g., battery degradations
        :param capacity: battery capacity in kWH
        :return: battery capacity in kWH
        """
        self.capacity = capacity

    def get_capacity_kwh(self):
        return self.capacity_kwh

    def set_soc(self, soc):
        self.soc = soc

    def update_soc(self, delta_soc):
        self.soc += delta_soc

    def get_soc(self):
        return self.soc

    def set_status(self, status):
        list_status = ['Parked', 'Driving', 'Charging', 'Discharging']
        if status in list_status:
            self.status =  list_status.index(status)
        else:
            print('Status is : Parked, Charging, Discharging or Driving')

    def get_status(self):
        return self.status

# TODO: ADD ENERGY COMPONENTS (e.g., ESS, HVAC)
