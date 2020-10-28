class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        path = ""  # 문자열 인애
        dic = {2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl',
               6: 'mno', 7: 'pqrs', 8: 'tuv', 9: 'wxyz'}

        def dfs(index, path):
            # 나온 문자열이 입력받은 숫자의 길이와 같으면 리턴
            if len(path) == len(digits):
                result.append(path)
                return

            # 입력값 자리수 만큼 반복
            for i in range(index, len(digits)):
                # 해당 숫자에 해당하는 모든 문자열 반복
                for j in dic[int(digits[i])]:
                    dfs(i + 1, path + j)  # 패스에 해당 문자 추가하며 재귀

        if not digits:
            return []

        result = []
        dfs(0, '')

        return result