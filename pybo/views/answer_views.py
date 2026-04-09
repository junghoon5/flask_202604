from datetime import datetime

from flask import Blueprint, request, redirect, url_for, render_template, g, flash

from pybo import db
from pybo.forms import AnswerForm
from pybo.models import Question, Answer
from pybo.views.auth_views import login_required


bp = Blueprint('answer', __name__, url_prefix='/answer')

@bp.route('/create/<int:question_id>', methods=['post'])
@login_required
def create(question_id):
    form = AnswerForm()
    # 답변 등록할 질문 DB 조회
    question = Question.query.get_or_404(question_id)
    # 사용자가 입력한 form태그의 'content'속성의 값을 변수에 담음
    if form.validate_on_submit():
        content = form.content.data

        # Answer 객체를 생성
        answer = Answer(content=content, created=datetime.now(), user=g.user)
        # 해당 질문에 답변 등록
        question.answer_set.append(answer)
        db.session.commit()
        return redirect(url_for('question.detail', question_id=question_id))

    return render_template('question/question_detail.html', question=question, form=form)

@bp.route('/modify/<int:answer_id>', methods=['GET', 'POST'])
@login_required
def modify(answer_id):
    answer = Answer.query.get_or_404(answer_id)
    if g.user != answer.user:
        flash('수정권한이 없습니다.')
        return redirect(url_for('question.detail', question_id=answer.question.id))
    if request.method == 'POST':
        form = AnswerForm()
        if form.validate_on_submit():
            form.populate_obj(answer)
            answer.modify_date = datetime.now()  # 수정일시 저장
            db.session.commit()
            return redirect(url_for('question.detail', question_id=answer.question.id))
    else:
        form = AnswerForm(obj=answer)
    return render_template('answer/answer_form.html', form=form)

@bp.route('/delete/<int:answer_id>')
@login_required
def delete(answer_id):
    answer = Answer.query.get_or_404(answer_id)
    if g.user != answer.user:
        flash('삭제 권한이 없습니다.')
    else:
        db.session.delete(answer)
        db.session.commit()
    return redirect(url_for('question.detail', question_id=answer.question_id))

