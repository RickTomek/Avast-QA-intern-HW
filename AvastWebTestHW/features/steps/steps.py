from behave import *
from nose.tools import assert_equal, assert_true
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@step('I navigate to the Avast test page')
def step_impl(context):
    context.browser.get("https://www.avast.com/business/products/qa-intern-business-antivirus-pro-plus")
    assert_equal(context.browser.title, "Business VPN, Password Protection - AVAST Antivirus Pro Plus")
    #context.browser.find_element(By.XPATH, "//span[@class = 'js-close close button transparent big']").click()

@step('I input "{count}" devices')
def step_impl(context, count):
    context.browser.find_element(By.XPATH, "//input[@type = 'number']").send_keys(Keys.CONTROL + "a")
    context.browser.find_element(By.XPATH, "//input[@type = 'number']").send_keys(count)
    element = WebDriverWait(context.browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[@class = 'price ']"))
    )
    context.price = context.browser.find_element(By.XPATH, "//span[@class = 'currency']").text
    context.price += context.browser.find_element(By.XPATH, "//span[@class = 'price ']").text
    context.price += "."+context.browser.find_element(By.XPATH, "//span[@class = 'decimals']").text
    context.browser.find_element(By.XPATH, "//a[@data-smb-test-id = 'a-1']").click()

@step('I am taken to cart page')
def step_impl(context):
    assert_equal(context.browser.title, "Avast Store – United States")


@step('I check final price')
def step_impl(context):
    context.finalPrice = context.browser.find_element(By.XPATH, "//div[@class = 'av_lineItem-listPrice']").text
    assert_equal(context.finalPrice, context.price)

@step('I click buy "{product}" "{price}"')
def step_impl(context, product, price):
    context.price = price
    context.browser.find_element(By.XPATH, "//a[@data-smb-test-id = '"+ product + "']").click()

