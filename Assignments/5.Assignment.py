from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List, Dict, Optional, Tuple

# =========================================
# Supporting Entities
# =========================================

class Crop:
    def __init__(self, name: str, ideal_moisture_range: Tuple[float, float]):
        self.name = name                      # Public
        self.ideal_moisture_range = ideal_moisture_range  # Public

    def __repr__(self):
        return f"Crop({self.name}, ideal={self.ideal_moisture_range})"


class Field:
    _next_id = 1  # Class attribute: auto increment id for fields

    def __init__(self, name: str, crop: Crop, area_acres: float):
        self.id = Field._next_id
        Field._next_id += 1
        self.name = name
        self.crop = crop
        self.area_acres = area_acres
        self._sensors: List[Sensor] = []      # Protected
        self._actuators: List[Actuator] = []  # Protected

    def add_sensor(self, sensor: "Sensor"):
        self._sensors.append(sensor)

    def add_actuator(self, act: "Actuator"):
        self._actuators.append(act)

    def sensors(self) -> List["Sensor"]:
        return list(self._sensors)

    def actuators(self) -> List["Actuator"]:
        return list(self._actuators)

    def __repr__(self):
        return f"Field(id={self.id}, name={self.name}, crop={self.crop.name})"


# =========================================
# Abstraction: Device -> Sensor / Actuator
# =========================================

class Device(ABC):
    def __init__(self, device_id: str, field: Field):
        self.device_id = device_id
        self.field = field
        self._online: bool = True  # Protected

    def is_online(self) -> bool:
        return self._online

    def set_online(self, state: bool):
        self._online = state

    @abstractmethod
    def info(self) -> str:
        ...


class Sensor(Device):
    @abstractmethod
    def read(self) -> Dict[str, float]:
        ...


class Actuator(Device):
    @abstractmethod
    def activate(self, **kwargs) -> str:
        ...


# =========================================
# Concrete Sensors
# =========================================

class SoilMoistureSensor(Sensor):
    def __init__(self, device_id: str, field: Field, calibration: float = 1.0):
        super().__init__(device_id, field)  # super()
        self._calibration = calibration      # Protected

    def read(self) -> Dict[str, float]:
        # In real life, we'd read hardware. Here we simulate deterministic values per field id.
        base = 20.0 + (self.field.id * 3.5)
        value = base * self._calibration
        return {"soil_moisture": round(value, 2)}

    def info(self) -> str:
        return f"SoilMoistureSensor({self.device_id}) on {self.field.name}"


class WeatherStation(Sensor):
    def read(self) -> Dict[str, float]:
        # simple simulated weather by field id
        temp = 25.0 + (self.field.id * 0.7)
        humidity = 55.0 - (self.field.id * 1.1)
        return {"temperature": round(temp, 1), "humidity": round(humidity, 1)}

    def info(self) -> str:
        return f"WeatherStation({self.device_id}) on {self.field.name}"


# =========================================
# Concrete Actuators
# =========================================

class IrrigationPump(Actuator):
    def __init__(self, device_id: str, field: Field, capacity_lpm: float):
        super().__init__(device_id, field)
        self.capacity_lpm = capacity_lpm

    def activate(self, minutes: int = 10) -> str:
        return f"Pump {self.device_id} irrigated {self.field.name} for {minutes} min"

    def info(self) -> str:
        return f"IrrigationPump({self.device_id}, {self.capacity_lpm} lpm) on {self.field.name}"


class Sprinkler(Actuator):
    def activate(self, minutes: int = 5) -> str:
        return f"Sprinkler {self.device_id} watered {self.field.name} for {minutes} min"

    def info(self) -> str:
        return f"Sprinkler({self.device_id}) on {self.field.name}"


# =========================================
# Users (Roles) – Abstraction + Inheritance + Encapsulation
# =========================================

