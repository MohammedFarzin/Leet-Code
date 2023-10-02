class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        count_a = 0
        count_b = 0

        for i in range(1, len(colors) - 1):
            current_color = colors[i]
            prev_color = colors[i-1]
            next_color = colors[i+1]

            if current_color == 'A' and next_color == 'A' and prev_color == 'A':
                count_a += 1
            elif current_color == 'B' and next_color == 'B' and prev_color == 'B':
                count_b += 1
        
        return count_a > count_b



sl = Solution()
colors = "ABBBBBBBAAA"
print(sl.winnerOfGame(colors))