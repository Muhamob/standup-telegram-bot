import pytz

timezone = pytz.timezone("Europe/Moscow")
days_of_week_dict = dict(zip(range(7), [
    'Понедельнике',
    'Вториник',
    'Среда',
    'Четверг',
    'Пятница',
    'Суббота',
    'Воскресенье',
]))
