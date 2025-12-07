def test_payment_calculations():
    payments = [100, 200, 300, 150]
    assert sum(payments) == 750

def test_participant_validation():
    participant = {'name': 'Иван', 'email': 'test@test.com', 'city': 'Москва'}
    assert 'name' in participant
    assert '@' in participant['email']

def test_statistics_calculation():
    data = [10, 20, 30, 40, 50]
    assert sum(data) == 150
    assert len(data) == 5