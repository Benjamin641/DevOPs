from accounts.forms import RegistrationForm
def test_home_page(client):
    response = client.get("/")
    assert response.status_code == 200

def test_registration_page(client):
    response = client.get("/registration")
    assert response.status_code == 200


def test_registration_form_missing_data(app):
    with app.test_request_context():
        form = RegistrationForm(data={})
        assert not form.validate()