Documentation:
- Input: Asset name (integer type: String1)
- Output: Full data tree of the asset with the given name.

Important:
- The variable type must be `String1!` (not `String!`) in the query definition.
- The GraphQL query should have a variable `$asset_name: String1!`.
- Use `$asset_name` in the `where` clause exactly as: `where: {name: {_eq: $asset_name}}`.
- The variables object must have `"asset_name": ?` (a string).
- The query returns multiple fields for the asset, including `id`, `rootId`, `name`, `description`, `ticker`, `icon`, `assetTypeId`, and `assetStatusId`.
