Documentation:
- Input: Root ID (integer type: Int2)
- Output: Full data tree of the profile with the given ID.

Important:
- The variable type must be `Int2!` (not `Int!`) in the query definition.
- The GraphQL query should have a variable `$root_id: Int2!`.
- Use `$root_id` in the `where` clause exactly as: `where: {id: {_eq: $root_id}}`.
- The variables object must have `"root_id": ?` (an integer, not a string).
- The query returns multiple fields for the root, including `id`, `slug`, and `urlMain`.
