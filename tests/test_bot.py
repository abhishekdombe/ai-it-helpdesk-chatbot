from src.bot import find_answer, load_faqs

faqs = load_faqs()


def test_password_question():
    assert "reset" in find_answer("I forgot my password", faqs).lower()


def test_vpn_question():
    assert "vpn" in find_answer("My VPN is not working", faqs).lower()


def test_unknown_question():
    assert find_answer("What is the weather today?", faqs) is None