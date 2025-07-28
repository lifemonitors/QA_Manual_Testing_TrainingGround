import requests
import argparse
from colorama import Fore, init

init(autoreset=True)

def test_login_form(url, username, password):
    session = requests.Session()

    payload = {
        "email": username,
        "password": password,
    }

    try:
        response = session.post(url, data=payload, timeout=10, allow_redirects=True)
    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"[ERROR] Request failed:\n{e}")
        return

    print(f"\nTarget URL: {Fore.CYAN + url}")
    print(f"Status Code: {Fore.YELLOW + str(response.status_code)}")

    if "incorrect" in response.text.lower() or "invalid" in response.text.lower():
        print(Fore.GREEN + "✅ Error message displayed as expected for invalid login.")
    elif response.url != url:
        print(Fore.YELLOW + "⚠️ Redirected after login attempt. Possibly accepted credentials or redirected to error page.")
        print("Final URL:", response.url)
    else:
        print(Fore.RED + "❌ No visible error or redirect. Check manually.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Test login form with invalid credentials.")
    parser.add_argument("url", help="Login form URL (e.g., https://example.com/login)")
    parser.add_argument("--username", default="fakeuser@mail.com", help="Fake email to test")
    parser.add_argument("--password", default="fakepass", help="Fake password to test")
    args = parser.parse_args()

    test_login_form(args.url, args.username, args.password)
