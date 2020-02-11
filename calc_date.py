# Day of Week --> Date

# DoW = day of week

# Assumes the date only gets smaller.
# e.g. querying about "Wed", "Tue", "Wed" means this Wednesday, this Tuesday...
# and the Wednesday from last week.

# Usage:
# 1. Use the factory to create a function with starting date and the DoW of that date.
# 2. Supply the DoW of the day you want to know the date.
# 3. The function returns the date.
# Tweak it to conform to date formats you use.
def calc_date_factory(start_dow, start_date):
    # remember the results from the previous query
    last_date = start_date
    last_dow = start_dow

    def calc_date(dow, skipped_weeks=0):
        # binds the names to the outside variables
        nonlocal last_date
        nonlocal last_dow

        # diff: the # of days from the desired date to now
        diff = (last_dow - dow) % 7 + skipped_weeks * 7
        this_date = last_date - diff

        # update states
        last_date = this_date
        last_dow = dow
        return this_date
    
    return calc_date


if __name__ == "__main__":
    calc_date = calc_date_factory(1, 30) # Today is Monday, 30th

    # See the attached image to get what this does
    print(calc_date(7)) # Last Sunday (Sunday from 1 week ago) is 29th
    print(calc_date(5)) # Last Friday is 27th
    print(calc_date(4)) # Last Thursday is 26th
    print(calc_date(4)) # Same, still 26th
    print(calc_date(3)) # Last Wednesday is 25th

    # If you want to specify skipped weeks
    # Same as regular results minus (7 * skipped_weeks)
    print(calc_date(2, 1)) # Tuesday from 2 weeks ago is 17th
    print(calc_date(5, 1)) # Friday from 4 weeks ago is 6th

