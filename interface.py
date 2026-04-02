from typing import Protocol, Dict, Any

class ISerializable(Protocol):
    def to_dict(self) -> Dict[str, Any]:
        ...