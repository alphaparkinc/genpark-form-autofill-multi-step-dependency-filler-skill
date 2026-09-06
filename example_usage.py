import json
from client import FormAutofillMultiStepDependencyFiller

def main():
    filler = FormAutofillMultiStepDependencyFiller()
    target_data = {
        "postal_code": "94105",
        "country": "US",
        "state": "CA",
        "full_name": "Jordan Lee"
    }
    available_fields = ["state", "country", "postal_code", "full_name"]
    result = filler.plan_autofill_sequence(target_data, available_fields)
    print("Autofill Sequence Plan:")
    print(json.dumps(result, indent=2))
    steps = [p["field"] for p in result["execution_plan"]]
    assert steps.index("country") < steps.index("state")
    assert steps.index("state") < steps.index("postal_code")
    print("Form autofill dependency filler verification: PASS")

if __name__ == "__main__":
    main()
