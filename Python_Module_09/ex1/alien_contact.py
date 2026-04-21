from pydantic import BaseModel, Field, ValidationError  # type: ignore
from pydantic import model_validator  # type: ignore
from typing import Optional, Union
from enum import Enum
from datetime import datetime


class ContactType(str, Enum):
    """
    Types of contact
    """
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    """
    The Observatory receives reports of alien contact from across the galaxy.
    These sensitive reports require sophisticated validation rules that go
    beyond simple field constraints.
    Different contact types have different requirements, and certain
    combinations of data indicate potentially fraudulent reports.
    This class creates the template and rules on each contact model
    """
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=300)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)  # max 24h
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = False  # Default value

    @model_validator(mode='after')
    def validate_event_constraints(self):
        # Rule 1: ID must start with "AC"
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with 'AC'")
        # Rule 2: Physical contacts must be verified
        if self.contact_type == ContactType.PHYSICAL and not self.is_verified:
            raise ValueError("Physical contacts must be verified")
        # Rule 3: Telepathic contact requires at least 3 witnesses
        if (
            self.contact_type == ContactType.TELEPATHIC
            and self.witness_count < 3
        ):
            raise ValueError("Telepathic contact requires "
                             "at least 3 witnesses")
        # Rule 4: Strong signals (> 7.0) should include received message
        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError("Strong signals must include a received message")
        return self


def create_contact(data: dict) -> Union[AlienContact, None]:
    """
    Check if data is valid and return a AlienContact model to use in report
    Or the error message if its invalid
    """
    try:
        return AlienContact(**data)
    except ValidationError as e:
        print("======================================\n"
              "Expected validation error:")
        for err in e.errors():
            print(err["msg"])


def report(alien_c: AlienContact) -> None:
    """
    Prints the report on the terminal from a certain AlienContact model
    """
    try:
        print("Alien Contact Log Validation\n"
              "======================================")
        print("Valid contact report:\n"
              f"ID: {alien_c.contact_id}\n"
              f"Type: {alien_c.contact_type.value}\n"
              f"Location: {alien_c.location}\n"
              f"Signal: {alien_c.signal_strength}/10\n"
              f"Duration: {alien_c.duration_minutes} minutes\n"
              f"Witnesses: {alien_c.witness_count}")
        if alien_c.message_received:
            print(f"Message: '{alien_c.message_received}'")
    except Exception as e:
        print(f"ERROR ON REPORT(): {e}")


if __name__ == '__main__':
    # OK ALIEN_CONTACT
    contact_data = {
        "contact_id": "AC_2024_001",
        "timestamp": datetime(2024, 1, 1, 10, 0, 0),
        "contact_type": ContactType.RADIO,
        "location": "Area 51, Nevada",
        "signal_strength": 8.5,
        "duration_minutes": 45,
        "witness_count": 5,
        "message_received": "Greetings from Zeta Reticuli"
    }
    ok_contact = create_contact(contact_data)
    if isinstance(ok_contact, AlienContact):
        report(ok_contact)

    # KO ALIEN_CONTACT
    failed_contact = {
        "contact_id": "AC_2013_002",
        "timestamp": datetime(2024, 1, 1, 10, 0, 0),
        "contact_type": ContactType.TELEPATHIC,
        "location": "Area 51, Nevada",
        "signal_strength": 8.5,
        "duration_minutes": 45,
        "witness_count": 1,
        "message_received": "Greetings from Nevermore"
    }
    ko_contact = create_contact(failed_contact)
    if isinstance(ko_contact, AlienContact):
        report(ko_contact)
