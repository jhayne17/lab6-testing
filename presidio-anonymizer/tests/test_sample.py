# tests/test_sample.py
from presidio_anonymizer.sample import sample_run_anonymizer


def test_sample_run_anonymizer_replaces_person_bond_example():
    # Act
    result = sample_run_anonymizer("My name is Bond.", 11, 15, "BIP")

    # Assert final text
    assert result.text == "My name is BIP."

    # Assert exactly one OperatorResult
    assert isinstance(result.items, list)
    assert len(result.items) == 1

    item = result.items[0]  # This is an OperatorResult object

    # Use attribute access (NOT subscripting)
    assert item.entity_type == "PERSON"
    assert item.text == "BIP"
    assert item.operator == "replace"

    # Explicit start/end asserts
    assert item.start == 11
    assert item.end == 14  # replacement occupies indices 11–13 (3 chars)

    # Length check
    assert (item.end - item.start) == len("BIP")
