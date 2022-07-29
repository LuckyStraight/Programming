import phonenumbers
from mynumber import number

from phonenumbers import geocoder
ch_number = phonenumbers.parse(number)
yourlocation = (geocoder.description_for_number(ch_number, "en"))

print(yourlocation)

#get service provider

from phonenumbers import carrier

service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider, "en"))


