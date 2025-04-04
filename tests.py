import pytest
from model import Question


def test_create_question():
    question = Question(title='q1')
    assert question.id != None

def test_create_multiple_questions():
    question1 = Question(title='q1')
    question2 = Question(title='q2')
    assert question1.id != question2.id

def test_create_question_with_invalid_title():
    with pytest.raises(Exception):
        Question(title='')
    with pytest.raises(Exception):
        Question(title='a'*201)
    with pytest.raises(Exception):
        Question(title='a'*500)

def test_create_question_with_valid_points():
    question = Question(title='q1', points=1)
    assert question.points == 1
    question = Question(title='q1', points=100)
    assert question.points == 100

def test_create_choice():
    question = Question(title='q1')
    
    question.add_choice('a', False)

    choice = question.choices[0]
    assert len(question.choices) == 1
    assert choice.text == 'a'
    assert not choice.is_correct

def test_create_question_with_max_selections():
    question = Question(title='q1', max_selections=2)
    assert question.max_selections == 2

def test_add_multiple_choices():
    question = Question(title='q1')
    question.add_choice('a', False)
    question.add_choice('b', False)
    assert len(question.choices) == 2

def test_remove_choice():
    question = Question(title='q1')
    question.add_choice('a', False)
    question.remove_choice_by_id(question.choices[0].id)
    assert len(question.choices) == 0

def test_remove_all_choices():
    question = Question(title='q1')
    question.add_choice('a', False)
    question.add_choice('b', False)
    question.remove_all_choices()
    assert len(question.choices) == 0

def test_select_choices():
    question = Question(title='q1')
    question.add_choice('a', True)
    question.add_choice('b', False)
    selected_choices = question.select_choices([question.choices[0].id])
    assert len(selected_choices) == 1

def test_set_correct_choices():
    question = Question(title='q1')
    question.add_choice('a', False)
    question.add_choice('b', False)
    question.set_correct_choices([question.choices[0].id])
    assert question.choices[0].is_correct

def test_create_choice_with_invalid_text():
    question = Question(title='q1')
    with pytest.raises(Exception):
        question.add_choice('', False)
    with pytest.raises(Exception):
        question.add_choice('a'*101, False)

def test_create_question_with_invalid_points():
    with pytest.raises(Exception):
        Question(title='q1', points=0)
    with pytest.raises(Exception):
        Question(title='q1', points=101)

def test_select_more_choices_than_allowed():
    question = Question(title='q1', max_selections=1)
    question.add_choice('a', True)
    question.add_choice('b', True)
    with pytest.raises(Exception):
        question.select_choices([question.choices[0].id, question.choices[1].id])

def test_create_question_with_title():
    question = Question(title='q1')
    assert question.title == 'q1'

@pytest.fixture
def questao_multipla_escolha():
    return {
        "enunciado": "Qual é a capital do Brasil?",
        "opcoes": ["São Paulo", "Rio de Janeiro", "Brasília", "Porto Alegre"],
        "resposta_certa": "Brasília"
    }

def test_questao_multipla_escolha(questao_multipla_escolha):
    assert questao_multipla_escolha["enunciado"] == "Qual é a capital do Brasil?"
    assert len(questao_multipla_escolha["opcoes"]) == 4
    assert questao_multipla_escolha["resposta_certa"] == "Brasília"

def test_questao_multipla_escolha_errada(questao_multipla_escolha):
    questao_multipla_escolha["resposta_certa"] = "São Paulo"
    assert questao_multipla_escolha["resposta_certa"] != "Brasília"