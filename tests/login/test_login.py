import pytest


@pytest.mark.parametrize(
    "email, password, expected",
    [
        pytest.param(
            "qa.ajax.app.automation@gmail.com",
            "password",
            False
        ),
        pytest.param(
            "email",
            "qa_automation_password",
            False
        ),
        pytest.param(
            "QA.AJAX.APP.AUTOMATION@GMAIL.COM",
            "QA_AUTOMATION_PASSWORD",
            False
        ),
        pytest.param(
            "",
            "",
            False
        ),
        pytest.param(
            "qa.ajax.app.automation@gmail.com",
            "qa_automation_password",
            True
        ),
    ],
)
def test_user_login(user_login_fixture, email: str, password: str, expected: bool, logger) -> None:
    logger.info(f"Testing log in function for user with next credentials: email - {email}, password - {password}.")
    actual = user_login_fixture.log_in(email=email, password=password)
    assert actual == expected
    logger.info(f"Test user login passed: {actual}.")
