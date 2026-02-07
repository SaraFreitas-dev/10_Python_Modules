from typing import Any
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    """Initialize the base abstract class."""
    def __init__(self) -> None:
        pass

    @abstractmethod
    def process(self, data: Any) -> str:
        """Process input data and return a formatted result."""
        ...

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """Validate input data before processing."""
        ...

    def format_output(self, result: str) -> str:
        """Return the processing result."""
        return (result)


class NumericProcessor(DataProcessor):
    """Process, validate and format nombers"""
    def __init__(self) -> None:
        super().__init__()

    def process(self, data: Any) -> str:
        """Process input data and return a formatted result."""
        try:
            if not self.validate(data):
                return "Error: invalid numeric data."
            total = 0
            total_sum = 0
            for num in data:
                total += 1
                total_sum += float(num)
            avg = total_sum / total
            return ("Initializing Numeric Processor...\n"
                    f"Processing data: {data}\n"
                    f"Validation: Numeric data verified\n"
                    f"Output: Processed {total} numeric values, "
                    f"sum={total_sum:.0f}, avg={avg:.1f}\n")
        except (TypeError, ValueError) as e:
            return f"Error: {e}. Something went wrong while processing data."

    def validate(self, data: Any) -> bool:
        """Validate input data before processing."""
        try:
            if isinstance(data, (str, bytes)):
                return False
            for i in data:
                float(i)
            return True
        except Exception:
            return False

    def format_output(self, result: str) -> str:
        """Return the processing result."""
        return super().format_output(result)


class TextProcessor(DataProcessor):
    """Process, validate and format text"""
    def __init__(self) -> None:
        super().__init__()

    def process(self, data: Any) -> str:
        """Process input data and return a formatted result."""
        try:
            if not self.validate(data):
                return "Error: invalid text data."
            chars = len(data)
            words = len(data.split())
            return (
                "Initializing Text Processor...\n"
                f"Processing data: \"{data}\"\n"
                "Validation: Text data verified\n"
                f"Output: Processed text: {chars} characters, {words} words\n"
            )
        except (TypeError, ValueError) as e:
            return f"Error: {e}. Something went wrong while processing data."

    def validate(self, data: Any) -> bool:
        """Validate input data before processing."""
        return isinstance(data, str)

    def format_output(self, result: str) -> str:
        """Return the processing result."""
        return super().format_output(result)


class LogProcessor(DataProcessor):
    """Process, validate and format logs"""
    def __init__(self) -> None:
        super().__init__()

    def process(self, data: Any) -> str:
        """Process input data and return a formatted result."""
        try:
            if not self.validate(data):
                return "Error: invalid log data."
            log_txt = data.split(":")
            if (log_txt[0] == "ERROR"):
                output = "[ALERT] ERROR level detected"
            elif (log_txt[0] == "OK"):
                output = "[INFO] INFO level detected"
            else:
                return ("Log processor error: "
                        f"\'{log_txt[0]}\' not valid")
            return (
                "Initializing Log Processor...\n"
                f"Processing data: \"{data}\"\n"
                f"Validation: Log entry verified\n"
                f"Output: {output}:{log_txt[1]}\n"
            )
        except (TypeError, ValueError) as e:
            return f"Error: {e}. Something went wrong while processing data."

    def validate(self, data: Any) -> bool:
        """Validate input data before processing."""
        return isinstance(data, str)

    def format_output(self, result: str) -> str:
        """Return the processing result."""
        return super().format_output(result)


def stream_processor():
    """Run processing demo using multiple processors."""
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")
    processors = [
        (NumericProcessor(), [1, 2, 3, 4, 5]),
        (TextProcessor(), "Hello Nexus World"),
        (LogProcessor(), "ERROR: Connection timeout")
    ]
    for proc, data in processors:
        print(f"{proc.process(data)}")

    print("=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...")
    processors_pol = [
        (NumericProcessor(), [1, 2, 3]),
        (TextProcessor(), "Hello World!"),
        (LogProcessor(), "OK: System ready")
    ]
    for i, (proc, data) in enumerate(processors_pol):
        result = proc.process(data)
        last_line = result.strip().split("\n")[-1]
        print(f"Result {i + 1}: {last_line.replace('Output: ', '')}")

    print("\nFoundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    stream_processor()
