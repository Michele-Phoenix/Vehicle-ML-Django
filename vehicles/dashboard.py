def get_frequency_table(data_list, column_name, display_name):
    # Count occurrences for a specific column
    counts = {}
    for row in data_list:
        val = row.get(column_name, 'N/A')
        counts[val] = counts.get(val, 0) + 1
    
    # Sort by value name
    sorted_counts = sorted(counts.items())
    
    # Build HTML table
    table_html = f'<table class="table table-bordered table-striped table-sm text-center">'
    table_html += f'<thead class="table-dark"><tr><th>{display_name}</th><th>Count</th></tr></thead>'
    table_html += '<tbody>'
    for val, count in sorted_counts:
        table_html += f'<tr><td>{val}</td><td>{count}</td></tr>'
    table_html += '</tbody></table>'
    
    return table_html

def frequency_table(data_list):
    # This remains for backward compatibility or as the main entry point
    return get_frequency_table(data_list, 'manufacturer', 'Manufacturer')
