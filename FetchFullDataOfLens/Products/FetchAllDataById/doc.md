Documentation:
- Input: Product ID (string type: String1)
- Output: Full data tree of the product with the given ID.

Important:
- The variable type must be `String1` (not `String1`) in the query definition.
- The GraphQL query should have a variable `$product_id: String1`.
- Use `$product_id` in the `where` clause exactly as: `where: {id: {_eq: $product_id}}`.
- The variables object must have `"product_id": ?` (an integer, not a string).
- The query returns multiple fields for the product, including `id`, `rootId`, `name`, `description`, `launchDate`, `isMainProduct`, `productStatusId`, and `productTypeId`.
