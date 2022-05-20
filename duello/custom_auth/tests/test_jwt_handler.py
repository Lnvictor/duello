import pytest


@pytest.mark.xfail(raises=ValueError)
def test_should_not_generate_token_due_invalid_certificate(jwt_handler_with_invalid_certificate):
    assert jwt_handler_with_invalid_certificate


def test_should_generate_token(jwt_handler):
    token = jwt_handler.gen_token(name='zezinho')
    assert token
