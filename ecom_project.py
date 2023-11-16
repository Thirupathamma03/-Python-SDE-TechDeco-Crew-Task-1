import logging
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException

# Set up logging
logging.basicConfig(filename='automation.log', level=logging.INFO)

# Set up the WebDriver (Chrome in this example)
driver = webdriver.Chrome()

try:
    # Open the e-commerce website
    driver.get("https://automationexercise.com/")
    driver.maximize_window()
    # new user sign up
    # Scenario: Product Browsing
    logging.info("Scenario: Product Browsing")
    view_product = driver.find_element(By.XPATH, "(//a[contains(text(),'View Product')])[1]")
    view_product.click()
    time.sleep(2)

    # Scenario: Add to Cart
    logging.info("Scenario: Add to Cart")
    # Add code to add a product to the cart
    add_cart = driver.find_element(By.XPATH, "//button[normalize-space()='Add to cart']")
    add_cart.click()
    time.sleep(2)

    view_cart = driver.find_element(By.XPATH, "(//p[@class='text-center'])[2]")
    view_cart.click()
    time.sleep(2)

    # Scenario: Purchase
    logging.info("Scenario: Purchase")
    # Add code to complete the purchase process

    check_out = driver.find_element(By.XPATH, "(//a[normalize-space()='Proceed To Checkout'])[1]")
    check_out.click()
    time.sleep(2)

    Rigister_link = driver.find_element(By.XPATH, "(//p[@class='text-center'])[2]")
    Rigister_link.click()
    time.sleep(2)

    signup_or_login = driver.find_element(By.XPATH, "//a[normalize-space()='Signup / Login']")
    signup_or_login.click()
    time.sleep(2)

    name_textbox=driver.find_element(By.XPATH, "//input[@placeholder='Name']")
    name_textbox.send_keys("lakshmi")
    time.sleep(2)

    email_textbox=driver.find_element(By.XPATH, "//input[@data-qa='signup-email']")
    email_textbox.send_keys("lthirupathamm@gmail.com")
    time.sleep(2)

    signup_button=driver.find_element(By.XPATH, "//button[normalize-space()='Signup']")
    signup_button.click()
    time.sleep(2)

    # enter account information

    button_click=driver.find_element(By.XPATH, "//input[@id='id_gender2']")
    button_click.click()
    time.sleep(2)

    password_textbox=driver.find_element(By.XPATH, "//input[@id='password']")
    password_textbox.send_keys("12345678")
    time.sleep(2)

    drp_day=Select(driver.find_element(By.XPATH, "//select[@id='days']"))
    drp_day.select_by_value("21")
    time.sleep(2)

    drp_month=Select(driver.find_element(By.XPATH, "//select[@id='months']"))
    drp_month.select_by_visible_text("March")
    time.sleep(2)

    drp_year=Select(driver.find_element(By.XPATH, "//select[@id='years']"))
    drp_year.select_by_value("1993")
    time.sleep(2)

    # Address information
    first_name=driver.find_element(By.XPATH, "//input[@id='first_name']")
    first_name.send_keys("lakshmi")
    time.sleep(2)

    last_name=driver.find_element(By.XPATH, "//input[@id='last_name']")
    last_name.send_keys("P")
    time.sleep(2)

    company_field=driver.find_element(By.XPATH, "//input[@id='company']")
    company_field.send_keys("QA AUTOMATION")
    time.sleep(2)

    address1_box=driver.find_element(By.XPATH, "//input[@id='address1']")
    address1_box.send_keys("Abc street")
    time.sleep(2)

    address2_box=driver.find_element(By.XPATH, "//input[@id='address2']")
    address2_box.send_keys("Bcc street")
    time.sleep(2)

    drp_country=Select(driver.find_element(By.XPATH, "//select[@id='country']"))
    drp_country.select_by_visible_text("India")
    time.sleep(2)

    state=driver.find_element(By.XPATH, "//input[@id='state']")
    state.send_keys("Andrapradash")
    time.sleep(2)

    city=driver.find_element(By.XPATH, "//input[@id='city']")
    city.send_keys("Ongole")
    time.sleep(2)

    zipcode=driver.find_element(By.XPATH, "//input[@id='zipcode']")
    zipcode.send_keys("523182")
    time.sleep(2)

    mobile_no=driver.find_element(By.XPATH, "//input[@id='mobile_number']")
    mobile_no.send_keys("123456789")
    time.sleep(2)

    create_account=driver.find_element(By.XPATH, "//button[normalize-space()='Create Account']")
    create_account.click()
    time.sleep(2)

    continue_button=driver.find_element(By.XPATH,"//a[normalize-space()='Continue']")
    continue_button.click()
    time.sleep(2)

    signup_or_login=driver.find_element(By.XPATH,"//a[normalize-space()='Signup / Login']")
    signup_or_login.click()
    time.sleep(2)

     # login your account
    email=driver.find_element(By.XPATH,"//input[@data-qa='login-email']")
    email.send_keys("lthirupathamm@gmail.com")
    time.sleep(2)

    password=driver.find_element(By.XPATH,"//input[@placeholder='Password']")
    password.send_keys("12345678")
    time.sleep(2)

    login_button=driver.find_element(By.XPATH,"//button[normalize-space()='Login']")
    login_button.click()
    time.sleep(2)

    cart=driver.find_element(By.XPATH,"//a[normalize-space()='Cart']")
    cart.click()
    time.sleep(2)

    check_out.click()

    placeorder=driver.find_element(By.XPATH,"//a[normalize-space()='Place Order']")
    placeorder.click()
    time.sleep(2)

    # payment method
    name_on_card=driver.find_element(By.XPATH,"//a[normalize-space()='Place Order']")
    name_on_card.send_keys("lakshmi")
    time.sleep(2)

    card_number=driver.find_element(By.XPATH,"//input[@name='card_number']")
    card_number.send_keys("123456789")
    time.sleep(2)

    cvc=driver.find_element(By.XPATH,"//input[@placeholder='ex. 311']")
    cvc.send_keys("321")
    time.sleep(2)

    month=driver.find_element(By.XPATH,"//input[@placeholder='MM']")
    month.send_keys("03")
    time.sleep(2)

    year=driver.find_element(By.XPATH,"//input[@placeholder='YYYY']")
    year.send_keys("2024")
    time.sleep(2)

    confirm_order=driver.find_element(By.XPATH,"//button[@id='submit']")
    time.sleep(2)


except Exception as e:
    logging.error(f"An error occurred: {str(e)}")
    driver.save_screenshot("error_screenshot.png")

finally:
    # Close the browser window
    driver.quit()

