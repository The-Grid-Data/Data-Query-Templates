Documentation:
- Input: Root ID (variable type: String3)
- Output: List of notes associated with the specified root ID.

Important:
- The variable type must be String3 (not String!) in the query definition
- The GraphQL query has a variable $root_id: String3
- Use $root_id in the where clause exactly as: where: {notes: {rootId: {_eq: $root_id}}}
- The query retrieves notes nested under the specified root ID