import json


class quiz:
    def __init__(self, question, answer, choices):
        self.question = question
        self.answer = answer
        self.choices = choices

    def solve(self):
        print(self.question)

        for i, choice in enumerate(self.choices, start=1):
            print(f"{i}. {choice}")

        while True:
            try:
                user_answer = int(
                    input("정답을 입력하세요: ").strip()
                )

                if user_answer not in range(1, 5):
                    print("1~4 사이의 숫자를 입력하세요.\n")
                    continue

                return user_answer == self.answer

            except ValueError:
                print("숫자만 입력하세요.\n")

    def to_dict(self):
        return {
            "question": self.question,
            "answer": self.answer,
            "choices": self.choices
        }


class QuizGame:
    def __init__(self):
        self.questions = []
        self.best_score = 0
        self.load_state()

    def get_default_questions(self):
        return [
            quiz(
                "대한민국의 수도는 어디일까요?",
                2,
                ["부산", "서울", "대전", "광주"]
            ),
            quiz(
                "지구에서 가장 큰 바다는?",
                3,
                ["대서양", "인도양", "태평양", "북극해"]
            ),
            quiz(
                "세계에서 가장 높은 산은?",
                1,
                ["에베레스트", "K2", "칸첸중가", "로체"]
            ),
            quiz(
                "세계에서 가장 긴 강은?",
                2,
                ["아마존강", "나일강", "양쯔강", "미시시피강"]
            ),
            quiz(
                "세계에서 가장 큰 뜨거운 사막은?",
                1,
                ["사하라 사막", "고비 사막", "아타카마 사막", "칼라하리 사막"]
            )
        ]

    def save_state(self):
        data = {
            "quizzes": [
                question.to_dict()
                for question in self.questions
            ],
            "best_score": self.best_score
        }

        try:
            with open(
                "state.json",
                "w",
                encoding="utf-8"
            ) as file:
                json.dump(
                    data,
                    file,
                    ensure_ascii=False,
                    indent=4
                )

        except OSError:
            print("state.json 파일을 저장하지 못했습니다.")

    def load_state(self):
        try:
            with open(
                "state.json",
                "r",
                encoding="utf-8"
            ) as file:
                data = json.load(file)

            quizzes_data = data["quizzes"]
            best_score = data["best_score"]

            loaded_questions = []

            for item in quizzes_data:
                question_text = item["question"]
                answer = item["answer"]
                choices = item["choices"]

                if not isinstance(question_text, str):
                    raise TypeError

                if not isinstance(answer, int):
                    raise TypeError

                if answer not in range(1, 5):
                    raise ValueError

                if not isinstance(choices, list):
                    raise TypeError

                if len(choices) != 4:
                    raise ValueError

                loaded_questions.append(
                    quiz(
                        question_text,
                        answer,
                        choices
                    )
                )

            if not isinstance(best_score, (int, float)):
                raise TypeError

            self.questions = loaded_questions
            self.best_score = best_score

        except FileNotFoundError:
            print("state.json 파일이 없습니다.")
            print("기본 퀴즈 데이터를 생성합니다.\n")

            self.questions = self.get_default_questions()
            self.best_score = 0
            self.save_state()

        except (
            json.JSONDecodeError,
            KeyError,
            TypeError,
            ValueError
        ):
            print("state.json 파일이 손상되었습니다.")
            print("기본 퀴즈 데이터로 복구합니다.\n")

            self.questions = self.get_default_questions()
            self.best_score = 0
            self.save_state()

        except OSError:
            print("state.json 파일을 읽지 못했습니다.")
            print("기본 퀴즈 데이터를 사용합니다.\n")

            self.questions = self.get_default_questions()
            self.best_score = 0

    def show_menu(self):
        print("-" * 30)
        print("선영의 퀴즈 게임".center(25))
        print("-" * 30)
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 점수 확인")
        print("5. 종료")
        print("-" * 30)

    def get_menu_choice(self):
        while True:
            try:
                choice = int(
                    input("선택: ").strip()
                )

                if choice not in range(1, 6):
                    print("1~5 사이의 숫자를 입력하세요.")
                    continue

                return choice

            except ValueError:
                print("숫자만 입력하세요.")

    def play_quiz(self):
        print("퀴즈 풀기 기능을 실행합니다.\n")

        if not self.questions:
            print("저장된 퀴즈가 없습니다.")
            return

        score_count = 0

        for i, quiz in enumerate(
            self.questions,
            start=1
        ):
            print(f"\n문제 {i}")

            if quiz.solve():
                print("정답입니다!\n")
                score_count += 1
            else:
                print("오답입니다.\n")

        total = len(self.questions)
        score = score_count / total * 100

        print(
            f"총 {total}문제 중 "
            f"{score_count}문제를 맞추셨습니다."
        )
        print(f"점수: {score:.2f}점")

        if score > self.best_score:
            self.best_score = score
            self.save_state()

            print(
                "축하합니다! "
                "최고 점수를 갱신했습니다."
            )

    def add_quiz(self):
        print("퀴즈 추가 기능을 실행합니다.\n")

        while True:
            question_text = input(
                "문제를 입력하세요: "
            ).strip()

            if question_text:
                break

            print("문제 내용을 비워둘 수 없습니다.")

        choices = []

        for i in range(4):
            while True:
                choice_text = input(
                    f"선택지 {i + 1}을 입력하세요: "
                ).strip()

                if choice_text:
                    choices.append(choice_text)
                    break

                print("선택지를 비워둘 수 없습니다.")

        while True:
            try:
                answer = int(
                    input(
                        "정답 번호를 입력하세요(1~4): "
                    ).strip()
                )

                if answer in range(1, 5):
                    break

                print(
                    "정답 번호는 "
                    "1부터 4 사이여야 합니다."
                )

            except ValueError:
                print("숫자만 입력하세요.")

        new_question = quiz(
            question_text,
            answer,
            choices
        )

        self.questions.append(new_question)
        self.save_state()

        print("퀴즈가 저장되었습니다.")
        print(
            f"현재 저장된 퀴즈: "
            f"{len(self.questions)}개"
        )

    def show_quizzes(self):
        print("퀴즈 목록 기능을 실행합니다.\n")

        if not self.questions:
            print("저장된 퀴즈가 없습니다.")
            return

        for i, quiz in enumerate(
            self.questions,
            start=1
        ):
            print(f"문제 {i}: {quiz.question}")

    def show_score(self):
        print("점수 확인 기능을 실행합니다.\n")

        if self.best_score > 0:
            print(
                f"최고 점수: "
                f"{self.best_score:.2f}점"
            )
        else:
            print("아직 최고 점수가 없습니다.")

    def run(self):
        while True:
            self.show_menu()
            choice = self.get_menu_choice()
            print("-" * 30)

            if choice == 1:
                self.play_quiz()

            elif choice == 2:
                self.add_quiz()

            elif choice == 3:
                self.show_quizzes()

            elif choice == 4:
                self.show_score()

            elif choice == 5:
                self.save_state()
                print("프로그램을 종료합니다.")
                break

            print()


game = QuizGame()

try:
    game.run()

except (KeyboardInterrupt, EOFError):
    print("\n입력이 중단되었습니다.")

    game.save_state()

    print("현재까지의 데이터를 저장했습니다.")
    print("프로그램을 안전하게 종료합니다.")