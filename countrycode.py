# Write a program to return the country code for various countries. Here’s a dictionary of different country codes - {'India' : '0091', 'Australia' : '0025', 'Nepal' : '00977'}.

country_code = {'India' : '0091',
                'Australia' : '0025',
                'Nepal' : '00977'}

print("The country code for India is - ")
print(country_code.get('India', "Found"))

print("The country code for Germany is - ")
print(country_code.get('Germany', "Not Found"))