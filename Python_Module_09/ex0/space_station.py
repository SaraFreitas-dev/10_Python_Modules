from pydantic import BaseModel, Field, ValidationError     # type: ignore
# For windows python3 -m venv venv
# source venv/bin/activate
# pip install pydantic
# deactivate (to leave venv)
from typing import Optional
from datetime import datetime


class SpaceStation_Model(BaseModel):
    """
    The Cosmic Data Observatory monitors hundreds of space
    stations across the galaxy.
    Each station reports vital statistics including crew size,
    power levels, and operational status.
    This class creates a SpaceStation model and
    acts as a validation system for this critical data.
    """
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    # ge = Greater or equal / le = Less or equal
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True  # Default value
    notes: Optional[str] = Field(default=None, max_length=200)


def report(station: SpaceStation_Model) -> None:
    """Prints the report on the terminal from a certain SpaceStation model"""
    try:
        print("Space Station Data Validation\n"
              "========================================")
        print("Valid station created:\n"
              f"ID: {station.station_id}\n"
              f"Name: {station.name}\n"
              f"Crew: {station.crew_size} people\n"
              f"Power: {station.power_level}%\n"
              f"Oxygen: {station.oxygen_level}%")
        status = "Operational" if station.is_operational else "Not operational"
        print(f"Status: {status}\n")

    except ValidationError as e:
        print("========================================\n"
              "Expected validation error:")
        for err in e.errors():
            print(err["msg"])


if __name__ == "__main__":
    try:
        station_data = {
            "station_id": "ISS001",
            "name": "International Space Station",
            "crew_size": 6,
            "power_level": 85.5,
            "last_maintenance": datetime(2024, 1, 1, 10, 0, 0),
            "oxygen_level": 92.3,
            "is_operational": True
        }
        int_station = SpaceStation_Model(**station_data)
        report(int_station)

        failed_station = {
            "station_id": "ISS001",
            "name": "International Space Station",
            "crew_size": 25,
            "power_level": 85.5,
            "last_maintenance": datetime(2024, 1, 1, 10, 0, 0),
            "oxygen_level": 92.3,
            "is_operational": True
        }
        f_station = SpaceStation_Model(**failed_station)
        report(f_station)

    except ValidationError as e:
        print("========================================\n"
              "Expected validation error:")
        for err in e.errors():
            print(err["msg"])