class User(ABC):
    platform = "Smart Farming System (OOP)"  # Class attribute

    def __init__(self, name: str, email: str, password: str):
        self.name = name                  # Public
        self.email = email                # Public
        self._role = "User"               # Protected
        self.__password = password        # Private

    # Encapsulation: controlled access to private data
    def verify_password(self, plain: str) -> bool:
        return self.__password == plain

    def masked_password(self) -> str:
        return "*" * len(self.__password)

    @classmethod
    def platform_info(cls) -> str:
        return f"Welcome to {cls.platform}"

    @staticmethod
    def guidelines() -> str:
        return "Monitor fields, irrigate wisely, and log activities accurately."

    @abstractmethod
    def role(self) -> str: ...


class Farmer(User):
    def __init__(self, name: str, email: str, password: str):
        super().__init__(name, email, password)
        self._role = "Farmer"
        self.fields: List[Field] = []

    def role(self) -> str:
        return self._role

    def register_field(self, field: Field):
        self.fields.append(field)


class Agronomist(User):
    def __init__(self, name: str, email: str, password: str):
        super().__init__(name, email, password)
        self._role = "Agronomist"

    def role(self) -> str:
        return self._role

    def recommend_irrigation(self, field: Field, latest_moisture: float) -> Optional[int]:
        low, high = field.crop.ideal_moisture_range
        if latest_moisture < low:
            return 15  # minutes
        elif latest_moisture > high:
            return 0   # skip
        return 5       # top-up


class FieldWorker(User):
    def __init__(self, name: str, email: str, password: str):
        super().__init__(name, email, password)
        self._role = "FieldWorker"

    def role(self) -> str:
        return self._role

    def run_actuator(self, act: Actuator, minutes: int) -> str:
        return act.activate(minutes=minutes)


class Admin(User):
    def __init__(self, name: str, email: str, password: str):
        super().__init__(name, email, password)
        self._role = "Admin"

    def role(self) -> str:
        return self._role

    def deactivate_user(self, app: "FarmApp", email: str) -> bool:
        return app.deactivate_user(email)


# =========================================
# Controller / Manager
# =========================================

class FarmApp:
    def __init__(self):
        self._users: Dict[str, User] = {}           # active users
        self._deactivated: Dict[str, User] = {}
        self._fields: Dict[int, Field] = {}
        self._logs: List[str] = []

    # ---- Users ----
    def register_user(self, user: User):
        self._users[user.email] = user
        self._logs.append(f"Registered {user.role()}: {user.name}")

    def deactivate_user(self, email: str) -> bool:
        user = self._users.pop(email, None)
        if user:
            self._deactivated[email] = user
            self._logs.append(f"Deactivated user: {user.name}")
            return True
        return False

    def find_user(self, email: str) -> Optional[User]:
        return self._users.get(email)

    # ---- Fields ----
    def add_field(self, field: Field):
        self._fields[field.id] = field
        self._logs.append(f"Added field {field.name} with crop {field.crop.name}")

    def fields(self) -> List[Field]:
        return list(self._fields.values())

    # ---- Operations ----
    def read_field_sensors(self, field: Field) -> Dict[str, float]:
        readings: Dict[str, float] = {}
        for s in field.sensors():
            readings.update(s.read())
        self._logs.append(f"Read sensors on {field.name}: {readings}")
        return readings

    def run_irrigation(self, field: Field, minutes: int) -> str:
        result_msgs = []
        for a in field.actuators():
            if isinstance(a, (IrrigationPump, Sprinkler)):
                msg = a.activate(minutes=minutes)
                result_msgs.append(msg)
        final = " | ".join(result_msgs) if result_msgs else "No irrigation devices on field."
        self._logs.append(f"Irrigation on {field.name}: {final}")
        return final

    # ---- Reports ----
    @staticmethod
    def count_entities(app: "FarmApp") -> Dict[str, int]:
        return {
            "users_active": len(app._users),
            "users_deactivated": len(app._deactivated),
            "fields": len(app._fields),
            "logs": len(app._logs),
        }

    def timeline(self) -> List[str]:
        return list(self._logs)


# =========================================
# Demo (non-interactive)
# =========================================

