import requests

def test_outbound_link_integrity(url_list):
    print(f"[+] Initializing link audit crawler across {len(url_list)} target connections.")
    audit_log = {}
    
    for url in url_list:
        try:
            # Send a fast HEAD request to check server status without loading heavy pages
            response = requests.head(url, timeout=5, allow_redirects=True)
            status = response.status_code
            status_text = "HEALTHY" if status == 200 else "ATTENTION REQUIRED"
        except requests.RequestException:
            status = 404
            status_text = "DEAD / UNREACHABLE ROUTE"
            
        audit_log[url] = {"status_code": status, "diagnostic": status_text}
        print(f"  - Link Check: {url} -> {status} ({status_text})")
        
    return audit_log

if __name__ == "__main__":
    links_to_test = [
        "https://www.google.com",
        "https://httpbin.org/status/404",
        "https://thisdomainiscompletelyfake12345.org"
    ]
    test_outbound_link_integrity(links_to_test)