import requests


url = "https://www.fema.gov/api/open/v2/PublicAssistanceFundedProjectsDetails"

api_data = requests.get(url)

print( api_data.json()['PublicAssistanceFundedProjectsDetails'][:3] )




# details = {
#   'name': 'ifeanyi',
#   'age': 35,
#   'favorite_colors': ['blue', 'red', 'black', 'brown']
# }

# print(details['favorite_colors'][:1])