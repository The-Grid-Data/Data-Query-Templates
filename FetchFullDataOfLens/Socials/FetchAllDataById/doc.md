Documentation:
- Input: Social ID (integer type: Int1)
- Output: Full data tree of the social with the given ID.

Important:
- The variable type must be `Int1!` (not `Int!`) in the query definition.
- The GraphQL query should have a variable `$social_id: Int1!`.
- Use `$social_id` in the `where` clause exactly as: `where: {id: {_eq: $social_id}}`.
- The variables object must have `"social_id": ?` (an integer, not a string).
- The query returns multiple fields for the social, including `id`, `rootId`, `name`, and `socialTypeId`.
