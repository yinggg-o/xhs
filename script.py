import time
from selenium.webdriver.support import expected_conditions as EC
import pyotp
import authenticator as authenticator
from selenium import webdriver
from selenium.webdriver.chrome.service import Service  # Import Service
from selenium.webdriver.chrome.options import Options  # Import Options for Chrome configuration
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

# Initialize ChromeDriver
service = Service("/opt/homebrew/bin/chromedriver")  # Update with the correct path
chrome_options = Options()
chrome_options.add_argument("start-maximized")
chrome_options.add_argument("--disable-web-security")
chrome_options.add_argument("--disable-site-isolation-trials")
chrome_options.add_argument("--allow-running-insecure-content")
driver = webdriver.Chrome(service=service, options=chrome_options)



# Open a new tab or window (if needed)
driver.execute_script("window.open('about:blank', '_blank');")
driver.switch_to.window(driver.window_handles[-1])
# Navigate to the post creation page
driver.get("")

# Explicit wait duration
timeout_duration = 30  # Adjust as needed for slow-loading sites

try:
    # Wait for the phone number input box to be present
    phone_number_field = WebDriverWait(driver, timeout_duration).until(
        EC.presence_of_element_located((By.XPATH, "//input[@placeholder='手机号']"))  # XPath for phone number field
    )

    # Ensure the input field is ready for interaction
    phone_number_field.clear()  # Clear any existing content
    phone_number_field.click()  # Give focus to the input field
    phone_number_field.send_keys("13648317852")  # Example: phone number

    # Wait for the verification code box to be activated
    verification_code_field = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, "//input[@placeholder='验证码']"))  # XPath for verification code field
    )

    # Enter the verification code
    verification_code_field.send_keys("1234")  # Example: verification code

    # Handle potential modals or overlays
    try:
        modal = driver.find_element(By.CLASS_NAME, "modal-overlay")  # Adjust locator for modals/overlays
        modal.click()  # Close the modal/overlay if found
    except:
        pass  # No modal/overlay, continue

    # Submit the form or click the login button
    login_button = driver.find_element(By.XPATH, "//button[text()='Login']")  # Adjust locator for login button
    login_button.click()

    # Check for successful login (example condition, adjust as needed)
    WebDriverWait(driver, timeout_duration).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(text(), '登录')]"))  # Adjust condition
    )
    print("Login successful!")

except TimeoutException as e:
    print("Timeout while waiting for elements:", e)  # Handle timeout exceptions
except Exception as e:
    print("An error occurred:", e)  # Handle other exceptions

finally:
    # Clean up by closing the browser
    driver.quit()


# # Pause to allow time for the authentication token to be generated
# time.sleep(5)  # Adjust as needed
#
# # Generate the 2FA token (TOTP example using pyotp)
# secret = "your_base32_secret"  # Base32 secret for TOTP
# totp = pyotp.TOTP(secret)  # Generate the TOTP instance
# token = totp.now()  # Get the current TOTP token
#
# # Enter the authentication token
# auth_token_field = WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.NAME, "auth_token"))  # Adjust locator as needed
# )
# auth_token_field.send_keys(token)  # Enter the TOTP token
#
# # Submit the authentication token
# submit_button = driver.find_element(By.XPATH, "//button[text()='Authenticate']")  # Adjust locator
# submit_button.click()
#
# # Check if login was successful
# try:
#     success_element = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Welcome')]"))  # Adjust locator
#     )
#     print("Login successful!")
# except Exception as e:
#     print("Login failed:", e)

# Close the browser
driver.quit()