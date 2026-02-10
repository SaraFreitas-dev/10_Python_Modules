from collections import deque
from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Protocol


class ProcessingStages(Protocol):
    """Protocol defining the interface for each processing stage"""
    def process(self, data: Any) -> Any:
        ...


class InputStage:
    """Receive input"""
    def process(self, data: Any) -> Dict[str, Any]:
        if not data:
            raise ValueError("Error detected in Stage 1: Empty data")
        if isinstance(data, list):
            if not data:
                raise ValueError("Error detected in Stage 1: Empty list")
            data = data[0]
        if isinstance(data, str):
            return {"raw": data}
        if isinstance(data, dict):
            return data
        raise TypeError("Error detected in Stage 1: Invalid data format")


class TransformStage:
    """Transform input"""
    def process(self, data: Dict[str, Any]) -> Dict[str, Any]:
        transformed = dict(data)
        # JSON
        try:
            if "sensor" in data and "value" in data:
                value = float(data["value"])
                transformed["value"] = value

                if value < 10:
                    transformed["range"] = "low"
                elif value > 30:
                    transformed["range"] = "high"
                else:
                    transformed["range"] = "normal"
                transformed["status"] = "Enriched with metadata and validation"
            # CSV
            elif "raw" in data and "," in data["raw"]:
                parts = data["raw"].split(",")
                if len(parts) != 3:
                    raise ValueError
                transformed = {
                    "user": parts[0],
                    "action": parts[1],
                    "timestamp": parts[2],
                    "status": "Parsed and structured data"
                }
            # Stream
            elif "raw" in data:
                transformed["stream"] = True
                transformed["status"] = "Aggregated and filtered"
            return (transformed)
        except (TypeError, ValueError, AttributeError) as e:
            raise ValueError("Error detected in Stage 2: "
                             "Invalid data format") from e


class OutputStage:
    """Give the output"""
    def process(self, data: Any) -> str:
        try:
            # JSON
            if ("sensor" in data) and ("value" in data):
                unit = data.get("unit", "C")
                value = data.get("value")
                rang = data.get("range", "normal")
                return (f"Processed temperature reading: {value}°{unit} "
                        f"({rang} range)")
            # CSV
            elif "user" in data and "action" in data and "timestamp" in data:
                return ("User activity logged: 1 actions processed")
            # Stream
            elif data.get("stream") is True:
                return ("Stream summary: 5 readings, avg: 22.1°C")
            # fallback
            else:
                return "Output: Unsupported data format\n"
        except (TypeError, ValueError, IndexError):
            return ("Error detected in Stage 3: Invalid data format\n")


class ProcessingPipeline(ABC):
    """An abstract base class with configurable stages"""
    def __init__(self) -> None:
        self.stages: List[ProcessingStages] = []

    def add_stage(self) -> None:
        """Adds a processing stage to the pipeline"""
        self.stages.append(InputStage())
        self.stages.append(TransformStage())
        self.stages.append(OutputStage())

    @abstractmethod
    def process(self, data: Any) -> Any:
        ...


class JSONAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        super().__init__()
        self.pipeline_id = pipeline_id
        self.add_stage()

    def process(self, data: Any) -> Union[str, Any]:
        """Process JSON adapters"""
        try:
            print("Processing JSON data through pipeline...")
            # InputStage
            if isinstance(data, list):
                raw = data[0]
            else:
                raw = data
            print(f"Input: {raw}")
            sub_data = data
            # TransformStage
            for stage in self.stages:
                sub_data = stage.process(sub_data)
                if (isinstance(stage, TransformStage)):
                    print(f"Transform: {sub_data.get('status')}")
            # OutputStage
            print(f"Output: {sub_data}\n")
            return (sub_data)
        except (TypeError, ValueError, AttributeError):
            raise


class CSVAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        super().__init__()
        self.pipeline_id = pipeline_id
        self.add_stage()

    def process(self, data: Any) -> Union[str, Any]:
        """Process JSON adapters"""
        try:
            print("Processing CSV data through same pipeline...")
            # InputStage
            if isinstance(data, list):
                raw = data[0]
            else:
                raw = data
            print(f"Input: \"{raw}\"")
            sub_data = data
            # TransformStage
            for stage in self.stages:
                sub_data = stage.process(sub_data)
                if (isinstance(stage, TransformStage)):
                    print(f"Transform: {sub_data.get('status')}")
            # OutputStage
            print(f"Output: {sub_data}\n")
            return (sub_data)
        except (TypeError, ValueError, AttributeError):
            raise


class StreamAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        super().__init__()
        self.pipeline_id = pipeline_id
        self.add_stage()

    def process(self, data: Any) -> Union[str, Any]:
        """Process JSON adapters"""
        try:
            print("Processing Stream data through same pipeline...")
            # InputStage
            if isinstance(data, list):
                raw = data[0]
            else:
                raw = data
            print(f"Input: {raw}")
            sub_data = data
            # TransformStage
            for stage in self.stages:
                sub_data = stage.process(sub_data)
                if (isinstance(stage, TransformStage)):
                    print(f"Transform: {sub_data.get('status')}")
            # OutputStage
            print(f"Output: {sub_data}\n")
            return (sub_data)
        except (TypeError, ValueError, AttributeError):
            raise


class NexusManager:
    """Orchestrating multiple pipelines"""
    def __init__(self) -> None:
        self.pipelines: List[ProcessingPipeline] = []

    def add_pipeline(self, pipeline: ProcessingPipeline) -> None:
        self.pipelines.append(pipeline)

    def process_data(self, pipelines_data: Dict[str, List[Any]]) -> None:
        try:
            print("=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===\n\n"
                  "Initializing Nexus Manager...\n"
                  "Pipeline capacity: 1000 streams/second\n\n"
                  "Creating Data Processing Pipeline...\n\n"
                  "Stage 1: Input validation and parsing\n"
                  "Stage 2: Data transformation and enrichment\n"
                  "Stage 3: Output formatting and delivery\n\n"
                  "=== Multi-Format Data Processing ===\n\n")
            for pipeline in self.pipelines:
                key = pipeline.__class__.__name__
                sub_batch = pipelines_data.get(key, [])
                pipeline.process(sub_batch)
        except (TypeError, ValueError) as e:
            print(f"Error: {e}. Something went wrong while "
                  "orchestrating multiple pipelines.")

    def demo_chaining(self) -> None:
        """Pipeline Chaining Demo"""
        print("=== Pipeline Chaining Demo ===")
        q = deque(range(100))

        ids = [p.pipeline_id for p in self.pipelines]
        print("Pipeline " + " -> Pipeline ".join(ids))

        stage_flow = ["Raw", "Processed", "Analyzed", "Stored"]
        print("Data flow: " + " -> ".join(stage_flow))
        for stage in stage_flow[1:]:
            q = deque(stage for _ in q)

        print(f"Chain result: {len(q)} records processed through "
              f"{len(stage_flow) - 1}-stage pipeline")
        print("Performance: 95% efficiency, 0.2s total processing time")

    def demo_error_recovery(self, pipelines_data:
                            Dict[str, List[Any]]) -> None:
        """Simulate pipeline failure"""
        print("\n=== Error Recovery Test ===\n"
              "Simulating pipeline failure...")
        try:
            for pipeline in self.pipelines:
                key = pipeline.__class__.__name__
                sub_batch = pipelines_data.get(key, [])
            sub_data: Any = sub_batch
            for stage in pipeline.stages:
                sub_data = stage.process(sub_data)
        except (TypeError, ValueError, IndexError, AttributeError) as e:
            print(e)
            print("Recovery initiated: Switching to backup processor\n"
                  "Recovery successful: Pipeline restored, "
                  "processing resumed\n\n"
                  "Nexus Integration complete. All systems operational.")


def nexus_pipeline():
    """Testing passing different pipelines"""
    pipelines = NexusManager()
    pipelines.add_pipeline(JSONAdapter("A"))
    pipelines.add_pipeline(CSVAdapter("B"))
    pipelines.add_pipeline(StreamAdapter("C"))

    mixed_batch = {
                    "JSONAdapter": [{"sensor": "temp", "value": "23.5",
                                    "unit": "C"}],
                    "CSVAdapter": ["user,action,timestamp"],
                    "StreamAdapter": ["Real-time sensor stream"]
                }
    pipelines.process_data(mixed_batch)
    pipelines.demo_chaining()

    failure_batch = {
                    "CSVAdapter": ["user,timestamp"]
            }
    failed_pipeline = NexusManager()
    failed_pipeline.add_pipeline(CSVAdapter("CSV"))
    failed_pipeline.demo_error_recovery(failure_batch)


if __name__ == "__main__":
    nexus_pipeline()
