'''

Word Search II [https://leetcode.com/problems/word-search-ii/] [Hard] [https://www.youtube.com/watch?v=asbcE9mZz_U]

Tags:

    **Trie(prefix tree)
    Backtracking
    Trie
    Depth-first Search
    Matrix
    Word Search

Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

Example 1:

    Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
    Output: ["eat","oath"]

Example 2:

    Input: board = [["a","b"],["c","d"]], words = ["abcb"]
    Output: []

Constraints:

    m == board.length
    n == board[i].length
    1 <= m, n <= 12
    board[i][j] is a lowercase English letter.
    1 <= words.length <= 3 * 104
    1 <= words[i].length <= 10
    words[i] consists of lowercase English letters.
    All the strings of words are unique.

Notes:

    Brute force solution is to use recursion and check all the possible combinations
    DFS solution is to use a trie to store all the words and then check if the words are in the trie
    Trie(prefix tree) is a tree data structure used to store strings

    
'''
