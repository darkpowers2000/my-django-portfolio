import re

def clean_and_parse_raw_strings(unstructured_blob):
    print("[+] Running structural regex pipeline parsing algorithms...")
    
    # Target common data patterns via string processing
    email_pattern = re.compile(r'[\w\.-]+@[\w\.-]+\.\w+')
    phone_pattern = re.compile(r'\+?\d{1,3}[-.\s]?\d{3}[-.\s]?\d{3}[-.\s]?\d{4}')
    
    emails = email_pattern.findall(unstructured_blob)
    phones = phone_pattern.findall(unstructured_blob)
    
    print(f"[+] Scrubbed structural layers. Found {len(emails)} emails and {len(phones)} telephone links.")
    return {"emails": list(set(emails)), "phones": list(set(phones))}

if __name__ == "__main__":
    sample_garbage_text = "Contact management via sales@prime.com or reach out to desk line +1 555-019-2834. Alternately write direct support team at support@prime.com."
    cleansed_data = clean_and_parse_raw_strings(sample_garbage_text)
    print(cleansed_data)