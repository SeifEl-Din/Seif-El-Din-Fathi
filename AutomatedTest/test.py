from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

users = [
    {"username": "standard_user", "password": "secret_sauce"},
    {"username": "problem_user", "password": "secret_sauce1"},
    {"username": "problem_user", "password": "secret_sauce"},
    {"username": "locked_out_user", "password": "secret_sauce"},
    {"username": "performance_glitch_user", "password": "secret_sauce"},
    {"username": "error_userr", "password": "secret_sauce"},
    {"username": "error_user", "password": "secret_sauce"},
    {"username": "visual_user", "password": "secret_sauce"},
    {"username": "problem_user", "password": "secret"}

]

# Launch Chrome browser using the webdriver module built in selenium
driver = webdriver.Chrome()
driver.maximize_window()

# Loop over all the credentials that are being tested
for user in users:
    # Open the Sauce Demo website
    driver.get("https://www.saucedemo.com/")

    # Wait for the page elements to load
    username_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "user-name")))
    password_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "password")))
    login_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "login-button")))

    # Enter the username and password
    username_field.send_keys(user["username"])  
    password_field.send_keys(user["password"]) 

    # Click the login button
    login_button.click()

    # Handle the exception if the credentials are not correctly matched
    try:
        error_message = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, "//h3[@data-test='error']"))
        )
        # If an error message is found
        # Handling the special case of the 'Locked_out_user'
        if "locked out" in error_message.text.lower():
            print(f"Login failed for user '{user['username']}'. User is locked out.")
        else:
            print(f"Login failed for user '{user['username']}'. Error message: {error_message.text}")

    # Handle the exception if error message is not found
    except Exception:
        print(f"Login successful for user '{user['username']}'.")

# Keep the browser opened until the user manually closes it
# This is done by entering an infinite loop and wait for an interaction from the user 
#while True:
#    pass  

# Close the browser after finishing the tests
driver.quit()
