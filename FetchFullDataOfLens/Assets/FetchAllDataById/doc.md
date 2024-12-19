Documentation:
- Input: Asset ID (integer type: Int1)
- Output: Full data tree of the asset with the given ID.

Important:
- The variable type must be `Int1!` (not `Int!`) in the query definition.
- The GraphQL query should have a variable `$asset_id: Int1!`.
- Use `$asset_id` in the `where` clause exactly as: `where: {id: {_eq: $asset_id}}`.
- The variables object must have `"asset_id": ?` (an integer, not a string).
- The query returns multiple fields for the asset, including `id`, `rootId`, `name`, `description`, `ticker`, `icon`, `assetTypeId`, and `assetStatusId`.
