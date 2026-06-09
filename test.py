def test_detects_new_field():

    expected = {
        "id": FieldDefinition("id", "integer")
    }

    incoming = {
        "id": "integer",
        "email": "string"
    }

    diff = schema_manager.compare(incoming)

    assert len(diff.new_fields) == 1
    assert diff.new_fields[0].name == "email"
    assert diff.is_compatible

def test_detects_removed_field():

    incoming = {}

    diff = schema_manager.compare(incoming)

    assert len(diff.removed_fields) == 1
    assert not diff.is_compatible

def test_detects_type_change():

    incoming = {
        "id": "string"
    }

    diff = schema_manager.compare(incoming)

    assert len(diff.type_changes) == 1
    assert diff.type_changes[0].field == "id"
    assert not diff.is_compatible

def test_matching_schema():

    incoming = {
        "id": "integer"
    }

    diff = schema_manager.compare(incoming)

    assert diff.new_fields == []
    assert diff.removed_fields == []
    assert diff.type_changes == []
    assert diff.is_compatible
