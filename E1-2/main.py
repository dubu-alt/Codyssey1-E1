# main.py
# 프로그램을 실행하는 메인 파일

from quiz_game import QuizGame  # quiz_game.py에서 QuizGame 클래스 가져오기

def main():
    """
    프로그램의 진입점(entry point)
    
    이 함수가 호출되면:
        1. QuizGame 객체 생성
        2. run() 메서드 실행 (게임 시작)
    """
    # QuizGame(): 게임 객체 생성
    game = QuizGame()
    
    # game.run(): 게임 시작
    game.run()

if __name__ == "__main__":
    main()
