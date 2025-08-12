from datetime import datetime

def check_date_range(start_date_str, end_date_str):
    """check if date range is valid - returns (is_valid, result)"""
    try:
        start = datetime.strptime(start_date_str, '%Y-%m-%d').date()
        end = datetime.strptime(end_date_str, '%Y-%m-%d').date()
        
        # start cant be after end
        if start > end:
            return False, "Start date cannot be after end date"
        
        # max 30 days
        if (end - start).days > 30:
            return False, "Date range cannot exceed 30 days"
            
        return True, (start, end)
    except ValueError:
        return False, "Invalid date format. Use YYYY-MM-DD"
