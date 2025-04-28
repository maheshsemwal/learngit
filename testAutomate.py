from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time


def get_credentials_from_file(file_path="pass.txt"):
    with open(file_path, "r") as f:
        username = f.readline().strip()
        password = f.readline().strip()
    return username, password

# Creating an instance of the webdriver
browser = webdriver.Chrome()

# Navigate to Google Forms
browser.get('https://forms.gle/35thfmLkBNpCatvE9')


# try:
questionsBox = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.XPATH, "//div[@role='list']"))
)
            
# Refresh the children list inside the loop
children = questionsBox.find_elements(By.XPATH, ".//div[@role='listitem']")

for child in children:
    # Find the last div within the child element
    last_div = child.find_elements(By.XPATH, ".//div[@role='heading']")
                
    # Check if there is at least one last_div
    if last_div:
        last_div = last_div[0]

        # Find the span tag within the last div
        span_tag = last_div.find_element(By.XPATH, ".//span")

        # Extract the question text from the span tag
        question_text = span_tag.text

        # Print or use the question text as needed
        print(f"Question: {question_text}")
        searchBrowser = webdriver.Chrome()
        searchBrowser.get('https://talkai.info/chat/')
        
        textBox = WebDriverWait(searchBrowser, 10).until(
            EC.presence_of_element_located((By.XPATH, '//textarea'))
        )
        textBox.send_keys(question_text)
        textBox.send_keys(Keys.ENTER)
        
        # Wait for the answer to load
        answerBox = WebDriverWait(searchBrowser, 10).until(
            EC.presence_of_element_located((By.XPATH, 'div[@class="chat__message"]//div[@class="chat__message__text"]/p'))
        )

        # Extract the text of the paragraph element within chat__message_text
        answer = answerBox.text
        print(f"Answer: {answer}")
        time.sleep(10)
        
        searchBrowser.close()
        
            
        options_div = child.find_elements(By.XPATH, ".//span[@role='presentation']")[0]
        option_div_inner = options_div.find_elements(By.XPATH, ".//div")[0]
            
        option_div_inner_child = option_div_inner.find_elements(By.XPATH, ".//div")
        
        i=0
        for option in option_div_inner_child:
            option = options_div.find_elements(By.XPATH, ".//span")[i]
            if answer.find(option.text) != -1:
                option.click()
                print(f"Correct option: {option.text}")
                break
            # option_text = option.text
            # print(f"Option: {option_text}")
            if(i>2):
                break
            i+=1

# Add any additional actions or logic here

# Sleep to keep the browser open for 10 seconds (for demonstration purposes)
time.sleep(10)

# Check if the questionsBox element has become stale
WebDriverWait(browser, 10).until(EC.staleness_of(questionsBox))

# except Exception as e:
#     print(f"An error occurred: {str(e)}")

print("Script executed successfully.")

# Closing the browser
browser.quit()
