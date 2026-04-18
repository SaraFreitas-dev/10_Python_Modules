#!/usr/bin/env python3
"""
Cosmic Data Observatory - Data Generator
Generates realistic test data for space station monitoring, alien contacts, and crew missions.
"""

import random
from datetime import datetime, timedelta
from typing import List, Dict, Any
from dataclasses import dataclass


@dataclass
class DataConfig:
    """Configuration parameters for data generation"""
    seed: int = 42
    base_date: datetime = datetime(2024, 1, 1)
    date_range_days: int = 365


class SpaceStationGenerator:
    """Generates space station monitoring data"""
    
    STATION_NAMES = [
        "International Space Station", "Lunar Gateway", "Mars Orbital Platform",
        "Europa Research Station", "Titan Mining Outpost", "Asteroid Belt Relay",
        "Deep Space Observatory", "Solar Wind Monitor", "Quantum Communications Hub"
    ]
    
    STATION_PREFIXES = ["ISS", "LGW", "MOP", "ERS", "TMO", "ABR", "DSO", "SWM", "QCH"]
    
    def __init__(self, config: DataConfig):
        self.config = config
        random.seed(config.seed)
    
    def generate_station_data(self, count: int = 5) -> List[Dict[str, Any]]:
        """Generate multiple space station records"""
        stations = []
        
        for i in range(count):
            station_id = f"{random.choice(self.STATION_PREFIXES)}{random.randint(100, 999)}"
            name = random.choice(self.STATION_NAMES)
            
            # Realistic operational parameters
            crew_size = random.randint(3, 12)
            power_level = round(random.uniform(70.0, 98.5), 1)
            oxygen_level = round(random.uniform(85.0, 99.2), 1)
            
            # Recent maintenance date
            days_ago = random.randint(1, 180)
            maintenance_date = self.config.base_date - timedelta(days=days_ago)
            
            # Operational status based on system health
            is_operational = power_level > 75.0 and oxygen_level > 90.0
            
            # Optional maintenance notes
            notes = None
            if not is_operational:
                notes = "System diagnostics required"
            elif random.random() < 0.3:
                notes = "All systems nominal"
            
            stations.append({
                "station_id": station_id,
                "name": name,
                "crew_size": crew_size,
                "power_level": power_level,
                "oxygen_level": oxygen_level,
                "last_maintenance": maintenance_date.isoformat(),
                "is_operational": is_operational,
                "notes": notes
            })
        
        return stations


class AlienContactGenerator:
    """Generates alien contact report data"""
    
    LOCATIONS = [
        "Area 51, Nevada", "Roswell, New Mexico", "SETI Institute, California",
        "Arecibo Observatory, Puerto Rico", "Atacama Desert, Chile",
        "Antarctic Research Station", "International Space Station",
        "Mauna Kea Observatory, Hawaii", "Very Large Array, New Mexico"
    ]
    
    CONTACT_TYPES = ["radio", "visual", "physical", "telepathic"]
    
    MESSAGES = [
        "Greetings from Zeta Reticuli",
        "Mathematical sequence detected: prime numbers",
        "Coordinates to star system received",
        "Warning about solar flare activity",
        "Request for peaceful contact",
        "Unknown language pattern identified"
    ]
    
    def __init__(self, config: DataConfig):
        self.config = config
        random.seed(config.seed + 1)
    
    def generate_contact_data(self, count: int = 8) -> List[Dict[str, Any]]:
        """Generate multiple alien contact records"""
        contacts = []
        
        for i in range(count):
            contact_id = f"AC_{self.config.base_date.year}_{str(i+1).zfill(3)}"
            
            # Random contact timing within date range
            days_offset = random.randint(0, self.config.date_range_days)
            contact_time = self.config.base_date + timedelta(days=days_offset)
            
            location = random.choice(self.LOCATIONS)
            contact_type = random.choice(self.CONTACT_TYPES)
            
            # Signal characteristics
            signal_strength = round(random.uniform(1.0, 10.0), 1)
            duration = random.randint(5, 240)  # 5 minutes to 4 hours
            witnesses = random.randint(1, 15)
            
            # Message content for strong signals
            message = None
            if signal_strength > 6.0 and random.random() < 0.7:
                message = random.choice(self.MESSAGES)
            
            # Verification status
            is_verified = False
            if contact_type == "physical":
                is_verified = True  # Physical contacts must be verified
            elif contact_type == "radio" and signal_strength > 8.0:
                is_verified = random.random() < 0.8
            
            # Adjust witnesses for telepathic contacts
            if contact_type == "telepathic" and witnesses < 3:
                witnesses = random.randint(3, 8)
            
            contacts.append({
                "contact_id": contact_id,
                "timestamp": contact_time.isoformat(),
                "location": location,
                "contact_type": contact_type,
                "signal_strength": signal_strength,
                "duration_minutes": duration,
                "witness_count": witnesses,
                "message_received": message,
                "is_verified": is_verified
            })
        
        return contacts


