Documentation:
- Input: Profile name (string type: String1)
- Output: Full data tree of the profile with the given name.

Important:
- The variable type must be `String1!` (not `String!`) in the query definition.
- The GraphQL query should have a variable `$profile_info_name: String1!`.
- Use `$profile_info_name` in the `where` clause exactly as: `where: {name: {_eq: $profile_info_name}}`.
- The variables object must have `"profile_info_name": ?` (a string).
- The query returns multiple fields for the profile info, including `id`, `rootId`, `name`, `logo`, `descriptionShort`, `descriptionLong`, `tagLine`, `foundingDate`, `profileStatusId`, `profileSectorId`, and `profileTypeId`.
