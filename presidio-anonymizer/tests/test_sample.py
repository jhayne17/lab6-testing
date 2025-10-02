from presidio_anonymizer.sample import sample_run_anonymizer


def test_sample_run_anonymizer_replaces_person():
    # Arrange + Act
    result = sample_run_anonymizer("My name is Bond.", 11, 15, "BIP")

    # Assert (use string form to avoid depending on internal classes)
    s = str(result)
    assert "text: My name is BIP." in s
    # The anonymized token spans 11–14 (3 chars: BIP)
    assert "'start': 11" in s
    assert "'end': 14" in s
    assert "'entity_type': 'PERSON'" in s
    assert "'text': 'BIP'" in s
    assert "'operator': 'replace'" in s
