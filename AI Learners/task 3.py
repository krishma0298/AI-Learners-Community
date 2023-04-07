def calculate_working_hours(start_time, end_time):
    """
    Calculates the number of hours Chef works.
    start_time: starting time in 12-hour clock format
    end_time: ending time in 12-hour clock format
    returns: number of hours Chef works
    """
    if end_time < start_time:
        end_time += 12
    
    working_hours = end_time - start_time
    
    return working_hours
start_time = 9  
end_time = 2    
working_hours = calculate_working_hours(start_time, end_time)
print(f"Chef works for {working_hours} hours.")

