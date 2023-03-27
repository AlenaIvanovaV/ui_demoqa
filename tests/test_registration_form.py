from allure_commons.types import Severity

from demoqa_tests.model.data.user import test_user
from demoqa_tests.model.pages.practice_form import PracticeForm
import allure


@allure.tag("UI test")
@allure.severity(Severity.CRITICAL)
@allure.story("Registration form")
@allure.feature("Forms")
@allure.label("owner", "OAO")
@allure.description("Verify registration process is successful")
def test_registration_user():

    # GIVEN
    with allure.step('Init Form'):
        practice_form = PracticeForm(test_user)

    # WHEN
    with allure.step('Enter users\'s registration data and send form'):
        practice_form.submit_form()

    # THEN
    with allure.step('Verify all sent data correctly submitted'):
        practice_form.should_have_submitted()

@allure.tag("UI test")
@allure.severity(Severity.CRITICAL)
@allure.story("Registration form")
@allure.feature("Forms")
@allure.label("owner", "OAO")
@allure.feature('Successful completion of the form with only required fields')
def test_fill_only_required_fields():
    # GIVEN
    with allure.step('Init Form'):
        practice_form = PracticeForm(test_user)

    with allure.step('Fill main fields'):
        practice_form.fill_name() \
            .select_gender() \
            .fill_contacts() \
            .input_address() \
            .submit()

    with allure.step('Check the filled data'):
        practice_form.check_data(test_user.first_name) \
            .check_data(test_user.last_name) \
            .check_data(test_user.gender) \
            .check_data(test_user.phone) \
            .check_data(test_user.email) \
            .check_data(test_user.address)