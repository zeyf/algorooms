import requests
import json

# API endpoint URL
url = 'https://leetcode.com/api/problems/algorithms/'

# Send a GET request to the API endpoint and get its JSON response
response = requests.get(url)
data = json.loads(response.text)

# Extract the list of questions from the JSON response
questions = []
for question in data['stat_status_pairs']:
    # Get the question title, URL, and difficulty level
    if question['paid_only'] == True:
        continue
    title = question['stat']['question__title']
    url = f"https://leetcode.com/problems/{question['stat']['question__title_slug']}"
    difficulty = question['difficulty']['level']
    
    # Add the question information to the list of questions
    questions.append({'title': title, 'url': url, 'difficulty': difficulty})

# Save the questions to a JSON file
with open('leetcode_questions.json', 'w') as f:
    json.dump(questions, f)