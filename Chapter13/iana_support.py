import datetime
from zoneinfo import ZoneInfo
nyc_tz = ZoneInfo("America/New_York")
la_tz = ZoneInfo("America/Los_Angeles")
dt = datetime.datetime(2022, 5, 21, hour=12, tzinfo=nyc_tz)
print(dt.isoformat())
