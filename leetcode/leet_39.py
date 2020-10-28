class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(sum, index, path):
            # 종료조건
            # sum을 하나씩 빼가면서 0이되면 경로저장
            # 0보다 작아지면 그냥 리턴

            if sum < 0:
                return
            if sum == 0:
                result.append(path)
                return

            for i in range(index, len(candidates)):
                dfs(sum - candidates[i], i, path + [candidates[i]])

        dfs(target, 0, [])

        return result
