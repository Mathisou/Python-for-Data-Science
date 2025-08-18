from datetime import datetime

seconds = (datetime.now() - datetime(1970, 1, 1)).total_seconds()
print(f"Seconds since January 1, 1970: {seconds:,} or {seconds:.2e} in scientific notation")

print(datetime.now().strftime("%b %d %Y"))