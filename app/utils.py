from datetime import datetime, date


class IDGenerator:
    """Генератор id для задач"""
    current_id = 0

    @classmethod
    def get_next_id(cls) -> int:
        cls.current_id += 1
        return cls.current_id


def is_valid_future_date(date_str: str, date_format: str = "%Y-%m-%d") -> bool:
    """Функция для проверки корректности даты"""
    try:
        parsed_date = datetime.strptime(date_str, date_format).date()

        return parsed_date > date.today()
    except ValueError:
        return False
