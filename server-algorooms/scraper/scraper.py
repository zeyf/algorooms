import requests
import json
from bs4 import BeautifulSoup
from selenium import webdriver


f = open('leetcode_questions.json')
data = json.load(f)

urlArray = []
for question in data:
    urlArray.append((question['title'], question['url']))



# Path to the chromedriver executable
chromedriver_path = 'usr/local/bin/chromedriver.exe'

# Initialize the webdriver
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Run the browser in headless mode
driver = webdriver.Chrome(executable_path=chromedriver_path, options=options)

count = 0
questions = []
for title, url in urlArray:
    if count == 20:
        break
    # Load the question page using the webdriver
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    
    # Get the question description and example inputs/outputs
    print("title: " + title)
    description = soup.find('div', {'class': '_1l1MA'}).get_text().strip()
    topics = []

    # allA = [  soup.find_all("a") ]

    tag = soup.find('div', {'class': 'mt-2 flex flex-wrap gap-y-3'})
    if tag != None:
        # tempTag = tag.get_text().strip()
        # print(tempTag)
        # topics.append(tempTag)
        tempTags = tag.find_all("a", href=True)
        for i in tempTags:
            topics.append(i.get_text())
        
    
    # Add the question information to the list of questions
    questions.append({
        'title': title,
        'description': description,
        'topics': topics
    })
    count += 1

# Save the questions to a JSON file
with open('QuestionDescription.json', 'w') as f:
    json.dump(questions, f)

# Quit the webdriver
driver.quit()
