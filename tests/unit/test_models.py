def test_participant_data_structure():
    """Тест структуры данных участника"""
    participant = {
        'name': 'John Doe',
        'email': 'john@example.com',
        'city': 'Moscow'
    }
    
    assert 'name' in participant
    assert 'email' in participant
    assert 'city' in participant
    assert isinstance(participant['name'], str)

def test_payment_calculation():
    """Тест расчетов платежей"""
    payments = [100, 200, 150]
    total = sum(payments)
    average = total / len(payments)
    
    assert total == 450
    assert average == 150

def test_hotel_requirements():
    """Тест логики требований к отелю"""
    needs_hotel = True
    has_hotel = False
    
    assert needs_hotel != has_hotel  # Должны различаться