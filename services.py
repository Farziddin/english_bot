questions = [
    {"question": "What 1?", "options": [{"name": "A", "answer": "1"}, {"name": "B", "answer": "2"}, {"name": "C", "answer": "3"}], "answer": "1"},
    {"question": "What 2?", "options": [{"name": "A", "answer": "1"}, {"name": "B", "answer": "2"}, {"name": "C", "answer": "3"}], "answer": "2"},
    {"question": "What 3?", "options": [{"name": "A", "answer": "1"}, {"name": "B", "answer": "2"}, {"name": "C", "answer": "3"}], "answer": "3"},
    {"question": "What 4?", "options": [{"name": "A", "answer": "1"}, {"name": "B", "answer": "2"}, {"name": "C", "answer": "3"}], "answer": "1"},
]


def get_question(question_id):
    question = questions[question_id]
    has_next = False
    if len(questions) > question_id + 1:
        has_next = True
    return {"question": question, "has_next": has_next}


def is_user_exist(user_id):
    if user_id:
        return True
    return False
