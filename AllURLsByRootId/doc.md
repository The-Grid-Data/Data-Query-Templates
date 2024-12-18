Documentation:
- Input: Root ID (integer type: Int1)
- Output: Full list of urls of a root with the given ID.

Important:
- The variable type must be `Int1!` (not Int!) in the query definition.
- The GraphQL query should have a variable `$root_id: Int1!`.
- Use `$root_id` in the `where` clause exactly as: `where: {id: {_eq: $root_id}}`.
- The variables object must have `"root_id": ?` (an integer, not a string).
- It includes nested fields under a given Root ID: `profileInfos`, `products`, `assets`, `entities` and `socials`.