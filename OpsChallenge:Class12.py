import requests

# Define header code translations
header_translations = {
    400: "Bad Request",
    401: "Unauthorized",
    403: "Forbidden",
    404: "Site not found",
    405: "Method Not Allowed",
    500: "Internal Server Error",
    502: "Bad Gateway",
    503: "Service Unavailable",
}

# Prompt user for URL and HTTP method
url = input("Enter the URL you want to access: ")
method = input(
    "Select HTTP method (GET, POST, PUT, DELETE, HEAD, PATCH, OPTIONS): "
).upper()

# Validate user input
valid_methods = {"GET", "POST", "PUT", "DELETE", "HEAD", "PATCH", "OPTIONS"}
if method not in valid_methods:
    print(f"Invalid method '{method}'. Please select a valid option.")
    exit(1)

# Print request information for confirmation
print(f"\nPreparing to send a {method} request to {url}.")
print(f"Request headers:")
print(f"\tUser-Agent: Python requests/{requests.__version__}")

# Ask for confirmation before proceeding
confirm = input("Continue (y/n): ").lower()
if confirm not in {"y", "yes"}:
    print("Request cancelled.")
    exit(0)

# Send request and get response
response = requests.request(method, url)

# Translate and print response code
status_code = response.status_code
print(f"\nResponse code: {status_code}")
if status_code in header_translations:
    print(f"\tTranslation: {header_translations[status_code]}")

# Print response headers
print(f"\nResponse headers:")
for header, value in response.headers.items():
    print(f"\t{header}: {value}")

# Print response content (optional)
# print(f"\nResponse content:")
# print(response.content)

print("\nRequest completed.")
