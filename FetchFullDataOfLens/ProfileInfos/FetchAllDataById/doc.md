Documentation:
- Input: Profile ID (integer type: String2)
- Output: Full data tree of the profile with the given ID.

Important:
- The variable type must be `String2!` (not `String!`) in the query definition.
- The GraphQL query should have a variable `$profile_info_id: String2!`.
- Use `$profile_info_id` in the `where` clause exactly as: `where: {id: {_eq: $profile_info_id}}`.
- The variables object must have `"profile_info_id": ?` (an integer, not a string).
- The query returns multiple fields for the profile info, including `id`, `rootId`, `name`, `logo`, `descriptionShort`, `descriptionLong`, `tagLine`, `foundingDate`, `profileStatusId`, `profileSectorId`, and `profileTypeId`.
