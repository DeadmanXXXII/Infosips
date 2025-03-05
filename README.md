# InfoSips - SIP Information Stealer

InfoSips is a penetration testing tool designed for ethical hacking and security research on vulnerable sips endpoints.
Use responsibly and report vulnerabilities to affected vendors.

## Infosips Script

This script exploits a vulnerable endpoints dynamically using wildcards to gather user information. It supports various command-line arguments for flexibility.


Yes, you can modify the script to request information from each stage dynamically. Instead of sending one request with a wildcard path, the script will iterate through each possible structure and send multiple requests, capturing responses from every stage.

---

How This Works:

1. Iterate Over Each Level: The script will generate different URL structures based on a specified wildcard depth.


2. Send Requests for Each Variation: It will send a request for:

/users/*

/users/*/*

/users/*/*/*

and so on, up to the specified depth.



3. Capture and Store Responses: Each response is logged and optionally saved to a file.




4. Dynamically Generates URL Paths:

The script starts with https://{base_url}/sips/sipsys/users/*

Then https://{base_url}/sips/sipsys/users/*/*

Then https://{base_url}/sips/sipsys/users/*/*/*

This continues up to --wildcard-depth (default: 3)



5. Sends Requests for Each Stage:

Requests data from each level

Stores responses if successful



6. Saves Responses to a File (Optional):

If --output file.txt is used, all responses are stored for later analysis.

Sends requests to:

https://example.com/sips/sipsys/users/*
https://example.com/sips/sipsys/users/*/*
https://example.com/sips/sipsys/users/*/*/*



---

How This Works:

1. Iterate Over Each Level: The script will generate different URL structures based on a specified wildcard depth.


2. Send Requests for Each Variation: It will send a request for:

/users/*

/users/*/*

/users/*/*/*

and so on, up to the specified depth.



3. Capture and Store Responses: Each response is logged and optionally saved to a file.





How This Works:

1. Dynamically Generates URL Paths:

The script starts with https://{base_url}/sips/sipsys/users/*

Then https://{base_url}/sips/sipsys/users/*/*

Then https://{base_url}/sips/sipsys/users/*/*/*

This continues up to --wildcard-depth (default: 3)



2. Sends Requests for Each Stage:

Requests data from each level

Stores responses if successful



3. Saves Responses to a File (Optional):

If --output file.txt is used, all responses are stored for later analysis.


---


✅ Requests Information from Every Stage
✅ Automatically Iterates Through Depths
✅ Handles Errors Gracefully (404, Timeout, etc.)
✅ Supports Output to File for Offline Analysis
✅ Works with Proxies and Custom Headers


---

## Installation
```bash
pip install infosips
```

Thank you for providing the script! Based on the functionality of your script, here's the correct list of commands and arguments your script accepts:

# Commands and Usage

## Usage

Run the script with the following command:

```bash
python infosips.py <base_url> [options]
```
Arguments

base_url (required): The base URL of the vulnerable server you are trying to exploit.


Optional Arguments:

--disable-ssl: Disable SSL verification for the request (useful if the server has invalid SSL certificates).

--timeout <seconds>: Set the timeout for the HTTP request (default is 10 seconds).

--verbose: Enable verbose output for detailed logging during the execution (logs request and response details).

--headers <json>: Provide custom headers in JSON format to include in the request. Example:

{"User-Agent": "my-custom-agent"}

--proxy <url>: Set a proxy server for the request. Example:

--proxy http://proxy.example.com

--output <file>: Specify an output file to save the responses retrieved from the server. The file will be saved in the same directory as the script.

--wildcard-depth <depth>: Specify the maximum depth of wildcards in the URL path (default is 3). This will control how many levels of wildcards (*) are used in the request URLs.


Example Commands

1. Basic usage with base URL:
```
python infosips.py http://vulnerable-server.com
```

2. Enable verbose output and custom headers:
```
python infosips.py http://vulnerable-server.com --verbose --headers '{"User-Agent": "my-custom-agent"}'
```

3. Use a proxy and disable SSL verification:
```
python infosips.py http://vulnerable-server.com --proxy http://proxy.example.com --disable-ssl
```

4. Save responses to a file:
```
python infosips.py http://vulnerable-server.com --output responses.txt
```

5. Set a custom timeout (5 seconds) and deeper wildcard depth (5 levels):
```
python infosips.py http://vulnerable-server.com --timeout 5 --wildcard-depth 5
```


Notes:

Wildcard paths are dynamically generated from the base URL. The script will attempt to exploit the endpoint at different wildcard depths to gather user information.

If a resource is not found (404), it will log a warning. If a request fails for other reasons, it will log an error message with the status code.

If an output file is provided, all successful responses will be saved in the specified file for further analysis.
