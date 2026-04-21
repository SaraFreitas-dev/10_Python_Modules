from pydantic import BaseModel, Field, ValidationError  # type: ignore
from pydantic import model_validator  # type: ignore
from typing import Union
from enum import Enum
from datetime import datetime


class Rank(str, Enum):
    """
    Define crew ranks
    """
    CADET = "Mission helper"
    OFFICER = "Engineering"
    LIEUTENANT = "Navigation"
    CAPTAIN = "Captain boss"
    COMMANDER = "Mission Command"


class CrewMember(BaseModel):
    """
    Individual crew member information
    """
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True  # default value


class SpaceMission(BaseModel):
    """
    Mission information plus the crew info
    """
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)  # Max 10 years
    crew: list[CrewMember] = Field(min_length=1, max_length=12)  # 1-12 members
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def validate_event_constraints(self):
        # Rule 1: Mission ID must start with "M"
        if not self.mission_id.startswith("M"):
            raise ValueError("Contact ID must start with 'M'")
        # Rule 2: Must have at least one Commander or Captain
        found = False
        for member in self.crew:
            if member.rank == Rank.COMMANDER or member.rank == Rank.CAPTAIN:
                found = True
                break
        if not found:
            raise ValueError("Mission must have at least "
                             "one Commander or Captain")
        # Rule 3: Long missions (> 365 days)
        # need 50% experienced crew (5+ years)
        if self.duration_days > 365:
            experienced_crew = 0
            for member in self.crew:
                if member.years_experience >= 5:
                    experienced_crew += 1

            total = len(self.crew)

            if experienced_crew < total / 2:
                raise ValueError("Long missions require at least "
                                 "50% experienced crew")
        # All crew members must be active
        if any(not member.is_active
               for member in self.crew):
            raise ValueError("All crew members must be active")
        return self


def create_mission(data: dict) -> Union[SpaceMission, None]:
    """
    Check if data is valid and return a SpaceMission model to use in report
    Or the error message if its invalid
    """
    try:
        return SpaceMission(**data)
    except ValidationError as e:
        print("\n=========================================\n"
              "Expected validation error:")
        for err in e.errors():
            print(err["msg"])


def report(space_m: SpaceMission) -> None:
    """
    Prints the report on the terminal from a certain SpaceMission model
    """
    try:
        print("Space Mission Crew Validation\n"
              "=========================================")
        print("Valid mission created:\n"
              f"Mission: {space_m.mission_name}\n"
              f"ID: {space_m.mission_id}\n"
              f"Destination: {space_m.destination}\n"
              f"Duration: {space_m.duration_days} days\n"
              f"Budget: ${space_m.budget_millions}M\n"
              f"Crew size: {len(space_m.crew)}\n"
              f"Crew members:")
        for member in space_m.crew:
            print(f"- {member.name} ({member.rank.name.lower()}) - "
                  f"{member.rank.value}")
    except Exception as e:
        print(f"ERROR ON REPORT(): {e}")


if __name__ == '__main__':
    # OK MISSION
    mission_data = {
        "mission_id": "M2024_MARS",
        "mission_name": "Mars Colony Establishment",
        "destination": "Mars",
        "launch_date": datetime(2024, 1, 1, 10, 0, 0),
        "duration_days": 900,
        "budget_millions": 2500.0,
        "crew": [
            {
                "member_id": "C001",
                "name": "Sarah Connor",
                "rank": Rank.COMMANDER,
                "age": 45,
                "specialization": "Leadership",
                "years_experience": 20,
                "is_active": True
            },
            {
                "member_id": "C002",
                "name": "John Smith",
                "rank": Rank.LIEUTENANT,
                "age": 35,
                "specialization": "Navigation",
                "years_experience": 10,
                "is_active": True
            },
            {
                "member_id": "C003",
                "name": "Alice Johnson",
                "rank": Rank.OFFICER,
                "age": 30,
                "specialization": "Engineering",
                "years_experience": 8,
                "is_active": True
            }
        ]
    }

    ok_mission = create_mission(mission_data)
    if isinstance(ok_mission, SpaceMission):
        report(ok_mission)

    # KO MISSION (sem commander/captain)
    failed_mission = {
        "mission_id": "M2024_FAIL",
        "mission_name": "Mars Colony Establishment",
        "destination": "Mars",
        "launch_date": datetime(2024, 1, 1, 10, 0, 0),
        "duration_days": 900,
        "budget_millions": 2500.0,
        "crew": [
            {
                "member_id": "C004",
                "name": "John Smith",
                "rank": Rank.LIEUTENANT,
                "age": 35,
                "specialization": "Navigation",
                "years_experience": 10,
                "is_active": True
            },
            {
                "member_id": "C005",
                "name": "Alice Johnson",
                "rank": Rank.OFFICER,
                "age": 30,
                "specialization": "Engineering",
                "years_experience": 8,
                "is_active": True
            }
        ]
    }

    ko_mission = create_mission(failed_mission)
    if isinstance(ko_mission, SpaceMission):
        report(ko_mission)
