import datetime


# Calculate the dates of this saturday and sunday
def get_dates_of_saturday_and_sunday():
    today = datetime.date.today()
    idx = (today.weekday() + 1) % 7
    sun = (today + datetime.timedelta(7-idx)).strftime('%Y-%m-%d')
    sat = (today + datetime.timedelta(6-idx)).strftime('%Y-%m-%d')
    return [sat, sun]
