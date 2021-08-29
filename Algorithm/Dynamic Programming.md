# Dynamic Programming

동일한 인풋에 의해 반복적인 솔루션이 발견되면, DP를 이용하여 최적화하는 것이 가능함.

기본 아이디어는 subproblem의 솔루션을 저장하여 다시 반복 계산하지 않고 필요할 때 사용하는 것.

즉, 하나의 문제는 단 한 번만 풀게하는 것.

이를 통해 exponential time complexity를 polynomial하게 줄이는 것이 가능함.

DP를 위한 가정은 두 가지가 있는데

- Overlapping subproblem : 큰 문제를 작은 문제로 바꿀 수 있다.
- Optimal substructure : 최적의 솔루션은 하위 구조에서도 최적의 솔루션을 가지고 있다.

# vs Greedy algorithm

Greedy는 종종 optimal solution을 보장하지 못하는 반면 DP는 기본적으로 보장함(모든 케이스에 대해 고려하기 때문에)

Greedy는 과거의 선택을 다시 보지않음. 이것 때문에 DP보다 오히려 더 빠름.

# LeetCode

[문제리스트](https://leetcode.com/discuss/general-discussion/1000929/solved-all-dynamic-programming-dp-problems-in-7-months)

[다익스트라 문제](https://leetcode.com/discuss/interview-question/731911/please-share-dijkstras-algorithm-questions)

다익스트라가 DP인 이유는 최종 경로까지의 최단 경로를 구하기 위해 여러개의 최단경로를 이용하여 구하기 때문



