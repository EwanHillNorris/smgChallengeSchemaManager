from dataclasses import dataclass
import yaml


@dataclass
class FieldDefinition:
    type: str
    nullable: bool


class SchemaManager:

    def __init__(self, config_path: str):
        with open(config_path) as f:
            config = yaml.safe_load(f)

        self.schema = {
            name: FieldDefinition(**attrs)
            for name, attrs in config["fields"].items()
        }

    def compare(self, incoming_schema: dict):
        changes = {
            "new_fields": [],
            "removed_fields": [],
            "type_changes": []
        }

        expected = self.schema

        for field in incoming_schema:
            if field not in expected:
                changes["new_fields"].append(field)

        for field in expected:
            if field not in incoming_schema:
                changes["removed_fields"].append(field)

        for field, dtype in incoming_schema.items():
            if field in expected and expected[field].type != dtype:
                changes["type_changes"].append({
                    "field": field,
                    "expected": expected[field].type,
                    "actual": dtype
                })

        return changes
