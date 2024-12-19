Documentation:
- Input: Entity name (string type: String1)
- Output: Full data tree of the entity with the given name.

Important:
- The variable type must be `String1!` (not `String!`) in the query definition.
- The GraphQL query should have a variable `$entity_name: String1!`.
- Use `$entity_name` in the `where` clause exactly as: `where: {name: {_eq: $entity_name}}`.
- The variables object must have `"entity_name": ?` (a string).
- The query returns multiple fields for the entity, including `id`, `leiNumber`, `localRegistrationNumber`, `name`, `rootId`, `taxIdentificationNumber`, `tradeName`, `entityTypeId`, `dateOfIncorporation`, `countryId`, and `address`.
