#!/usr/bin/env python3
"""
Data export utilities for the Cosmic Data Observatory
Exports generated data to JSON, CSV, and Python formats for testing
"""

import json
import csv
from pathlib import Path
from typing import List, Dict, Any, Union
from data_generator import SpaceStationGenerator, AlienContactGenerator, CrewMissionGenerator, DataConfig


class DataExporter:
    """Handles data export in multiple formats"""
    
    def __init__(self, output_dir: str = "generated_data"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
    
    def export_to_json(self, data: List[Dict[str, Any]], filename: str) -> Path:
        """Export data to JSON format"""
        filepath = self.output_dir / f"{filename}.json"
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        return filepath
    
    def export_to_csv(self, data: List[Dict[str, Any]], filename: str) -> Path:
        """Export flat data to CSV format"""
        if not data:
            return None
        
        filepath = self.output_dir / f"{filename}.csv"
        
        # Handle nested data by flattening
        flat_data = []
        for item in data:
            flat_item = self._flatten_dict(item)
            flat_data.append(flat_item)
        
        # Get all unique keys for CSV headers
        all_keys = set()
        for item in flat_data:
            all_keys.update(item.keys())
        
        with open(filepath, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=sorted(all_keys))
            writer.writeheader()
            writer.writerows(flat_data)
        
        return filepath
    
    def export_to_python(self, data: List[Dict[str, Any]], filename: str, variable_name: str) -> Path:
        """Export data as Python variable for direct import"""
        filepath = self.output_dir / f"{filename}.py"
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(f'"""\nGenerated test data for {filename}\n"""\n\n')
            # Use repr() to get proper Python syntax instead of JSON
            f.write(f'{variable_name} = {self._format_python_data(data)}\n')
        
        return filepath
    
    def _format_python_data(self, data: Any, indent: int = 0) -> str:
        """Format data as valid Python code with proper True/False/None"""
        indent_str = '    ' * indent
        next_indent_str = '    ' * (indent + 1)
        
        if data is None:
            return 'None'
        elif isinstance(data, bool):
            return 'True' if data else 'False'
        elif isinstance(data, (int, float)):
            return str(data)
        elif isinstance(data, str):
            # Escape quotes and format as Python string
            return repr(data)
        elif isinstance(data, list):
            if not data:
                return '[]'
            items = []
            for item in data:
                formatted_item = self._format_python_data(item, indent + 1)
                items.append(f'{next_indent_str}{formatted_item}')
            return '[\n' + ',\n'.join(items) + f'\n{indent_str}]'
        elif isinstance(data, dict):
            if not data:
                return '{}'
            items = []
            for key, value in data.items():
                formatted_value = self._format_python_data(value, indent + 1)
                items.append(f'{next_indent_str}{repr(key)}: {formatted_value}')
            return '{\n' + ',\n'.join(items) + f'\n{indent_str}}}'
        else:
            return repr(data)
    
    def _flatten_dict(self, d: Dict[str, Any], parent_key: str = '', sep: str = '_') -> Dict[str, Any]:
        """Flatten nested dictionary for CSV export"""
        items = []
        
        for k, v in d.items():
            new_key = f"{parent_key}{sep}{k}" if parent_key else k
            
            if isinstance(v, dict):
                items.extend(self._flatten_dict(v, new_key, sep=sep).items())
            elif isinstance(v, list) and v and isinstance(v[0], dict):
                # Handle list of dictionaries by creating numbered entries
                for i, item in enumerate(v):
                    if isinstance(item, dict):
                        items.extend(self._flatten_dict(item, f"{new_key}_{i}", sep=sep).items())
                    else:
                        items.append((f"{new_key}_{i}", item))
            elif isinstance(v, list):
                # Simple list - join as string
                items.append((new_key, ', '.join(map(str, v))))
            else:
                items.append((new_key, v))
        
        return dict(items)


def generate_all_datasets():
    """Generate complete datasets for all exercise types"""
    config = DataConfig()
    exporter = DataExporter()
    
    print("🔄 Generating complete datasets...")
    
    # Generate space station data
    station_gen = SpaceStationGenerator(config)
    stations = station_gen.generate_station_data(10)
    
    # Generate alien contact data
    contact_gen = AlienContactGenerator(config)
    contacts = contact_gen.generate_contact_data(15)
    
    # Generate mission data
    mission_gen = CrewMissionGenerator(config)
    missions = mission_gen.generate_mission_data(5)
    
    # Export in multiple formats
    datasets = [
        (stations, "space_stations", "SPACE_STATIONS"),
        (contacts, "alien_contacts", "ALIEN_CONTACTS"),
        (missions, "space_missions", "SPACE_MISSIONS")
    ]
    
    exported_files = []
    
    for data, filename, var_name in datasets:
        # Export to JSON
        json_file = exporter.export_to_json(data, filename)
        exported_files.append(json_file)
        
        # Export to Python
        py_file = exporter.export_to_python(data, filename, var_name)
        exported_files.append(py_file)
        
        # Export to CSV (only for non-nested data)
        if filename != "space_missions":  # Missions have nested crew data
            csv_file = exporter.export_to_csv(data, filename)
            if csv_file:
                exported_files.append(csv_file)
    
    print(f"✅ Generated {len(exported_files)} data files:")
    for file_path in exported_files:
        print(f"  📄 {file_path}")
    
    return exported_files


def create_test_scenarios():
    """Create specific test scenarios for validation testing"""
    config = DataConfig()
    exporter = DataExporter()
    
    # Invalid space station data
    invalid_stations = [
        {
            "station_id": "TOOLONG123456",  # Too long
            "name": "Test Station",
            "crew_size": 25,  # Too many crew
            "power_level": 85.0,
            "oxygen_level": 92.0,
            "last_maintenance": "2024-01-15T10:30:00",
            "is_operational": True
        },
        {
            "station_id": "TS",  # Too short
            "name": "",  # Empty name
            "crew_size": 0,  # No crew
            "power_level": -10.0,  # Negative power
            "oxygen_level": 150.0,  # Over 100%
            "last_maintenance": "2024-01-15T10:30:00",
            "is_operational": True
        }
    ]
    
    # Invalid alien contacts
    invalid_contacts = [
        {
            "contact_id": "WRONG_FORMAT",  # Doesn't start with AC
            "timestamp": "2024-01-15T14:30:00",
            "location": "Area 51",
            "contact_type": "radio",
            "signal_strength": 8.5,
            "duration_minutes": 45,
            "witness_count": 5,
            "message_received": None,  # Strong signal without message
            "is_verified": False
        },
        {
            "contact_id": "AC_2024_002",
            "timestamp": "2024-01-16T09:15:00",
            "location": "Roswell",
            "contact_type": "telepathic",
            "signal_strength": 6.2,
            "duration_minutes": 30,
            "witness_count": 1,  # Too few witnesses for telepathic
            "message_received": None,
            "is_verified": False
        }
    ]
    
    # Export test scenarios
    exporter.export_to_json(invalid_stations, "invalid_stations")
    exporter.export_to_json(invalid_contacts, "invalid_contacts")
    
    print("🧪 Created validation test scenarios")


if __name__ == "__main__":
    generate_all_datasets()
    create_test_scenarios()
    print("\n🎯 All data files ready for testing!")
