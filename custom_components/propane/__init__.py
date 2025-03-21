import re
import mechanicalsoup


browser = mechanicalsoup.StatefulBrowser(
    soup_config={'features': 'lxml'},
    raise_on_404=True,
)
# Uncomment for a more verbose output:
# browser.set_verbose(2)

browser.open("https://averyoilandpropane.myfuelportal.com/Account/Login?ReturnUrl=Tank")

browser.select_form('form[action="/Account/Login?ReturnUrl=Tank"]')
browser["EmailAddress"] = "email"
browser["Password"] = "password"
resp = browser.submit_selected()

# Uncomment to launch a web browser on the current page:
# browser.launch_browser()

browser.open("https://averyoilandpropane.myfuelportal.com/Tank")
# verify we are now logged in
page = browser.page

percent_remaining_section = page.find("div", class_="progress-bar")
if percent_remaining_section is not None:
    percent_remaining_percent = percent_remaining_section.text.strip()
    percent_remaining_elements = percent_remaining_percent.split("%")
    percent_remaining = percent_remaining_elements[0]
    print(f"Percent remaining: {percent_remaining}")

reading_date_section = page.find(string=re.compile("Reading Date:")).strip()
if reading_date_section is not None:
    reading_elements = reading_date_section.strip().split(":")
    reading_date = reading_elements[1].strip()
    print(f"reading date: {reading_date}")

last_delivery_date_section = page.find(string=re.compile("Last Delivery:"))
if last_delivery_date_section is not None:
    last_delivery_date_elements = last_delivery_date_section.strip().split(":")
    last_delivery_date = last_delivery_date_elements[1].strip()
    print(f"last delivery date: {last_delivery_date}")
