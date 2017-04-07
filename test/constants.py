BASE_USERNAME='haeno.krk@gmail.com'
BASE_URL='https://core.futuresimple.com/sales/users/login/'
BASE_PASSWORD='qwerty123456'


LOGIN_EMAIL_NAME= 'user[email]'
LOGIN_PASSWD_NAME = 'user[password]'
LOGIN_BUTTON_XPATH = "//button[contains(., 'Log in')]"

HEADER_USERID_XPATH = "//li[@id='user-dd']"
MAIN_PAGE_CONTENT_PANE_ID = 'user-dd'
BASE_TITLE = 'Login to Base'


LEADS_NAVI_ID = "nav-leads"
LEADS_PROFILE_EDIT_BTN_XPATH = "//a[@class='btn btn-mini detail-edit']"
LEADS_PROFILE_STATUS_XPATH = "//span[@class='lead-status']"
LEADS_NEW_REMOVE_XPATH = "//a[@class='remove']"
LEADS_NEW_CONFIRM_REMOVE_XPATH = "//a[@class='btn btn-primary btn-danger  confirm']"
LEADS_NEW_BUTTON_XPATH = "//a[@id='leads-new']"
LEADS_NEW_FNAME_XPATH = "//input[contains(@id,'lead-first-name')]"
LEADS_NEW_LNAME_XPATH = "//input[contains(@id,'lead-last-name')]"
LEADS_NEW_COMPANY_XPATH = "//input[contains(@id,'lead-company-name')]"
LEADS_NEW_TITLE_XPATH = "//input[contains(@id,'lead-title')]"
LEADS_NEW_EMAIL_XPATH = "//input[contains(@id,'lead-email')]"
LEADS_NEW_MOBILE_XPATH = "//input[contains(@id,'lead-mobile')]"
LEADS_NEW_PHONE_XPATH = "//input[contains(@id,'lead-phone')]"
LEADS_NEW_STREET_XPATH = "//input[contains(@id,'lead-street')]"
LEADS_NEW_CITY_XPATH = "//input[contains(@id,'lead-city')]"
LEADS_NEW_ZIP_XPATH = "//input[contains(@id,'lead-zip')]"
LEADS_NEW_REGION_XPATH = "//input[contains(@id,'lead-region')]"
LEADS_NEW_COUNTRY_XPATH = "//div[@class='controls inline country_select']"
LEADS_NEW_COUNTRY_INPUT_XPATH = "//div[@class='chzn-search']"
LEADS_NEW_STATUS_XPATH = "//div[@class='control-group'][label[@for='status_id']]"
LEADS_NEW_STATUS_INPUT_XPATH = "//div[@class='control-group'][label[@for='status_id']]//div[@class='chzn-search']"
LEADS_NEW_OWNER_XPATH = "//div[@class='control-group'][div[@class='controls inline owner-select']]"
LEADS_NEW_OWNER_INPUT_XPATH = "//div[@class='control-group'][div[@class='controls inline owner-select']]//div[@class='chzn-search']"
LEADS_NEW_SOURCE_XPATH = "//div[@class='source-select-field']"
LEADS_NEW_SOURCE_INPUT_XPATH = "//div[@class='source-select-field']//div[@class='chzn-search']"
LEADS_NEW_INDUSTRY_XPATH = "//div[@class='industry-field']"
LEADS_NEW_INDUSTRY_INPUT_XPATH = "//div[@class='industry-field']//div[@class='chzn-search']"
LEADS_NEW_TAGS_XPATH = "//div[@class='tags-field']//ul[@class='chzn-choices']"
LEADS_NEW_SAVE_BUTTON_XPATH = "//button[@class='save btn btn-large btn-primary']"

DDMENU_SETTINGS_XPATH = "//li[@class='settings']//strong[text()='Settings']"

SETTINGS_LEADS_XPATH = "//li[@class='leads']"
SETTINGS_LEADS_STATUS_XPATH = "//a[@data-toggle='lead-status']"

TEST_USER_PROFILE = dict(
    first_name = 'John',
    last_name = 'Doe',
    company = 'BaseLab',
    title = 'Mr',
    email = 'jdoe@baselab.com',
    mobile = '601123456',
    phone = '121234567',
    street = 'Elm Str',
    city = 'Krakow',
    zipcode = '12345',
    region = 'malopolska',
    country = 'Poland',
    status = 'New',
    owner = 'Mateusz Bochenek',
    source = '',
    industry = 'Banks',
    tags1 = 'test_tag',
    tags2 = 'test_tag2',
    abbrv = 'MB'
    )
