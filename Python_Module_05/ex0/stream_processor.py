from typing import Any
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def process(self, data: Any) -> str:
        ...

    @abstractmethod
    def validate(self, data: Any) -> bool:
        ...

    def format_output(self, result: str) -> str:
        return (f"Output: {result}")


class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def process(self, data: Any) -> str:
        try:
            if not self.validate(data):
                return "Error: invalid numeric data."
            total = 0
            sum = 0
            for num in data:
                total += 1
                sum += num
            avg = sum / total
            return (f"Processing data: {data}\n"
                    f"Validation: Numeric data verified\n"
                    f"Output: Processed {total} numeric values, "
                    f"sum={sum}, avg={avg:.1f}\n")
        except (TypeError, ValueError) as e:
            return f"Error: {e}. Something went wrong while processing data."

    def validate(self, data) -> bool:
        try:
            for i in data:
                float(i)
            return True
        except Exception:
            return False

    def format_output(self, result: str) -> str:
        return (result)


class TextProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()


class LogProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()


def stream_processor():
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")
    numeric_data = NumericProcessor()
    result = numeric_data.process([1, 2, 3, 4, 5])
    print(numeric_data.format_output(result))


if __name__ == "__main__":
    stream_processor()
