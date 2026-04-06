import locale
locale.setlocale(locale.LC_ALL, '')

# 날짜시간데이터 포메팅 함수
def format_datetime(value, fmt='%y년 %m월 %d일 %p %I:%M'):
    return value.strftime(fmt)