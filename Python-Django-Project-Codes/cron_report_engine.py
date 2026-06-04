from datetime import datetime
import json
import os

def generate_cron_business_brief(data_source_dict):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H%M")
    report_filename = f"daily_brief_{timestamp}.json"
    
    print(f"[+] Cron Scheduler triggered successfully at {datetime.now()}")
    
    payload_wrapper = {
        "generated_at": str(datetime.now()),
        "pipeline_integrity": "SECURE",
        "metrics": data_source_dict
    }
    
    with open(report_filename, 'w') as file:
        json.dump(payload_wrapper, file, indent=4)
        
    print(f"[+] Daily matrix compiled. Object dumped cleanly to file storage system as: {report_filename}")

if __name__ == "__main__":
    mock_inventory_dataset = {"total_items_processed": 14205, "system_health_index": "100%"}
    generate_cron_business_brief(mock_inventory_dataset)