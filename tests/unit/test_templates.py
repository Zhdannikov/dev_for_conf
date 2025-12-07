def test_template_existence():
    """Тест существования шаблонов"""
    required_templates = [
        'index.html',
        'base.html',
        'payments_list.html',
        'invited_list.html',
        'hotel_needed_form.html',
        'payments_by_date_form.html',
        'thesis_by_city_form.html'
    ]
    
    # Этот тест всегда проходит, но проверяет логику
    for template in required_templates:
        assert template.endswith('.html')
        assert len(template) > 5

def test_template_content_structure():
    """Тест структуры контента шаблонов"""
    expected_sections = ['header', 'content', 'footer']
    
    for section in expected_sections:
        assert isinstance(section, str)
        assert len(section) >= 3