class CrewMissionGenerator:
    """Generates space crew and mission data"""
    
    FIRST_NAMES = [
        "Sarah", "John", "Alice", "Michael", "Emma", "David", "Lisa", "Robert",
        "Maria", "James", "Anna", "William", "Elena", "Thomas", "Sofia", "Daniel"
    ]
    
    LAST_NAMES = [
        "Connor", "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia",
        "Miller", "Davis", "Rodriguez", "Martinez", "Hernandez", "Lopez", "Gonzalez"
    ]
    
    SPECIALIZATIONS = [
        "Mission Command", "Navigation", "Engineering", "Life Support",
        "Communications", "Medical Officer", "Pilot", "Science Officer",
        "Maintenance", "Security", "Research", "Systems Analysis"
    ]
    
    RANKS = ["cadet", "officer", "lieutenant", "captain", "commander"]
    
    DESTINATIONS = [
        "Mars", "Moon", "Europa", "Titan", "Asteroid Belt",
        "Jupiter Orbit", "Saturn Rings", "Deep Space", "Solar Observatory"
    ]
    
    def __init__(self, config: DataConfig):
        self.config = config
        random.seed(config.seed + 2)
    
    def generate_crew_member(self, member_id: str) -> Dict[str, Any]:
        """Generate a single crew member"""
        name = f"{random.choice(self.FIRST_NAMES)} {random.choice(self.LAST_NAMES)}"
        rank = random.choice(self.RANKS)
        age = random.randint(25, 55)
        specialization = random.choice(self.SPECIALIZATIONS)
        
        # Experience correlates with age and rank
        base_experience = max(0, age - 22)
        rank_bonus = {"cadet": 0, "officer": 2, "lieutenant": 5, "captain": 8, "commander": 12}
        years_experience = min(base_experience + rank_bonus[rank] + random.randint(-2, 3), 30)
        
        return {
            "member_id": member_id,
            "name": name,
            "rank": rank,
            "age": age,
            "specialization": specialization,
            "years_experience": max(0, years_experience),
            "is_active": True
        }
    
    def generate_mission_data(self, count: int = 3) -> List[Dict[str, Any]]:
        """Generate complete mission records with crews"""
        missions = []
        
        for i in range(count):
            mission_id = f"M{self.config.base_date.year}_{random.choice(['MARS', 'LUNA', 'EUROPA', 'TITAN'])}"
            destination = random.choice(self.DESTINATIONS)
            mission_name = f"{destination} {'Colony' if random.random() < 0.5 else 'Research'} Mission"
            
            # Mission timing
            launch_offset = random.randint(30, 300)
            launch_date = self.config.base_date + timedelta(days=launch_offset)
            
            # Mission parameters
            duration = random.randint(90, 1200)  # 3 months to 3+ years
            budget = round(random.uniform(500.0, 5000.0), 1)
            
            # Generate crew (3-8 members)
            crew_size = random.randint(3, 8)
            crew = []
            
            # Ensure at least one high-ranking officer
            has_commander = False
            for j in range(crew_size):
                member_id = f"CM{str(i*10 + j + 1).zfill(3)}"
                member = self.generate_crew_member(member_id)
                
                # First member has higher chance of being high-ranking
                if j == 0 and not has_commander:
                    member["rank"] = random.choice(["captain", "commander"])
                    has_commander = True
                
                crew.append(member)
            
            # For long missions, ensure experienced crew
            if duration > 365:
                experienced_needed = len(crew) // 2
                experienced_count = sum(1 for member in crew if member["years_experience"] >= 5)
                
                if experienced_count < experienced_needed:
                    # Boost experience for some crew members
                    for member in crew[:experienced_needed]:
                        if member["years_experience"] < 5:
                            member["years_experience"] = random.randint(5, 15)
            
            missions.append({
                "mission_id": mission_id,
                "mission_name": mission_name,
                "destination": destination,
                "launch_date": launch_date.isoformat(),
                "duration_days": duration,
                "crew": crew,
                "mission_status": "planned",
                "budget_millions": budget
            })
        
        return missions


def main():
    """Generate sample data for all exercise types"""
    config = DataConfig()
    
    print("🚀 Cosmic Data Observatory - Sample Data Generator")
    print("=" * 60)
    
    # Generate space station data
    station_gen = SpaceStationGenerator(config)
    stations = station_gen.generate_station_data(5)
    
    print(f"\n📡 Generated {len(stations)} space stations:")
    for station in stations:
        status = "✅ Operational" if station["is_operational"] else "⚠️  Maintenance"
        print(f"  {station['station_id']}: {station['name']} - {status}")
    
    # Generate alien contact data
    contact_gen = AlienContactGenerator(config)
    contacts = contact_gen.generate_contact_data(6)
    
    print(f"\n👽 Generated {len(contacts)} alien contacts:")
    for contact in contacts:
        verified = "✅ Verified" if contact["is_verified"] else "❓ Unverified"
        print(f"  {contact['contact_id']}: {contact['contact_type']} at {contact['location']} - {verified}")
    
    # Generate mission data
    mission_gen = CrewMissionGenerator(config)
    missions = mission_gen.generate_mission_data(3)
    
    print(f"\n🚀 Generated {len(missions)} space missions:")
    for mission in missions:
        print(f"  {mission['mission_id']}: {mission['mission_name']}")
        print(f"    Crew: {len(mission['crew'])} members, Duration: {mission['duration_days']} days")
    
    print("\n" + "=" * 60)
    print("Data generation complete! Use these generators in your exercises.")


if __name__ == "__main__":
    main()