def demo() -> str:
    app = FarmApp()

    # Users
    farmer = Farmer("Anita", "anita@farm.com", "farmer123")
    ag = Agronomist("Dr. Rao", "rao@agri.org", "agro456")
    worker = FieldWorker("Sanjay", "sanjay@farm.com", "work789")
    admin = Admin("Priya", "admin@farm.com", "root000")

    for u in (farmer, ag, worker, admin):
        app.register_user(u)

    # Fields & Crops
    rice = Crop("Rice", ideal_moisture_range=(35.0, 60.0))
    wheat = Crop("Wheat", ideal_moisture_range=(20.0, 40.0))

    f1 = Field("North Plot", rice, 2.5)
    f2 = Field("East Plot", wheat, 3.0)

    # Attach devices
    sm1 = SoilMoistureSensor("SMS-101", f1, calibration=1.0)
    ws1 = WeatherStation("WS-201", f1)
    pump1 = IrrigationPump("P-301", f1, capacity_lpm=120)
    spr1 = Sprinkler("SP-401", f1)

    sm2 = SoilMoistureSensor("SMS-102", f2, calibration=0.9)
    ws2 = WeatherStation("WS-202", f2)
    pump2 = IrrigationPump("P-302", f2, capacity_lpm=150)

    for dev in (sm1, ws1, pump1, spr1):
        f1.add_sensor(dev) if isinstance(dev, Sensor) else f1.add_actuator(dev)
        if isinstance(dev, Actuator):
            pass
    # add actuators separately where needed
    f1.add_actuator(pump1)
    f1.add_actuator(spr1)

    for dev in (sm2, ws2, pump2):
        f2.add_sensor(dev) if isinstance(dev, Sensor) else f2.add_actuator(dev)
    f2.add_actuator(pump2)

    # Register fields to system and farmer
    for fld in (f1, f2):
        app.add_field(fld)
        farmer.register_field(fld)

    # Read sensors & get agronomist recommendation
    r1 = app.read_field_sensors(f1)
    moisture1 = r1.get("soil_moisture", 0.0)
    rec_minutes_1 = ag.recommend_irrigation(f1, moisture1)

    # Worker runs irrigation based on recommendation
    if rec_minutes_1 and rec_minutes_1 > 0:
        run_msg_1 = worker.run_actuator(pump1, rec_minutes_1)
        app._logs.append(run_msg_1)
        app.run_irrigation(f1, max(0, rec_minutes_1 - 5))  # top up with sprinklers

    # Field 2
    r2 = app.read_field_sensors(f2)
    moisture2 = r2.get("soil_moisture", 0.0)
    rec_minutes_2 = ag.recommend_irrigation(f2, moisture2)
    if rec_minutes_2 and rec_minutes_2 > 0:
        run_msg_2 = worker.run_actuator(pump2, rec_minutes_2)
        app._logs.append(run_msg_2)
        app.run_irrigation(f2, 0)  # only pump ran above

    # Admin deactivates a user (example of admin power)
    admin.deactivate_user(app, worker.email)

    # Reports
    counts = FarmApp.count_entities(app)

    lines = []
    lines.append(User.platform_info())
    lines.append(User.guidelines())
    lines.append("\n-- FIELDS --")
    for fld in app.fields():
        lines.append(f"{fld} with sensors {[s.info() for s in fld.sensors()]} and actuators {[a.info() for a in fld.actuators()]}")
    lines.append("\n-- SENSOR READINGS --")
    lines.append(f"F1 Readings: {r1}")
    lines.append(f"F2 Readings: {r2}")
    lines.append("\n-- ACTIONS & RECOMMENDATIONS --")
    lines.append(f"Field 1 moisture={moisture1} -> recommend={rec_minutes_1} min")
    lines.append(f"Field 2 moisture={moisture2} -> recommend={rec_minutes_2} min")
    lines.append("\n-- COUNTS --")
    for k, v in counts.items():
        lines.append(f"{k}: {v}")
    lines.append("\n-- TIMELINE --")
    lines.extend(app.timeline())
    lines.append("\n-- ENCAPSULATION CHECK --")
    lines.append(f"Farmer masked password: {farmer.masked_password()} (verify 'wrong'={farmer.verify_password('wrong')}, 'farmer123'={farmer.verify_password('farmer123')})")

    return "\n".join(lines)


if __name__ == "__main__":
    print(demo())
