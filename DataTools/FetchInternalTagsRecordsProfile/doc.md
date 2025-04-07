Documentation:
- Input: Row ID (variable type: String3)
- Output: List of internal tags associated with a specific record identified by row ID and table name

Important:
- The variable type must be String3 in the query definition
- The GraphQL query has a variable $row_id: String3
- Use $row_id in the where clause exactly as: where: {rowId: {_eq: $row_id}}
- The tableName parameter is hardcoded to "profileInfos"
- The query filters internal tag records by both row ID and table name