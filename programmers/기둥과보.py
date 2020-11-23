#규칙에 맞는지 확인하는 함수를 만들고
#명령에 따라 벽을 세워본뒤 확인함수를 돌리고, 되면 그대로 안되면 다시 뺀다.
#완전탐색으로.
#기둥과 보 조건.
# 기둥은 바닥 위에 있거나 보의 한쪽 끝 부분 위에 있거나, 또는 다른 기둥 위에 있어야 합니다.
# 보는 한쪽 끝 부분이 기둥 위에 있거나, 또는 양쪽 끝 부분이 다른 보와 동시에 연결되어 있어야 합니다.
# 기둥은 좌표를 기준으로 위쪽으로 1칸.
# 보는 좌표를 기준으로 오른쪽으로 1칸.
# 명령에서 0은 기둥, 1은 보
# 벽면을 벗어나게 기둥, 보를 설치하는 경우는 없습니다
# 마지막 그래프의 상태를 출력하는 경우를 봐서 그래프 표현을 정해야하는데 어렵네
# 그래프로 할 필요는 없다. [x, y, structure] 형식으로만 하면 됨.!!!!!!!!!!!!!!!!!!!!!!!

def solution(n, build_frame):
    answer = []

    def check(answer):
        for struct in answer:
            x, y, structure = struct
            if structure == 1:
                # 보는 한쪽 끝 부분이 기둥 위에 있거나, 또는 양쪽 끝 부분이 다른 보와 동시에 연결되어 있어야 합니다.
                if [x, y-1, 0] in answer or [x+1, y-1,0] in answer or ([x-1,y,1] in answer and [x+1,y,1] in answer):
                    continue
                else:
                    return False
            else: #기둥이다.
                # 기둥은 바닥 위에 있거나 보의 한쪽 끝 부분 위에 있거나, 또는 다른 기둥 위에 있어야 합니다.
                if y == 0 or [x, y, 1] in answer or [x-1, y, 1] in answer or [x, y-1, 0] in answer:
                    continue
                else:
                    return False
        return True

    def do():
        for build in build_frame:
            x, y, structure, op = build
            if op == 1:
                answer.append([x, y, structure])
                if not check(answer):
                    answer.remove([x, y, structure])
            else:
                answer.remove([x, y, structure])
                if not check(answer):
                    answer.append([x, y, structure])
    do()
    answer.sort()

    return answer