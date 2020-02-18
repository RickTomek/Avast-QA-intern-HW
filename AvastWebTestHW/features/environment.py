from selenium import webdriver


def before_all(context):
    context.browser = webdriver.Firefox()
    # context.browser = webdriver.Chrome() if you have set chromedriver in your PATH
    context.browser.set_page_load_timeout(10)
    context.browser.implicitly_wait(10)
    context.browser.maximize_window()


def after_all(context):
    context.browser.quit()
