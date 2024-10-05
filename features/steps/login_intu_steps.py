import behave
from behave import given, when, then
from selenium import webdriver
from pages.login_intu import LogInIntuPage
from pages.dashboard_intu import DashboardIntuPage

@given('the user is in the intu login page')
def step_user_is_in_login_page(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.icesi.edu.co/moodle/login/index.php")
    context.login_page = LogInIntuPage(context.driver)

@when('the user logs in with valid intu credentials')
def step_enter_credentials(context):
    # Aquí usa login_page, que es lo que inicializaste en el paso anterior
    context.login_page.login("", "")

@then('user should be redirected to dashboard page')
def step_final(context):
    dashboard_intu = DashboardIntuPage(context.driver)
    assert dashboard_intu.is_search_displayed()
