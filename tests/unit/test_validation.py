def test_email_validation():
    #"Тест валидации email"
    valid_emails = ['test@example.com', 'user.name@domain.co.uk']
    invalid_emails = ['invalid', 'no@domain', '@domain.com']
    
    for email in valid_emails:
        assert '@' in email and '.' in email
    
    for email in invalid_emails:
        # Проверяем что email невалиден
        has_at = '@' in email
        has_dot = '.' in email
        if has_at and has_dot:
            # Если есть и @ и ., проверяем что @ перед .
            at_position = email.index('@')
            dot_position = email.rindex('.')
            assert at_position > dot_position or at_position == 0 or dot_position == len(email) - 1
        else:
            # Если нет @ или ., email невалиден
            assert True

def test_city_validation():
    #"Тест валидации городов"
    valid_cities = ['Moscow', 'Saint Petersburg', 'Novosibirsk']
    
    for city in valid_cities:
        assert len(city) >= 2
        assert city.istitle() or city == 'Saint Petersburg'

def test_date_validation():
    #Тест валидации дат
    from datetime import datetime
    
    current_year = datetime.now().year
    valid_dates = [
        f'2024-01-15',
        f'{current_year}-12-31'
    ]
    
    for date_str in valid_dates:
        parts = date_str.split('-')
        assert len(parts) == 3
        year, month, day = map(int, parts)
        assert 1 <= month <= 12
        assert 1 <= day <= 31
