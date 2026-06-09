# models.py

from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class FieldDefinition:
    name: str
    data_type: str
    nullable: bool = True


@dataclass(frozen=True)
class TypeChange:
    field: str
    expected_type: str
    actual_type: str


@dataclass
class SchemaDiff:
    new_fields: list[FieldDefinition]
    removed_fields: list[FieldDefinition]
    type_changes: list[TypeChange]

    @property
    def is_compatible(self) -> bool:
        return (
            len(self.removed_fields) == 0
            and len(self.type_changes) == 0
        )
