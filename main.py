class question:
    total = 0
    score = 0
    def __init__(self, question, answer,choices):
        self.question = question
        self.answer = answer
        self.choices = choices

    def solve(self):
        print(self.question)
        i = 1
        for choice in self.choices:
            print(f"{i}. {choice}")
            i += 1

        user_answer = int(input("정답을 입력하세요: "))

        if user_answer == self.answer:
            print("정답입니다!\n")
            question.score += 1
        else:
            print("오답입니다.\n")
        question.total += 1

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
    quiz1 = question("대한민국의 수도는 어디일까요?", 2, ["부산", "서울", "대전", "광주"])
    print("문제1")
    quiz1.solve()
    quiz2 = question("지구에서 가장 큰 바다는?", 3, ["대서양", "인도양",  "태평양", "북극해"])
    print("문제2")
    quiz2.solve()
    quiz3 = question("세계에서 가장 높은 산은?", 1, ["에베레스트", "K2", "칸첸중가", "로체"])
    print("문제3")
    quiz3.solve()
    quiz4 = question("세계에서 가장 긴 강은?", 2, ["아마존강", "나일강", "양쯔강", "미시시피강"])
    print("문제4")
    quiz4.solve()
    quiz5 = question("세계에서 가장 큰 사막은?", 1, ["사하라", "고비", "아타카마", "칸쿤"])
    print("문제5")
    quiz5.solve()
    print(f"총 {question.total}문제 중 {question.score}문제를 맞추셨습니다.")
    print(f"점수: {question.score/question.total*100:.2f}점")
