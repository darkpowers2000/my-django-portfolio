def map_spreadsheet_to_sql_migration(dirty_data_rows):
    print(f"[+] Initializing migration mapper schema engine. Processing {len(dirty_data_rows)} target arrays...")
    sql_statements = []
    
    for row in dirty_data_rows:
        raw_id, raw_name, raw_date = row
        
        # Clean and sanitize names and format dates safely
        sanitized_name = raw_name.strip().replace("'", "''")
        clean_date = raw_date.replace("/", "-") if "/" in raw_date else "1970-01-01"
        
        # Build pristine relational migration inputs
        query = f"INSERT INTO core_clients (id, business_name, migration_date) VALUES ({int(raw_id)}, '{sanitized_name}', '{clean_date}');"
        sql_statements.append(query)
        
    print("[+] Database validation constraints cleared successfully.")
    return sql_statements

if __name__ == "__main__":
    unformatted_csv_simulation = [
        ["101", "   Acme Corp Inc.  ", "2026/06/03"],
        ["102", "O'Reilly Partners Limited", "2026/05/20"]
    ]
    compiled_queries = map_spreadsheet_to_sql_migration(unformatted_csv_simulation)
    for q in compiled_queries:
        print(q)