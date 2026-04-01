from datetime import datetime

from flask import Blueprint, request, redirect, url_for

from pybo import db
from pybo.models import Question, Answer

bp = Blueprint('answer', __name__, url_prefix='/answer')

@bp.route('/create/<int:question_id>', methods=['post'])
def create(question_id):
    # 답변 등록할 질문 DB 조회
    question = Question.query.get(question_id)
    # 사용자가 입력한 form태그의 'content'속성의 값을 변수에 담음
    content = request.form.get('content')
    # Answer 객체를 생성
    answer = Answer(content=content, created=datetime.now())
    # 해당 질문에 답변 등록
    question.answer_set.append(answer)
    db.session.commit()

    return redirect(url_for('question.detail', question_id=question_id))