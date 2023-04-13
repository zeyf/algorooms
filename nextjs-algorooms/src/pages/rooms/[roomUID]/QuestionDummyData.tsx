export default {
    questionIndex: 36,
    questionTitle: "Valid Sudoku",
    questionDifficulty: "Simple",
    questionBody: `
    Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

        1. Each row must contain the digits 1-9 without repetition.
    
        2. Each column must contain the digits 1-9 without repetition.
        
        3. Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

    Note:

    A Sudoku board (partially filled) could be valid but is not necessarily solvable.
    Only the filled cells need to be validated according to the mentioned rules.
    
    `,

    questionConstraints: [
        `board.length == 9`,
        `board[i].length == 9`,
        `board[i][j] is a digit 1-9 or '.'.`
    ],
    questionExamples: [
        {
            questionExampleInput: `board =
            [["5","3",".",".","7",".",".",".","."],
            ["6",".",".","1","9","5",".",".","."],
            [".","9","8",".",".",".",".","6","."],
            ["4",".",".","8",".","3",".",".","1"],
            ["8",".",".",".","6",".",".",".","3"],
            ["7",".",".",".","2",".",".",".","6"],
            [".","6",".",".",".",".","2","8","."],
            [".",".",".","4","1","9",".",".","5"],
            [".",".",".",".","8",".",".","7","9"]]`,
            questionExampleOutput: `true`,
            questionExampleExplanation: ""
        },
        {
            questionExampleInput: `board = 
            [["8","3",".",".","7",".",".",".","."],
            ["6",".",".","1","9","5",".",".","."],
            [".","9","8",".",".",".",".","6","."],
            ["8",".",".",".","6",".",".",".","3"],
            ["4",".",".","8",".","3",".",".","1"],
            ["7",".",".",".","2",".",".",".","6"],
            [".","6",".",".",".",".","2","8","."],
            [".",".",".","4","1","9",".",".","5"],
            [".",".",".",".","8",".",".","7","9"]]`,
            questionExampleOutput: `false`,
            questionExampleExplanation: `Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.`
        }
    ],
    questionHints: [

    ],
    questionTopics: [
        "Array",
        "Hash Table",
        "Matrix"
    ]
};