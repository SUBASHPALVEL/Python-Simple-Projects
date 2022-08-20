# 1 importing statement

import phonenumbers as ph
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone

# 2 Getting the phone number from user

number = input(" Phone Number: ")
number = ph.parse(number)

# 3 Getting details of the phone number

country = geocoder.description_for_number(number, "en")
sim_card_provider = carrier.name_for_number(number, "en")
time_zone = timezone.time_zones_for_number(number)

# 4 Displaying the details

print("Country: ", country)
print("Sim_card provider: ", sim_card_provider)
print("Time Zone: ", time_zone)