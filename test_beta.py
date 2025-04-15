import os
import re
import requests

ENDPOINT = 'https://beta.node.thegrid.id/graphql'
ROOT_DIR = os.getcwd()

SKIP_FOLDERS = ['Validation', 'DataTools']


def find_query_files(directory):
    """Find all query.gql files in the directory and subdirectories."""
    query_files = []
    for root, dirs, files in os.walk(directory):
        # Skip directories that are in the SKIP_FOLDERS list
        dirs[:] = [d for d in dirs if d not in SKIP_FOLDERS]

        for file in files:
            if file == 'query.gql':
                query_files.append(os.path.join(root, file))
    return query_files

def extract_variables(query_content):
    """Extract variable names from a GraphQL query and create simple test values."""
    variable_regex = r'\$(\w+):\s*(\w+!?)'
    variables = {}

    for match in re.finditer(variable_regex, query_content):
        var_name = match.group(1)
        variables[var_name] = "test-value"

    return variables


def execute_query(query_path, variables):
    """Test a GraphQL query against the endpoint."""
    with open(query_path, 'r') as f:
        query_content = f.read()

    relative_path = os.path.relpath(query_path, ROOT_DIR)

    headers = {'Content-Type': 'application/json'}

    request_data = {
        'query': query_content,
        'variables': variables
    }

    print(f"Testing: {relative_path}")

    try:
        response = requests.post(
            ENDPOINT,
            json=request_data,
            headers=headers,
            timeout=10
        )

        success = 200 <= response.status_code < 300 and 'errors' not in response.json()
        status = '✅' if success else '❌'
        print(f"{status} {relative_path} ({response.status_code})")

        return {
            'path': relative_path,
            'success': success
        }

    except Exception as e:
        print(f"❌ {relative_path} (Error: {str(e)})")
        return {
            'path': relative_path,
            'success': False
        }


def main():
    """Main function to test all GraphQL queries."""
    print(f"GraphQL Query Tester - Testing against {ENDPOINT}")
    print(f"Finding query files in {ROOT_DIR} (skipping {', '.join(SKIP_FOLDERS)})...")

    query_files = find_query_files(ROOT_DIR)
    print(f"Found {len(query_files)} query files.\n")

    results = []

    for query_file in query_files:
        with open(query_file, 'r') as f:
            query_content = f.read()

        mock_variables = extract_variables(query_content)
        result = execute_query(query_file, mock_variables)
        results.append(result)

    successful = sum(1 for r in results if r['success'])
    print(f"\nResults: {successful}/{len(results)} queries successful")


if __name__ == "__main__":
    main()
