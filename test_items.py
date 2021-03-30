import time
link = "http://selenium1py.pythonanywhere.com/catalogue/hackers-painters_185/"

def test_button_add_to_basket_exists(browser):
    browser.get(link)
    time.sleep(10)
    button = browser.find_elements_by_css_selector('button.btn-add-to-basket')
    assert len(button) > 0, "Where is my button?"