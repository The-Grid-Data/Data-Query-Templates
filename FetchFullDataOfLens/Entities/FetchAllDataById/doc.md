Documentation:
- Input: Entity ID (integer type: String2)
- Output: Full data tree of the entity with the given ID.

Important:
- The variable type must be `String2!` (not `String!`) in the query definition.
- The GraphQL query should have a variable `$entity_id: String2!`.
- Use `$entity_id` in the `where` clause exactly as: `where: {id: {_eq: $entity_id}}`.
- The variables object must have `"entity_id": ?` (an integer, not a string).
- The query returns multiple fields for the entity, including `id`, `leiNumber`, `localRegistrationNumber`, `name`, `rootId`, `taxIdentificationNumber`, `tradeName`, `entityTypeId`, `dateOfIncorporation`, `countryId`, and `address`.
