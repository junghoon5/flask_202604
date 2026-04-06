from datetime import datetime
from pybo import create_app, db
from pybo.models import Question

def insert_test_data(n=300):
    """테스트용 질문 데이터 n개"""
    app = create_app()    # Flask 컨텍스트 가 필요
    with app.app_context():
        for i in range(n):
            q = Question(
                subject='테스트 데이터입니다:[%03d]'%i,
                content='내용없음',
                created=datetime.now()
            )
            db.session.add(q)

        db.session.commit()
        print(f'{n}개의 테스트 데이터가 생성되었습니다.')

if __name__ == '__main__':
    insert_test_data()