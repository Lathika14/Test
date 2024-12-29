# features/steps/web_steps.py

from behave import then
from selenium.webdriver.common.by import By

@then('I should see "{text}" on the page')
def step_impl(context, text):
    assert text in context.driver.page_source