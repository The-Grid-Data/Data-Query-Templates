Documentation:
- Input: Social ID (string type: String1)
- Output: Full data tree of the social with the given name.

Important:
- The variable type must be `String1!` (not `String!`) in the query definition.
- The GraphQL query should have a variable `$social_name: String1!`.
- Use `$social_name` in the `where` clause exactly as: `where: {name: {_eq: $social_name}}`.
- The variables object must have `"social_name": ?` (a string).
- The query returns multiple fields for the social, including `id`, `rootId`, `name`, and `socialTypeId`.
