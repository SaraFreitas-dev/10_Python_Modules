#!/usr/bin/env python3
"""
Cyber Archives Training Data Generator

Generates structured test data for file operation exercises with comprehensive
error handling, type safety, and extensible architecture.
"""

import json
import sys
from functools import wraps
from pathlib import Path
from typing import Dict, List, Optional, Union, Callable, Any
from datetime import datetime


def handle_file_errors(func: Callable) -> Callable:
    """Decorator for consistent file operation error handling."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except FileNotFoundError as e:
            print(f"Error: File not found - {e}")
            return None
        except PermissionError as e:
            print(f"Error: Permission denied - {e}")
            return None
        except IOError as e:
            print(f"Error: I/O operation failed - {e}")
            return None
        except Exception as e:
            print(f"Unexpected error in {func.__name__}: {e}")
            return None
    return wrapper


def validate_output(func: Callable) -> Callable:
    """Decorator to validate generated content before writing."""
    @wraps(func)
    def wrapper(self, filename: str, content: str, *args, **kwargs):
        if not content or not content.strip():
            raise ValueError(f"Empty content for {filename}")
        if len(content) > 10000:  # Reasonable size limit
            raise ValueError(f"Content too large for {filename}")
        return func(self, filename, content, *args, **kwargs)
    return wrapper


class DataTemplates:
    """Centralized template definitions with metadata."""

    @staticmethod
    def get_templates() -> Dict[str, Dict[str, Union[str, List[str]]]]:
        """Returns all available data templates."""
        return {
            "ancient_fragment": {
                "content": [
                    "[FRAGMENT 001] Digital preservation protocols "
                    "established 2087",
                    "[FRAGMENT 002] Knowledge must survive the entropy "
                    "wars",
                    "[FRAGMENT 003] Every byte saved is a victory against "
                    "oblivion"
                ],
                "type": "historical_data",
                "encoding": "utf-8"
            },
            "classified_data": {
                "content": [
                    "[CLASSIFIED] Quantum encryption keys recovered",
                    "[CLASSIFIED] Archive integrity: 100%"
                ],
                "type": "security_data",
                "classification": "restricted"
            },
            "security_protocols": {
                "content": "[CLASSIFIED] New security protocols archived",
                "type": "protocol_data",
                "version": "3.1.0"
            },
            "standard_archive": {
                "content": "Knowledge preserved for humanity",
                "type": "standard_data",
                "status": "active"
            },
            "corrupted_archive": {
                "content": "DATA_CORRUPTION_ERROR_0x7F4A",
                "type": "error_simulation",
                "error_code": "0x7F4A"
            }
        }


class ArchiveDataGenerator:
    """Main data generation class with comprehensive file operations."""

    def __init__(self, base_path: Optional[str] = None) -> None:
        """Initialize generator with optional base path."""
        self.base_path = Path(base_path) if base_path else Path(".")
        self.templates = DataTemplates.get_templates()
        self.generated_files: List[str] = []

        # Ensure base directory exists
        try:
            self.base_path.mkdir(parents=True, exist_ok=True)
        except Exception as e:
            print(f"Warning: Could not create base directory: {e}")

    @validate_output
    @handle_file_errors
    def _write_file(self, filename: str, content: str) -> bool:
        """Write content to file with comprehensive error handling."""
        file_path = self.base_path / filename

        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)

        self.generated_files.append(filename)
        print(f"Generated: {filename}")
        return True

    def _format_content(self, template_data: Dict[str, Any]) -> str:
        """Format template content into string representation."""
        content = template_data.get("content", "")

        if isinstance(content, list):
            return "\n".join(content)
        elif isinstance(content, str):
            return content
        else:
            return str(content)

    @handle_file_errors
    def generate_ancient_fragment(self) -> Optional[bool]:
        """Generate ancient fragment training file."""
        template = self.templates["ancient_fragment"]
        content = self._format_content(template)
        return self._write_file("ancient_fragment.txt", content)

    @handle_file_errors
    def generate_classified_data(self) -> Optional[bool]:
        """Generate classified data training file."""
        template = self.templates["classified_data"]
        content = self._format_content(template)
        return self._write_file("classified_data.txt", content)

    @handle_file_errors
    def generate_security_protocols(self) -> Optional[bool]:
        """Generate security protocols training file."""
        template = self.templates["security_protocols"]
        content = self._format_content(template)
        return self._write_file("security_protocols.txt", content)

    @handle_file_errors
    def generate_standard_archive(self) -> Optional[bool]:
        """Generate standard archive training file."""
        template = self.templates["standard_archive"]
        content = self._format_content(template)
        return self._write_file("standard_archive.txt", content)

    @handle_file_errors
    def generate_corrupted_archive(self) -> Optional[bool]:
        """Generate corrupted archive simulation file."""
        template = self.templates["corrupted_archive"]
        content = self._format_content(template)
        return self._write_file("corrupted_archive.txt", content)

    @handle_file_errors
    def generate_sample_json(self) -> Optional[bool]:
        """Generate JSON configuration with metadata and scenarios."""
        sample_data = {
            "metadata": {
                "version": "2.1.0",
                "generated": datetime.now().isoformat(),
                "generator": "ArchiveDataGenerator"
            },
            "file_types": [
                "ancient_fragment",
                "classified_data",
                "standard_archive"
            ],
            "test_scenarios": [
                {
                    "name": "basic_recovery",
                    "files": ["ancient_fragment.txt"],
                    "description": "Basic file reading operations"
                },
                {
                    "name": "secure_access",
                    "files": ["classified_data.txt"],
                    "description": "Secure file handling with context "
                                   "managers"
                },
                {
                    "name": "crisis_response",
                    "files": [
                        "standard_archive.txt",
                        "corrupted_archive.txt"
                    ],
                    "description": "Error handling and exception "
                                   "management"
                }
            ],
            "templates": {
                name: {
                    "type": template.get("type", "unknown"),
                    "has_content": bool(template.get("content"))
                }
                for name, template in self.templates.items()
            }
        }

        try:
            json_content = json.dumps(
                sample_data,
                indent=2,
                ensure_ascii=False
            )
            return self._write_file("sample_data.json", json_content)
        except (TypeError, ValueError) as e:
            print(f"Error serializing JSON data: {e}")
            return None

    def generate_all_files(self) -> Dict[str, bool]:
        """Generate all training files and return success status."""
        print("=== CYBER ARCHIVES - DATA GENERATOR ===")
        print("Generating training files...")
        print()

        # Define generation methods with their descriptions
        generators = [
            (self.generate_ancient_fragment, "Ancient fragment data"),
            (self.generate_classified_data, "Classified security data"),
            (self.generate_security_protocols,
             "Security protocol definitions"),
            (self.generate_standard_archive, "Standard archive content"),
            (self.generate_corrupted_archive, "Corrupted data simulation"),
            (self.generate_sample_json, "JSON configuration sample")
        ]

        results = {}
        successful = 0

        for generator_func, description in generators:
            try:
                result = generator_func()
                results[generator_func.__name__] = result is not None
                if result:
                    successful += 1
            except Exception as e:
                print(f"Failed to generate {description}: {e}")
                results[generator_func.__name__] = False

        print()
        print(f"Generation complete: {successful}/{len(generators)} "
              f"files created successfully")

        if successful == len(generators):
            print("All training files ready for Data Archivist exercises")
        else:
            print("Some files failed to generate - check error messages "
                  "above")

        return results

    def get_generated_files(self) -> List[str]:
        """Return list of successfully generated files."""
        return self.generated_files.copy()

    def cleanup_generated_files(self) -> int:
        """Remove all generated files and return count of deleted files."""
        deleted_count = 0

        for filename in self.generated_files:
            try:
                file_path = self.base_path / filename
                if file_path.exists():
                    file_path.unlink()
                    deleted_count += 1
            except Exception as e:
                print(f"Could not delete {filename}: {e}")

        self.generated_files.clear()
        return deleted_count


def main() -> None:
    """Main entry point with command-line argument handling."""
    try:
        # Check for optional base path argument
        base_path = sys.argv[1] if len(sys.argv) > 1 else None

        generator = ArchiveDataGenerator(base_path)
        results = generator.generate_all_files()

        # Exit with appropriate code based on results
        if all(results.values()):
            sys.exit(0)
        else:
            sys.exit(1)

    except KeyboardInterrupt:
        print("\nGeneration interrupted by user")
        sys.exit(130)
    except Exception as e:
        print(f"Fatal error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
