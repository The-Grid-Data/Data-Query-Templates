Documentation:
- Input: Product name (integer type: String1)
- Output: Full data tree of the product with the given name.

Important:
- The variable type must be `String1!` (not `String!`) in the query definition.
- The GraphQL query should have a variable `$product_name: String1!`.
- Use `$product_name` in the `where` clause exactly as: `where: {name: {_eq: $produc_name}}`.
- The variables object must have `"product_name": ?` (a string).
- The query returns multiple fields for the product, including `id`, `rootId`, `name`, `description`, `launchDate`, `isMainProduct`, `productStatusId`, and `productTypeId`.
