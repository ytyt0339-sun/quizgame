import json

class Question:
    total = 0
    score = 0

    def __init__(self, question, answer, choices):
        self.question = question
        self.answer = answer
        self.choices = choices

    def solve(self):
        print(self.question)

        for i, choice in enumerate(self.choices, start=1):
            print(f"{i}. {choice}")

        user_answer = int(input("정답을 입력하세요: "))

        if user_answer == self.answer:
            print("정답입니다!\n")
            Question.score += 1
        else:
            print("오답입니다.\n")

        Question.total += 1

    def to_dict(self):
        return {
            "question": self.question,
            "answer": self.answer,
            "choices": self.choices
        }

def save_questions(questions):
    data = []

    for quiz in questions:
        data.append(quiz.to_dict())

    with open("questions.json", "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def load_questions():
    try:
        with open("questions.json", "r", encoding="utf-8") as file:
            data = json.load(file)

        questions = []

        for item in data:
            quiz = Question(
                item["question"],
                item["answer"],
                item["choices"]
            )
            questions.append(quiz)

        return questions

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        return []

# 기본 퀴즈 목록
questions = load_questions()

if not questions:
    questions = [
        Question(
            "대한민국의 수도는 어디일까요?",
            2,
            ["부산", "서울", "대전", "광주"]
        ),
        Question(
            "지구에서 가장 큰 바다는?",
            3,
            ["대서양", "인도양", "태평양", "북극해"]
        ),
        Question(
            "세계에서 가장 높은 산은?",
            1,
            ["에베레스트", "K2", "칸첸중가", "로체"]
        ),
        Question(
            "세계에서 가장 긴 강은?",
            2,
            ["아마존강", "나일강", "양쯔강", "미시시피강"]
        ),
        Question(
            "세계에서 가장 큰 뜨거운 사막은?",
            1,
            ["사하라 사막", "고비 사막", "아타카마 사막", "칼라하리 사막"]
        )
    ]

    save_questions(questions)



print("-" * 30)
print("선영의 퀴즈 게임".center(25))
print("-" * 30)
print("1. 퀴즈 풀기")
print("2. 퀴즈 추가")
print("3. 퀴즈 목록")
print("4. 점수 확인")
print("5. 종료")
print("-" * 30)

choice = int(input("선택: "))
print("-" * 30)

if choice == 1:
    print("퀴즈 풀기 기능을 실행합니다.\n")

    Question.total = 0
    Question.score = 0

    for i, quiz in enumerate(questions, start=1):
        print(f"문제 {i}")
        quiz.solve()

    print(f"총 {Question.total}문제 중 {Question.score}문제를 맞추셨습니다.")
    print(f"점수: {Question.score / Question.total * 100:.2f}점")

elif choice == 2:
    print("퀴즈 추가 기능을 실행합니다.\n")

    while True:
        question_text = input("문제를 입력하세요: ").strip()

        if question_text:
            break

        print("문제 내용을 비워둘 수 없습니다.")

    new_choices = []

    for i in range(4):
        while True:
            choice_text = input(f"선택지 {i + 1}을 입력하세요: ").strip()

            if choice_text:
                new_choices.append(choice_text)
                break

            print("선택지를 비워둘 수 없습니다.")

    while True:
        try:
            answer = int(input("정답 번호를 입력하세요(1~4): "))

            if 1 <= answer <= 4:
                break

            print("정답 번호는 1부터 4 사이여야 합니다.")

        except ValueError:
            print("숫자만 입력하세요.")

    new_question = Question(
        question_text,
        answer,
        new_choices
    )

    questions.append(new_question)
    save_questions(questions)

    print("퀴즈가 저장되었습니다.")
    print(f"현재 저장된 퀴즈: {len(questions)}개")

elif choice == 3:
    print("퀴즈 목록 기능을 실행합니다.\n")

    if not questions:
        print("저장된 퀴즈가 없습니다.")
    else:
        for i, quiz in enumerate(questions, start=1):
            print(f"문제 {i}: {quiz.question}")
            
