# 1 importing statements

import time
import psutil
from plyer import notification


# 2 Accessing battery information

battery = psutil.sensors_battery()
percent = battery.percent

# 3 Notifying the remaining battery percentage

notification.notify(
    title="Battery Percentage",
    message=str(percent) + "% Battery Remaining",
    timeout=20
)

