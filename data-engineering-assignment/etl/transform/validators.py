import json
from pathlib import Path
from typing import Dict, List, Any
import re

# Load rules once
RULES_PATH = Path("etl/rules/validation_rules.json")
with open(RULES_PATH, "r") as f:
    VALIDATION_RULES = json.load(f)



def validate_row(row: Dict[str, Any], table: str) -> List[str]:
    """
    Validate a single row based on rules for the given table.
    Returns a list of validation error messages.
    """
    errors = []
    rules = VALIDATION_RULES.get(table, {})

    # Required fields
    for field in rules.get("required_fields", []):
        if not row.get(field):
            errors.append(f"Missing {field}")

    # Regex checks
    for field, pattern in rules.get("regex", {}).items():
        value = row.get(field)
        if value and not re.match(pattern, str(value)):
            errors.append(f"{field} does not match pattern")

    # Type checks
    for field, dtype in rules.get("types", {}).items():
        value = row.get(field)
        if value is not None:
            try:
                if dtype == "int":
                    int(value)
                elif dtype == "float":
                    float(value)
                # Add more types if needed
            except ValueError:
                errors.append(f"{field} must be {dtype}")

    return errors



def validate_rows(rows: List[Dict[str, Any]], table: str) -> (List[Dict[str, Any]], List[Dict[str, Any]]):
    """
    Splits rows into valid and invalid lists based on table-specific rules.
    """
    valid_rows = []
    invalid_rows = []

    for row in rows:
        errors = validate_row(row, table)
        if errors:
            row["_errors"] = errors
            invalid_rows.append(row)
        else:
            valid_rows.append(row)

    return valid_rows, invalid_rows
