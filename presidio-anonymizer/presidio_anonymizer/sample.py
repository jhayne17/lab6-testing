from presidio_anonymizer import AnonymizerEngine
from presidio_anonymizer.entities import RecognizerResult, OperatorConfig


def sample_run_anonymizer(text: str, start: int, end: int, replacement: str = "BIP"):
    """
    Run the anonymizer with given parameters.

    :param text: Input text
    :param start: Start index of entity
    :param end: End index of entity
    :param replacement: Replacement string for the entity
    :return: Anonymization result
    """
    # Initialize the engine
    engine = AnonymizerEngine()

    # Invoke the anonymize function with the text, analyzer results, and operators
    result = engine.anonymize(
        text=text,
        analyzer_results=[
            RecognizerResult(entity_type="PERSON", start=start, end=end, score=0.8)
        ],
        operators={"PERSON": OperatorConfig("replace", {"new_value": replacement})},
    )

    # Print for demonstration
    print(result)

    return result


if __name__ == "__main__":
    # Example run with parameters for manual execution
    output = sample_run_anonymizer("My name is Bond.", 11, 15, "BIP")
    # Save to variable 'output' so it can be used in future tests if needed
