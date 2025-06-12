import random
MIN_NUMBER = 0
MAX_NUMBER = 50
PARITY_PAYOUT = 1
EXACT_PAYOUT = 50

def get_player_choice(
    balance
):

    while True:

        try:

            # 잔액 표시
            print("현재 잔액: ")
            print(f"{balance:.0f}")
            print("원")

            # 숫자 입력
            prompt_number_start = "숫자를 선택하세요 ("
            prompt_number_mid1 = str(MIN_NUMBER)
            prompt_number_mid2 = "~"
            prompt_number_mid3 = str(MAX_NUMBER)
            prompt_number_end = "): "
            full_number_prompt = (
                prompt_number_start
                + prompt_number_mid1
                + prompt_number_mid2
                + prompt_number_mid3
                + prompt_number_end
            )
            choice_input = input(full_number_prompt)
            choice = int(choice_input)

            if choice < MIN_NUMBER:
                raise ValueError
            if choice > MAX_NUMBER:
                raise ValueError

            # 베팅 금액 입력
            bet_prompt = "베팅할 금액을 입력하세요 (숫자만 입력): "
            bet_input = input(bet_prompt)
            bet = float(bet_input)

            if bet <= 0:
                raise ValueError
            if bet > balance:
                raise ValueError

            return choice, bet

        except ValueError:

            msg1 = str(MIN_NUMBER)
            msg2 = "~"
            msg3 = str(MAX_NUMBER)
            msg4 = " 사이의 숫자와 "
            msg5 = "잔액 이하의 양수 금액을 입력하세요.\n"
            error_message = msg1 + msg2 + msg3 + msg4 + msg5
            print(error_message)