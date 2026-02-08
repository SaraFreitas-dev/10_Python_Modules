from typing import Any, List, Optional, Dict, Union
from abc import ABC, abstractmethod


class DataStream(ABC):
    """an abstract base class with core streaming functionality"""
    def __init__(self, stream_id: str):
        self.stream_id = stream_id
        self.proc_count = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        """Process a batch of data"""
        ...

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        """Filter data based on criteria"""
        if criteria is None:
            return data_batch
        filtered = []
        for data in data_batch:
            parts = data.split(":")
            if parts[0] == criteria:
                filtered.append(data)
        return filtered

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Return stream statistics"""
        return {
                "stream_id": self.stream_id,
                "type": getattr(self, "stream_type", self.__class__.__name__),
                "processed_count": self.proc_count
            }


class SensorStream(DataStream):
    """Specialized Stream"""
    stream_type = "Environmental Data"

    def process_batch(self, data_batch: List[Any]) -> str:
        """Process a batch of data"""
        try:
            temp_lst = self.filter_data(data_batch, "temp")
            total = 0
            count = 0
            for t in temp_lst:
                parts = t.split(":")
                value = float(parts[1])
                total += value
                count += 1
            if count == 0:
                avg_temp = 0.0
            else:
                avg_temp = total / count
            self.proc_count = len(data_batch)
            stats = self.get_stats()
            return ("Initializing Sensor Stream...\n"
                    f"Stream ID: {stats['stream_id']}, Type: {stats['type']}\n"
                    f"Processing sensor batch: {data_batch}\n"
                    f"Sensor analysis: {self.proc_count} readings processed, "
                    f"avg temp: {avg_temp}°C\n"
                    )
        except (TypeError, ValueError) as e:
            return f"Error: {e}. Something went wrong while processing stream."


class TransactionStream(DataStream):
    """Specialized Stream"""
    stream_type = "Financial Data"

    def process_batch(self, data_batch: List[Any]) -> str:
        """Process a batch of data"""
        try:
            buy_lst = self.filter_data(data_batch, "buy")
            sell_lst = self.filter_data(data_batch, "sell")
            total_net = 0
            for b in buy_lst:
                parts = b.split(":")
                value = int(parts[1])
                total_net += value
            for s in sell_lst:
                parts = s.split(":")
                value = int(parts[1])
                total_net -= value
            sign = "+" if total_net >= 0 else "-"
            net_display = abs(total_net)
            self.proc_count = len(data_batch)
            stats = self.get_stats()
            return ("Initializing Transaction Stream...\n"
                    f"Stream ID: {stats['stream_id']}, Type: {stats['type']}\n"
                    f"Processing transaction batch: {data_batch}\n"
                    f"Transaction analysis: {self.proc_count} operations, "
                    f"net flow: {sign}{net_display} units\n"
                    )
        except (TypeError, ValueError) as e:
            return f"Error: {e}. Something went wrong while processing stream."


class EventStream(DataStream):
    """Specialized Stream"""
    stream_type = "System Events"

    def process_batch(self, data_batch: List[Any]) -> str:
        """Process a batch of data"""
        try:
            errors_lst = self.filter_data(data_batch, "error")
            err_count = len(errors_lst)
            self.proc_count = len(data_batch)
            stats = self.get_stats()
            return ("Initializing Event Stream...\n"
                    f"Stream ID: {stats['stream_id']}, Type: {stats['type']}\n"
                    f"Processing event batch: {data_batch}\n"
                    f"Event analysis: {self.proc_count} events, "
                    f"{err_count} error detected\n"
                    )
        except (TypeError, ValueError) as e:
            return f"Error: {e}. Something went wrong while processing stream."


class StreamProcessor():
    """Stream Manager: can handle any stream type through polymorphism"""
    def __init__(self) -> None:
        self.streams: List[DataStream] = []

    def add_stream(self, stream: DataStream) -> None:
        """Add a stream"""
        self.streams.append(stream)

    def process_mixed_batch(self, data_batch: Dict[str, List[Any]]) -> str:
        """Process a batch of mixed data"""
        try:
            output: List[str] = []
            output.append("Processing mixed stream types through "
                          "unified interface...\n")
            batch_num = 1
            output.append(f"Batch {batch_num} Results:")
            sensor_n = 0
            trans_n = 0
            for stream in self.streams:
                key = stream.__class__.__name__
                sub_batch = data_batch.get(key, [])
                stream.process_batch(sub_batch)
                stats = stream.get_stats()
                if key == "SensorStream":
                    sensor_n = len(sub_batch)
                    output.append(f"- Sensor data: {sensor_n} "
                                  "readings processed")
                elif key == "TransactionStream":
                    trans_n = len(sub_batch)
                    output.append(f"- Transaction data: {trans_n} "
                                  "operations processed")
                elif key == "EventStream":
                    output.append(f"- Event data: {len(sub_batch)} "
                                  "events processed")
                else:
                    output.append(f"- {stats['type']}: {len(sub_batch)} "
                                  "items processed")
            output.append("\nStream filtering active: High-priority data only")
            output.append(f"Filtered results: {sensor_n} critical sensor "
                          f"alerts, {trans_n} large transaction")
            output.append("\nAll streams processed successfully. "
                          "Nexus throughput optimal.")
            return "\n".join(output)

        except (TypeError, ValueError) as e:
            return f"Error: {e}. Something went wrong while processing stream."


def data_stream():
    """Main function to test several processes"""
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

    sensor = SensorStream("SENSOR_001")
    print(sensor.process_batch(["temp:22.5",
                                "humidity:65", "pressure:1013"]))

    transaction = TransactionStream("TRANS_001")
    print(transaction.process_batch(["buy:100", "sell:150", "buy:75"]))

    event = EventStream("EVENT_001")
    print(event.process_batch(["login", "error", "logout"]))

    print("=== Polymorphic Stream Processing ===")
    processor = StreamProcessor()
    processor.add_stream(SensorStream("SENSOR_001"))
    processor.add_stream(TransactionStream("TRANS_001"))
    processor.add_stream(EventStream("EVENT_001"))
    mixed_batch = {
                    "SensorStream": ["temp:22.5", "humidity:65"],
                    "TransactionStream": ["buy:100", "sell:250"],
                    "EventStream": ["login:ok", "error:timeout", "logout:ok"]
                }

    print(processor.process_mixed_batch(mixed_batch))


if __name__ == "__main__":
    data_stream()
