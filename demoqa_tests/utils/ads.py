from selene.support.shared import browser

from selene import have, command

ads = browser.all('[id^=google_ads][id$=container__]')


def remove_ads(browser):
    ads = browser.all('[id^=google_ads][id$=container__]')
    ads.with_(timeout=10).should(have.size_greater_than_or_equal(3)).perform(
        command.js.remove
    )

    if ads.with_(timeout=2).wait_until(have.size_greater_than_or_equal(2)):
        ads.perform(command.js.remove)