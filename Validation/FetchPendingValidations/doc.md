Documentation:
- Input: None (no parameters required)
- Output: List of all validation records with pending status.

Important:
- The query filters validation records using a hardcoded value: isPending: {_eq: "1"}
- The isPending value is passed as a string ("1") rather than a boolean
- The query returns all fields in the validation table for pending records