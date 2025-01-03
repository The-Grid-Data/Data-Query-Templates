Documentation:
- Input: Asset ID (integer type: String2)
- Output: Full data tree of the asset with the given ID.

Important:
- The variable type must be `String2!` (not `String!`) in the query definition.
- The GraphQL query should have a variable `$asset_id: String2!`.
- Use `$asset_id` in the `where` clause exactly as: `where: {id: {_eq: $asset_id}}`.
- The variables object must have `"asset_id": ?` (an integer, not a string).
- The query returns multiple fields for the asset, including `id`, `rootId`, `name`, `description`, `ticker`, `icon`, `assetTypeId`, and `assetStatusId`.
