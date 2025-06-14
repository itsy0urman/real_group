import random
MIN_NUMBER = 0
MAX_NUMBER = 50
PARITY_PAYOUT = 1
EXACT_PAYOUT = 50

import math

def get_player_choice(balance):
    while True:
        try:
            # 잔액 표시
            print(f"현재 잔액: {balance:.0f}원")

            # 숫자 입력
            choice = int(input(f"숫자를 선택하세요 ({MIN_NUMBER}~{MAX_NUMBER}): "))
            if choice < MIN_NUMBER or choice > MAX_NUMBER:
                raise ValueError

            # 베팅 금액 입력
            bet_input = input("베팅할 금액을 입력하세요 (숫자만 또는 all in/half/quarter): ").strip().lower()

            # special keywords 처리
            if bet_input in ("all in", "all-in", "allin"):
                bet = balance
            elif bet_input == "half":
                bet = balance // 2
            elif bet_input == "quarter":
                bet = balance // 4
            else:
                bet = float(bet_input)

            # 유효성 검사
            if bet <= 0 or bet > balance:
                raise ValueError

            return choice, bet

        except ValueError:
            print(f"{MIN_NUMBER}~{MAX_NUMBER} 사이의 숫자와, 0초과 현재 잔액({balance:.0f}원) 이하의 금액을 입력하세요.\n")

def evaluate_round(
    player_number,
    bet_amount,
    computer_number
):

    equal_check = (player_number == computer_number)

    if equal_check:

        gain_exact = bet_amount * EXACT_PAYOUT
        net_gain = gain_exact
        outcome = "Exact Match! 숫자까지 맞추셨습니다."

    else:

        player_parity = player_number % 2
        computer_parity = computer_number % 2
        parity_match = (player_parity == computer_parity)

        if parity_match:

            gain_parity = bet_amount * PARITY_PAYOUT
            net_gain = gain_parity
            outcome = "Parity Match! 짝/홀만 맞추셨습니다."

        else:

            loss_amount = -bet_amount
            net_gain = loss_amount
            outcome = "패배했습니다. 짝/홀 모두 틀리셨습니다."

    return outcome, net_gain

def play_game():

    line1 = "=== 짝/홀 & 숫자 맞추기 도박 게임 ==="
    print(line1)

    line2 = "처음 참가자에게 1,000,000원을 지급합니다."
    print(line2)

    part1 = "짝수/홀수만 맞추면 배당률 "
    part2 = str(PARITY_PAYOUT)
    part3 = ":1, "
    part4 = "숫자까지 정확히 맞추면 배당률 "
    part5 = str(EXACT_PAYOUT)
    part6 = ":1 입니다.\n"
    full_info = part1 + part2 + part3 + part4 + part5 + part6
    print(full_info)

    balance = 1_000_000
    initial_balance = balance
    admin_profit = 0

    while True:

        player_number, bet_amount = get_player_choice(
            balance
        )

        lower_bound = MIN_NUMBER
        upper_bound = MAX_NUMBER
        computer_number = random.randint(
            lower_bound,
            upper_bound
        )

        print("\n컴퓨터가 뽑은 숫자: ")
        print(computer_number)

        outcome, net_gain = evaluate_round(
            player_number,
            bet_amount,
            computer_number
        )

        balance = balance + net_gain
        admin_profit = admin_profit - net_gain

        if net_gain > 0:

            print(outcome)
            print("→ 베팅 ", end="")
            print(f"{bet_amount:.0f}", end="")
            print("원, 순수익 ", end="")
            print(f"{net_gain:.0f}", end="")
            print("원 획득")

        elif net_gain == 0:

            print(outcome)
            print("→ 베팅 ", end="")
            print(f"{bet_amount:.0f}", end="")
            print("원, 순수익 0원 (원금 유지)")

        else:

            print(outcome)
            print("→ 베팅 ", end="")
            print(f"{bet_amount:.0f}", end="")
            print("원 전액 손실")

        print("현재 잔액: ")
        print(f"{balance:.0f}")
        print("원\n")

        if balance <= 0:

            print("You lose")
            break

        cont_prompt = "한 판 더 하시겠습니까? (y/n): "
        cont_input = input(cont_prompt)
        cont = cont_input.strip().lower()

        if cont != "y":
            break

    player_profit = balance - initial_balance

    print("\n=== 게임 종료 ===")
    print("플레이어 최종 잔액: ")
    print(f"{balance:.0f}")
    print("원")
    print("플레이어 수익/손실: ")
    print(f"{player_profit:+,.0f}")
    print("원")
    print("관리자 수익/손실: ")
    print(f"{admin_profit:+,.0f}")
    print("원")
    print("즐거운 시간 되셨길 바랍니다!")




if __name__ == "__main__":

    play_game()