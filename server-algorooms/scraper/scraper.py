import requests
import json
import re;
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By


# open the questions url json
f = open('leetcode_questions.json')
data = json.load(f)

# store all the urls in an array
urlArray = []
for question in data:
    urlArray.append((question['title'], question['url'], question['difficulty']))

# Path to the chromedriver executable
chromedriver_path = 'usr/local/bin/chromedriver.exe'

# Initialize the webdriver
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Run the browser in headless mode
driver = webdriver.Chrome(executable_path=chromedriver_path, options=options)

count = 0
questions = []
for title, url, difficulty in urlArray:
    if count == 10:
        break

    # Load the question page using the webdriver
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    
    
    # Get the question description and example inputs/outputs
    print(f"#{count + 1}\ttitle: {title}")
    mainContainer = soup.find('div', {'class': '_1l1MA'})
    description = mainContainer.get_text().strip()
    examples = [  ];
    pre_tags = mainContainer.find_all('pre')


    inputRegex, outputRegex, explanationRegex = r"Input(\n|: ).*", r"Output(\n|: ).*", r"Explanation(\n|: ).*"; 
    for ex in pre_tags:
        exampleText = ex.get_text();

        inputText = re.search(inputRegex, exampleText);
        inputText = "" if inputText == None else inputText.group();

        outputText = re.search(outputRegex, exampleText);
        outputText = "" if outputText == None else outputText.group();

        explanationText = re.search(explanationRegex, exampleText);
        explanationText = "" if explanationText == None else explanationText.group();

        examples.append({
            "input": inputText,
            "output": outputText,
            "explanation": explanationText
        });

    topics = []

    # find div that contains the topic tags
    tag = soup.find('div', {'class': 'mt-2 flex flex-wrap gap-y-3'})
    if tag != None:
        # create an array that finds all the a tags that have an href
        tempTags = tag.find_all("a", href=True)
        for thing in tempTags:
            # append the text of the a tag into the topics array
            topics.append(thing.get_text())

    
    def translateDifficulty(score):
        if score == 1:
            return "Easy";
        elif score == 2:
            return "Medium";
        return "Hard";
    
    constraints = description.split("Constraints:\n\n")[1]
    separateConstraints = constraints.split("\n")



    # If we have at least one topic
    if len(topics) > 0:
        # Add the question information to the list of questions
        questions.append({
            'title': title,
            'description': description.split("Example 1")[0],
            'examples': examples,
            'topics': topics,
            "difficulty": translateDifficulty(difficulty),
            "constraints": separateConstraints
        });

    count += 1

# Save the questions to a JSON file
with open('QuestionDescription.json', 'w') as f:
    json.dump(questions, f)

# Quit the webdriver
driver.quit()
