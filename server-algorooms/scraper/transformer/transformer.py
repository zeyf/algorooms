import re;
import os;
import json;

TEST_INJECTION_PLACEMENT_TERM_SWAP = "7xY5rPU32L37eQ7WCYP0108thgf7u5Uj3M8Eq076K87Nk6ExIjPcO71878dX9fVt88Uxp8zDVM12bM4BgmS37gRDIdmxmJ7ENZ0v";

questions = [
  {
    "title": "Make Costs of Paths Equal in a Binary Tree",
    "description": "You are given an integer n representing the number of nodes in a perfect binary tree consisting of nodes numbered from 1 to n. The root of the tree is node 1 and each node i in the tree has two children where the left child is the node 2 * i and the right child is 2 * i + 1.\nEach node in the tree also has a cost represented by a given 0-indexed integer array cost of size n where cost[i] is the cost of node i + 1. You are allowed to increment the cost of any node by 1 any number of times.\nReturn the minimum number of increments you need to make the cost of paths from the root to each leaf node equal.\nNote:\n\nA perfect binary tree is a tree where each node, except the leaf nodes, has exactly 2 children.\nThe cost of a path is the sum of costs of nodes in the path.\n\n \n",
    "examples": [
      {
        "input": "Input: n = 7, cost = [1,5,2,2,3,3,1]",
        "output": "Output: 6",
        "explanation": "Explanation: We can do the following increments:"
      },
      {
        "input": "Input: n = 3, cost = [5,3,3]",
        "output": "Output: 0",
        "explanation": "Explanation: The two paths already have equal total costs, so no increments are needed."
      }
    ],
    "topics": [
      "Array",
      "Dynamic Programming",
      "Greedy",
      "Tree",
      "Binary Tree"
    ],
    "difficulty": "Medium",
    "constraints": [
      "3 <= n <= 105",
      "n + 1 is a power of 2",
      "cost.length == n",
      "1 <= cost[i] <= 104"
    ],
    "hints": [
      "The path from the root to a leaf that has the maximum cost should not be modified.",
      "The optimal way is to increase all other paths to make their costs equal to the path with maximum cost."
    ]
  },
  {
    "title": "Number of Adjacent Elements With the Same Color",
    "description": "There is a 0-indexed array nums of length n. Initially, all elements are uncolored (has a value of 0).\nYou are given a 2D integer array queries where queries[i] = [indexi, colori].\nFor each query, you color the index indexi with the color colori in the array nums.\nReturn an array answer of the same length as queries where answer[i] is the number of adjacent elements with the same color after the ith query.\nMore formally, answer[i] is the number of indices j, such that 0 <= j < n - 1 and nums[j] == nums[j + 1] and nums[j] != 0 after the ith query.\n \n",
    "examples": [
      {
        "input": "Input: n = 4, queries = [[0,2],[1,2],[3,1],[1,1],[2,1]]",
        "output": "Output: [0,1,1,0,2]",
        "explanation": "Explanation: Initially array nums = [0,0,0,0], where 0 denotes uncolored elements of the array."
      },
      {
        "input": "Input: n = 1, queries = [[0,100000]]",
        "output": "Output: [0]",
        "explanation": "Explanation: Initially array nums = [0], where 0 denotes uncolored elements of the array."
      }
    ],
    "topics": [
      "Array"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= n <= 105",
      "1 <= queries.length <= 105",
      "queries[i].length == 2",
      "0 <= indexi <= n - 1",
      "1 <=  colori <= 105"
    ],
    "hints": [
      "Since at each query, only one element is being recolored, we just need to focus on its neighbors.",
      "If an element that is changed on the i-th query had the same color as its right element answer decreases by 1. Similarly contributes its left element too.",
      "After changing the color, if the element has the same color as its right element answer increases by 1. Similarly contributes its left element too."
    ]
  },
  {
    "title": "Frequency Tracker",
    "description": "Design a data structure that keeps track of the values in it and answers some queries regarding their frequencies.\nImplement the FrequencyTracker class.\n\nFrequencyTracker(): Initializes the FrequencyTracker object with an empty array initially.\nvoid add(int number): Adds number to the data structure.\nvoid deleteOne(int number): Deletes one occurence of number from the data structure. The data structure may not contain number, and in this case nothing is deleted.\nbool hasFrequency(int frequency): Returns true if there is a number in the data structure that occurs frequency number of times, otherwise, it returns false.\n\n \n",
    "examples": [
      {
        "input": "Input\n[\"FrequencyTracker\", \"add\", \"add\", \"hasFrequency\"]",
        "output": "Output\n[null, null, null, true]",
        "explanation": "Explanation\nFrequencyTracker frequencyTracker = new FrequencyTracker();"
      },
      {
        "input": "Input\n[\"FrequencyTracker\", \"add\", \"deleteOne\", \"hasFrequency\"]",
        "output": "Output\n[null, null, null, false]",
        "explanation": "Explanation\nFrequencyTracker frequencyTracker = new FrequencyTracker();"
      },
      {
        "input": "Input\n[\"FrequencyTracker\", \"hasFrequency\", \"add\", \"hasFrequency\"]",
        "output": "Output\n[null, false, null, true]",
        "explanation": "Explanation\nFrequencyTracker frequencyTracker = new FrequencyTracker();"
      }
    ],
    "topics": [
      "Hash Table",
      "Design"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= number <= 105",
      "1 <= frequency <= 105",
      "At most, 2 * 105 calls will be made to add, deleteOne, and hasFrequency in total."
    ],
    "hints": [
      "Put all the numbers in a hash map (or just an integer array given the number range is small) to maintain each number’s frequency dynamically.",
      "Put each frequency in another hash map (or just an integer array given the range is small, note there are only 200000 calls in total) to maintain each kind of frequency dynamically.",
      "Keep the 2 hash maps in sync."
    ]
  },
  {
    "title": "Find the Distinct Difference Array",
    "description": "You are given a 0-indexed array nums of length n.\nThe distinct difference array of nums is an array diff of length n such that diff[i] is equal to the number of distinct elements in the suffix nums[i + 1, ..., n - 1] subtracted from the number of distinct elements in the prefix nums[0, ..., i].\nReturn the distinct difference array of nums.\nNote that nums[i, ..., j] denotes the subarray of nums starting at index i and ending at index j inclusive. Particularly, if i > j then nums[i, ..., j] denotes an empty subarray.\n \n",
    "examples": [
      {
        "input": "Input: nums = [1,2,3,4,5]",
        "output": "Output: [-3,-1,1,3,5]",
        "explanation": "Explanation: For index i = 0, there is 1 element in the prefix and 4 distinct elements in the suffix. Thus, diff[0] = 1 - 4 = -3."
      },
      {
        "input": "Input: nums = [3,2,3,4,2]",
        "output": "Output: [-2,-1,0,2,3]",
        "explanation": "Explanation: For index i = 0, there is 1 element in the prefix and 3 distinct elements in the suffix. Thus, diff[0] = 1 - 3 = -2."
      }
    ],
    "topics": [
      "Array",
      "Hash Table"
    ],
    "difficulty": "Easy",
    "constraints": [
      "1 <= n == nums.length <= 50",
      "1 <= nums[i] <= 50"
    ],
    "hints": [
      "Which data structure will help you maintain distinct elements?",
      "Iterate over all possible prefix sizes. Then, use a nested loop to add the elements of the prefix to a set, and another nested loop to add the elements of the suffix to another set."
    ]
  },
  {
    "title": "Maximum Sum With Exactly K Elements ",
    "description": "You are given a 0-indexed integer array nums and an integer k. Your task is to perform the following operation exactly k times in order to maximize your score:\n\nSelect an element m from nums.\nRemove the selected element m from the array.\nAdd a new element with a value of m + 1 to the array.\nIncrease your score by m.\n\nReturn the maximum score you can achieve after performing the operation exactly k times.\n \n",
    "examples": [
      {
        "input": "Input: nums = [1,2,3,4,5], k = 3",
        "output": "Output: 18",
        "explanation": "Explanation: We need to choose exactly 3 elements from nums to maximize the sum."
      },
      {
        "input": "Input: nums = [5,5,5], k = 2",
        "output": "Output: 11",
        "explanation": "Explanation: We need to choose exactly 2 elements from nums to maximize the sum."
      }
    ],
    "topics": [
      "Array",
      "Greedy"
    ],
    "difficulty": "Easy",
    "constraints": [
      "1 <= nums.length <= 100",
      "1 <= nums[i] <= 100",
      "1 <= k <= 100"
    ],
    "hints": []
  },
  {
    "title": "Find the Prefix Common Array of Two Arrays",
    "description": "You are given two 0-indexed integer permutations A and B of length n.\nA prefix common array of A and B is an array C such that C[i] is equal to the count of numbers that are present at or before the index i in both A and B.\nReturn the prefix common array of A and B.\nA sequence of n integers is called a permutation if it contains all integers from 1 to n exactly once.\n \n",
    "examples": [
      {
        "input": "Input: A = [1,3,2,4], B = [3,1,2,4]",
        "output": "Output: [0,2,3,4]",
        "explanation": "Explanation: At i = 0: no number is common, so C[0] = 0."
      },
      {
        "input": "Input: A = [2,3,1], B = [3,1,2]",
        "output": "Output: [0,1,3]",
        "explanation": "Explanation: At i = 0: no number is common, so C[0] = 0."
      }
    ],
    "topics": [
      "Array",
      "Hash Table"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= A.length == B.length == n <= 50",
      "1 <= A[i], B[i] <= n",
      "It is guaranteed that A and B are both a permutation of n integers."
    ],
    "hints": [
      "Consider keeping a frequency array that stores the count of occurrences of each number till index i.",
      "If a number occurred two times, it means it occurred in both A and B since they’re both permutations so add one to the answer."
    ]
  },
  {
    "title": "Make Array Empty",
    "description": "You are given an integer array nums containing distinct numbers, and you can perform the following operations until the array is empty:\n\nIf the first element has the smallest value, remove it\nOtherwise, put the first element at the end of the array.\n\nReturn an integer denoting the number of operations it takes to make nums empty.\n \n",
    "examples": [
      {
        "input": "Input: nums = [3,4,-1]",
        "output": "Output: 5",
        "explanation": ""
      },
      {
        "input": "Input: nums = [1,2,4,3]",
        "output": "Output: 5",
        "explanation": ""
      },
      {
        "input": "Input: nums = [1,2,3]",
        "output": "Output: 3",
        "explanation": ""
      }
    ],
    "topics": [
      "Array",
      "Binary Search",
      "Greedy",
      "Binary Indexed Tree",
      "Segment Tree",
      "Sorting",
      "Ordered Set"
    ],
    "difficulty": "Hard",
    "constraints": [
      "1 <= nums.length <= 105",
      "-109 <= nums[i] <= 109",
      "All values in nums are distinct."
    ],
    "hints": [
      "Understand the order in which the indices are removed from the array.",
      "We don’t really need to delete or move the elements, only the array length matters.",
      "Upon removing an index, decide how many steps it takes to move to the next one.",
      "Use a data structure to speed up the calculation."
    ]
  },
  {
    "title": "Maximum Number of Fish in a Grid",
    "description": "You are given a 0-indexed 2D matrix grid of size m x n, where (r, c) represents:\n\nA land cell if grid[r][c] = 0, or\nA water cell containing grid[r][c] fish, if grid[r][c] > 0.\n\nA fisher can start at any water cell (r, c) and can do the following operations any number of times:\n\nCatch all the fish at cell (r, c), or\nMove to any adjacent water cell.\n\nReturn the maximum number of fish the fisher can catch if he chooses his starting cell optimally, or 0 if no water cell exists.\nAn adjacent cell of the cell (r, c), is one of the cells (r, c + 1), (r, c - 1), (r + 1, c) or (r - 1, c) if it exists.\n \n",
    "examples": [
      {
        "input": "Input: grid = [[0,2,1,0],[4,0,0,3],[1,0,0,4],[0,3,2,0]]",
        "output": "Output: 7",
        "explanation": "Explanation: The fisher can start at cell (1,3) and collect 3 fish, then move to cell (2,3) and collect 4 fish."
      },
      {
        "input": "Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,1]]",
        "output": "Output: 1",
        "explanation": "Explanation: The fisher can start at cells (0,0) or (3,3) and collect a single fish. "
      }
    ],
    "topics": [
      "Array",
      "Depth-First Search",
      "Breadth-First Search",
      "Union Find",
      "Matrix"
    ],
    "difficulty": "Medium",
    "constraints": [
      "m == grid.length",
      "n == grid[i].length",
      "1 <= m, n <= 10",
      "0 <= grid[i][j] <= 10"
    ],
    "hints": [
      "Run DFS from each non-zero cell.",
      "Each time you pick a cell to start from, add up the number of fish contained in the cells you visit."
    ]
  },
  {
    "title": "Minimum Number of Operations to Make All Array Elements Equal to 1",
    "description": "You are given a 0-indexed array nums consisiting of positive integers. You can do the following operation on the array any number of times:\n\nSelect an index i such that 0 <= i < n - 1 and replace either of nums[i] or nums[i+1] with their gcd value.\n\nReturn the minimum number of operations to make all elements of nums equal to 1. If it is impossible, return -1.\nThe gcd of two integers is the greatest common divisor of the two integers.\n \n",
    "examples": [
      {
        "input": "Input: nums = [2,6,3,4]",
        "output": "Output: 4",
        "explanation": "Explanation: We can do the following operations:"
      },
      {
        "input": "Input: nums = [2,10,6,14]",
        "output": "Output: -1",
        "explanation": "Explanation: It can be shown that it is impossible to make all the elements equal to 1."
      }
    ],
    "topics": [
      "Array",
      "Math",
      "Number Theory"
    ],
    "difficulty": "Medium",
    "constraints": [
      "2 <= nums.length <= 50",
      "1 <= nums[i] <= 106",
      "",
      " ",
      "Follow-up:",
      "The O(n) time complexity solution works, but could you find an O(1) constant time complexity solution?"
    ],
    "hints": [
      "Note that if you have at least one occurrence of 1 in the array, then you can make all the other elements equal to 1 with one operation each.",
      "Try finding the shortest subarray with a gcd equal to 1."
    ]
  },
  {
    "title": "Sum Multiples",
    "description": "Given a positive integer n, find the sum of all integers in the range [1, n] inclusive that are divisible by 3, 5, or 7.\nReturn an integer denoting the sum of all numbers in the given range satisfying the constraint.\n \n",
    "examples": [
      {
        "input": "Input: n = 7",
        "output": "Output: 21",
        "explanation": "Explanation: Numbers in the range [1, 7] that are divisible by 3, 5, or 7 are 3, 5, 6, 7. The sum of these numbers is 21."
      },
      {
        "input": "Input: n = 10",
        "output": "Output: 40",
        "explanation": "Explanation: Numbers in the range [1, 10] that are divisible by 3, 5, or 7 are 3, 5, 6, 7, 9, 10. The sum of these numbers is 40."
      },
      {
        "input": "Input: n = 9",
        "output": "Output: 30",
        "explanation": "Explanation: Numbers in the range [1, 9] that are divisible by 3, 5, or 7 are 3, 5, 6, 7, 9. The sum of these numbers is 30."
      }
    ],
    "topics": [
      "Array",
      "Math",
      "Number Theory"
    ],
    "difficulty": "Easy",
    "constraints": [
      "1 <= n <= 103"
    ],
    "hints": [
      "Iterate through the range 1 to n and count numbers divisible by either 3, 5, or 7."
    ]
  },
  {
    "title": "Sliding Subarray Beauty",
    "description": "Given an integer array nums containing n integers, find the beauty of each subarray of size k.\nThe beauty of a subarray is the xth smallest integer in the subarray if it is negative, or 0 if there are fewer than x negative integers.\nReturn an integer array containing n - k + 1 integers, which denote the beauty of the subarrays in order from the first index in the array.\n\n\nA subarray is a contiguous non-empty sequence of elements within an array.\n\n\n \n",
    "examples": [
      {
        "input": "Input: nums = [1,-1,-3,-2,3], k = 3, x = 2",
        "output": "Output: [-1,-2,-2]",
        "explanation": "Explanation: There are 3 subarrays with size k = 3. "
      },
      {
        "input": "Input: nums = [-1,-2,-3,-4,-5], k = 2, x = 2",
        "output": "Output: [-1,-2,-3,-4]",
        "explanation": "Explanation: There are 4 subarrays with size k = 2."
      },
      {
        "input": "Input: nums = [-3,1,2,-3,0,-3], k = 2, x = 1",
        "output": "Output: [-3,0,-3,-3,-3]",
        "explanation": "Explanation: There are 5 subarrays with size k = 2."
      }
    ],
    "topics": [
      "Array",
      "Hash Table",
      "Sliding Window"
    ],
    "difficulty": "Medium",
    "constraints": [
      "n == nums.length ",
      "1 <= n <= 105",
      "1 <= k <= n",
      "1 <= x <= k ",
      "-50 <= nums[i] <= 50"
    ],
    "hints": [
      "Try to maintain the frequency of negative numbers in the current window of size k.",
      "The x^th smallest negative integer can be gotten by iterating through the frequencies of the numbers in order."
    ]
  },
  {
    "title": "Calculate Delayed Arrival Time",
    "description": "You are given a positive integer arrivalTime denoting the arrival time of a train in hours, and another positive integer delayedTime denoting the amount of delay in hours.\nReturn the time when the train will arrive at the station.\nNote that the time in this problem is in 24-hours format.\n \n",
    "examples": [
      {
        "input": "Input: arrivalTime = 15, delayedTime = 5 ",
        "output": "Output: 20 ",
        "explanation": "Explanation: Arrival time of the train was 15:00 hours. It is delayed by 5 hours. Now it will reach at 15+5 = 20 (20:00 hours)."
      },
      {
        "input": "Input: arrivalTime = 13, delayedTime = 11",
        "output": "Output: 0",
        "explanation": "Explanation: Arrival time of the train was 13:00 hours. It is delayed by 11 hours. Now it will reach at 13+11=24 (Which is denoted by 00:00 in 24 hours format so return 0)."
      }
    ],
    "topics": [
      "Math"
    ],
    "difficulty": "Easy",
    "constraints": [
      "1 <= arrivaltime < 24",
      "1 <= delayedTime <= 24"
    ],
    "hints": [
      "Use the modulo operator to handle the case when the arrival time plus the delayed time goes beyond 24 hours.",
      "If the arrival time plus the delayed time is greater than or equal to 24, you can also subtract 24 to get the time in the 24-hour format."
    ]
  },
  {
    "title": "Minimize the Total Price of the Trips",
    "description": "There exists an undirected and unrooted tree with n nodes indexed from 0 to n - 1. You are given the integer n and a 2D integer array edges of length n - 1, where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree.\nEach node has an associated price. You are given an integer array price, where price[i] is the price of the ith node.\nThe price sum of a given path is the sum of the prices of all nodes lying on that path.\nAdditionally, you are given a 2D integer array trips, where trips[i] = [starti, endi] indicates that you start the ith trip from the node starti and travel to the node endi by any path you like.\nBefore performing your first trip, you can choose some non-adjacent nodes and halve the prices.\nReturn the minimum total price sum to perform all the given trips.\n \n",
    "examples": [
      {
        "input": "Input: n = 4, edges = [[0,1],[1,2],[1,3]], price = [2,2,10,6], trips = [[0,3],[2,1],[2,3]]",
        "output": "Output: 23",
        "explanation": "Explanation: The diagram above denotes the tree after rooting it at node 2. The first part shows the initial tree and the second part shows the tree after choosing nodes 0, 2, and 3, and making their price half."
      },
      {
        "input": "Input: n = 2, edges = [[0,1]], price = [2,2], trips = [[0,0]]",
        "output": "Output: 1",
        "explanation": "Explanation: The diagram above denotes the tree after rooting it at node 0. The first part shows the initial tree and the second part shows the tree after choosing node 0, and making its price half."
      }
    ],
    "topics": [
      "Array",
      "Dynamic Programming",
      "Tree",
      "Depth-First Search"
    ],
    "difficulty": "Hard",
    "constraints": [
      "1 <= n <= 50",
      "edges.length == n - 1",
      "0 <= ai, bi <= n - 1",
      "edges represents a valid tree.",
      "price.length == n",
      "price[i] is an even integer.",
      "1 <= price[i] <= 1000",
      "1 <= trips.length <= 100",
      "0 <= starti, endi <= n - 1"
    ],
    "hints": [
      "The final answer is the price[i] * freq[i], where freq[i] is the number of times node i was visited during the trip, and price[i] is the final price.",
      "To find freq[i] we will use dfs or bfs for each trip and update every node on the path start and end.",
      "Finally, to find the final price[i] we will use dynamic programming on the tree. Let dp(v, 0/1) denote the minimum total price with the node v’s price being halved or not."
    ]
  },
  {
    "title": "Row With Maximum Ones",
    "description": "Given a m x n binary matrix mat, find the 0-indexed position of the row that contains the maximum count of ones, and the number of ones in that row.\nIn case there are multiple rows that have the maximum count of ones, the row with the smallest row number should be selected.\nReturn an array containing the index of the row, and the number of ones in it.\n \n",
    "examples": [
      {
        "input": "Input: mat = [[0,1],[1,0]]",
        "output": "Output: [0,1]",
        "explanation": "Explanation: Both rows have the same number of 1's. So we return the index of the smaller row, 0, and the maximum count of ones (1). So, the answer is [0,1]. "
      },
      {
        "input": "Input: mat = [[0,0,0],[0,1,1]]",
        "output": "Output: [1,2]",
        "explanation": "Explanation: The row indexed 1 has the maximum count of ones (2). So we return its index, 1, and the count. So, the answer is [1,2]."
      },
      {
        "input": "Input: mat = [[0,0],[1,1],[0,0]]",
        "output": "Output: [1,2]",
        "explanation": "Explanation: The row indexed 1 has the maximum count of ones (2). So the answer is [1,2]."
      }
    ],
    "topics": [
      "Array",
      "Matrix"
    ],
    "difficulty": "Easy",
    "constraints": [
      "m == mat.length ",
      "n == mat[i].length ",
      "1 <= m, n <= 100 ",
      "mat[i][j] is either 0 or 1."
    ],
    "hints": [
      "Iterate through each row and keep the count of ones."
    ]
  },
  {
    "title": "Minimum Additions to Make Valid String",
    "description": "Given a string word to which you can insert letters \"a\", \"b\" or \"c\" anywhere and any number of times, return the minimum number of letters that must be inserted so that word becomes valid.\nA string is called valid if it can be formed by concatenating the string \"abc\" several times.\n \n",
    "examples": [
      {
        "input": "Input: word = \"b\"",
        "output": "Output: 2",
        "explanation": "Explanation: Insert the letter \"a\" right before \"b\", and the letter \"c\" right next to \"a\" to obtain the valid string \"abc\"."
      },
      {
        "input": "Input: word = \"aaa\"",
        "output": "Output: 6",
        "explanation": "Explanation: Insert letters \"b\" and \"c\" next to each \"a\" to obtain the valid string \"abcabcabc\"."
      },
      {
        "input": "Input: word = \"abc\"",
        "output": "Output: 0",
        "explanation": "Explanation: word is already valid. No modifications are needed. "
      }
    ],
    "topics": [
      "String",
      "Dynamic Programming",
      "Stack",
      "Greedy"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= word.length <= 50",
      "word consists of letters \"a\", \"b\" and \"c\" only."
    ],
    "hints": [
      "Maintain a pointer on word and another pointer on string “abc”.",
      "If the two characters that are being pointed to differ, Increment the answer and the pointer to the string “abc” by one."
    ]
  },
  {
    "title": "Minimum Reverse Operations",
    "description": "You are given an integer n and an integer p in the range [0, n - 1]. Representing a 0-indexed array arr of length n where all positions are set to 0's, except position p which is set to 1.\nYou are also given an integer array banned containing some positions from the array. For the ith position in banned, arr[banned[i]] = 0, and banned[i] != p.\nYou can perform multiple operations on arr. In an operation, you can choose a subarray with size k and reverse the subarray. However, the 1 in arr should never go to any of the positions in banned. In other words, after each operation arr[banned[i]] remains 0.\nReturn an array ans where for each i from [0, n - 1], ans[i] is the minimum number of reverse operations needed to bring the 1 to position i in arr, or -1 if it is impossible.\n\nA subarray is a contiguous non-empty sequence of elements within an array.\nThe values of ans[i] are independent for all i's.\nThe reverse of an array is an array containing the values in reverse order.\n\n \n",
    "examples": [
      {
        "input": "Input: n = 4, p = 0, banned = [1,2], k = 4",
        "output": "Output: [0,-1,-1,1]",
        "explanation": "Explanation: In this case k = 4 so there is only one possible reverse operation we can perform, which is reversing the whole array. Initially, 1 is placed at position 0 so the amount of operations we need for position 0 is 0. We can never place a 1 on the banned positions, so the answer for positions 1 and 2 is -1. Finally, with one reverse operation we can bring the 1 to index 3, so the answer for position 3 is 1. "
      },
      {
        "input": "Input: n = 5, p = 0, banned = [2,4], k = 3",
        "output": "Output: [0,-1,-1,-1,-1]",
        "explanation": "Explanation: In this case the 1 is initially at position 0, so the answer for that position is 0. We can perform reverse operations of size 3. The 1 is currently located at position 0, so we need to reverse the subarray [0, 2] for it to leave that position, but reversing that subarray makes position 2 have a 1, which shouldn't happen. So, we can't move the 1 from position 0, making the result for all the other positions -1. "
      },
      {
        "input": "Input: n = 4, p = 2, banned = [0,1,3], k = 1",
        "output": "Output: [-1,-1,0,-1]",
        "explanation": "Explanation: In this case we can only perform reverse operations of size 1. So the 1 never changes its position."
      }
    ],
    "topics": [
      "Array",
      "Breadth-First Search",
      "Ordered Set"
    ],
    "difficulty": "Hard",
    "constraints": [
      "1 <= n <= 105",
      "0 <= p <= n - 1",
      "0 <= banned.length <= n - 1",
      "0 <= banned[i] <= n - 1",
      "1 <= k <= n ",
      "banned[i] != p",
      "all values in banned are unique"
    ],
    "hints": [
      "Can we use a breadth-first search to find the minimum number of operations?",
      "Find the beginning and end indices of the subarray of size k that can be reversed to bring 1 to a particular position.",
      "Can we visit every index or do we need to consider the parity of k?"
    ]
  },
  {
    "title": "Mice and Cheese",
    "description": "There are two mice and n different types of cheese, each type of cheese should be eaten by exactly one mouse.\nA point of the cheese with index i (0-indexed) is:\n\nreward1[i] if the first mouse eats it.\nreward2[i] if the second mouse eats it.\n\nYou are given a positive integer array reward1, a positive integer array reward2, and a non-negative integer k.\nReturn the maximum points the mice can achieve if the first mouse eats exactly k types of cheese.\n \n",
    "examples": [
      {
        "input": "Input: reward1 = [1,1,3,4], reward2 = [4,4,1,1], k = 2",
        "output": "Output: 15",
        "explanation": "Explanation: In this example, the first mouse eats the 2nd (0-indexed) and the 3rd types of cheese, and the second mouse eats the 0th and the 1st types of cheese."
      },
      {
        "input": "Input: reward1 = [1,1], reward2 = [1,1], k = 2",
        "output": "Output: 2",
        "explanation": "Explanation: In this example, the first mouse eats the 0th (0-indexed) and 1st types of cheese, and the second mouse does not eat any cheese."
      }
    ],
    "topics": [
      "Array",
      "Greedy",
      "Sorting",
      "Heap (Priority Queue)"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= n == reward1.length == reward2.length <= 105",
      "1 <= reward1[i], reward2[i] <= 1000",
      "0 <= k <= n"
    ],
    "hints": [
      "The intended solution uses greedy approach.",
      "Imagine at first that the second mouse eats all the cheese, then we should choose k types of cheese with the maximum sum of - reward2[i] + reward1[i]."
    ]
  },
  {
    "title": "Convert an Array Into a 2D Array With Conditions",
    "description": "You are given an integer array nums. You need to create a 2D array from nums satisfying the following conditions:\n\nThe 2D array should contain only the elements of the array nums.\nEach row in the 2D array contains distinct integers.\nThe number of rows in the 2D array should be minimal.\n\nReturn the resulting array. If there are multiple answers, return any of them.\nNote that the 2D array can have a different number of elements on each row.\n \n",
    "examples": [
      {
        "input": "Input: nums = [1,3,4,1,2,3,1]",
        "output": "Output: [[1,3,4,2],[1,3],[1]]",
        "explanation": "Explanation: We can create a 2D array that contains the following rows:"
      },
      {
        "input": "Input: nums = [1,2,3,4]",
        "output": "Output: [[4,3,2,1]]",
        "explanation": "Explanation: All elements of the array are distinct, so we can keep all of them in the first row of the 2D array."
      }
    ],
    "topics": [
      "Array",
      "Hash Table"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= nums.length <= 200",
      "1 <= nums[i] <= nums.length"
    ],
    "hints": [
      "Process the elements in the array one by one in any order and only create a new row in the matrix when we cannot put it into the existing rows",
      "We can simply iterate over the existing rows of the matrix to see if we can place each element."
    ]
  },
  {
    "title": "Find the Longest Balanced Substring of a Binary String",
    "description": "You are given a binary string s consisting only of zeroes and ones.\nA substring of s is considered balanced if all zeroes are before ones and the number of zeroes is equal to the number of ones inside the substring. Notice that the empty substring is considered a balanced substring.\nReturn the length of the longest balanced substring of s.\nA substring is a contiguous sequence of characters within a string.\n \n",
    "examples": [
      {
        "input": "Input: s = \"01000111\"",
        "output": "Output: 6",
        "explanation": "Explanation: The longest balanced substring is \"000111\", which has length 6."
      },
      {
        "input": "Input: s = \"00111\"",
        "output": "Output: 4",
        "explanation": "Explanation: The longest balanced substring is \"0011\", which has length 4. "
      },
      {
        "input": "Input: s = \"111\"",
        "output": "Output: 0",
        "explanation": "Explanation: There is no balanced substring except the empty substring, so the answer is 0."
      }
    ],
    "topics": [
      "String"
    ],
    "difficulty": "Easy",
    "constraints": [
      "1 <= s.length <= 50",
      "'0' <= s[i] <= '1'"
    ],
    "hints": [
      "Consider iterating over each subarray and checking if it’s balanced or not.",
      "Among all balanced subarrays, the answer is the longest one of them."
    ]
  },
  {
    "title": "Prime In Diagonal",
    "description": "You are given a 0-indexed two-dimensional integer array nums.\nReturn the largest prime number that lies on at least one of the diagonals of nums. In case, no prime is present on any of the diagonals, return 0.\nNote that:\n\nAn integer is prime if it is greater than 1 and has no positive integer divisors other than 1 and itself.\nAn integer val is on one of the diagonals of nums if there exists an integer i for which nums[i][i] = val or an i for which nums[i][nums.length - i - 1] = val.\n\n\nIn the above diagram, one diagonal is [1,5,9] and another diagonal is [3,5,7].\n \n",
    "examples": [
      {
        "input": "Input: nums = [[1,2,3],[5,6,7],[9,10,11]]",
        "output": "Output: 11",
        "explanation": "Explanation: The numbers 1, 3, 6, 9, and 11 are the only numbers present on at least one of the diagonals. Since 11 is the largest prime, we return 11."
      },
      {
        "input": "Input: nums = [[1,2,3],[5,17,7],[9,11,10]]",
        "output": "Output: 17",
        "explanation": "Explanation: The numbers 1, 3, 9, 10, and 17 are all present on at least one of the diagonals. 17 is the largest prime, so we return 17."
      }
    ],
    "topics": [
      "Array",
      "Math",
      "Matrix",
      "Number Theory"
    ],
    "difficulty": "Easy",
    "constraints": [
      "1 <= nums.length <= 300",
      "nums.length == numsi.length",
      "1 <= nums[i][j] <= 4*106"
    ],
    "hints": [
      "Iterate over the diagonals of the matrix and check for each element.",
      "Check if the element is prime or not in O(sqrt(n)) time."
    ]
  },
  {
    "title": "Sum of Distances",
    "description": "You are given a 0-indexed integer array nums. There exists an array arr of length nums.length, where arr[i] is the sum of |i - j| over all j such that nums[j] == nums[i] and j != i. If there is no such j, set arr[i] to be 0.\nReturn the array arr.\n \n",
    "examples": [
      {
        "input": "Input: nums = [1,3,1,1,2]",
        "output": "Output: [5,0,3,4,0]",
        "explanation": "Explanation: "
      },
      {
        "input": "Input: nums = [0,5,3]",
        "output": "Output: [0,0,0]",
        "explanation": "Explanation: Since each element in nums is distinct, arr[i] = 0 for all i."
      }
    ],
    "topics": [
      "Array",
      "Hash Table",
      "Prefix Sum"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= nums.length <= 105",
      "0 <= nums[i] <= 109"
    ],
    "hints": [
      "Can we use the prefix sum here?",
      "For each number x, collect all the indices where x occurs, and calculate the prefix sum of the array.",
      "For each occurrence of x, the indices to the right will be regular subtraction while the indices to the left will be reversed subtraction."
    ]
  },
  {
    "title": "Minimize the Maximum Difference of Pairs",
    "description": "You are given a 0-indexed integer array nums and an integer p. Find p pairs of indices of nums such that the maximum difference amongst all the pairs is minimized. Also, ensure no index appears more than once amongst the p pairs.\nNote that for a pair of elements at the index i and j, the difference of this pair is |nums[i] - nums[j]|, where |x| represents the absolute value of x.\nReturn the minimum maximum difference among all p pairs. We define the maximum of an empty set to be zero.\n \n",
    "examples": [
      {
        "input": "Input: nums = [10,1,2,7,1,3], p = 2",
        "output": "Output: 1",
        "explanation": "Explanation: The first pair is formed from the indices 1 and 4, and the second pair is formed from the indices 2 and 5. "
      },
      {
        "input": "Input: nums = [4,2,1,2], p = 1",
        "output": "Output: 0",
        "explanation": "Explanation: Let the indices 1 and 3 form a pair. The difference of that pair is |2 - 2| = 0, which is the minimum we can attain."
      }
    ],
    "topics": [
      "Array",
      "Binary Search",
      "Greedy"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= nums.length <= 105",
      "0 <= nums[i] <= 109",
      "0 <= p <= (nums.length)/2"
    ],
    "hints": [
      "Can we use dynamic programming here?",
      "To minimize the answer, the array should be sorted first.",
      "The recurrence relation is fn(i, x) = min(fn(i+1, x), max(abs(nums[i]-nums[i+1]), fn(i+2, p-1)), and fn(0,p) gives the desired answer."
    ]
  },
  {
    "title": "Minimum Operations to Make All Array Elements Equal",
    "description": "You are given an array nums consisting of positive integers.\nYou are also given an integer array queries of size m. For the ith query, you want to make all of the elements of nums equal to queries[i]. You can perform the following operation on the array any number of times:\n\nIncrease or decrease an element of the array by 1.\n\nReturn an array answer of size m where answer[i] is the minimum number of operations to make all elements of nums equal to queries[i].\nNote that after each query the array is reset to its original state.\n \n",
    "examples": [
      {
        "input": "Input: nums = [3,1,6,8], queries = [1,5]",
        "output": "Output: [14,10]",
        "explanation": "Explanation: For the first query we can do the following operations:"
      },
      {
        "input": "Input: nums = [2,9,6,3], queries = [10]",
        "output": "Output: [20]",
        "explanation": "Explanation: We can increase each value in the array to 10. The total number of operations will be 8 + 1 + 4 + 7 = 20."
      }
    ],
    "topics": [
      "Array",
      "Binary Search",
      "Sorting",
      "Prefix Sum"
    ],
    "difficulty": "Medium",
    "constraints": [
      "n == nums.length",
      "m == queries.length",
      "1 <= n, m <= 105",
      "1 <= nums[i], queries[i] <= 109"
    ],
    "hints": [
      "For each query, you should decrease all elements greater than queries[i] and increase all elements less than queries[i].",
      "The answer is the sum of absolute differences between queries[i] and every element of the array. How do you calculate that optimally?"
    ]
  },
  {
    "title": "Collect Coins in a Tree",
    "description": "There exists an undirected and unrooted tree with n nodes indexed from 0 to n - 1. You are given an integer n and a 2D integer array edges of length n - 1, where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree. You are also given an array coins of size n where coins[i] can be either 0 or 1, where 1 indicates the presence of a coin in the vertex i.\nInitially, you choose to start at any vertex in the tree. Then, you can perform the following operations any number of times: \n\nCollect all the coins that are at a distance of at most 2 from the current vertex, or\nMove to any adjacent vertex in the tree.\n\nFind the minimum number of edges you need to go through to collect all the coins and go back to the initial vertex.\nNote that if you pass an edge several times, you need to count it into the answer several times.\n \n",
    "examples": [
      {
        "input": "Input: coins = [1,0,0,0,0,1], edges = [[0,1],[1,2],[2,3],[3,4],[4,5]]",
        "output": "Output: 2",
        "explanation": "Explanation: Start at vertex 2, collect the coin at vertex 0, move to vertex 3, collect the coin at vertex 5 then move back to vertex 2."
      },
      {
        "input": "Input: coins = [0,0,0,1,1,0,0,1], edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[5,6],[5,7]]",
        "output": "Output: 2",
        "explanation": "Explanation: Start at vertex 0, collect the coins at vertices 4 and 3, move to vertex 2,  collect the coin at vertex 7, then move back to vertex 0."
      }
    ],
    "topics": [
      "Array",
      "Tree",
      "Graph",
      "Topological Sort"
    ],
    "difficulty": "Hard",
    "constraints": [
      "n == coins.length",
      "1 <= n <= 3 * 104",
      "0 <= coins[i] <= 1",
      "edges.length == n - 1",
      "edges[i].length == 2",
      "0 <= ai, bi < n",
      "ai != bi",
      "edges represents a valid tree."
    ],
    "hints": [
      "All leaves that do not have a coin are redundant and can be deleted from the tree.",
      "Remove the leaves that do not have coins on them, so that the resulting tree will have a coin on every leaf.",
      "In the remaining tree, remove each leaf node and its parent from the tree. The remaining nodes in the tree are the ones that must be visited. Hence, the answer is equal to (# remaining nodes -1) * 2"
    ]
  },
  {
    "title": "Prime Subtraction Operation",
    "description": "You are given a 0-indexed integer array nums of length n.\nYou can perform the following operation as many times as you want:\n\nPick an index i that you haven’t picked before, and pick a prime p strictly less than nums[i], then subtract p from nums[i].\n\nReturn true if you can make nums a strictly increasing array using the above operation and false otherwise.\nA strictly increasing array is an array whose each element is strictly greater than its preceding element.\n \n",
    "examples": [
      {
        "input": "Input: nums = [4,9,6,10]",
        "output": "Output: true",
        "explanation": "Explanation: In the first operation: Pick i = 0 and p = 3, and then subtract 3 from nums[0], so that nums becomes [1,9,6,10]."
      },
      {
        "input": "Input: nums = [6,8,11,12]",
        "output": "Output: true",
        "explanation": "Explanation: Initially nums is sorted in strictly increasing order, so we don't need to make any operations."
      },
      {
        "input": "Input: nums = [5,8,3]",
        "output": "Output: false",
        "explanation": "Explanation: It can be proven that there is no way to perform operations to make nums sorted in strictly increasing order, so the answer is false."
      }
    ],
    "topics": [
      "Array",
      "Math",
      "Binary Search",
      "Greedy",
      "Number Theory"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= nums.length <= 1000",
      "1 <= nums[i] <= 1000",
      "nums.length == n"
    ],
    "hints": [
      "Think about if we have many primes to subtract from nums[i]. Which prime is more optimal?",
      "The most optimal prime to subtract from nums[i] is the one that makes nums[i] the smallest as possible and greater than nums[i-1]."
    ]
  },
  {
    "title": "K Items With the Maximum Sum",
    "description": "There is a bag that consists of items, each item has a number 1, 0, or -1 written on it.\nYou are given four non-negative integers numOnes, numZeros, numNegOnes, and k.\nThe bag initially contains:\n\nnumOnes items with 1s written on them.\nnumZeroes items with 0s written on them.\nnumNegOnes items with -1s written on them.\n\nWe want to pick exactly k items among the available items. Return the maximum possible sum of numbers written on the items.\n \n",
    "examples": [
      {
        "input": "Input: numOnes = 3, numZeros = 2, numNegOnes = 0, k = 2",
        "output": "Output: 2",
        "explanation": "Explanation: We have a bag of items with numbers written on them {1, 1, 1, 0, 0}. We take 2 items with 1 written on them and get a sum in a total of 2."
      },
      {
        "input": "Input: numOnes = 3, numZeros = 2, numNegOnes = 0, k = 4",
        "output": "Output: 3",
        "explanation": "Explanation: We have a bag of items with numbers written on them {1, 1, 1, 0, 0}. We take 3 items with 1 written on them, and 1 item with 0 written on it, and get a sum in a total of 3."
      }
    ],
    "topics": [
      "Math",
      "Greedy"
    ],
    "difficulty": "Easy",
    "constraints": [
      "0 <= numOnes, numZeros, numNegOnes <= 50",
      "0 <= k <= numOnes + numZeros + numNegOnes"
    ],
    "hints": [
      "It is always optimal to take items with the number 1 written on them as much as possible.",
      "If k > numOnes, after taking all items with the number 1, it is always optimal to take items with the number 0 written on them as much as possible.",
      "If k > numOnes + numZeroes we are forced to take k - numOnes - numZeroes -1s."
    ]
  },
  {
    "title": "Left and Right Sum Differences",
    "description": "Given a 0-indexed integer array nums, find a 0-indexed integer array answer where:\n\nanswer.length == nums.length.\nanswer[i] = |leftSum[i] - rightSum[i]|.\n\nWhere:\n\nleftSum[i] is the sum of elements to the left of the index i in the array nums. If there is no such element, leftSum[i] = 0.\nrightSum[i] is the sum of elements to the right of the index i in the array nums. If there is no such element, rightSum[i] = 0.\n\nReturn the array answer.\n \n",
    "examples": [
      {
        "input": "Input: nums = [10,4,8,3]",
        "output": "Output: [15,1,11,22]",
        "explanation": "Explanation: The array leftSum is [0,10,14,22] and the array rightSum is [15,11,3,0]."
      },
      {
        "input": "Input: nums = [1]",
        "output": "Output: [0]",
        "explanation": "Explanation: The array leftSum is [0] and the array rightSum is [0]."
      }
    ],
    "topics": [
      "Array",
      "Prefix Sum"
    ],
    "difficulty": "Easy",
    "constraints": [
      "1 <= nums.length <= 1000",
      "1 <= nums[i] <= 105"
    ],
    "hints": [
      "For each index i, maintain two variables leftSum and rightSum.",
      "Iterate on the range j: [0 … i - 1] and add nums[j] to the leftSum and similarly iterate on the range j: [i + 1 … nums.length - 1] and add nums[j] to the rightSum."
    ]
  },
  {
    "title": "Find the Divisibility Array of a String",
    "description": "You are given a 0-indexed string word of length n consisting of digits, and a positive integer m.\nThe divisibility array div of word is an integer array of length n such that:\n\ndiv[i] = 1 if the numeric value of word[0,...,i] is divisible by m, or\ndiv[i] = 0 otherwise.\n\nReturn the divisibility array of word.\n \n",
    "examples": [
      {
        "input": "Input: word = \"998244353\", m = 3",
        "output": "Output: [1,1,0,0,0,1,1,0,0]",
        "explanation": "Explanation: There are only 4 prefixes that are divisible by 3: \"9\", \"99\", \"998244\", and \"9982443\"."
      },
      {
        "input": "Input: word = \"1010\", m = 10",
        "output": "Output: [0,1,0,1]",
        "explanation": "Explanation: There are only 2 prefixes that are divisible by 10: \"10\", and \"1010\"."
      }
    ],
    "topics": [
      "Array",
      "Math",
      "String"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= n <= 105",
      "word.length == n",
      "word consists of digits from 0 to 9",
      "1 <= m <= 109"
    ],
    "hints": [
      "We can check if the numeric value of the prefix of the given string is divisible by m by computing the remainder of the numeric value of the prefix when divided by m.",
      "The remainder of the numeric value of a prefix ending at index i can be computed from the remainder of the prefix ending at index i-1."
    ]
  },
  {
    "title": "Find the Maximum Number of Marked Indices",
    "description": "You are given a 0-indexed integer array nums.\nInitially, all of the indices are unmarked. You are allowed to make this operation any number of times:\n\nPick two different unmarked indices i and j such that 2 * nums[i] <= nums[j], then mark i and j.\n\nReturn the maximum possible number of marked indices in nums using the above operation any number of times.\n \n",
    "examples": [
      {
        "input": "Input: nums = [3,5,2,4]",
        "output": "Output: 2",
        "explanation": "Explanation: In the first operation: pick i = 2 and j = 1, the operation is allowed because 2 * nums[2] <= nums[1]. Then mark index 2 and 1."
      },
      {
        "input": "Input: nums = [9,2,5,4]",
        "output": "Output: 4",
        "explanation": "Explanation: In the first operation: pick i = 3 and j = 0, the operation is allowed because 2 * nums[3] <= nums[0]. Then mark index 3 and 0."
      },
      {
        "input": "Input: nums = [7,6,8]",
        "output": "Output: 0",
        "explanation": "Explanation: There is no valid operation to do, so the answer is 0."
      }
    ],
    "topics": [
      "Array",
      "Two Pointers",
      "Binary Search",
      "Greedy",
      "Sorting"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= nums.length <= 105",
      "1 <= nums[i] <= 109"
    ],
    "hints": [
      "Think about how to check that performing k operations is possible.",
      "To perform k operations, it’s optimal to use the smallest k elements and the largest k elements and think about how to match them.",
      "It’s optimal to match the ith smallest number with the k-i + 1 largest number.",
      "Now we need to binary search on the answer and find the greatest possible valid k."
    ]
  },
  {
    "title": "Minimum Time to Visit a Cell In a Grid",
    "description": "You are given a m x n matrix grid consisting of non-negative integers where grid[row][col] represents the minimum time required to be able to visit the cell (row, col), which means you can visit the cell (row, col) only when the time you visit it is greater than or equal to grid[row][col].\nYou are standing in the top-left cell of the matrix in the 0th second, and you must move to any adjacent cell in the four directions: up, down, left, and right. Each move you make takes 1 second.\nReturn the minimum time required in which you can visit the bottom-right cell of the matrix. If you cannot visit the bottom-right cell, then return -1.\n \n",
    "examples": [
      {
        "input": "Input: grid = [[0,1,3,2],[5,1,2,5],[4,3,8,6]]",
        "output": "Output: 7",
        "explanation": "Explanation: One of the paths that we can take is the following:"
      },
      {
        "input": "Input: grid = [[0,2,4],[3,2,1],[1,0,4]]",
        "output": "Output: -1",
        "explanation": "Explanation: There is no path from the top left to the bottom-right cell."
      }
    ],
    "topics": [
      "Array",
      "Breadth-First Search",
      "Graph",
      "Heap (Priority Queue)",
      "Matrix",
      "Shortest Path"
    ],
    "difficulty": "Hard",
    "constraints": [
      "m == grid.length",
      "n == grid[i].length",
      "2 <= m, n <= 1000",
      "4 <= m * n <= 105",
      "0 <= grid[i][j] <= 105",
      "grid[0][0] == 0"
    ],
    "hints": [
      "Try using some algorithm that can find the shortest paths on a graph.",
      "Consider the case where you have to go back and forth between two cells of the matrix to unlock some other cells."
    ]
  },
  {
    "title": "Minimum Operations to Reduce an Integer to 0",
    "description": "You are given a positive integer n, you can do the following operation any number of times:\n\nAdd or subtract a power of 2 from n.\n\nReturn the minimum number of operations to make n equal to 0.\nA number x is power of 2 if x == 2i where i >= 0.\n \n",
    "examples": [
      {
        "input": "Input: n = 39",
        "output": "Output: 3",
        "explanation": "Explanation: We can do the following operations:"
      },
      {
        "input": "Input: n = 54",
        "output": "Output: 3",
        "explanation": "Explanation: We can do the following operations:"
      }
    ],
    "topics": [
      "Dynamic Programming",
      "Greedy",
      "Bit Manipulation"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= n <= 105"
    ],
    "hints": [
      "Can we set/unset the bits in binary representation?",
      "If there are multiple adjacent ones, how can we optimally add and subtract in 2 operations such that all ones get unset?",
      "Bonus: Try to solve the problem with higher constraints: n ≤ 10^18."
    ]
  },
  {
    "title": "Count the Number of Square-Free Subsets",
    "description": "You are given a positive integer 0-indexed array nums.\nA subset of the array nums is square-free if the product of its elements is a square-free integer.\nA square-free integer is an integer that is divisible by no square number other than 1.\nReturn the number of square-free non-empty subsets of the array nums. Since the answer may be too large, return it modulo 109 + 7.\nA non-empty subset of nums is an array that can be obtained by deleting some (possibly none but not all) elements from nums. Two subsets are different if and only if the chosen indices to delete are different.\n \n",
    "examples": [
      {
        "input": "Input: nums = [3,4,4,5]",
        "output": "Output: 3",
        "explanation": "Explanation: There are 3 square-free subsets in this example:"
      },
      {
        "input": "Input: nums = [1]",
        "output": "Output: 1",
        "explanation": "Explanation: There is 1 square-free subset in this example:"
      }
    ],
    "topics": [
      "Array",
      "Math",
      "Dynamic Programming",
      "Bit Manipulation",
      "Bitmask"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= nums.length <= 1000",
      "1 <= nums[i] <= 30"
    ],
    "hints": [
      "There are 10 primes before number 30.",
      "Label primes from {2, 3, … 29} with {0,1, … 9} and let DP(i, mask) denote the number of subsets before index: i with the subset of taken primes: mask.",
      "If the mask and prime factorization of nums[i] have a common prime, then it is impossible to add to the current subset, otherwise, it is possible."
    ]
  },
  {
    "title": "Find the String with LCP",
    "description": "We define the lcp matrix of any 0-indexed string word of n lowercase English letters as an n x n grid such that:\n\nlcp[i][j] is equal to the length of the longest common prefix between the substrings word[i,n-1] and word[j,n-1].\n\nGiven an n x n matrix lcp, return the alphabetically smallest string word that corresponds to lcp. If there is no such string, return an empty string.\nA string a is lexicographically smaller than a string b (of the same length) if in the first position where a and b differ, string a has a letter that appears earlier in the alphabet than the corresponding letter in b. For example, \"aabd\" is lexicographically smaller than \"aaca\" because the first position they differ is at the third letter, and 'b' comes before 'c'.\n \n",
    "examples": [
      {
        "input": "Input: lcp = [[4,0,2,0],[0,3,0,1],[2,0,2,0],[0,1,0,1]]",
        "output": "Output: \"abab\"",
        "explanation": "Explanation: lcp corresponds to any 4 letter string with two alternating letters. The lexicographically smallest of them is \"abab\"."
      },
      {
        "input": "Input: lcp = [[4,3,2,1],[3,3,2,1],[2,2,2,1],[1,1,1,1]]",
        "output": "Output: \"aaaa\"",
        "explanation": "Explanation: lcp corresponds to any 4 letter string with a single distinct letter. The lexicographically smallest of them is \"aaaa\". "
      },
      {
        "input": "Input: lcp = [[4,3,2,1],[3,3,2,1],[2,2,2,1],[1,1,1,3]]",
        "output": "Output: \"\"",
        "explanation": "Explanation: lcp[3][3] cannot be equal to 3 since word[3,...,3] consists of only a single letter; Thus, no answer exists."
      }
    ],
    "topics": [
      "String",
      "Dynamic Programming",
      "Greedy",
      "Union Find"
    ],
    "difficulty": "Hard",
    "constraints": [
      "1 <= n == lcp.length == lcp[i].length <= 1000",
      "0 <= lcp[i][j] <= n"
    ],
    "hints": [
      "Use the LCP array to determine which groups of elements must be equal.",
      "Match the smallest letter to the group that contains the smallest unassigned index.",
      "Build the LCP matrix of the resulting string then check if it is equal to the target LCP."
    ]
  },
  {
    "title": "Merge Two 2D Arrays by Summing Values",
    "description": "You are given two 2D integer arrays nums1 and nums2.\n\nnums1[i] = [idi, vali] indicate that the number with the id idi has a value equal to vali.\nnums2[i] = [idi, vali] indicate that the number with the id idi has a value equal to vali.\n\nEach array contains unique ids and is sorted in ascending order by id.\nMerge the two arrays into one array that is sorted in ascending order by id, respecting the following conditions:\n\nOnly ids that appear in at least one of the two arrays should be included in the resulting array.\nEach id should be included only once and its value should be the sum of the values of this id in the two arrays. If the id does not exist in one of the two arrays then its value in that array is considered to be 0.\n\nReturn the resulting array. The returned array must be sorted in ascending order by id.\n \n",
    "examples": [
      {
        "input": "Input: nums1 = [[1,2],[2,3],[4,5]], nums2 = [[1,4],[3,2],[4,1]]",
        "output": "Output: [[1,6],[2,3],[3,2],[4,6]]",
        "explanation": "Explanation: The resulting array contains the following:"
      },
      {
        "input": "Input: nums1 = [[2,4],[3,6],[5,5]], nums2 = [[1,3],[4,3]]",
        "output": "Output: [[1,3],[2,4],[3,6],[4,3],[5,5]]",
        "explanation": "Explanation: There are no common ids, so we just include each id with its value in the resulting list."
      }
    ],
    "topics": [
      "Array",
      "Hash Table",
      "Two Pointers"
    ],
    "difficulty": "Easy",
    "constraints": [
      "1 <= nums1.length, nums2.length <= 200",
      "nums1[i].length == nums2[j].length == 2",
      "1 <= idi, vali <= 1000",
      "Both arrays contain unique ids.",
      "Both arrays are in strictly ascending order by id."
    ],
    "hints": [
      "Use a dictionary/hash map to keep track of the indices and their sum\nvalues."
    ]
  },
  {
    "title": "Minimum Score by Changing Two Elements",
    "description": "You are given a 0-indexed integer array nums.\n\nThe low score of nums is the minimum value of |nums[i] - nums[j]| over all 0 <= i < j < nums.length.\nThe high score of nums is the maximum value of |nums[i] - nums[j]| over all 0 <= i < j < nums.length.\nThe score of nums is the sum of the high and low scores of nums.\n\nTo minimize the score of nums, we can change the value of at most two elements of nums.\nReturn the minimum possible score after changing the value of at most two elements of nums.\nNote that |x| denotes the absolute value of x.\n \n",
    "examples": [
      {
        "input": "Input: nums = [1,4,3]",
        "output": "Output: 0",
        "explanation": "Explanation: Change value of nums[1] and nums[2] to 1 so that nums becomes [1,1,1]. Now, the value of |nums[i] - nums[j]| is always equal to 0, so we return 0 + 0 = 0."
      },
      {
        "input": "Input: nums = [1,4,7,8,5]",
        "output": "Output: 3",
        "explanation": "Explanation: Change nums[0] and nums[1] to be 6. Now nums becomes [6,6,7,8,5]."
      }
    ],
    "topics": [
      "Array",
      "Greedy",
      "Sorting"
    ],
    "difficulty": "Medium",
    "constraints": [
      "3 <= nums.length <= 105",
      "1 <= nums[i] <= 109"
    ],
    "hints": [
      "Changing the minimum or maximum values will only minimize the score.",
      "Think about what all possible pairs of minimum and maximum values can be changed to form the minimum score."
    ]
  },
  {
    "title": "Minimum Impossible OR",
    "description": "You are given a 0-indexed integer array nums.\nWe say that an integer x is expressible from nums if there exist some integers 0 <= index1 < index2 < ... < indexk < nums.length for which nums[index1] | nums[index2] | ... | nums[indexk] = x. In other words, an integer is expressible if it can be written as the bitwise OR of some subsequence of nums.\nReturn the minimum positive non-zero integer that is not expressible from nums.\n \n",
    "examples": [
      {
        "input": "Input: nums = [2,1]",
        "output": "Output: 4",
        "explanation": "Explanation: 1 and 2 are already present in the array. We know that 3 is expressible, since nums[0] | nums[1] = 2 | 1 = 3. Since 4 is not expressible, we return 4."
      },
      {
        "input": "Input: nums = [5,3,2]",
        "output": "Output: 1",
        "explanation": "Explanation: We can show that 1 is the smallest number that is not expressible."
      }
    ],
    "topics": [
      "Array",
      "Bit Manipulation",
      "Brainteaser"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= nums.length <= 105",
      "1 <= nums[i] <= 109"
    ],
    "hints": [
      "Think about forming numbers in the powers of 2 using their bit representation.",
      "The minimum power of 2 not present in the array will be the first number that could not be expressed using the given operation."
    ]
  },
  {
    "title": "Maximum Difference by Remapping a Digit",
    "description": "You are given an integer num. You know that Danny Mittal will sneakily remap one of the 10 possible digits (0 to 9) to another digit.\nReturn the difference between the maximum and minimum values Danny can make by remapping exactly one digit in num.\nNotes:\n\nWhen Danny remaps a digit d1 to another digit d2, Danny replaces all occurrences of d1 in num with d2.\nDanny can remap a digit to itself, in which case num does not change.\nDanny can remap different digits for obtaining minimum and maximum values respectively.\nThe resulting number after remapping can contain leading zeroes.\nWe mentioned \"Danny Mittal\" to congratulate him on being in the top 10 in Weekly Contest 326.\n\n \n",
    "examples": [
      {
        "input": "Input: num = 11891",
        "output": "Output: 99009",
        "explanation": "Explanation: "
      },
      {
        "input": "Input: num = 90",
        "output": "Output: 99",
        "explanation": ""
      }
    ],
    "topics": [
      "Math",
      "Greedy"
    ],
    "difficulty": "Easy",
    "constraints": [
      "1 <= num <= 108"
    ],
    "hints": [
      "Try to remap the first non-zero digit to 9 to obtain the maximum number.",
      "Try to remap the first non-nine digit to 0 to obtain the minimum number."
    ]
  },
  {
    "title": "Handling Sum Queries After Update",
    "description": "You are given two 0-indexed arrays nums1 and nums2 and a 2D array queries of queries. There are three types of queries:\n\nFor a query of type 1, queries[i] = [1, l, r]. Flip the values from 0 to 1 and from 1 to 0 in nums1 from index l to index r. Both l and r are 0-indexed.\nFor a query of type 2, queries[i] = [2, p, 0]. For every index 0 <= i < n, set nums2[i] = nums2[i] + nums1[i] * p.\nFor a query of type 3, queries[i] = [3, 0, 0]. Find the sum of the elements in nums2.\n\nReturn an array containing all the answers to the third type queries.\n \n",
    "examples": [
      {
        "input": "Input: nums1 = [1,0,1], nums2 = [0,0,0], queries = [[1,1,1],[2,1,0],[3,0,0]]",
        "output": "Output: [3]",
        "explanation": "Explanation: After the first query nums1 becomes [1,1,1]. After the second query, nums2 becomes [1,1,1], so the answer to the third query is 3. Thus, [3] is returned."
      },
      {
        "input": "Input: nums1 = [1], nums2 = [5], queries = [[2,0,0],[3,0,0]]",
        "output": "Output: [5]",
        "explanation": "Explanation: After the first query, nums2 remains [5], so the answer to the second query is 5. Thus, [5] is returned."
      }
    ],
    "topics": [
      "Array",
      "Segment Tree"
    ],
    "difficulty": "Hard",
    "constraints": [
      "1 <= nums1.length,nums2.length <= 105",
      "nums1.length = nums2.length",
      "1 <= queries.length <= 105",
      "queries[i].length = 3",
      "0 <= l <= r <= nums1.length - 1",
      "0 <= p <= 106",
      "0 <= nums1[i] <= 1",
      "0 <= nums2[i] <= 109"
    ],
    "hints": [
      "Use the Lazy Segment Tree to process the queries quickly."
    ]
  },
  {
    "title": "Subsequence With the Minimum Score",
    "description": "You are given two strings s and t.\nYou are allowed to remove any number of characters from the string t.\nThe score of the string is 0 if no characters are removed from the string t, otherwise:\n\nLet left be the minimum index among all removed characters.\nLet right be the maximum index among all removed characters.\n\nThen the score of the string is right - left + 1.\nReturn the minimum possible score to make t a subsequence of s.\nA subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., \"ace\" is a subsequence of \"abcde\" while \"aec\" is not).\n \n",
    "examples": [
      {
        "input": "Input: s = \"abacaba\", t = \"bzaa\"",
        "output": "Output: 1",
        "explanation": "Explanation: In this example, we remove the character \"z\" at index 1 (0-indexed)."
      },
      {
        "input": "Input: s = \"cde\", t = \"xyz\"",
        "output": "Output: 3",
        "explanation": "Explanation: In this example, we remove characters \"x\", \"y\" and \"z\" at indices 0, 1, and 2 (0-indexed)."
      }
    ],
    "topics": [
      "Two Pointers",
      "String",
      "Binary Search"
    ],
    "difficulty": "Hard",
    "constraints": [
      "1 <= s.length, t.length <= 105",
      "s and t consist of only lowercase English letters."
    ],
    "hints": [
      "Maintain two pointers: i and j. We need to perform a similar operation: while t[0:i] + t[j:n] is not a subsequence of the string s, increase j.",
      "We can check the condition greedily. Create the array leftmost[i] which denotes minimum index k, such that in prefix s[0:k] exists subsequence t[0:i]. Similarly, we define rightmost[i].",
      "If leftmost[i] < rightmost[j] then t[0:i] + t[j:n] is the subsequence of s."
    ]
  },
  {
    "title": "Substring XOR Queries",
    "description": "You are given a binary string s, and a 2D integer array queries where queries[i] = [firsti, secondi].\nFor the ith query, find the shortest substring of s whose decimal value, val, yields secondi when bitwise XORed with firsti. In other words, val ^ firsti == secondi.\nThe answer to the ith query is the endpoints (0-indexed) of the substring [lefti, righti] or [-1, -1] if no such substring exists. If there are multiple answers, choose the one with the minimum lefti.\nReturn an array ans where ans[i] = [lefti, righti] is the answer to the ith query.\nA substring is a contiguous non-empty sequence of characters within a string.\n \n",
    "examples": [
      {
        "input": "Input: s = \"101101\", queries = [[0,5],[1,2]]",
        "output": "Output: [[0,2],[2,3]]",
        "explanation": "Explanation: For the first query the substring in range [0,2] is \"101\" which has a decimal value of 5, and 5 ^ 0 = 5, hence the answer to the first query is [0,2]. In the second query, the substring in range [2,3] is \"11\", and has a decimal value of 3, and 3 ^ 1 = 2. So, [2,3] is returned for the second query. "
      },
      {
        "input": "Input: s = \"0101\", queries = [[12,8]]",
        "output": "Output: [[-1,-1]]",
        "explanation": "Explanation: In this example there is no substring that answers the query, hence [-1,-1] is returned."
      },
      {
        "input": "Input: s = \"1\", queries = [[4,5]]",
        "output": "Output: [[0,0]]",
        "explanation": "Explanation: For this example, the substring in range [0,0] has a decimal value of 1, and 1 ^ 4 = 5. So, the answer is [0,0]."
      }
    ],
    "topics": [
      "Array",
      "Hash Table",
      "String",
      "Bit Manipulation"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= s.length <= 104",
      "s[i] is either '0' or '1'.",
      "1 <= queries.length <= 105",
      "0 <= firsti, secondi <= 109"
    ],
    "hints": [
      "You do not need to consider substrings having lengths greater than 30.",
      "Pre-process all substrings with lengths not greater than 30, and add the best endpoints to a dictionary."
    ]
  },
  {
    "title": "Count the Number of Fair Pairs",
    "description": "Given a 0-indexed integer array nums of size n and two integers lower and upper, return the number of fair pairs.\nA pair (i, j) is fair if:\n\n0 <= i < j < n, and\nlower <= nums[i] + nums[j] <= upper\n\n \n",
    "examples": [
      {
        "input": "Input: nums = [0,1,7,4,4,5], lower = 3, upper = 6",
        "output": "Output: 6",
        "explanation": "Explanation: There are 6 fair pairs: (0,3), (0,4), (0,5), (1,3), (1,4), and (1,5)."
      },
      {
        "input": "Input: nums = [1,7,9,2,5], lower = 11, upper = 11",
        "output": "Output: 1",
        "explanation": "Explanation: There is a single fair pair: (2,3)."
      }
    ],
    "topics": [
      "Array",
      "Two Pointers",
      "Binary Search",
      "Sorting"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= nums.length <= 105",
      "nums.length == n",
      "-109 <= nums[i] <= 109",
      "-109 <= lower <= upper <= 109"
    ],
    "hints": [
      "Sort the array in ascending order.",
      "For each number in the array, keep track of the smallest and largest numbers in the array that can form a fair pair with this number.",
      "As you move to larger number, both boundaries move down."
    ]
  },
  {
    "title": "Find the Array Concatenation Value",
    "description": "You are given a 0-indexed integer array nums.\nThe concatenation of two numbers is the number formed by concatenating their numerals.\n\nFor example, the concatenation of 15, 49 is 1549.\n\nThe concatenation value of nums is initially equal to 0. Perform this operation until nums becomes empty:\n\nIf there exists more than one number in nums, pick the first element and last element in nums respectively and add the value of their concatenation to the concatenation value of nums, then delete the first and last element from nums.\nIf one element exists, add its value to the concatenation value of nums, then delete it.\n\nReturn the concatenation value of the nums.\n \n",
    "examples": [
      {
        "input": "Input: nums = [7,52,2,4]",
        "output": "Output: 596",
        "explanation": "Explanation: Before performing any operation, nums is [7,52,2,4] and concatenation value is 0."
      },
      {
        "input": "Input: nums = [5,14,13,8,12]",
        "output": "Output: 673",
        "explanation": "Explanation: Before performing any operation, nums is [5,14,13,8,12] and concatenation value is 0."
      }
    ],
    "topics": [
      "Array",
      "Two Pointers",
      "Simulation"
    ],
    "difficulty": "Easy",
    "constraints": [
      "1 <= nums.length <= 1000",
      "1 <= nums[i] <= 104"
    ],
    "hints": [
      "Consider simulating the process to calculate the answer",
      "iterate until the array becomes empty. In each iteration, concatenate the first element to the last element and add their concatenation value to the answer.",
      "Don’t forget to handle cases when one element is left in the end, not two elements."
    ]
  },
  {
    "title": "Minimum Number of Visited Cells in a Grid",
    "description": "You are given a 0-indexed m x n integer matrix grid. Your initial position is at the top-left cell (0, 0).\nStarting from the cell (i, j), you can move to one of the following cells:\n\nCells (i, k) with j < k <= grid[i][j] + j (rightward movement), or\nCells (k, j) with i < k <= grid[i][j] + i (downward movement).\n\nReturn the minimum number of cells you need to visit to reach the bottom-right cell (m - 1, n - 1). If there is no valid path, return -1.\n \n",
    "examples": [
      {
        "input": "Input: grid = [[3,4,2,1],[4,2,3,1],[2,1,0,0],[2,4,0,0]]",
        "output": "Output: 4",
        "explanation": "Explanation: The image above shows one of the paths that visits exactly 4 cells."
      },
      {
        "input": "Input: grid = [[3,4,2,1],[4,2,1,1],[2,1,1,0],[3,4,1,0]]",
        "output": "Output: 3",
        "explanation": "Explanation: The image above shows one of the paths that visits exactly 3 cells."
      },
      {
        "input": "Input: grid = [[2,1,0],[1,0,0]]",
        "output": "Output: -1",
        "explanation": "Explanation: It can be proven that no path exists."
      }
    ],
    "topics": [
      "Array",
      "Binary Search",
      "Dynamic Programming",
      "Stack",
      "Union Find",
      "Binary Indexed Tree",
      "Segment Tree"
    ],
    "difficulty": "Hard",
    "constraints": [
      "m == grid.length",
      "n == grid[i].length",
      "1 <= m, n <= 105",
      "1 <= m * n <= 105",
      "0 <= grid[i][j] < m * n",
      "grid[m - 1][n - 1] == 0"
    ],
    "hints": [
      "For each cell (i,j), it is critical to find out the minimum number of steps to reach (i,j), denoted dis[i][j], quickly, given the tight constraint.",
      "Calculate dis[i][j] going left to right, top to bottom.",
      "Suppose we want to calculate dis[i][j], keep track of a priority queue that stores (dis[i][k], i, k) for all k ≤ j, and another priority queue that stores (dis[k][j], k, j) for all k ≤ i."
    ]
  },
  {
    "title": "The Number of Beautiful Subsets",
    "description": "You are given an array nums of positive integers and a positive integer k.\nA subset of nums is beautiful if it does not contain two integers with an absolute difference equal to k.\nReturn the number of non-empty beautiful subsets of the array nums.\nA subset of nums is an array that can be obtained by deleting some (possibly none) elements from nums. Two subsets are different if and only if the chosen indices to delete are different.\n \n",
    "examples": [
      {
        "input": "Input: nums = [2,4,6], k = 2",
        "output": "Output: 4",
        "explanation": "Explanation: The beautiful subsets of the array nums are: [2], [4], [6], [2, 6]."
      },
      {
        "input": "Input: nums = [1], k = 1",
        "output": "Output: 1",
        "explanation": "Explanation: The beautiful subset of the array nums is [1]."
      }
    ],
    "topics": [
      "Array",
      "Dynamic Programming",
      "Backtracking"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= nums.length <= 20",
      "1 <= nums[i], k <= 1000"
    ],
    "hints": [
      "Sort the array nums and create another array cnt of size nums[i].",
      "Use backtracking to generate all the beautiful subsets. If cnt[nums[i] - k] is positive, then it is impossible to add nums[i] in the subset, and we just move to the next index. Otherwise, it is also possible to add nums[i] in the subset, in this case, increase cnt[nums[i]], and move to the next index.",
      "Bonus: Can you solve the problem in O(n log n)?"
    ]
  },
  {
    "title": "Find Score of an Array After Marking All Elements",
    "description": "You are given an array nums consisting of positive integers.\nStarting with score = 0, apply the following algorithm:\n\nChoose the smallest integer of the array that is not marked. If there is a tie, choose the one with the smallest index.\nAdd the value of the chosen integer to score.\nMark the chosen element and its two adjacent elements if they exist.\nRepeat until all the array elements are marked.\n\nReturn the score you get after applying the above algorithm.\n \n",
    "examples": [
      {
        "input": "Input: nums = [2,1,3,4,5,2]",
        "output": "Output: 7",
        "explanation": "Explanation: We mark the elements as follows:"
      },
      {
        "input": "Input: nums = [2,3,5,1,3,2]",
        "output": "Output: 5",
        "explanation": "Explanation: We mark the elements as follows:"
      }
    ],
    "topics": [
      "Array",
      "Sorting",
      "Heap (Priority Queue)",
      "Simulation"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= nums.length <= 105",
      "1 <= nums[i] <= 106"
    ],
    "hints": [
      "Try simulating the process of marking the elements and their adjacent.",
      "If there is an element that was already marked, then you skip it."
    ]
  },
  {
    "title": "Find the Maximum Divisibility Score",
    "description": "You are given two 0-indexed integer arrays nums and divisors.\nThe divisibility score of divisors[i] is the number of indices j such that nums[j] is divisible by divisors[i].\nReturn the integer divisors[i] with the maximum divisibility score. If there is more than one integer with the maximum score, return the minimum of them.\n \n",
    "examples": [
      {
        "input": "Input: nums = [4,7,9,3,9], divisors = [5,2,3]",
        "output": "Output: 3",
        "explanation": "Explanation: The divisibility score for every element in divisors is:"
      },
      {
        "input": "Input: nums = [20,14,21,10], divisors = [5,7,5]",
        "output": "Output: 5",
        "explanation": "Explanation: The divisibility score for every element in divisors is:"
      },
      {
        "input": "Input: nums = [12], divisors = [10,16]",
        "output": "Output: 10",
        "explanation": "Explanation: The divisibility score for every element in divisors is:"
      }
    ],
    "topics": [
      "Array"
    ],
    "difficulty": "Easy",
    "constraints": [
      "1 <= nums.length, divisors.length <= 1000",
      "1 <= nums[i], divisors[i] <= 109"
    ],
    "hints": [
      "Consider counting for each element in divisors the count of elements in nums divisible by it using bruteforce.",
      "After counting for each divisor, take the one with the maximum count. In case of a tie, take the minimum one of them."
    ]
  },
  {
    "title": "Take Gifts From the Richest Pile",
    "description": "You are given an integer array gifts denoting the number of gifts in various piles. Every second, you do the following:\n\nChoose the pile with the maximum number of gifts.\nIf there is more than one pile with the maximum number of gifts, choose any.\nLeave behind the floor of the square root of the number of gifts in the pile. Take the rest of the gifts.\n\nReturn the number of gifts remaining after k seconds.\n \n",
    "examples": [
      {
        "input": "Input: gifts = [25,64,9,4,100], k = 4",
        "output": "Output: 29",
        "explanation": "Explanation: "
      },
      {
        "input": "Input: gifts = [1,1,1,1], k = 4",
        "output": "Output: 4",
        "explanation": "Explanation: "
      }
    ],
    "topics": [
      "Array",
      "Heap (Priority Queue)",
      "Simulation"
    ],
    "difficulty": "Easy",
    "constraints": [
      "1 <= gifts.length <= 103",
      "1 <= gifts[i] <= 109",
      "1 <= k <= 103"
    ],
    "hints": [
      "How can you keep track of the largest gifts in the array",
      "What is an efficient way to find the square root of a number?",
      "Can you keep adding up the values of the gifts while ensuring they are in a certain order?",
      "Can we use a priority queue or heap here?"
    ]
  },
  {
    "title": "Count Vowel Strings in Ranges",
    "description": "You are given a 0-indexed array of strings words and a 2D array of integers queries.\nEach query queries[i] = [li, ri] asks us to find the number of strings present in the range li to ri (both inclusive) of words that start and end with a vowel.\nReturn an array ans of size queries.length, where ans[i] is the answer to the ith query.\nNote that the vowel letters are 'a', 'e', 'i', 'o', and 'u'.\n \n",
    "examples": [
      {
        "input": "Input: words = [\"aba\",\"bcb\",\"ece\",\"aa\",\"e\"], queries = [[0,2],[1,4],[1,1]]",
        "output": "Output: [2,3,0]",
        "explanation": "Explanation: The strings starting and ending with a vowel are \"aba\", \"ece\", \"aa\" and \"e\"."
      },
      {
        "input": "Input: words = [\"a\",\"e\",\"i\"], queries = [[0,2],[0,1],[2,2]]",
        "output": "Output: [3,2,1]",
        "explanation": "Explanation: Every string satisfies the conditions, so we return [3,2,1]."
      }
    ],
    "topics": [
      "Array",
      "String",
      "Prefix Sum"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= words.length <= 105",
      "1 <= words[i].length <= 40",
      "words[i] consists only of lowercase English letters.",
      "sum(words[i].length) <= 3 * 105",
      "1 <= queries.length <= 105",
      "0 <= li <= ri < words.length"
    ],
    "hints": [
      "Precompute the prefix sum of strings that start and end with vowels.",
      "Use unordered_set to store vowels.",
      "Check if the first and last characters of the string are present in the vowels set.",
      "Subtract prefix sum for range [l-1, r] to find the number of strings starting and ending with vowels."
    ]
  },
  {
    "title": "House Robber IV",
    "description": "There are several consecutive houses along a street, each of which has some money inside. There is also a robber, who wants to steal money from the homes, but he refuses to steal from adjacent homes.\nThe capability of the robber is the maximum amount of money he steals from one house of all the houses he robbed.\nYou are given an integer array nums representing how much money is stashed in each house. More formally, the ith house from the left has nums[i] dollars.\nYou are also given an integer k, representing the minimum number of houses the robber will steal from. It is always possible to steal at least k houses.\nReturn the minimum capability of the robber out of all the possible ways to steal at least k houses.\n \n",
    "examples": [
      {
        "input": "Input: nums = [2,3,5,9], k = 2",
        "output": "Output: 5",
        "explanation": "Explanation: "
      },
      {
        "input": "Input: nums = [2,7,9,3,1], k = 2",
        "output": "Output: 2",
        "explanation": "Explanation: There are 7 ways to rob the houses. The way which leads to minimum capability is to rob the house at index 0 and 4. Return max(nums[0], nums[4]) = 2."
      }
    ],
    "topics": [
      "Array",
      "Binary Search"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= nums.length <= 105",
      "1 <= nums[i] <= 109",
      "1 <= k <= (nums.length + 1)/2"
    ],
    "hints": [
      "Can we use binary search to find the minimum value of a non-contiguous subsequence of a given size k?",
      "Initialize the search range with the minimum and maximum elements of the input array.",
      "Use a check function to determine if it is possible to select k non-consecutive elements that are less than or equal to the current \"guess\" value.",
      "Adjust the search range based on the outcome of the check function, until the range converges and the minimum value is found."
    ]
  },
  {
    "title": "Rearranging Fruits",
    "description": "You have two fruit baskets containing n fruits each. You are given two 0-indexed integer arrays basket1 and basket2 representing the cost of fruit in each basket. You want to make both baskets equal. To do so, you can use the following operation as many times as you want:\n\nChose two indices i and j, and swap the ith fruit of basket1 with the jth fruit of basket2.\nThe cost of the swap is min(basket1[i],basket2[j]).\n\nTwo baskets are considered equal if sorting them according to the fruit cost makes them exactly the same baskets.\nReturn the minimum cost to make both the baskets equal or -1 if impossible.\n \n",
    "examples": [
      {
        "input": "Input: basket1 = [4,2,2,2], basket2 = [1,4,1,2]",
        "output": "Output: 1",
        "explanation": "Explanation: Swap index 1 of basket1 with index 0 of basket2, which has cost 1. Now basket1 = [4,1,2,2] and basket2 = [2,4,1,2]. Rearranging both the arrays makes them equal."
      },
      {
        "input": "Input: basket1 = [2,3,4,1], basket2 = [3,2,5,1]",
        "output": "Output: -1",
        "explanation": "Explanation: It can be shown that it is impossible to make both the baskets equal."
      }
    ],
    "topics": [
      "Array",
      "Hash Table",
      "Greedy"
    ],
    "difficulty": "Hard",
    "constraints": [
      "basket1.length == bakste2.length",
      "1 <= basket1.length <= 105",
      "1 <= basket1[i],basket2[i] <= 109"
    ],
    "hints": [
      "Create two frequency maps for both arrays, and find the minimum element among all elements of both arrays.",
      "Check if the sum of frequencies of an element in both arrays is odd, if so return -1",
      "Store the elements that need to be swapped in a vector, and sort it.",
      "Can we reduce swapping cost with the help of minimum element?",
      "Calculate the minimum cost of swapping."
    ]
  },
  {
    "title": "Lexicographically Smallest Beautiful String",
    "description": "A string is beautiful if:\n\nIt consists of the first k letters of the English lowercase alphabet.\nIt does not contain any substring of length 2 or more which is a palindrome.\n\nYou are given a beautiful string s of length n and a positive integer k.\nReturn the lexicographically smallest string of length n, which is larger than s and is beautiful. If there is no such string, return an empty string.\nA string a is lexicographically larger than a string b (of the same length) if in the first position where a and b differ, a has a character strictly larger than the corresponding character in b.\n\nFor example, \"abcd\" is lexicographically larger than \"abcc\" because the first position they differ is at the fourth character, and d is greater than c.\n\n \n",
    "examples": [
      {
        "input": "Input: s = \"abcz\", k = 26",
        "output": "Output: \"abda\"",
        "explanation": "Explanation: The string \"abda\" is beautiful and lexicographically larger than the string \"abcz\"."
      },
      {
        "input": "Input: s = \"dc\", k = 4",
        "output": "Output: \"\"",
        "explanation": "Explanation: It can be proven that there is no string that is lexicographically larger than the string \"dc\" and is beautiful."
      }
    ],
    "topics": [
      "String",
      "Greedy"
    ],
    "difficulty": "Hard",
    "constraints": [
      "1 <= n == s.length <= 105",
      "4 <= k <= 26",
      "s is a beautiful string."
    ],
    "hints": [
      "If the string does not contain any palindromic substrings of lengths 2 and 3, then the string does not contain any palindromic substrings at all.",
      "Iterate from right to left and if it is possible to increase character at index i without creating any palindromic substrings of lengths 2 and 3, then increase it.",
      "After increasing the character at index i, set every character after index i equal to character a. With this, we will ensure that we have created a lexicographically larger string than s, which does not contain any palindromes before index i and is lexicographically the smallest.",
      "Finally, we are just left with a case to fix palindromic substrings, which come after index i. This can be done with a similar method mentioned in the second hint."
    ]
  },
  {
    "title": "Minimum Cost of a Path With Special Roads",
    "description": "You are given an array start where start = [startX, startY] represents your initial position (startX, startY) in a 2D space. You are also given the array target where target = [targetX, targetY] represents your target position (targetX, targetY).\nThe cost of going from a position (x1, y1) to any other position in the space (x2, y2) is |x2 - x1| + |y2 - y1|.\nThere are also some special roads. You are given a 2D array specialRoads where specialRoads[i] = [x1i, y1i, x2i, y2i, costi] indicates that the ith special road can take you from (x1i, y1i) to (x2i, y2i) with a cost equal to costi. You can use each special road any number of times.\nReturn the minimum cost required to go from (startX, startY) to (targetX, targetY).\n \n",
    "examples": [
      {
        "input": "Input: start = [1,1], target = [4,5], specialRoads = [[1,2,3,3,2],[3,4,4,5,1]]",
        "output": "Output: 5",
        "explanation": "Explanation: The optimal path from (1,1) to (4,5) is the following:"
      },
      {
        "input": "Input: start = [3,2], target = [5,7], specialRoads = [[3,2,3,4,4],[3,3,5,5,5],[3,4,5,6,6]]",
        "output": "Output: 7",
        "explanation": "Explanation: It is optimal to not use any special edges and go directly from the starting to the ending position with a cost |5 - 3| + |7 - 2| = 7."
      }
    ],
    "topics": [
      "Array",
      "Graph",
      "Heap (Priority Queue)",
      "Shortest Path"
    ],
    "difficulty": "Medium",
    "constraints": [
      "start.length == target.length == 2",
      "1 <= startX <= targetX <= 105",
      "1 <= startY <= targetY <= 105",
      "1 <= specialRoads.length <= 200",
      "specialRoads[i].length == 5",
      "startX <= x1i, x2i <= targetX",
      "startY <= y1i, y2i <= targetY",
      "1 <= costi <= 105"
    ],
    "hints": [
      "It can be proven that it is optimal to go only to the positions that are either the start or the end of a special road or the target position.",
      "Consider all positions given to you as nodes in a graph, and the edges of the graph are the special roads.",
      "Now the problem is equivalent to finding the shortest path in a directed graph."
    ]
  },
  {
    "title": "First Completely Painted Row or Column",
    "description": "You are given a 0-indexed integer array arr, and an m x n integer matrix mat. arr and mat both contain all the integers in the range [1, m * n].\nGo through each index i in arr starting from index 0 and paint the cell in mat containing the integer arr[i].\nReturn the smallest index i at which either a row or a column will be completely painted in mat.\n \n",
    "examples": [
      {
        "input": "Input: arr = [1,3,4,2], mat = [[1,4],[2,3]]",
        "output": "Output: 2",
        "explanation": "Explanation: The moves are shown in order, and both the first row and second column of the matrix become fully painted at arr[2]."
      },
      {
        "input": "Input: arr = [2,8,7,4,1,3,5,6,9], mat = [[3,2,5],[1,4,6],[8,7,9]]",
        "output": "Output: 3",
        "explanation": "Explanation: The second column becomes fully painted at arr[3]."
      }
    ],
    "topics": [
      "Array",
      "Hash Table",
      "Matrix"
    ],
    "difficulty": "Medium",
    "constraints": [
      "m == mat.length",
      "n = mat[i].length",
      "arr.length == m * n",
      "1 <= m, n <= 105",
      "1 <= m * n <= 105",
      "1 <= arr[i], mat[r][c] <= m * n",
      "All the integers of arr are unique.",
      "All the integers of mat are unique."
    ],
    "hints": [
      "Can we use a frequency array?",
      "Pre-process the positions of the values in the matrix.",
      "Traverse the array and increment the corresponding row and column frequency using the pre-processed positions.",
      "If the row frequency becomes equal to the number of columns, or vice-versa return the current index."
    ]
  },
  {
    "title": "Determine the Winner of a Bowling Game",
    "description": "You are given two 0-indexed integer arrays player1 and player2, that represent the number of pins that player 1 and player 2 hit in a bowling game, respectively.\nThe bowling game consists of n turns, and the number of pins in each turn is exactly 10.\nAssume a player hit xi pins in the ith turn. The value of the ith turn for the player is:\n\n2xi if the player hit 10 pins in any of the previous two turns.\nOtherwise, It is xi.\n\nThe score of the player is the sum of the values of their n turns.\nReturn\n\n1 if the score of player 1 is more than the score of player 2,\n2 if the score of player 2 is more than the score of player 1, and\n0 in case of a draw.\n\n \n",
    "examples": [
      {
        "input": "Input: player1 = [4,10,7,9], player2 = [6,5,2,3]",
        "output": "Output: 1",
        "explanation": "Explanation: The score of player1 is 4 + 10 + 2*7 + 2*9 = 46."
      },
      {
        "input": "Input: player1 = [3,5,7,6], player2 = [8,10,10,2]",
        "output": "Output: 2",
        "explanation": "Explanation: The score of player1 is 3 + 5 + 7 + 6 = 21."
      },
      {
        "input": "Input: player1 = [2,3], player2 = [4,1]",
        "output": "Output: 0",
        "explanation": "Explanation: The score of player1 is 2 + 3 = 5"
      }
    ],
    "topics": [
      "Array",
      "Simulation"
    ],
    "difficulty": "Easy",
    "constraints": [
      "n == player1.length == player2.length",
      "1 <= n <= 1000",
      "0 <= player1[i], player2[i] <= 10"
    ],
    "hints": [
      "Think about simulating the process to calculate the answer.",
      "Iterate over each element and check the previous two elements. See if one of them is 10 and can affect the score."
    ]
  },
  {
    "title": "Count Increasing Quadruplets",
    "description": "Given a 0-indexed integer array nums of size n containing all numbers from 1 to n, return the number of increasing quadruplets.\nA quadruplet (i, j, k, l) is increasing if:\n\n0 <= i < j < k < l < n, and\nnums[i] < nums[k] < nums[j] < nums[l].\n\n \n",
    "examples": [
      {
        "input": "Input: nums = [1,3,2,4,5]",
        "output": "Output: 2",
        "explanation": "Explanation: "
      },
      {
        "input": "Input: nums = [1,2,3,4]",
        "output": "Output: 0",
        "explanation": "Explanation: There exists only one quadruplet with i = 0, j = 1, k = 2, l = 3, but since nums[j] < nums[k], we return 0."
      }
    ],
    "topics": [
      "Array",
      "Dynamic Programming",
      "Binary Indexed Tree",
      "Enumeration",
      "Prefix Sum"
    ],
    "difficulty": "Hard",
    "constraints": [
      "4 <= nums.length <= 4000",
      "1 <= nums[i] <= nums.length",
      "All the integers of nums are unique. nums is a permutation."
    ],
    "hints": [
      "Can you loop over all possible (j, k) and find the answer?",
      "We can pre-compute all possible (i, j) and (k, l) and store them in 2 matrices.",
      "The answer will the sum of prefix[j][k] * suffix[k][j]."
    ]
  },
  {
    "title": "Put Marbles in Bags",
    "description": "You have k bags. You are given a 0-indexed integer array weights where weights[i] is the weight of the ith marble. You are also given the integer k.\nDivide the marbles into the k bags according to the following rules:\n\nNo bag is empty.\nIf the ith marble and jth marble are in a bag, then all marbles with an index between the ith and jth indices should also be in that same bag.\nIf a bag consists of all the marbles with an index from i to j inclusively, then the cost of the bag is weights[i] + weights[j].\n\nThe score after distributing the marbles is the sum of the costs of all the k bags.\nReturn the difference between the maximum and minimum scores among marble distributions.\n \n",
    "examples": [
      {
        "input": "Input: weights = [1,3,5,1], k = 2",
        "output": "Output: 4",
        "explanation": "Explanation: "
      },
      {
        "input": "Input: weights = [1, 3], k = 2",
        "output": "Output: 0",
        "explanation": "Explanation: The only distribution possible is [1],[3]. "
      }
    ],
    "topics": [
      "Array",
      "Greedy",
      "Sorting",
      "Heap (Priority Queue)"
    ],
    "difficulty": "Hard",
    "constraints": [
      "1 <= k <= weights.length <= 105",
      "1 <= weights[i] <= 109"
    ],
    "hints": [
      "Each bag will contain a sub-array.",
      "Only the endpoints of the sub-array matter.",
      "Try to use a priority queue."
    ]
  },
  {
    "title": "Count Collisions of Monkeys on a Polygon",
    "description": "There is a regular convex polygon with n vertices. The vertices are labeled from 0 to n - 1 in a clockwise direction, and each vertex has exactly one monkey. The following figure shows a convex polygon of 6 vertices.\n\nEach monkey moves simultaneously to a neighboring vertex. A neighboring vertex for a vertex i can be:\n\nthe vertex (i + 1) % n in the clockwise direction, or\nthe vertex (i - 1 + n) % n in the counter-clockwise direction.\n\nA collision happens if at least two monkeys reside on the same vertex after the movement or intersect on an edge.\nReturn the number of ways the monkeys can move so that at least one collision  happens. Since the answer may be very large, return it modulo 109 + 7.\nNote that each monkey can only move once.\n \n",
    "examples": [
      {
        "input": "Input: n = 3",
        "output": "Output: 6",
        "explanation": "Explanation: There are 8 total possible movements."
      },
      {
        "input": "Input: n = 4",
        "output": "Output: 14",
        "explanation": "Explanation: It can be shown that there are 14 ways for the monkeys to collide."
      }
    ],
    "topics": [
      "Math",
      "Recursion"
    ],
    "difficulty": "Medium",
    "constraints": [
      "3 <= n <= 109"
    ],
    "hints": [
      "Try counting the number of ways in which the monkeys will not collide."
    ]
  },
  {
    "title": "Count Distinct Numbers on Board",
    "description": "You are given a positive integer n, that is initially placed on a board. Every day, for 109 days, you perform the following procedure:\n\nFor each number x present on the board, find all numbers 1 <= i <= n such that x % i == 1.\nThen, place those numbers on the board.\n\nReturn the number of distinct integers present on the board after 109 days have elapsed.\nNote:\n\nOnce a number is placed on the board, it will remain on it until the end.\n% stands for the modulo operation. For example, 14 % 3 is 2.\n\n \n",
    "examples": [
      {
        "input": "Input: n = 5",
        "output": "Output: 4",
        "explanation": "Explanation: Initially, 5 is present on the board. "
      },
      {
        "input": "Input: n = 3",
        "output": "Output: 2",
        "explanation": "Explanation: "
      }
    ],
    "topics": [
      "Array",
      "Hash Table",
      "Math",
      "Simulation"
    ],
    "difficulty": "Easy",
    "constraints": [
      "1 <= n <= 100"
    ],
    "hints": [
      "For n > 2, n % (n - 1) == 1 thus n - 1 will be added on the board the next day.",
      "As the operations are performed for so long time, all the numbers lesser than n except 1 will be added to the board.",
      "What will happen if n == 1?"
    ]
  },
  {
    "title": "Design Graph With Shortest Path Calculator",
    "description": "There is a directed weighted graph that consists of n nodes numbered from 0 to n - 1. The edges of the graph are initially represented by the given array edges where edges[i] = [fromi, toi, edgeCosti] meaning that there is an edge from fromi to toi with the cost edgeCosti.\nImplement the Graph class:\n\nGraph(int n, int[][] edges) initializes the object with n nodes and the given edges.\naddEdge(int[] edge) adds an edge to the list of edges where edge = [from, to, edgeCost]. It is guaranteed that there is no edge between the two nodes before adding this one.\nint shortestPath(int node1, int node2) returns the minimum cost of a path from node1 to node2. If no path exists, return -1. The cost of a path is the sum of the costs of the edges in the path.\n\n \n",
    "examples": [
      {
        "input": "Input\n[\"Graph\", \"shortestPath\", \"shortestPath\", \"addEdge\", \"shortestPath\"]",
        "output": "Output\n[null, 6, -1, null, 6]",
        "explanation": "Explanation\nGraph g = new Graph(4, [[0, 2, 5], [0, 1, 2], [1, 2, 1], [3, 0, 3]]);"
      }
    ],
    "topics": [
      "Graph",
      "Design",
      "Heap (Priority Queue)",
      "Shortest Path"
    ],
    "difficulty": "Hard",
    "constraints": [
      "1 <= n <= 100",
      "0 <= edges.length <= n * (n - 1)",
      "edges[i].length == edge.length == 3",
      "0 <= fromi, toi, from, to, node1, node2 <= n - 1",
      "1 <= edgeCosti, edgeCost <= 106",
      "There are no repeated edges and no self-loops in the graph at any point.",
      "At most 100 calls will be made for addEdge.",
      "At most 100 calls will be made for shortestPath."
    ],
    "hints": [
      "After adding each edge, update your graph with the new edge, and you can calculate the shortest path in your graph each time the shortestPath method is called.",
      "Use dijkstra’s algorithm to calculate the shortest paths."
    ]
  },
  {
    "title": "Cousins in Binary Tree II",
    "description": "Given the root of a binary tree, replace the value of each node in the tree with the sum of all its cousins' values.\nTwo nodes of a binary tree are cousins if they have the same depth with different parents.\nReturn the root of the modified tree.\nNote that the depth of a node is the number of edges in the path from the root node to it.\n \n",
    "examples": [
      {
        "input": "Input: root = [5,4,9,1,10,null,7]",
        "output": "Output: [0,0,0,7,7,null,11]",
        "explanation": "Explanation: The diagram above shows the initial binary tree and the binary tree after changing the value of each node."
      },
      {
        "input": "Input: root = [3,1,2]",
        "output": "Output: [0,0,0]",
        "explanation": "Explanation: The diagram above shows the initial binary tree and the binary tree after changing the value of each node."
      }
    ],
    "topics": [
      "Hash Table",
      "Tree",
      "Depth-First Search",
      "Breadth-First Search",
      "Binary Tree"
    ],
    "difficulty": "Medium",
    "constraints": [
      "The number of nodes in the tree is in the range [1, 105].",
      "1 <= Node.val <= 104"
    ],
    "hints": [
      "Use DFS two times.",
      "For the first time, find the sum of values of all the levels of the binary tree.",
      "For the second time, update the value of the node with the sum of the values of the current level - sibling node’s values."
    ]
  },
  {
    "title": "Find the Score of All Prefixes of an Array",
    "description": "We define the conversion array conver of an array arr as follows:\n\nconver[i] = arr[i] + max(arr[0..i]) where max(arr[0..i]) is the maximum value of arr[j] over 0 <= j <= i.\n\nWe also define the score of an array arr as the sum of the values of the conversion array of arr.\nGiven a 0-indexed integer array nums of length n, return an array ans of length n where ans[i] is the score of the prefix nums[0..i].\n \n",
    "examples": [
      {
        "input": "Input: nums = [2,3,7,5,10]",
        "output": "Output: [4,10,24,36,56]",
        "explanation": "Explanation: "
      },
      {
        "input": "Input: nums = [1,1,2,4,8,16]",
        "output": "Output: [2,4,8,16,32,64]",
        "explanation": "Explanation: "
      }
    ],
    "topics": [
      "Array",
      "Prefix Sum"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= nums.length <= 105",
      "1 <= nums[i] <= 109"
    ],
    "hints": [
      "Keep track of the prefix maximum of the array",
      "Establish a relationship between ans[i] and ans[i-1]",
      "for 0 < i < n, ans[i] = ans[i-1]+conver[i]. In other words, array ans is the prefix sum array of the conversion array"
    ]
  },
  {
    "title": "Find the Width of Columns of a Grid",
    "description": "You are given a 0-indexed m x n integer matrix grid. The width of a column is the maximum length of its integers.\n\nFor example, if grid = [[-10], [3], [12]], the width of the only column is 3 since -10 is of length 3.\n\nReturn an integer array ans of size n where ans[i] is the width of the ith column.\nThe length of an integer x with len digits is equal to len if x is non-negative, and len + 1 otherwise.\n \n",
    "examples": [
      {
        "input": "Input: grid = [[1],[22],[333]]",
        "output": "Output: [3]",
        "explanation": "Explanation: In the 0th column, 333 is of length 3."
      },
      {
        "input": "Input: grid = [[-15,1,3],[15,7,12],[5,6,-2]]",
        "output": "Output: [3,1,2]",
        "explanation": "Explanation: "
      }
    ],
    "topics": [
      "Array",
      "Matrix"
    ],
    "difficulty": "Easy",
    "constraints": [
      "m == grid.length",
      "n == grid[i].length",
      "1 <= m, n <= 100 ",
      "-109 <= grid[r][c] <= 109"
    ],
    "hints": [
      "You can find the length of a number by dividing it by 10 and then rounding it down again and again until this number becomes equal to 0. Add 1 if this number is negative.",
      "Traverse the matrix column-wise to find the maximum length in each column."
    ]
  },
  {
    "title": "Maximize Win From Two Segments",
    "description": "There are some prizes on the X-axis. You are given an integer array prizePositions that is sorted in non-decreasing order, where prizePositions[i] is the position of the ith prize. There could be different prizes at the same position on the line. You are also given an integer k.\nYou are allowed to select two segments with integer endpoints. The length of each segment must be k. You will collect all prizes whose position falls within at least one of the two selected segments (including the endpoints of the segments). The two selected segments may intersect.\n\nFor example if k = 2, you can choose segments [1, 3] and [2, 4], and you will win any prize i that satisfies 1 <= prizePositions[i] <= 3 or 2 <= prizePositions[i] <= 4.\n\nReturn the maximum number of prizes you can win if you choose the two segments optimally.\n \n",
    "examples": [
      {
        "input": "Input: prizePositions = [1,1,2,2,3,3,5], k = 2",
        "output": "Output: 7",
        "explanation": "Explanation: In this example, you can win all 7 prizes by selecting two segments [1, 3] and [3, 5]."
      },
      {
        "input": "Input: prizePositions = [1,2,3,4], k = 0",
        "output": "Output: 2",
        "explanation": "Explanation: For this example, one choice for the segments is [3, 3] and [4, 4], and you will be able to get 2 prizes. "
      }
    ],
    "topics": [
      "Array",
      "Binary Search",
      "Sliding Window"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= prizePositions.length <= 105",
      "1 <= prizePositions[i] <= 109",
      "0 <= k <= 109 ",
      "prizePositions is sorted in non-decreasing order."
    ],
    "hints": [
      "Try solving the problem for one interval.",
      "Using the solution with one interval, how can you combine that with a second interval?"
    ]
  },
  {
    "title": "Shortest Cycle in a Graph",
    "description": "There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1. The edges in the graph are represented by a given 2D integer array edges, where edges[i] = [ui, vi] denotes an edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.\nReturn the length of the shortest cycle in the graph. If no cycle exists, return -1.\nA cycle is a path that starts and ends at the same node, and each edge in the path is used only once.\n \n",
    "examples": [
      {
        "input": "Input: n = 7, edges = [[0,1],[1,2],[2,0],[3,4],[4,5],[5,6],[6,3]]",
        "output": "Output: 3",
        "explanation": "Explanation: The cycle with the smallest length is : 0 -> 1 -> 2 -> 0 "
      },
      {
        "input": "Input: n = 4, edges = [[0,1],[0,2]]",
        "output": "Output: -1",
        "explanation": "Explanation: There are no cycles in this graph."
      }
    ],
    "topics": [
      "Breadth-First Search",
      "Graph"
    ],
    "difficulty": "Hard",
    "constraints": [
      "2 <= n <= 1000",
      "1 <= edges.length <= 1000",
      "edges[i].length == 2",
      "0 <= ui, vi < n",
      "ui != vi",
      "There are no repeated edges."
    ],
    "hints": [
      "How can BFS be used?",
      "For each vertex u, calculate the length of the shortest cycle that contains vertex u using BFS"
    ]
  },
  {
    "title": "Make K-Subarray Sums Equal",
    "description": "You are given a 0-indexed integer array arr and an integer k. The array arr is circular. In other words, the first element of the array is the next element of the last element, and the last element of the array is the previous element of the first element.\nYou can do the following operation any number of times:\n\nPick any element from arr and increase or decrease it by 1.\n\nReturn the minimum number of operations such that the sum of each subarray of length k is equal.\nA subarray is a contiguous part of the array.\n \n",
    "examples": [
      {
        "input": "Input: arr = [1,4,1,3], k = 2",
        "output": "Output: 1",
        "explanation": "Explanation: we can do one operation on index 1 to make its value equal to 3."
      },
      {
        "input": "Input: arr = [2,5,5,7], k = 3",
        "output": "Output: 5",
        "explanation": "Explanation: we can do three operations on index 0 to make its value equal to 5 and two operations on index 3 to make its value equal to 5."
      }
    ],
    "topics": [
      "Array",
      "Math",
      "Sorting",
      "Number Theory"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= k <= arr.length <= 105",
      "1 <= arr[i] <= 109"
    ],
    "hints": [
      "Think about gcd(n, k). How will it help to calculate the answer?",
      "indices i and j are in the same group if gcd(n, k) mod i = gcd(n, k) mod j. Each group should have equal elements. Think about the minimum number of operations for each group",
      "The minimum number of operations for each group equals the summation of differences between the elements and the median of elements inside the group."
    ]
  },
  {
    "title": "Find the Substring With Maximum Cost",
    "description": "You are given a string s, a string chars of distinct characters and an integer array vals of the same length as chars.\nThe cost of the substring is the sum of the values of each character in the substring. The cost of an empty string is considered 0.\nThe value of the character is defined in the following way:\n\nIf the character is not in the string chars, then its value is its corresponding position (1-indexed) in the alphabet.\n\n\t\nFor example, the value of 'a' is 1, the value of 'b' is 2, and so on. The value of 'z' is 26.\n\n\nOtherwise, assuming i is the index where the character occurs in the string chars, then its value is vals[i].\n\nReturn the maximum cost among all substrings of the string s.\n \n",
    "examples": [
      {
        "input": "Input: s = \"adaa\", chars = \"d\", vals = [-1000]",
        "output": "Output: 2",
        "explanation": "Explanation: The value of the characters \"a\" and \"d\" is 1 and -1000 respectively."
      },
      {
        "input": "Input: s = \"abc\", chars = \"abc\", vals = [-1,-1,-1]",
        "output": "Output: 0",
        "explanation": "Explanation: The value of the characters \"a\", \"b\" and \"c\" is -1, -1, and -1 respectively."
      }
    ],
    "topics": [
      "Array",
      "Hash Table",
      "String",
      "Dynamic Programming"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= s.length <= 105",
      "s consist of lowercase English letters.",
      "1 <= chars.length <= 26",
      "chars consist of distinct lowercase English letters.",
      "vals.length == chars.length",
      "-1000 <= vals[i] <= 1000"
    ],
    "hints": [
      "Create a new integer array where arr[i] denotes the value of character s[i].",
      "We can use Kadane’s maximum subarray sum algorithm to find the maximum cost."
    ]
  },
  {
    "title": "Form Smallest Number From Two Digit Arrays",
    "description": "Given two arrays of unique digits nums1 and nums2, return the smallest number that contains at least one digit from each array.\n \n",
    "examples": [
      {
        "input": "Input: nums1 = [4,1,3], nums2 = [5,7]",
        "output": "Output: 15",
        "explanation": "Explanation: The number 15 contains the digit 1 from nums1 and the digit 5 from nums2. It can be proven that 15 is the smallest number we can have."
      },
      {
        "input": "Input: nums1 = [3,5,2,6], nums2 = [3,1,7]",
        "output": "Output: 3",
        "explanation": "Explanation: The number 3 contains the digit 3 which exists in both arrays."
      }
    ],
    "topics": [
      "Array",
      "Hash Table",
      "Enumeration"
    ],
    "difficulty": "Easy",
    "constraints": [
      "1 <= nums1.length, nums2.length <= 9",
      "1 <= nums1[i], nums2[i] <= 9",
      "All digits in each array are unique."
    ],
    "hints": [
      "How many digits will the resulting number have at most?",
      "The resulting number will have either one or two digits. Try to find when each case is possible."
    ]
  },
  {
    "title": "Minimum Time to Repair Cars",
    "description": "You are given an integer array ranks representing the ranks of some mechanics. ranksi is the rank of the ith mechanic. A mechanic with a rank r can repair n cars in r * n2 minutes.\nYou are also given an integer cars representing the total number of cars waiting in the garage to be repaired.\nReturn the minimum time taken to repair all the cars.\nNote: All the mechanics can repair the cars simultaneously.\n \n",
    "examples": [
      {
        "input": "Input: ranks = [4,2,3,1], cars = 10",
        "output": "Output: 16",
        "explanation": "Explanation: "
      },
      {
        "input": "Input: ranks = [5,1,8], cars = 6",
        "output": "Output: 16",
        "explanation": "Explanation: "
      }
    ],
    "topics": [
      "Array",
      "Binary Search"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= ranks.length <= 105",
      "1 <= ranks[i] <= 100",
      "1 <= cars <= 106"
    ],
    "hints": [
      "For a predefined fixed time, can all the cars be repaired?",
      "Try using binary search on the answer."
    ]
  },
  {
    "title": "Maximize Greatness of an Array",
    "description": "You are given a 0-indexed integer array nums. You are allowed to permute nums into a new array perm of your choosing.\nWe define the greatness of nums be the number of indices 0 <= i < nums.length for which perm[i] > nums[i].\nReturn the maximum possible greatness you can achieve after permuting nums.\n \n",
    "examples": [
      {
        "input": "Input: nums = [1,3,5,2,1,3,1]",
        "output": "Output: 4",
        "explanation": "Explanation: One of the optimal rearrangements is perm = [2,5,1,3,3,1,1]."
      },
      {
        "input": "Input: nums = [1,2,3,4]",
        "output": "Output: 3",
        "explanation": "Explanation: We can prove the optimal perm is [2,3,4,1]."
      }
    ],
    "topics": [
      "Array",
      "Two Pointers",
      "Greedy",
      "Sorting"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= nums.length <= 105",
      "0 <= nums[i] <= 109"
    ],
    "hints": [
      "Can we use sorting and two pointers here?",
      "Assign every element the next bigger unused element as many times as possible."
    ]
  },
  {
    "title": "Distribute Money to Maximum Children",
    "description": "You are given an integer money denoting the amount of money (in dollars) that you have and another integer children denoting the number of children that you must distribute the money to.\nYou have to distribute the money according to the following rules:\n\nAll money must be distributed.\nEveryone must receive at least 1 dollar.\nNobody receives 4 dollars.\n\nReturn the maximum number of children who may receive exactly 8 dollars if you distribute the money according to the aforementioned rules. If there is no way to distribute the money, return -1.\n \n",
    "examples": [
      {
        "input": "Input: money = 20, children = 3",
        "output": "Output: 1",
        "explanation": "Explanation: "
      },
      {
        "input": "Input: money = 16, children = 2",
        "output": "Output: 2",
        "explanation": "Explanation: Each child can be given 8 dollars."
      }
    ],
    "topics": [
      "Math",
      "Greedy"
    ],
    "difficulty": "Easy",
    "constraints": [
      "1 <= money <= 200",
      "2 <= children <= 30"
    ],
    "hints": [
      "Can we distribute the money according to the rules if we give 'k' children exactly 8 dollars?",
      "Brute force to find the largest possible value of k, or return -1 if there doesn’t exist any such k."
    ]
  },
  {
    "title": "Check Knight Tour Configuration",
    "description": "There is a knight on an n x n chessboard. In a valid configuration, the knight starts at the top-left cell of the board and visits every cell on the board exactly once.\nYou are given an n x n integer matrix grid consisting of distinct integers from the range [0, n * n - 1] where grid[row][col] indicates that the cell (row, col) is the grid[row][col]th cell that the knight visited. The moves are 0-indexed.\nReturn true if grid represents a valid configuration of the knight's movements or false otherwise.\nNote that a valid knight move consists of moving two squares vertically and one square horizontally, or two squares horizontally and one square vertically. The figure below illustrates all the possible eight moves of a knight from some cell.\n\n \n",
    "examples": [
      {
        "input": "Input: grid = [[0,11,16,5,20],[17,4,19,10,15],[12,1,8,21,6],[3,18,23,14,9],[24,13,2,7,22]]",
        "output": "Output: true",
        "explanation": "Explanation: The above diagram represents the grid. It can be shown that it is a valid configuration."
      },
      {
        "input": "Input: grid = [[0,3,6],[5,8,1],[2,7,4]]",
        "output": "Output: false",
        "explanation": "Explanation: The above diagram represents the grid. The 8th move of the knight is not valid considering its position after the 7th move."
      }
    ],
    "topics": [
      "Array",
      "Depth-First Search",
      "Breadth-First Search",
      "Matrix",
      "Simulation"
    ],
    "difficulty": "Medium",
    "constraints": [
      "n == grid.length == grid[i].length",
      "3 <= n <= 7",
      "0 <= grid[row][col] < n * n",
      "All integers in grid are unique."
    ],
    "hints": [
      "It is enough to check if each move of the knight is valid.",
      "Try all cases of the knight's movements to check if a move is valid."
    ]
  },
  {
    "title": "Smallest Missing Non-negative Integer After Operations",
    "description": "You are given a 0-indexed integer array nums and an integer value.\nIn one operation, you can add or subtract value from any element of nums.\n\nFor example, if nums = [1,2,3] and value = 2, you can choose to subtract value from nums[0] to make nums = [-1,2,3].\n\nThe MEX (minimum excluded) of an array is the smallest missing non-negative integer in it.\n\nFor example, the MEX of [-1,2,3] is 0 while the MEX of [1,0,3] is 2.\n\nReturn the maximum MEX of nums after applying the mentioned operation any number of times.\n \n",
    "examples": [
      {
        "input": "Input: nums = [1,-10,7,13,6,8], value = 5",
        "output": "Output: 4",
        "explanation": "Explanation: One can achieve this result by applying the following operations:"
      },
      {
        "input": "Input: nums = [1,-10,7,13,6,8], value = 7",
        "output": "Output: 2",
        "explanation": "Explanation: One can achieve this result by applying the following operation:"
      }
    ],
    "topics": [
      "Array",
      "Hash Table",
      "Math",
      "Greedy"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= nums.length, value <= 105",
      "-109 <= nums[i] <= 109"
    ],
    "hints": [
      "Think about using modular arithmetic.",
      "if x = nums[i] (mod value), then we can make nums[i] equal to x  after some number of operations",
      "How does finding the frequency of (nums[i] mod value) help?"
    ]
  },
  {
    "title": "Number of Even and Odd Bits",
    "description": "You are given a positive integer n.\nLet even denote the number of even indices in the binary representation of n (0-indexed) with value 1.\nLet odd denote the number of odd indices in the binary representation of n (0-indexed) with value 1.\nReturn an integer array answer where answer = [even, odd].\n \n",
    "examples": [
      {
        "input": "Input: n = 17",
        "output": "Output: [2,0]",
        "explanation": "Explanation: The binary representation of 17 is 10001. "
      },
      {
        "input": "Input: n = 2",
        "output": "Output: [0,1]",
        "explanation": "Explanation: The binary representation of 2 is 10."
      }
    ],
    "topics": [
      "Bit Manipulation"
    ],
    "difficulty": "Easy",
    "constraints": [
      "1 <= n <= 1000"
    ],
    "hints": [
      "Maintain two integer variables, even and odd, to count the number of even and odd indices in the binary representation of integer n.",
      "Divide n by 2 while n is positive, and if n modulo 2 is 1, add 1 to its corresponding variable."
    ]
  },
  {
    "title": "Minimum Time to Complete All Tasks",
    "description": "There is a computer that can run an unlimited number of tasks at the same time. You are given a 2D integer array tasks where tasks[i] = [starti, endi, durationi] indicates that the ith task should run for a total of durationi seconds (not necessarily continuous) within the inclusive time range [starti, endi].\nYou may turn on the computer only when it needs to run a task. You can also turn it off if it is idle.\nReturn the minimum time during which the computer should be turned on to complete all tasks.\n \n",
    "examples": [
      {
        "input": "Input: tasks = [[2,3,1],[4,5,1],[1,5,2]]",
        "output": "Output: 2",
        "explanation": "Explanation: "
      },
      {
        "input": "Input: tasks = [[1,3,2],[2,5,3],[5,6,2]]",
        "output": "Output: 4",
        "explanation": "Explanation: "
      }
    ],
    "topics": [
      "Array",
      "Binary Search",
      "Stack",
      "Greedy",
      "Sorting"
    ],
    "difficulty": "Hard",
    "constraints": [
      "1 <= tasks.length <= 2000",
      "tasks[i].length == 3",
      "1 <= starti, endi <= 2000",
      "1 <= durationi <= endi - starti + 1"
    ],
    "hints": [
      "Sort the tasks in ascending order of end time",
      "Since there are only up to 2000 time points to consider, you can check them one by one",
      "It is always beneficial to run the task as late as possible so that later tasks can run simultaneously."
    ]
  },
  {
    "title": "Count the Number of Beautiful Subarrays",
    "description": "You are given a 0-indexed integer array nums. In one operation, you can:\n\nChoose two different indices i and j such that 0 <= i, j < nums.length.\nChoose a non-negative integer k such that the kth bit (0-indexed) in the binary representation of nums[i] and nums[j] is 1.\nSubtract 2k from nums[i] and nums[j].\n\nA subarray is beautiful if it is possible to make all of its elements equal to 0 after applying the above operation any number of times.\nReturn the number of beautiful subarrays in the array nums.\nA subarray is a contiguous non-empty sequence of elements within an array.\n \n",
    "examples": [
      {
        "input": "Input: nums = [4,3,1,2,4]",
        "output": "Output: 2",
        "explanation": "Explanation: There are 2 beautiful subarrays in nums: [4,3,1,2,4] and [4,3,1,2,4]."
      },
      {
        "input": "Input: nums = [1,10,4]",
        "output": "Output: 0",
        "explanation": "Explanation: There are no beautiful subarrays in nums."
      }
    ],
    "topics": [
      "Array",
      "Hash Table",
      "Bit Manipulation",
      "Prefix Sum"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= nums.length <= 105",
      "0 <= nums[i] <= 106"
    ],
    "hints": [
      "A subarray is beautiful if its xor is equal to zero.",
      "Compute the prefix xor for every index, then the xor of subarray [left, right] is equal to zero if prefix_xor[left] ^ perfix_xor[right] == 0",
      "Iterate from left to right and maintain a hash table to count the number of indices equal to the current prefix xor."
    ]
  },
  {
    "title": "Rearrange Array to Maximize Prefix Score",
    "description": "You are given a 0-indexed integer array nums. You can rearrange the elements of nums to any order (including the given order).\nLet prefix be the array containing the prefix sums of nums after rearranging it. In other words, prefix[i] is the sum of the elements from 0 to i in nums after rearranging it. The score of nums is the number of positive integers in the array prefix.\nReturn the maximum score you can achieve.\n \n",
    "examples": [
      {
        "input": "Input: nums = [2,-1,0,1,-3,3,-3]",
        "output": "Output: 6",
        "explanation": "Explanation: We can rearrange the array into nums = [2,3,1,-1,-3,0,-3]."
      },
      {
        "input": "Input: nums = [-2,-3,0]",
        "output": "Output: 0",
        "explanation": "Explanation: Any rearrangement of the array will result in a score of 0."
      }
    ],
    "topics": [
      "Array",
      "Greedy",
      "Sorting",
      "Prefix Sum"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= nums.length <= 105",
      "-106 <= nums[i] <= 106"
    ],
    "hints": [
      "The best order of the array is in decreasing order.",
      "Sort the array in decreasing order and count the number of positive values in the prefix sum array."
    ]
  },
  {
    "title": "Count the Number of Vowel Strings in Range",
    "description": "You are given a 0-indexed array of string words and two integers left and right.\nA string is called a vowel string if it starts with a vowel character and ends with a vowel character where vowel characters are 'a', 'e', 'i', 'o', and 'u'.\nReturn the number of vowel strings words[i] where i belongs to the inclusive range [left, right].\n \n",
    "examples": [
      {
        "input": "Input: words = [\"are\",\"amy\",\"u\"], left = 0, right = 2",
        "output": "Output: 2",
        "explanation": "Explanation: "
      },
      {
        "input": "Input: words = [\"hey\",\"aeo\",\"mu\",\"ooo\",\"artro\"], left = 1, right = 4",
        "output": "Output: 3",
        "explanation": "Explanation: "
      }
    ],
    "topics": [
      "Array",
      "String"
    ],
    "difficulty": "Easy",
    "constraints": [
      "1 <= words.length <= 1000",
      "1 <= words[i].length <= 10",
      "words[i] consists of only lowercase English letters.",
      "0 <= left <= right < words.length"
    ],
    "hints": [
      "consider iterating over all strings from left to right and use an if condition to check if the first character and last character are vowels."
    ]
  },
  {
    "title": "Count Number of Possible Root Nodes",
    "description": "Alice has an undirected tree with n nodes labeled from 0 to n - 1. The tree is represented as a 2D integer array edges of length n - 1 where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree.\nAlice wants Bob to find the root of the tree. She allows Bob to make several guesses about her tree. In one guess, he does the following:\n\nChooses two distinct integers u and v such that there exists an edge [u, v] in the tree.\nHe tells Alice that u is the parent of v in the tree.\n\nBob's guesses are represented by a 2D integer array guesses where guesses[j] = [uj, vj] indicates Bob guessed uj to be the parent of vj.\nAlice being lazy, does not reply to each of Bob's guesses, but just says that at least k of his guesses are true.\nGiven the 2D integer arrays edges, guesses and the integer k, return the number of possible nodes that can be the root of Alice's tree. If there is no such tree, return 0.\n \n",
    "examples": [
      {
        "input": "Input: edges = [[0,1],[1,2],[1,3],[4,2]], guesses = [[1,3],[0,1],[1,0],[2,4]], k = 3",
        "output": "Output: 3",
        "explanation": "Explanation: "
      },
      {
        "input": "Input: edges = [[0,1],[1,2],[2,3],[3,4]], guesses = [[1,0],[3,4],[2,1],[3,2]], k = 1",
        "output": "Output: 5",
        "explanation": "Explanation: "
      }
    ],
    "topics": [
      "Hash Table",
      "Dynamic Programming",
      "Tree",
      "Depth-First Search"
    ],
    "difficulty": "Hard",
    "constraints": [
      "edges.length == n - 1",
      "2 <= n <= 105",
      "1 <= guesses.length <= 105",
      "0 <= ai, bi, uj, vj <= n - 1",
      "ai != bi",
      "uj != vj",
      "edges represents a valid tree.",
      "guesses[j] is an edge of the tree.",
      "guesses is unique.",
      "0 <= k <= guesses.length"
    ],
    "hints": [
      "How can we check if any node can be the root?",
      "Can we use this information to check its neighboring nodes?",
      "When we traverse from current node to a neighboring node, how will we update our answer?"
    ]
  },
  {
    "title": "Count Ways to Group Overlapping Ranges",
    "description": "You are given a 2D integer array ranges where ranges[i] = [starti, endi] denotes that all integers between starti and endi (both inclusive) are contained in the ith range.\nYou are to split ranges into two (possibly empty) groups such that:\n\nEach range belongs to exactly one group.\nAny two overlapping ranges must belong to the same group.\n\nTwo ranges are said to be overlapping if there exists at least one integer that is present in both ranges.\n\nFor example, [1, 3] and [2, 5] are overlapping because 2 and 3 occur in both ranges.\n\nReturn the total number of ways to split ranges into two groups. Since the answer may be very large, return it modulo 109 + 7.\n \n",
    "examples": [
      {
        "input": "Input: ranges = [[6,10],[5,15]]",
        "output": "Output: 2",
        "explanation": "Explanation: "
      },
      {
        "input": "Input: ranges = [[1,3],[10,20],[2,5],[4,8]]",
        "output": "Output: 4",
        "explanation": "Explanation: "
      }
    ],
    "topics": [
      "Array",
      "Sorting"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= ranges.length <= 105",
      "ranges[i].length == 2",
      "0 <= starti <= endi <= 109"
    ],
    "hints": [
      "Can we use sorting here?",
      "Sort the ranges and merge the overlapping ranges. Then count number of non-overlapping ranges.",
      "How many ways can we group these non-overlapping ranges?"
    ]
  },
  {
    "title": "Split With Minimum Sum",
    "description": "Given a positive integer num, split it into two non-negative integers num1 and num2 such that:\n\nThe concatenation of num1 and num2 is a permutation of num.\n\n\t\nIn other words, the sum of the number of occurrences of each digit in num1 and num2 is equal to the number of occurrences of that digit in num.\n\n\nnum1 and num2 can contain leading zeros.\n\nReturn the minimum possible sum of num1 and num2.\nNotes:\n\nIt is guaranteed that num does not contain any leading zeros.\nThe order of occurrence of the digits in num1 and num2 may differ from the order of occurrence of num.\n\n \n",
    "examples": [
      {
        "input": "Input: num = 4325",
        "output": "Output: 59",
        "explanation": "Explanation: We can split 4325 so that num1 is 24 and num2 is 35, giving a sum of 59. We can prove that 59 is indeed the minimal possible sum."
      },
      {
        "input": "Input: num = 687",
        "output": "Output: 75",
        "explanation": "Explanation: We can split 687 so that num1 is 68 and num2 is 7, which would give an optimal sum of 75."
      }
    ],
    "topics": [
      "Math",
      "Greedy",
      "Sorting"
    ],
    "difficulty": "Easy",
    "constraints": [
      "10 <= num <= 109"
    ],
    "hints": [
      "Sort the digits of num in non decreasing order.",
      "Assign digits to num1 and num2 alternatively."
    ]
  },
  {
    "title": "Count Total Number of Colored Cells",
    "description": "There exists an infinitely large two-dimensional grid of uncolored unit cells. You are given a positive integer n, indicating that you must do the following routine for n minutes:\n\nAt the first minute, color any arbitrary unit cell blue.\nEvery minute thereafter, color blue every uncolored cell that touches a blue cell.\n\nBelow is a pictorial representation of the state of the grid after minutes 1, 2, and 3.\n\nReturn the number of colored cells at the end of n minutes.\n \n",
    "examples": [
      {
        "input": "Input: n = 1",
        "output": "Output: 1",
        "explanation": "Explanation: After 1 minute, there is only 1 blue cell, so we return 1."
      },
      {
        "input": "Input: n = 2",
        "output": "Output: 5",
        "explanation": "Explanation: After 2 minutes, there are 4 colored cells on the boundary and 1 in the center, so we return 5. "
      }
    ],
    "topics": [
      "Math"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= n <= 105"
    ],
    "hints": [
      "Derive a mathematical relation between total number of colored cells and the time elapsed in minutes."
    ]
  },
  {
    "title": "Number of Ways to Earn Points",
    "description": "There is a test that has n types of questions. You are given an integer target and a 0-indexed 2D integer array types where types[i] = [counti, marksi] indicates that there are counti questions of the ith type, and each one of them is worth marksi points.\n\n\nReturn the number of ways you can earn exactly target points in the exam. Since the answer may be too large, return it modulo 109 + 7.\nNote that questions of the same type are indistinguishable.\n\nFor example, if there are 3 questions of the same type, then solving the 1st and 2nd questions is the same as solving the 1st and 3rd questions, or the 2nd and 3rd questions.\n\n \n",
    "examples": [
      {
        "input": "Input: target = 6, types = [[6,1],[3,2],[2,3]]",
        "output": "Output: 7",
        "explanation": "Explanation: You can earn 6 points in one of the seven ways:"
      },
      {
        "input": "Input: target = 5, types = [[50,1],[50,2],[50,5]]",
        "output": "Output: 4",
        "explanation": "Explanation: You can earn 5 points in one of the four ways:"
      },
      {
        "input": "Input: target = 18, types = [[6,1],[3,2],[2,3]]",
        "output": "Output: 1",
        "explanation": "Explanation: You can only earn 18 points by answering all questions."
      }
    ],
    "topics": [
      "Array",
      "Dynamic Programming"
    ],
    "difficulty": "Hard",
    "constraints": [
      "1 <= target <= 1000",
      "n == types.length",
      "1 <= n <= 50",
      "types[i].length == 2",
      "1 <= counti, marksi <= 50"
    ],
    "hints": [
      "Use Dynamic Programming",
      "Let ways[i][points] be the number of ways to score a given number of points after solving some questions of the first i types.",
      "ways[i][points] is equal to the sum of ways[i-1][points - solved * marks[i] over 0 <= solved <= count_i"
    ]
  },
  {
    "title": "Split the Array to Make Coprime Products",
    "description": "You are given a 0-indexed integer array nums of length n.\nA split at an index i where 0 <= i <= n - 2 is called valid if the product of the first i + 1 elements and the product of the remaining elements are coprime.\n\nFor example, if nums = [2, 3, 3], then a split at the index i = 0 is valid because 2 and 9 are coprime, while a split at the index i = 1 is not valid because 6 and 3 are not coprime. A split at the index i = 2 is not valid because i == n - 1.\n\nReturn the smallest index i at which the array can be split validly or -1 if there is no such split.\nTwo values val1 and val2 are coprime if gcd(val1, val2) == 1 where gcd(val1, val2) is the greatest common divisor of val1 and val2.\n \n",
    "examples": [
      {
        "input": "Input: nums = [4,7,8,15,3,5]",
        "output": "Output: 2",
        "explanation": "Explanation: The table above shows the values of the product of the first i + 1 elements, the remaining elements, and their gcd at each index i."
      },
      {
        "input": "Input: nums = [4,7,15,8,3,5]",
        "output": "Output: -1",
        "explanation": "Explanation: The table above shows the values of the product of the first i + 1 elements, the remaining elements, and their gcd at each index i."
      }
    ],
    "topics": [
      "Array",
      "Hash Table",
      "Math",
      "Number Theory"
    ],
    "difficulty": "Hard",
    "constraints": [
      "n == nums.length",
      "1 <= n <= 104",
      "1 <= nums[i] <= 106"
    ],
    "hints": [
      "Two numbers with GCD equal to 1 have no common prime divisor.",
      "Find the prime factorization of the left and right sides and check if they share a prime divisor."
    ]
  },
  {
    "title": "Kth Largest Sum in a Binary Tree",
    "description": "You are given the root of a binary tree and a positive integer k.\nThe level sum in the tree is the sum of the values of the nodes that are on the same level.\nReturn the kth largest level sum in the tree (not necessarily distinct). If there are fewer than k levels in the tree, return -1.\nNote that two nodes are on the same level if they have the same distance from the root.\n \n",
    "examples": [
      {
        "input": "Input: root = [5,8,9,2,1,3,7,4,6], k = 2",
        "output": "Output: 13",
        "explanation": "Explanation: The level sums are the following:"
      },
      {
        "input": "Input: root = [1,2,null,3], k = 1",
        "output": "Output: 3",
        "explanation": "Explanation: The largest level sum is 3."
      }
    ],
    "topics": [
      "Binary Search",
      "Tree",
      "Breadth-First Search"
    ],
    "difficulty": "Medium",
    "constraints": [
      "The number of nodes in the tree is n.",
      "2 <= n <= 105",
      "1 <= Node.val <= 106",
      "1 <= k <= n"
    ],
    "hints": [
      "Find the sum of values of nodes on each level and return the kth largest one.",
      "To find the sum of the values of nodes on each level, you can use a DFS or BFS algorithm to traverse the tree and keep track of the level of each node."
    ]
  },
  {
    "title": "Pass the Pillow",
    "description": "There are n people standing in a line labeled from 1 to n. The first person in the line is holding a pillow initially. Every second, the person holding the pillow passes it to the next person standing in the line. Once the pillow reaches the end of the line, the direction changes, and people continue passing the pillow in the opposite direction.\n\nFor example, once the pillow reaches the nth person they pass it to the n - 1th person, then to the n - 2th person and so on.\n\nGiven the two positive integers n and time, return the index of the person holding the pillow after time seconds.\n \n",
    "examples": [
      {
        "input": "Input: n = 4, time = 5",
        "output": "Output: 2",
        "explanation": "Explanation: People pass the pillow in the following way: 1 -> 2 -> 3 -> 4 -> 3 -> 2."
      },
      {
        "input": "Input: n = 3, time = 2",
        "output": "Output: 3",
        "explanation": "Explanation: People pass the pillow in the following way: 1 -> 2 -> 3."
      }
    ],
    "topics": [
      "Math",
      "Simulation"
    ],
    "difficulty": "Easy",
    "constraints": [
      "2 <= n <= 1000",
      "1 <= time <= 1000"
    ],
    "hints": [
      "Maintain two integer variables, direction and i, where direction denotes the current direction in which the pillow should pass, and i denotes an index of the person holding the pillow.",
      "While time is positive, update the current index with the current direction. If the index reaches the end of the line, multiply direction by - 1."
    ]
  },
  {
    "title": "Time to Cross a Bridge",
    "description": "There are k workers who want to move n boxes from an old warehouse to a new one. You are given the two integers n and k, and a 2D integer array time of size k x 4 where time[i] = [leftToRighti, pickOldi, rightToLefti, putNewi].\nThe warehouses are separated by a river and connected by a bridge. The old warehouse is on the right bank of the river, and the new warehouse is on the left bank of the river. Initially, all k workers are waiting on the left side of the bridge. To move the boxes, the ith worker (0-indexed) can :\n\nCross the bridge from the left bank (new warehouse) to the right bank (old warehouse) in leftToRighti minutes.\nPick a box from the old warehouse and return to the bridge in pickOldi minutes. Different workers can pick up their boxes simultaneously.\nCross the bridge from the right bank (old warehouse) to the left bank (new warehouse) in rightToLefti minutes.\nPut the box in the new warehouse and return to the bridge in putNewi minutes. Different workers can put their boxes simultaneously.\n\nA worker i is less efficient than a worker j if either condition is met:\n\nleftToRighti + rightToLefti > leftToRightj + rightToLeftj\nleftToRighti + rightToLefti == leftToRightj + rightToLeftj and i > j\n\nThe following rules regulate the movement of the workers through the bridge :\n\nIf a worker x reaches the bridge while another worker y is crossing the bridge, x waits at their side of the bridge.\nIf the bridge is free, the worker waiting on the right side of the bridge gets to cross the bridge. If more than one worker is waiting on the right side, the one with the lowest efficiency crosses first.\nIf the bridge is free and no worker is waiting on the right side, and at least one box remains at the old warehouse, the worker on the left side of the river gets to cross the bridge. If more than one worker is waiting on the left side, the one with the lowest efficiency crosses first.\n\nReturn the instance of time at which the last worker reaches the left bank of the river after all n boxes have been put in the new warehouse.\n \n",
    "examples": [
      {
        "input": "Input: n = 1, k = 3, time = [[1,1,2,1],[1,1,3,1],[1,1,4,1]]",
        "output": "Output: 6",
        "explanation": "Explanation: "
      },
      {
        "input": "Input: n = 3, k = 2, time = [[1,9,1,8],[10,10,10,10]]",
        "output": "Output: 50",
        "explanation": "Explanation: "
      }
    ],
    "topics": [
      "Array",
      "Heap (Priority Queue)",
      "Simulation"
    ],
    "difficulty": "Hard",
    "constraints": [
      "1 <= n, k <= 104",
      "time.length == k",
      "time[i].length == 4",
      "1 <= leftToRighti, pickOldi, rightToLefti, putNewi <= 1000"
    ],
    "hints": [
      "Try simulating this process.",
      "We can use a priority queue to query over the least efficient worker."
    ]
  },
  {
    "title": "Disconnect Path in a Binary Matrix by at Most One Flip",
    "description": "You are given a 0-indexed m x n binary matrix grid. You can move from a cell (row, col) to any of the cells (row + 1, col) or (row, col + 1) that has the value 1. The matrix is disconnected if there is no path from (0, 0) to (m - 1, n - 1).\nYou can flip the value of at most one (possibly none) cell. You cannot flip the cells (0, 0) and (m - 1, n - 1).\nReturn true if it is possible to make the matrix disconnect or false otherwise.\nNote that flipping a cell changes its value from 0 to 1 or from 1 to 0.\n \n",
    "examples": [
      {
        "input": "Input: grid = [[1,1,1],[1,0,0],[1,1,1]]",
        "output": "Output: true",
        "explanation": "Explanation: We can change the cell shown in the diagram above. There is no path from (0, 0) to (2, 2) in the resulting grid."
      },
      {
        "input": "Input: grid = [[1,1,1],[1,0,1],[1,1,1]]",
        "output": "Output: false",
        "explanation": "Explanation: It is not possible to change at most one cell such that there is not path from (0, 0) to (2, 2)."
      }
    ],
    "topics": [
      "Array",
      "Dynamic Programming",
      "Depth-First Search",
      "Breadth-First Search",
      "Matrix"
    ],
    "difficulty": "Medium",
    "constraints": [
      "m == grid.length",
      "n == grid[i].length",
      "1 <= m, n <= 1000",
      "1 <= m * n <= 105",
      "grid[i][j] is either 0 or 1.",
      "grid[0][0] == grid[m - 1][n - 1] == 1"
    ],
    "hints": [
      "We can consider the grid a graph with edges between adjacent cells.",
      "If you can find two non-intersecting paths from (0, 0) to (m - 1, n - 1) then the answer is false. Otherwise, it is always true."
    ]
  },
  {
    "title": "Maximum Number of Integers to Choose From a Range I",
    "description": "You are given an integer array banned and two integers n and maxSum. You are choosing some number of integers following the below rules:\n\nThe chosen integers have to be in the range [1, n].\nEach integer can be chosen at most once.\nThe chosen integers should not be in the array banned.\nThe sum of the chosen integers should not exceed maxSum.\n\nReturn the maximum number of integers you can choose following the mentioned rules.\n \n",
    "examples": [
      {
        "input": "Input: banned = [1,6,5], n = 5, maxSum = 6",
        "output": "Output: 2",
        "explanation": "Explanation: You can choose the integers 2 and 4."
      },
      {
        "input": "Input: banned = [1,2,3,4,5,6,7], n = 8, maxSum = 1",
        "output": "Output: 0",
        "explanation": "Explanation: You cannot choose any integer while following the mentioned conditions."
      },
      {
        "input": "Input: banned = [11], n = 7, maxSum = 50",
        "output": "Output: 7",
        "explanation": "Explanation: You can choose the integers 1, 2, 3, 4, 5, 6, and 7."
      }
    ],
    "topics": [
      "Array",
      "Hash Table",
      "Binary Search",
      "Greedy",
      "Sorting"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= banned.length <= 104",
      "1 <= banned[i], n <= 104",
      "1 <= maxSum <= 109"
    ],
    "hints": [
      "Keep the banned numbers that are less than n in a set.",
      "Loop over the numbers from 1 to n and if the number is not banned, use it.",
      "Keep adding numbers while they are not banned, and their sum is less than k."
    ]
  },
  {
    "title": "Separate the Digits in an Array",
    "description": "Given an array of positive integers nums, return an array answer that consists of the digits of each integer in nums after separating them in the same order they appear in nums.\nTo separate the digits of an integer is to get all the digits it has in the same order.\n\nFor example, for the integer 10921, the separation of its digits is [1,0,9,2,1].\n\n \n",
    "examples": [
      {
        "input": "Input: nums = [13,25,83,77]",
        "output": "Output: [1,3,2,5,8,3,7,7]",
        "explanation": "Explanation: "
      },
      {
        "input": "Input: nums = [7,1,3,9]",
        "output": "Output: [7,1,3,9]",
        "explanation": "Explanation: The separation of each integer in nums is itself."
      }
    ],
    "topics": [
      "Array",
      "Simulation"
    ],
    "difficulty": "Easy",
    "constraints": [
      "1 <= nums.length <= 1000",
      "1 <= nums[i] <= 105"
    ],
    "hints": [
      "Convert each number into a list and append that list to the answer.",
      "You can convert the integer into a string to do that easily."
    ]
  },
  {
    "title": "Maximum Subsequence Score",
    "description": "You are given two 0-indexed integer arrays nums1 and nums2 of equal length n and a positive integer k. You must choose a subsequence of indices from nums1 of length k.\nFor chosen indices i0, i1, ..., ik - 1, your score is defined as:\n\nThe sum of the selected elements from nums1 multiplied with the minimum of the selected elements from nums2.\nIt can defined simply as: (nums1[i0] + nums1[i1] +...+ nums1[ik - 1]) * min(nums2[i0] , nums2[i1], ... ,nums2[ik - 1]).\n\nReturn the maximum possible score.\nA subsequence of indices of an array is a set that can be derived from the set {0, 1, ..., n-1} by deleting some or no elements.\n \n",
    "examples": [
      {
        "input": "Input: nums1 = [1,3,3,2], nums2 = [2,1,3,4], k = 3",
        "output": "Output: 12",
        "explanation": "Explanation: "
      },
      {
        "input": "Input: nums1 = [4,2,3,1,1], nums2 = [7,5,10,9,6], k = 1",
        "output": "Output: 30",
        "explanation": "Explanation: "
      }
    ],
    "topics": [
      "Array",
      "Greedy",
      "Sorting",
      "Heap (Priority Queue)"
    ],
    "difficulty": "Medium",
    "constraints": [
      "n == nums1.length == nums2.length",
      "1 <= n <= 105",
      "0 <= nums1[i], nums2[j] <= 105",
      "1 <= k <= n"
    ],
    "hints": [
      "How can we use sorting here?",
      "Try sorting the two arrays based on second array.",
      "Loop through nums2 and compute the max product given the minimum is nums2[i]. Update the answer accordingly."
    ]
  },
  {
    "title": "Check if Point Is Reachable",
    "description": "There exists an infinitely large grid. You are currently at point (1, 1), and you need to reach the point (targetX, targetY) using a finite number of steps.\nIn one step, you can move from point (x, y) to any one of the following points:\n\n(x, y - x)\n(x - y, y)\n(2 * x, y)\n(x, 2 * y)\n\nGiven two integers targetX and targetY representing the X-coordinate and Y-coordinate of your final position, return true if you can reach the point from (1, 1) using some number of steps, and false otherwise.\n \n",
    "examples": [
      {
        "input": "Input: targetX = 6, targetY = 9",
        "output": "Output: false",
        "explanation": "Explanation: It is impossible to reach (6,9) from (1,1) using any sequence of moves, so false is returned."
      },
      {
        "input": "Input: targetX = 4, targetY = 7",
        "output": "Output: true",
        "explanation": "Explanation: You can follow the path (1,1) -> (1,2) -> (1,4) -> (1,8) -> (1,7) -> (2,7) -> (4,7)."
      }
    ],
    "topics": [
      "Math",
      "Number Theory"
    ],
    "difficulty": "Hard",
    "constraints": [
      "1 <= targetX, targetY <= 109"
    ],
    "hints": [
      "Let’s go in reverse order, from (targetX, targetY) to (1, 1). So, now we can move from (x, y) to (x+y, y), (x, y+x), (x/2, y) if x is even, and (x, y/2) if y is even.",
      "When is it optimal to use the third and fourth operations?",
      "Think how GCD of (x, y) is affected if we apply the first two operations.",
      "How can we check if we can reach (1, 1) using the GCD value calculate above?"
    ]
  },
  {
    "title": "Minimum Common Value",
    "description": "Given two integer arrays nums1 and nums2, sorted in non-decreasing order, return the minimum integer common to both arrays. If there is no common integer amongst nums1 and nums2, return -1.\nNote that an integer is said to be common to nums1 and nums2 if both arrays have at least one occurrence of that integer.\n \n",
    "examples": [
      {
        "input": "Input: nums1 = [1,2,3], nums2 = [2,4]",
        "output": "Output: 2",
        "explanation": "Explanation: The smallest element common to both arrays is 2, so we return 2."
      },
      {
        "input": "Input: nums1 = [1,2,3,6], nums2 = [2,3,4,5]",
        "output": "Output: 2",
        "explanation": "Explanation: There are two common elements in the array 2 and 3 out of which 2 is the smallest, so 2 is returned."
      }
    ],
    "topics": [
      "Array",
      "Hash Table",
      "Two Pointers",
      "Binary Search"
    ],
    "difficulty": "Easy",
    "constraints": [
      "1 <= nums1.length, nums2.length <= 105",
      "1 <= nums1[i], nums2[j] <= 109",
      "Both nums1 and nums2 are sorted in non-decreasing order."
    ],
    "hints": [
      "Try to use a set.",
      "Otherwise, try to use a two-pointer approach."
    ]
  },
  {
    "title": "Minimum Cost to Split an Array",
    "description": "You are given an integer array nums and an integer k.\nSplit the array into some number of non-empty subarrays. The cost of a split is the sum of the importance value of each subarray in the split.\nLet trimmed(subarray) be the version of the subarray where all numbers which appear only once are removed.\n\nFor example, trimmed([3,1,2,4,3,4]) = [3,4,3,4].\n\nThe importance value of a subarray is k + trimmed(subarray).length.\n\nFor example, if a subarray is [1,2,3,3,3,4,4], then trimmed([1,2,3,3,3,4,4]) = [3,3,3,4,4].The importance value of this subarray will be k + 5.\n\nReturn the minimum possible cost of a split of nums.\nA subarray is a contiguous non-empty sequence of elements within an array.\n \n",
    "examples": [
      {
        "input": "Input: nums = [1,2,1,2,1,3,3], k = 2",
        "output": "Output: 8",
        "explanation": "Explanation: We split nums to have two subarrays: [1,2], [1,2,1,3,3]."
      },
      {
        "input": "Input: nums = [1,2,1,2,1], k = 2",
        "output": "Output: 6",
        "explanation": "Explanation: We split nums to have two subarrays: [1,2], [1,2,1]."
      },
      {
        "input": "Input: nums = [1,2,1,2,1], k = 5",
        "output": "Output: 10",
        "explanation": "Explanation: We split nums to have one subarray: [1,2,1,2,1]."
      }
    ],
    "topics": [
      "Array",
      "Hash Table",
      "Dynamic Programming",
      "Counting"
    ],
    "difficulty": "Hard",
    "constraints": [
      "1 <= nums.length <= 1000",
      "0 <= nums[i] < nums.length",
      "1 <= k <= 109"
    ],
    "hints": [
      "Let's denote dp[r] = minimum cost to partition the first r elements of nums. What would be the transitions of such dynamic programming?",
      "dp[r] = min(dp[l] + importance(nums[l..r])) over all 0 <= l < r. This already gives us an O(n^3) approach, as importance can be calculated in linear time, and there are a total of O(n^2) transitions.",
      "Can you think of a way to compute multiple importance values of related subarrays faster?",
      "importance(nums[l-1..r]) is either importance(nums[l..r]) if a new unique element is added, importance(nums[l..r]) + 1 if an old element that appeared at least twice is added, or importance(nums[l..r]) + 2, if a previously unique element is duplicated. This allows us to compute importance(nums[l..r]) for all 0 <= l < r in O(n) by keeping a frequency table and decreasing l from r-1 down to 0."
    ]
  },
  {
    "title": "Apply Bitwise Operations to Make Strings Equal",
    "description": "You are given two 0-indexed binary strings s and target of the same length n. You can do the following operation on s any number of times:\n\nChoose two different indices i and j where 0 <= i, j < n.\nSimultaneously, replace s[i] with (s[i] OR s[j]) and s[j] with (s[i] XOR s[j]).\n\nFor example, if s = \"0110\", you can choose i = 0 and j = 2, then simultaneously replace s[0] with (s[0] OR s[2] = 0 OR 1 = 1), and s[2] with (s[0] XOR s[2] = 0 XOR 1 = 1), so we will have s = \"1110\".\nReturn true if you can make the string s equal to target, or false otherwise.\n \n",
    "examples": [
      {
        "input": "Input: s = \"1010\", target = \"0110\"",
        "output": "Output: true",
        "explanation": "Explanation: We can do the following operations:"
      },
      {
        "input": "Input: s = \"11\", target = \"00\"",
        "output": "Output: false",
        "explanation": "Explanation: It is not possible to make s equal to target with any number of operations."
      }
    ],
    "topics": [
      "String",
      "Bit Manipulation"
    ],
    "difficulty": "Medium",
    "constraints": [
      "n == s.length == target.length",
      "2 <= n <= 105",
      "s and target consist of only the digits 0 and 1."
    ],
    "hints": [
      "Think of when it is impossible to convert the string to the target.",
      "If exactly one of the strings is having all 0’s, then it is impossible. And it is possible in all other cases. Why is that true?"
    ]
  },
  {
    "title": "Sort the Students by Their Kth Score",
    "description": "There is a class with m students and n exams. You are given a 0-indexed m x n integer matrix score, where each row represents one student and score[i][j] denotes the score the ith student got in the jth exam. The matrix score contains distinct integers only.\nYou are also given an integer k. Sort the students (i.e., the rows of the matrix) by their scores in the kth (0-indexed) exam from the highest to the lowest.\nReturn the matrix after sorting it.\n \n",
    "examples": [
      {
        "input": "Input: score = [[10,6,9,1],[7,5,11,2],[4,8,3,15]], k = 2",
        "output": "Output: [[7,5,11,2],[10,6,9,1],[4,8,3,15]]",
        "explanation": "Explanation: In the above diagram, S denotes the student, while E denotes the exam."
      },
      {
        "input": "Input: score = [[3,4],[5,6]], k = 0",
        "output": "Output: [[5,6],[3,4]]",
        "explanation": "Explanation: In the above diagram, S denotes the student, while E denotes the exam."
      }
    ],
    "topics": [
      "Array",
      "Sorting",
      "Matrix"
    ],
    "difficulty": "Medium",
    "constraints": [
      "m == score.length",
      "n == score[i].length",
      "1 <= m, n <= 250",
      "1 <= score[i][j] <= 105",
      "score consists of distinct integers.",
      "0 <= k < n"
    ],
    "hints": [
      "Find the row with the highest score in the kth exam and swap it with the first row.",
      "After fixing the first row, perform the same operation for the rest of the rows, and the matrix's rows will get sorted one by one."
    ]
  },
  {
    "title": "Alternating Digit Sum",
    "description": "You are given a positive integer n. Each digit of n has a sign according to the following rules:\n\nThe most significant digit is assigned a positive sign.\nEach other digit has an opposite sign to its adjacent digits.\n\nReturn the sum of all digits with their corresponding sign.\n \n",
    "examples": [
      {
        "input": "Input: n = 521",
        "output": "Output: 4",
        "explanation": "Explanation: (+5) + (-2) + (+1) = 4."
      },
      {
        "input": "Input: n = 111",
        "output": "Output: 1",
        "explanation": "Explanation: (+1) + (-1) + (+1) = 1."
      },
      {
        "input": "Input: n = 886996",
        "output": "Output: 0",
        "explanation": "Explanation: (+8) + (-8) + (+6) + (-9) + (+9) + (-6) = 0."
      }
    ],
    "topics": [
      "Math"
    ],
    "difficulty": "Easy",
    "constraints": [
      "1 <= n <= 109"
    ],
    "hints": [
      "The first step is to loop over the digits. We can convert the integer into a string, an array of digits, or just loop over its digits.",
      "Keep a variable sign that initially equals 1 and a variable answer that initially equals 0.",
      "Each time you loop over a digit i, add sign * i to answer, then multiply sign by -1."
    ]
  },
  {
    "title": "Minimize the Maximum of Two Arrays",
    "description": "We have two arrays arr1 and arr2 which are initially empty. You need to add positive integers to them such that they satisfy all the following conditions:\n\narr1 contains uniqueCnt1 distinct positive integers, each of which is not divisible by divisor1.\narr2 contains uniqueCnt2 distinct positive integers, each of which is not divisible by divisor2.\nNo integer is present in both arr1 and arr2.\n\nGiven divisor1, divisor2, uniqueCnt1, and uniqueCnt2, return the minimum possible maximum integer that can be present in either array.\n \n",
    "examples": [
      {
        "input": "Input: divisor1 = 2, divisor2 = 7, uniqueCnt1 = 1, uniqueCnt2 = 3",
        "output": "Output: 4",
        "explanation": "Explanation: "
      },
      {
        "input": "Input: divisor1 = 3, divisor2 = 5, uniqueCnt1 = 2, uniqueCnt2 = 1",
        "output": "Output: 3",
        "explanation": "Explanation: "
      },
      {
        "input": "Input: divisor1 = 2, divisor2 = 4, uniqueCnt1 = 8, uniqueCnt2 = 2",
        "output": "Output: 15",
        "explanation": "Explanation: "
      }
    ],
    "topics": [
      "Math",
      "Binary Search",
      "Number Theory"
    ],
    "difficulty": "Medium",
    "constraints": [
      "2 <= divisor1, divisor2 <= 105",
      "1 <= uniqueCnt1, uniqueCnt2 < 109",
      "2 <= uniqueCnt1 + uniqueCnt2 <= 109"
    ],
    "hints": [
      "Use binary search to find smallest maximum element.",
      "Add numbers divisible by x in nums2 and vice versa."
    ]
  },
  {
    "title": "Difference Between Maximum and Minimum Price Sum",
    "description": "There exists an undirected and initially unrooted tree with n nodes indexed from 0 to n - 1. You are given the integer n and a 2D integer array edges of length n - 1, where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree.\nEach node has an associated price. You are given an integer array price, where price[i] is the price of the ith node.\nThe price sum of a given path is the sum of the prices of all nodes lying on that path.\nThe tree can be rooted at any node root of your choice. The incurred cost after choosing root is the difference between the maximum and minimum price sum amongst all paths starting at root.\nReturn the maximum possible cost amongst all possible root choices.\n \n",
    "examples": [
      {
        "input": "Input: n = 6, edges = [[0,1],[1,2],[1,3],[3,4],[3,5]], price = [9,8,7,6,10,5]",
        "output": "Output: 24",
        "explanation": "Explanation: The diagram above denotes the tree after rooting it at node 2. The first part (colored in red) shows the path with the maximum price sum. The second part (colored in blue) shows the path with the minimum price sum."
      },
      {
        "input": "Input: n = 3, edges = [[0,1],[1,2]], price = [1,1,1]",
        "output": "Output: 2",
        "explanation": "Explanation: The diagram above denotes the tree after rooting it at node 0. The first part (colored in red) shows the path with the maximum price sum. The second part (colored in blue) shows the path with the minimum price sum."
      }
    ],
    "topics": [
      "Array",
      "Dynamic Programming",
      "Tree",
      "Depth-First Search"
    ],
    "difficulty": "Hard",
    "constraints": [
      "1 <= n <= 105",
      "edges.length == n - 1",
      "0 <= ai, bi <= n - 1",
      "edges represents a valid tree.",
      "price.length == n",
      "1 <= price[i] <= 105"
    ],
    "hints": [
      "The minimum price sum is always the price of a rooted node.",
      "Let’s root the tree at vertex 0 and find the answer from this perspective.",
      "In the optimal answer maximum price is the sum of the prices of nodes on the path from “u” to “v” where either “u” or “v” is the parent of the second one or neither is a parent of the second one.",
      "The first case is easy to find. For the second case, notice that in the optimal path, “u” and “v” are both leaves. Then we can use dynamic programming to find such a path.",
      "Let DP(v,1) denote “the maximum price sum from node v to leaf, where v is a parent of that leaf” and let DP(v,0) denote “the maximum price sum from node v to leaf, where v is a parent of that leaf - price[leaf]”. Then the answer is maximum of DP(u,0) + DP(v,1) + price[parent] where u, v are directly connected to vertex “parent”."
    ]
  },
  {
    "title": "Count the Number of Good Subarrays",
    "description": "Given an integer array nums and an integer k, return the number of good subarrays of nums.\nA subarray arr is good if it there are at least k pairs of indices (i, j) such that i < j and arr[i] == arr[j].\nA subarray is a contiguous non-empty sequence of elements within an array.\n \n",
    "examples": [
      {
        "input": "Input: nums = [1,1,1,1,1], k = 10",
        "output": "Output: 1",
        "explanation": "Explanation: The only good subarray is the array nums itself."
      },
      {
        "input": "Input: nums = [3,1,4,3,2,2,4], k = 2",
        "output": "Output: 4",
        "explanation": "Explanation: There are 4 different good subarrays:"
      }
    ],
    "topics": [
      "Array",
      "Hash Table",
      "Sliding Window"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= nums.length <= 105",
      "1 <= nums[i], k <= 109"
    ],
    "hints": [
      "For a fixed index l, try to find the minimum value of index r, such that the subarray is not good",
      "When a number is added to a subarray, it increases the number of pairs by its previous appearances.",
      "When a number is removed from the subarray, it decreases the number of pairs by its remaining appearances.",
      "Maintain 2-pointers l and r such that we can keep in account the number of equal pairs."
    ]
  },
  {
    "title": "Increment Submatrices by One",
    "description": "You are given a positive integer n, indicating that we initially have an n x n 0-indexed integer matrix mat filled with zeroes.\nYou are also given a 2D integer array query. For each query[i] = [row1i, col1i, row2i, col2i], you should do the following operation:\n\nAdd 1 to every element in the submatrix with the top left corner (row1i, col1i) and the bottom right corner (row2i, col2i). That is, add 1 to mat[x][y] for all row1i <= x <= row2i and col1i <= y <= col2i.\n\nReturn the matrix mat after performing every query.\n \n",
    "examples": [
      {
        "input": "Input: n = 3, queries = [[1,1,2,2],[0,0,1,1]]",
        "output": "Output: [[1,1,0],[1,2,1],[0,1,1]]",
        "explanation": "Explanation: The diagram above shows the initial matrix, the matrix after the first query, and the matrix after the second query."
      },
      {
        "input": "Input: n = 2, queries = [[0,0,1,1]]",
        "output": "Output: [[1,1],[1,1]]",
        "explanation": "Explanation: The diagram above shows the initial matrix and the matrix after the first query."
      }
    ],
    "topics": [
      "Array",
      "Matrix",
      "Prefix Sum"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= n <= 500",
      "1 <= queries.length <= 104",
      "0 <= row1i <= row2i < n",
      "0 <= col1i <= col2i < n"
    ],
    "hints": [
      "Imagine each row as a separate array. Instead of updating the whole submatrix together, we can use prefix sum to update each row separately.",
      "For each query, iterate over the rows i in the range [row1, row2] and add 1 to prefix sum S[i][col1], and subtract 1 from S[i][col2 + 1].",
      "After doing this operation for all the queries, update each row separately with S[i][j] = S[i][j] + S[i][j - 1]."
    ]
  },
  {
    "title": "Difference Between Element Sum and Digit Sum of an Array",
    "description": "You are given a positive integer array nums.\n\nThe element sum is the sum of all the elements in nums.\nThe digit sum is the sum of all the digits (not necessarily distinct) that appear in nums.\n\nReturn the absolute difference between the element sum and digit sum of nums.\nNote that the absolute difference between two integers x and y is defined as |x - y|.\n \n",
    "examples": [
      {
        "input": "Input: nums = [1,15,6,3]",
        "output": "Output: 9",
        "explanation": "Explanation: "
      },
      {
        "input": "Input: nums = [1,2,3,4]",
        "output": "Output: 0",
        "explanation": ""
      }
    ],
    "topics": [
      "Array",
      "Math"
    ],
    "difficulty": "Easy",
    "constraints": [
      "1 <= nums.length <= 2000",
      "1 <= nums[i] <= 2000"
    ],
    "hints": [
      "Use a simple for loop to iterate each number.",
      "How you can get the digit for each number?"
    ]
  },
  {
    "title": "Find Xor-Beauty of Array",
    "description": "You are given a 0-indexed integer array nums.\nThe effective value of three indices i, j, and k is defined as ((nums[i] | nums[j]) & nums[k]).\nThe xor-beauty of the array is the XORing of the effective values of all the possible triplets of indices (i, j, k) where 0 <= i, j, k < n.\nReturn the xor-beauty of nums.\nNote that:\n\nval1 | val2 is bitwise OR of val1 and val2.\nval1 & val2 is bitwise AND of val1 and val2.\n\n \n",
    "examples": [
      {
        "input": "Input: nums = [1,4]",
        "output": "Output: 5",
        "explanation": "Explanation: "
      },
      {
        "input": "Input: nums = [15,45,20,2,34,35,5,44,32,30]",
        "output": "Output: 34",
        "explanation": "Explanation: The xor-beauty of the given array is 34."
      }
    ],
    "topics": [
      "Array",
      "Math",
      "Bit Manipulation"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= nums.length <= 105",
      "1 <= nums[i] <= 109"
    ],
    "hints": [
      "Try to simplify the given expression.",
      "Try constructing the answer bit by bit."
    ]
  },
  {
    "title": "Find Consecutive Integers from a Data Stream",
    "description": "For a stream of integers, implement a data structure that checks if the last k integers parsed in the stream are equal to value.\nImplement the DataStream class:\n\nDataStream(int value, int k) Initializes the object with an empty integer stream and the two integers value and k.\nboolean consec(int num) Adds num to the stream of integers. Returns true if the last k integers are equal to value, and false otherwise. If there are less than k integers, the condition does not hold true, so returns false.\n\n \n",
    "examples": [
      {
        "input": "Input\n[\"DataStream\", \"consec\", \"consec\", \"consec\", \"consec\"]",
        "output": "Output\n[null, false, false, true, false]",
        "explanation": "Explanation\nDataStream dataStream = new DataStream(4, 3); //value = 4, k = 3 "
      }
    ],
    "topics": [
      "Hash Table",
      "Design",
      "Queue",
      "Counting",
      "Data Stream"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= value, num <= 109",
      "1 <= k <= 105",
      "At most 105 calls will be made to consec."
    ],
    "hints": [
      "Keep track of the last integer which is not equal to value.",
      "Use a queue-type data structure to store the last k integers."
    ]
  },
  {
    "title": "Categorize Box According to Criteria",
    "description": "Given four integers length, width, height, and mass, representing the dimensions and mass of a box, respectively, return a string representing the category of the box.\n\nThe box is \"Bulky\" if:\n\n\t\nAny of the dimensions of the box is greater or equal to 104.\nOr, the volume of the box is greater or equal to 109.\n\n\nIf the mass of the box is greater or equal to 100, it is \"Heavy\".\nIf the box is both \"Bulky\" and \"Heavy\", then its category is \"Both\".\nIf the box is neither \"Bulky\" nor \"Heavy\", then its category is \"Neither\".\nIf the box is \"Bulky\" but not \"Heavy\", then its category is \"Bulky\".\nIf the box is \"Heavy\" but not \"Bulky\", then its category is \"Heavy\".\n\nNote that the volume of the box is the product of its length, width and height.\n \n",
    "examples": [
      {
        "input": "Input: length = 1000, width = 35, height = 700, mass = 300",
        "output": "Output: \"Heavy\"",
        "explanation": "Explanation: "
      },
      {
        "input": "Input: length = 200, width = 50, height = 800, mass = 50",
        "output": "Output: \"Neither\"",
        "explanation": "Explanation: "
      }
    ],
    "topics": [
      "Math"
    ],
    "difficulty": "Easy",
    "constraints": [
      "1 <= length, width, height <= 105",
      "1 <= mass <= 103"
    ],
    "hints": [
      "Use conditional statements to find the right category of the box."
    ]
  },
  {
    "title": "Maximize the Minimum Powered City",
    "description": "You are given a 0-indexed integer array stations of length n, where stations[i] represents the number of power stations in the ith city.\nEach power station can provide power to every city in a fixed range. In other words, if the range is denoted by r, then a power station at city i can provide power to all cities j such that |i - j| <= r and 0 <= i, j <= n - 1.\n\nNote that |x| denotes absolute value. For example, |7 - 5| = 2 and |3 - 10| = 7.\n\nThe power of a city is the total number of power stations it is being provided power from.\nThe government has sanctioned building k more power stations, each of which can be built in any city, and have the same range as the pre-existing ones.\nGiven the two integers r and k, return the maximum possible minimum power of a city, if the additional power stations are built optimally.\nNote that you can build the k power stations in multiple cities.\n \n",
    "examples": [
      {
        "input": "Input: stations = [1,2,4,5,0], r = 1, k = 2",
        "output": "Output: 5",
        "explanation": "Explanation: "
      },
      {
        "input": "Input: stations = [4,4,4,4], r = 0, k = 3",
        "output": "Output: 4",
        "explanation": "Explanation: "
      }
    ],
    "topics": [
      "Array",
      "Binary Search",
      "Greedy",
      "Queue",
      "Sliding Window",
      "Prefix Sum"
    ],
    "difficulty": "Hard",
    "constraints": [
      "n == stations.length",
      "1 <= n <= 105",
      "0 <= stations[i] <= 105",
      "0 <= r <= n - 1",
      "0 <= k <= 109"
    ],
    "hints": [
      "Pre calculate the number of stations on each city using Line Sweep.",
      "Use binary search to maximize the minimum."
    ]
  },
  {
    "title": "Maximal Score After Applying K Operations",
    "description": "You are given a 0-indexed integer array nums and an integer k. You have a starting score of 0.\nIn one operation:\n\nchoose an index i such that 0 <= i < nums.length,\nincrease your score by nums[i], and\nreplace nums[i] with ceil(nums[i] / 3).\n\nReturn the maximum possible score you can attain after applying exactly k operations.\nThe ceiling function ceil(val) is the least integer greater than or equal to val.\n \n",
    "examples": [
      {
        "input": "Input: nums = [10,10,10,10,10], k = 5",
        "output": "Output: 50",
        "explanation": "Explanation: Apply the operation to each array element exactly once. The final score is 10 + 10 + 10 + 10 + 10 = 50."
      },
      {
        "input": "Input: nums = [1,10,3,3,3], k = 3",
        "output": "Output: 17",
        "explanation": "Explanation: You can do the following operations:"
      }
    ],
    "topics": [
      "Array",
      "Greedy",
      "Heap (Priority Queue)"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= nums.length, k <= 105",
      "1 <= nums[i] <= 109"
    ],
    "hints": [
      "It is always optimal to select the greatest element in the array.",
      "Use a heap to query for the maximum in O(log n) time."
    ]
  },
  {
    "title": "Make Number of Distinct Characters Equal",
    "description": "You are given two 0-indexed strings word1 and word2.\nA move consists of choosing two indices i and j such that 0 <= i < word1.length and 0 <= j < word2.length and swapping word1[i] with word2[j].\nReturn true if it is possible to get the number of distinct characters in word1 and word2 to be equal with exactly one move. Return false otherwise.\n \n",
    "examples": [
      {
        "input": "Input: word1 = \"ac\", word2 = \"b\"",
        "output": "Output: false",
        "explanation": "Explanation: Any pair of swaps would yield two distinct characters in the first string, and one in the second string."
      },
      {
        "input": "Input: word1 = \"abcc\", word2 = \"aab\"",
        "output": "Output: true",
        "explanation": "Explanation: We swap index 2 of the first string with index 0 of the second string. The resulting strings are word1 = \"abac\" and word2 = \"cab\", which both have 3 distinct characters."
      },
      {
        "input": "Input: word1 = \"abcde\", word2 = \"fghij\"",
        "output": "Output: true",
        "explanation": "Explanation: Both resulting strings will have 5 distinct characters, regardless of which indices we swap."
      }
    ],
    "topics": [
      "Hash Table",
      "String",
      "Counting"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= word1.length, word2.length <= 105",
      "word1 and word2 consist of only lowercase English letters."
    ],
    "hints": [
      "Create a frequency array of the letters of each string.",
      "There are 26*26 possible pairs of letters to swap. Can we try them all?",
      "Iterate over all possible pairs of letters and check if swapping them will yield two strings that have the same number of distinct characters. Use the frequency array for the check."
    ]
  },
  {
    "title": "Maximum Count of Positive Integer and Negative Integer",
    "description": "Given an array nums sorted in non-decreasing order, return the maximum between the number of positive integers and the number of negative integers.\n\nIn other words, if the number of positive integers in nums is pos and the number of negative integers is neg, then return the maximum of pos and neg.\n\nNote that 0 is neither positive nor negative.\n \n",
    "examples": [
      {
        "input": "Input: nums = [-2,-1,-1,1,2,3]",
        "output": "Output: 3",
        "explanation": "Explanation: There are 3 positive integers and 3 negative integers. The maximum count among them is 3."
      },
      {
        "input": "Input: nums = [-3,-2,-1,0,0,1,2]",
        "output": "Output: 3",
        "explanation": "Explanation: There are 2 positive integers and 3 negative integers. The maximum count among them is 3."
      },
      {
        "input": "Input: nums = [5,20,66,1314]",
        "output": "Output: 4",
        "explanation": "Explanation: There are 4 positive integers and 0 negative integers. The maximum count among them is 4."
      }
    ],
    "topics": [
      "Array",
      "Binary Search",
      "Counting"
    ],
    "difficulty": "Easy",
    "constraints": [
      "1 <= nums.length <= 2000",
      "-2000 <= nums[i] <= 2000",
      "nums is sorted in a non-decreasing order.",
      "",
      " ",
      "Follow up: Can you solve the problem in O(log(n)) time complexity?"
    ],
    "hints": [
      "Count how many positive integers and negative integers are in the array.",
      "Since the array is sorted, can we use the binary search?"
    ]
  },
  {
    "title": "Closest Prime Numbers in Range",
    "description": "Given two positive integers left and right, find the two integers num1 and num2 such that:\n\nleft <= nums1 < nums2 <= right .\nnums1 and nums2 are both prime numbers.\nnums2 - nums1 is the minimum amongst all other pairs satisfying the above conditions.\n\nReturn the positive integer array ans = [nums1, nums2]. If there are multiple pairs satisfying these conditions, return the one with the minimum nums1 value or [-1, -1] if such numbers do not exist.\nA number greater than 1 is called prime if it is only divisible by 1 and itself.\n \n",
    "examples": [
      {
        "input": "Input: left = 10, right = 19",
        "output": "Output: [11,13]",
        "explanation": "Explanation: The prime numbers between 10 and 19 are 11, 13, 17, and 19."
      },
      {
        "input": "Input: left = 4, right = 6",
        "output": "Output: [-1,-1]",
        "explanation": "Explanation: There exists only one prime number in the given range, so the conditions cannot be satisfied."
      }
    ],
    "topics": [
      "Math",
      "Number Theory"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= left <= right <= 106"
    ],
    "hints": [
      "Use Sieve of Eratosthenes to mark numbers that are primes.",
      "Iterate from right to left and find pair with the minimum distance between marked numbers."
    ]
  },
  {
    "title": "Distinct Prime Factors of Product of Array",
    "description": "Given an array of positive integers nums, return the number of distinct prime factors in the product of the elements of nums.\nNote that:\n\nA number greater than 1 is called prime if it is divisible by only 1 and itself.\nAn integer val1 is a factor of another integer val2 if val2 / val1 is an integer.\n\n \n",
    "examples": [
      {
        "input": "Input: nums = [2,4,3,7,10,6]",
        "output": "Output: 4",
        "explanation": ""
      },
      {
        "input": "Input: nums = [2,4,8,16]",
        "output": "Output: 1",
        "explanation": ""
      }
    ],
    "topics": [
      "Array",
      "Hash Table",
      "Math",
      "Number Theory"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= nums.length <= 104",
      "2 <= nums[i] <= 1000"
    ],
    "hints": [
      "Do not multiply all the numbers together, as the product is too big to store.",
      "Think about how each individual number's prime factors contribute to the prime factors of the product of the entire array.",
      "Find the prime factors of each element in nums, and store all of them in a set to avoid duplicates."
    ]
  },
  {
    "title": "Count the Digits That Divide a Number",
    "description": "Given an integer num, return the number of digits in num that divide num.\nAn integer val divides nums if nums % val == 0.\n \n",
    "examples": [
      {
        "input": "Input: num = 7",
        "output": "Output: 1",
        "explanation": "Explanation: 7 divides itself, hence the answer is 1."
      },
      {
        "input": "Input: num = 121",
        "output": "Output: 2",
        "explanation": "Explanation: 121 is divisible by 1, but not 2. Since 1 occurs twice as a digit, we return 2."
      },
      {
        "input": "Input: num = 1248",
        "output": "Output: 4",
        "explanation": "Explanation: 1248 is divisible by all of its digits, hence the answer is 4."
      }
    ],
    "topics": [
      "Math"
    ],
    "difficulty": "Easy",
    "constraints": [
      "1 <= num <= 109",
      "num does not contain 0 as one of its digits."
    ],
    "hints": [
      "Use mod by 10 to retrieve the least significant digit of the number",
      "Divide the number by 10, then round it down so that the second least significant digit becomes the least significant digit of the number",
      "Use your language’s mod operator to see if a number is a divisor of another."
    ]
  },
  {
    "title": "Difference Between Ones and Zeros in Row and Column",
    "description": "You are given a 0-indexed m x n binary matrix grid.\nA 0-indexed m x n difference matrix diff is created with the following procedure:\n\nLet the number of ones in the ith row be onesRowi.\nLet the number of ones in the jth column be onesColj.\nLet the number of zeros in the ith row be zerosRowi.\nLet the number of zeros in the jth column be zerosColj.\ndiff[i][j] = onesRowi + onesColj - zerosRowi - zerosColj\n\nReturn the difference matrix diff.\n \n",
    "examples": [
      {
        "input": "Input: grid = [[0,1,1],[1,0,1],[0,0,1]]",
        "output": "Output: [[0,0,4],[0,0,4],[-2,-2,2]]",
        "explanation": ""
      },
      {
        "input": "Input: grid = [[1,1,1],[1,1,1]]",
        "output": "Output: [[5,5,5],[5,5,5]]",
        "explanation": ""
      }
    ],
    "topics": [
      "Array",
      "Matrix",
      "Simulation"
    ],
    "difficulty": "Medium",
    "constraints": [
      "m == grid.length",
      "n == grid[i].length",
      "1 <= m, n <= 105",
      "1 <= m * n <= 105",
      "grid[i][j] is either 0 or 1."
    ],
    "hints": [
      "You need to reuse information about a row or a column many times. Try storing it to avoid computing it multiple times.",
      "Use an array to store the number of 1’s in each row and another array to store the number of 1’s in each column. Once you know the number of 1’s in each row or column, you can also easily calculate the number of 0’s."
    ]
  },
  {
    "title": "Count Anagrams",
    "description": "You are given a string s containing one or more words. Every consecutive pair of words is separated by a single space ' '.\nA string t is an anagram of string s if the ith word of t is a permutation of the ith word of s.\n\nFor example, \"acb dfe\" is an anagram of \"abc def\", but \"def cab\" and \"adc bef\" are not.\n\nReturn the number of distinct anagrams of s. Since the answer may be very large, return it modulo 109 + 7.\n \n",
    "examples": [
      {
        "input": "Input: s = \"too hot\"",
        "output": "Output: 18",
        "explanation": "Explanation: Some of the anagrams of the given string are \"too hot\", \"oot hot\", \"oto toh\", \"too toh\", and \"too oht\"."
      },
      {
        "input": "Input: s = \"aa\"",
        "output": "Output: 1",
        "explanation": "Explanation: There is only one anagram possible for the given string."
      }
    ],
    "topics": [
      "Hash Table",
      "Math",
      "String",
      "Combinatorics",
      "Counting"
    ],
    "difficulty": "Hard",
    "constraints": [
      "1 <= s.length <= 105",
      "s consists of lowercase English letters and spaces ' '.",
      "There is single space between consecutive words."
    ],
    "hints": [
      "For each word, can you count the number of permutations possible if all characters are distinct?",
      "How to reduce overcounting when letters are repeated?",
      "The product of the counts of distinct permutations of all words will give the final answer."
    ]
  },
  {
    "title": "Minimum Operations to Make Array Equal II",
    "description": "You are given two integer arrays nums1 and nums2 of equal length n and an integer k. You can perform the following operation on nums1:\n\nChoose two indexes i and j and increment nums1[i] by k and decrement nums1[j] by k. In other words, nums1[i] = nums1[i] + k and nums1[j] = nums1[j] - k.\n\nnums1 is said to be equal to nums2 if for all indices i such that 0 <= i < n, nums1[i] == nums2[i].\nReturn the minimum number of operations required to make nums1 equal to nums2. If it is impossible to make them equal, return -1.\n \n",
    "examples": [
      {
        "input": "Input: nums1 = [4,3,1,4], nums2 = [1,3,7,1], k = 3",
        "output": "Output: 2",
        "explanation": "Explanation: In 2 operations, we can transform nums1 to nums2."
      },
      {
        "input": "Input: nums1 = [3,8,5,2], nums2 = [2,4,1,6], k = 1",
        "output": "Output: -1",
        "explanation": "Explanation: It can be proved that it is impossible to make the two arrays equal."
      }
    ],
    "topics": [
      "Array",
      "Math",
      "Greedy"
    ],
    "difficulty": "Medium",
    "constraints": [
      "n == nums1.length == nums2.length",
      "2 <= n <= 105",
      "0 <= nums1[i], nums2[j] <= 109",
      "0 <= k <= 105"
    ],
    "hints": [
      "What are the cases for which we cannot make nums1 == nums2?",
      "For minimum moves, if nums1[i] < nums2[i], then we should never decrement nums1[i]. \nIf nums1[i] > nums2[i], then we should never increment nums1[i]."
    ]
  },
  {
    "title": "Reward Top K Students",
    "description": "You are given two string arrays positive_feedback and negative_feedback, containing the words denoting positive and negative feedback, respectively. Note that no word is both positive and negative.\nInitially every student has 0 points. Each positive word in a feedback report increases the points of a student by 3, whereas each negative word decreases the points by 1.\nYou are given n feedback reports, represented by a 0-indexed string array report and a 0-indexed integer array student_id, where student_id[i] represents the ID of the student who has received the feedback report report[i]. The ID of each student is unique.\nGiven an integer k, return the top k students after ranking them in non-increasing order by their points. In case more than one student has the same points, the one with the lower ID ranks higher.\n \n",
    "examples": [
      {
        "input": "Input: positive_feedback = [\"smart\",\"brilliant\",\"studious\"], negative_feedback = [\"not\"], report = [\"this student is studious\",\"the student is smart\"], student_id = [1,2], k = 2",
        "output": "Output: [1,2]",
        "explanation": "Explanation: "
      },
      {
        "input": "Input: positive_feedback = [\"smart\",\"brilliant\",\"studious\"], negative_feedback = [\"not\"], report = [\"this student is not studious\",\"the student is smart\"], student_id = [1,2], k = 2",
        "output": "Output: [2,1]",
        "explanation": "Explanation: "
      }
    ],
    "topics": [
      "Array",
      "Hash Table",
      "String",
      "Sorting",
      "Heap (Priority Queue)"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= positive_feedback.length, negative_feedback.length <= 104",
      "1 <= positive_feedback[i].length, negative_feedback[j].length <= 100",
      "Both positive_feedback[i] and negative_feedback[j] consists of lowercase English letters.",
      "No word is present in both positive_feedback and negative_feedback.",
      "n == report.length == student_id.length",
      "1 <= n <= 104",
      "report[i] consists of lowercase English letters and spaces ' '.",
      "There is a single space between consecutive words of report[i].",
      "1 <= report[i].length <= 100",
      "1 <= student_id[i] <= 109",
      "All the values of student_id[i] are unique.",
      "1 <= k <= n"
    ],
    "hints": [
      "Hash the positive and negative feedback words separately.",
      "Calculate the points for each student’s feedback.",
      "Sort the students accordingly to find the top k among them."
    ]
  },
  {
    "title": "Maximum Enemy Forts That Can Be Captured",
    "description": "You are given a 0-indexed integer array forts of length n representing the positions of several forts. forts[i] can be -1, 0, or 1 where:\n\n-1 represents there is no fort at the ith position.\n0 indicates there is an enemy fort at the ith position.\n1 indicates the fort at the ith the position is under your command.\n\nNow you have decided to move your army from one of your forts at position i to an empty position j such that:\n\n0 <= i, j <= n - 1\nThe army travels over enemy forts only. Formally, for all k where min(i,j) < k < max(i,j), forts[k] == 0.\n\nWhile moving the army, all the enemy forts that come in the way are captured.\nReturn the maximum number of enemy forts that can be captured. In case it is impossible to move your army, or you do not have any fort under your command, return 0.\n \n",
    "examples": [
      {
        "input": "Input: forts = [1,0,0,-1,0,0,0,0,1]",
        "output": "Output: 4",
        "explanation": ""
      },
      {
        "input": "Input: forts = [0,0,1,-1]",
        "output": "Output: 0",
        "explanation": "Explanation: Since no enemy fort can be captured, 0 is returned."
      }
    ],
    "topics": [
      "Array",
      "Two Pointers"
    ],
    "difficulty": "Easy",
    "constraints": [
      "1 <= forts.length <= 1000",
      "-1 <= forts[i] <= 1"
    ],
    "hints": [
      "For each fort under your command, check if you can move the army from here.",
      "If yes, find the closest empty positions satisfying all criteria.",
      "How can two-pointers be used to solve this problem optimally?"
    ]
  },
  {
    "title": "Number of Great Partitions",
    "description": "You are given an array nums consisting of positive integers and an integer k.\nPartition the array into two ordered groups such that each element is in exactly one group. A partition is called great if the sum of elements of each group is greater than or equal to k.\nReturn the number of distinct great partitions. Since the answer may be too large, return it modulo 109 + 7.\nTwo partitions are considered distinct if some element nums[i] is in different groups in the two partitions.\n \n",
    "examples": [
      {
        "input": "Input: nums = [1,2,3,4], k = 4",
        "output": "Output: 6",
        "explanation": "Explanation: The great partitions are: ([1,2,3], [4]), ([1,3], [2,4]), ([1,4], [2,3]), ([2,3], [1,4]), ([2,4], [1,3]) and ([4], [1,2,3])."
      },
      {
        "input": "Input: nums = [3,3,3], k = 4",
        "output": "Output: 0",
        "explanation": "Explanation: There are no great partitions for this array."
      },
      {
        "input": "Input: nums = [6,6], k = 2",
        "output": "Output: 2",
        "explanation": "Explanation: We can either put nums[0] in the first partition or in the second partition."
      }
    ],
    "topics": [
      "Array",
      "Dynamic Programming"
    ],
    "difficulty": "Hard",
    "constraints": [
      "1 <= nums.length, k <= 1000",
      "1 <= nums[i] <= 109"
    ],
    "hints": [
      "If the sum of the array is smaller than 2*k, then it is impossible to find a great partition.",
      "Solve the reverse problem, that is, find the number of partitions where the sum of elements of at least one of the two groups is smaller than k."
    ]
  },
  {
    "title": "Maximum Tastiness of Candy Basket",
    "description": "You are given an array of positive integers price where price[i] denotes the price of the ith candy and a positive integer k.\nThe store sells baskets of k distinct candies. The tastiness of a candy basket is the smallest absolute difference of the prices of any two candies in the basket.\nReturn the maximum tastiness of a candy basket.\n \n",
    "examples": [
      {
        "input": "Input: price = [13,5,1,8,21,2], k = 3",
        "output": "Output: 8",
        "explanation": "Explanation: Choose the candies with the prices [13,5,21]."
      },
      {
        "input": "Input: price = [1,3,1], k = 2",
        "output": "Output: 2",
        "explanation": "Explanation: Choose the candies with the prices [1,3]."
      },
      {
        "input": "Input: price = [7,7,7,7], k = 2",
        "output": "Output: 0",
        "explanation": "Explanation: Choosing any two distinct candies from the candies we have will result in a tastiness of 0."
      }
    ],
    "topics": [
      "Array",
      "Binary Search",
      "Sorting"
    ],
    "difficulty": "Medium",
    "constraints": [
      "2 <= k <= price.length <= 105",
      "1 <= price[i] <= 109"
    ],
    "hints": [
      "The answer is binary searchable.",
      "For some x, we can use a greedy strategy to check if it is possible to pick k distinct candies with tastiness being at least x.",
      "Sort prices and iterate from left to right. For some price[i] check if the price difference between the last taken candy and price[i] is at least x. If so, add the candy i to the basket.",
      "So, a candy basket with tastiness x can be achieved if the basket size is bigger than or equal to k."
    ]
  },
  {
    "title": "Take K of Each Character From Left and Right",
    "description": "You are given a string s consisting of the characters 'a', 'b', and 'c' and a non-negative integer k. Each minute, you may take either the leftmost character of s, or the rightmost character of s.\nReturn the minimum number of minutes needed for you to take at least k of each character, or return -1 if it is not possible to take k of each character.\n \n",
    "examples": [
      {
        "input": "Input: s = \"aabaaaacaabc\", k = 2",
        "output": "Output: 8",
        "explanation": "Explanation: "
      },
      {
        "input": "Input: s = \"a\", k = 1",
        "output": "Output: -1",
        "explanation": "Explanation: It is not possible to take one 'b' or 'c' so return -1."
      }
    ],
    "topics": [
      "Hash Table",
      "String",
      "Sliding Window"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= s.length <= 105",
      "s consists of only the letters 'a', 'b', and 'c'.",
      "0 <= k <= s.length"
    ],
    "hints": [
      "Start by counting the frequency of each character and checking if it is possible.",
      "If you take x characters from the left side, what is the minimum number of characters you need to take from the right side? Find this for all values of x in the range 0 ≤ x ≤ s.length.",
      "Use a two-pointers approach to avoid computing the same information multiple times."
    ]
  },
  {
    "title": "Shortest Distance to Target String in a Circular Array",
    "description": "You are given a 0-indexed circular string array words and a string target. A circular array means that the array's end connects to the array's beginning.\n\nFormally, the next element of words[i] is words[(i + 1) % n] and the previous element of words[i] is words[(i - 1 + n) % n], where n is the length of words.\n\nStarting from startIndex, you can move to either the next word or the previous word with 1 step at a time.\nReturn the shortest distance needed to reach the string target. If the string target does not exist in words, return -1.\n \n",
    "examples": [
      {
        "input": "Input: words = [\"hello\",\"i\",\"am\",\"leetcode\",\"hello\"], target = \"hello\", startIndex = 1",
        "output": "Output: 1",
        "explanation": "Explanation: We start from index 1 and can reach \"hello\" by"
      },
      {
        "input": "Input: words = [\"a\",\"b\",\"leetcode\"], target = \"leetcode\", startIndex = 0",
        "output": "Output: 1",
        "explanation": "Explanation: We start from index 0 and can reach \"leetcode\" by"
      },
      {
        "input": "Input: words = [\"i\",\"eat\",\"leetcode\"], target = \"ate\", startIndex = 0",
        "output": "Output: -1",
        "explanation": "Explanation: Since \"ate\" does not exist in words, we return -1."
      }
    ],
    "topics": [
      "Array",
      "String"
    ],
    "difficulty": "Easy",
    "constraints": [
      "1 <= words.length <= 100",
      "1 <= words[i].length <= 100",
      "words[i] and target consist of only lowercase English letters.",
      "0 <= startIndex < words.length"
    ],
    "hints": [
      "You have two options, either move straight to the left or move straight to the right.",
      "Find the first target word and record the distance.",
      "Choose the one with the minimum distance."
    ]
  },
  {
    "title": "Cycle Length Queries in a Tree",
    "description": "You are given an integer n. There is a complete binary tree with 2n - 1 nodes. The root of that tree is the node with the value 1, and every node with a value val in the range [1, 2n - 1 - 1] has two children where:\n\nThe left node has the value 2 * val, and\nThe right node has the value 2 * val + 1.\n\nYou are also given a 2D integer array queries of length m, where queries[i] = [ai, bi]. For each query, solve the following problem:\n\nAdd an edge between the nodes with values ai and bi.\nFind the length of the cycle in the graph.\nRemove the added edge between nodes with values ai and bi.\n\nNote that:\n\nA cycle is a path that starts and ends at the same node, and each edge in the path is visited only once.\nThe length of a cycle is the number of edges visited in the cycle.\nThere could be multiple edges between two nodes in the tree after adding the edge of the query.\n\nReturn an array answer of length m where answer[i] is the answer to the ith query.\n \n",
    "examples": [
      {
        "input": "Input: n = 3, queries = [[5,3],[4,7],[2,3]]",
        "output": "Output: [4,5,3]",
        "explanation": "Explanation: The diagrams above show the tree of 23 - 1 nodes. Nodes colored in red describe the nodes in the cycle after adding the edge."
      },
      {
        "input": "Input: n = 2, queries = [[1,2]]",
        "output": "Output: [2]",
        "explanation": "Explanation: The diagram above shows the tree of 22 - 1 nodes. Nodes colored in red describe the nodes in the cycle after adding the edge."
      }
    ],
    "topics": [
      "Tree",
      "Binary Tree"
    ],
    "difficulty": "Hard",
    "constraints": [
      "2 <= n <= 30",
      "m == queries.length",
      "1 <= m <= 105",
      "queries[i].length == 2",
      "1 <= ai, bi <= 2n - 1",
      "ai != bi"
    ],
    "hints": [
      "Find the distance between nodes “a” and “b”.",
      "distance(a, b) = depth(a) + depth(b) - 2 * LCA(a, b). Where depth(a) denotes depth from root to node “a” and LCA(a, b) denotes the lowest common ancestor of nodes “a” and “b”.",
      "To find LCA(a, b), iterate over all ancestors of node “a” and check if it is the ancestor of node “b” too. If so, take the one with maximum depth."
    ]
  },
  {
    "title": "Add Edges to Make Degrees of All Nodes Even",
    "description": "There is an undirected graph consisting of n nodes numbered from 1 to n. You are given the integer n and a 2D array edges where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi. The graph can be disconnected.\nYou can add at most two additional edges (possibly none) to this graph so that there are no repeated edges and no self-loops.\nReturn true if it is possible to make the degree of each node in the graph even, otherwise return false.\nThe degree of a node is the number of edges connected to it.\n \n",
    "examples": [
      {
        "input": "Input: n = 5, edges = [[1,2],[2,3],[3,4],[4,2],[1,4],[2,5]]",
        "output": "Output: true",
        "explanation": "Explanation: The above diagram shows a valid way of adding an edge."
      },
      {
        "input": "Input: n = 4, edges = [[1,2],[3,4]]",
        "output": "Output: true",
        "explanation": "Explanation: The above diagram shows a valid way of adding two edges."
      },
      {
        "input": "Input: n = 4, edges = [[1,2],[1,3],[1,4]]",
        "output": "Output: false",
        "explanation": "Explanation: It is not possible to obtain a valid graph with adding at most 2 edges."
      }
    ],
    "topics": [
      "Hash Table",
      "Graph"
    ],
    "difficulty": "Hard",
    "constraints": [
      "3 <= n <= 105",
      "2 <= edges.length <= 105",
      "edges[i].length == 2",
      "1 <= ai, bi <= n",
      "ai != bi",
      "There are no repeated edges."
    ],
    "hints": [
      "Notice that each edge that we add changes the degree of exactly 2 nodes.",
      "The number of nodes with an odd degree in the original graph should be either 0, 2, or 4. Try to work on each of these cases."
    ]
  },
  {
    "title": "Smallest Value After Replacing With Sum of Prime Factors",
    "description": "You are given a positive integer n.\nContinuously replace n with the sum of its prime factors.\n\nNote that if a prime factor divides n multiple times, it should be included in the sum as many times as it divides n.\n\nReturn the smallest value n will take on.\n \n",
    "examples": [
      {
        "input": "Input: n = 15",
        "output": "Output: 5",
        "explanation": "Explanation: Initially, n = 15."
      },
      {
        "input": "Input: n = 3",
        "output": "Output: 3",
        "explanation": "Explanation: Initially, n = 3."
      }
    ],
    "topics": [
      "Math",
      "Number Theory"
    ],
    "difficulty": "Medium",
    "constraints": [
      "2 <= n <= 105"
    ],
    "hints": [
      "Every time you replace n, it will become smaller until it is a prime number, where it will keep the same value each time you replace it.",
      "n decreases logarithmically, allowing you to simulate the process.",
      "To find the prime factors, iterate through all numbers less than n from least to greatest and find the maximum number of times each number divides n."
    ]
  },
  {
    "title": "Count Pairs Of Similar Strings",
    "description": "You are given a 0-indexed string array words.\nTwo strings are similar if they consist of the same characters.\n\nFor example, \"abca\" and \"cba\" are similar since both consist of characters 'a', 'b', and 'c'.\nHowever, \"abacba\" and \"bcfd\" are not similar since they do not consist of the same characters.\n\nReturn the number of pairs (i, j) such that 0 <= i < j <= word.length - 1 and the two strings words[i] and words[j] are similar.\n \n",
    "examples": [
      {
        "input": "Input: words = [\"aba\",\"aabb\",\"abcd\",\"bac\",\"aabc\"]",
        "output": "Output: 2",
        "explanation": "Explanation: There are 2 pairs that satisfy the conditions:"
      },
      {
        "input": "Input: words = [\"aabb\",\"ab\",\"ba\"]",
        "output": "Output: 3",
        "explanation": "Explanation: There are 3 pairs that satisfy the conditions:"
      },
      {
        "input": "Input: words = [\"nba\",\"cba\",\"dba\"]",
        "output": "Output: 0",
        "explanation": "Explanation: Since there does not exist any pair that satisfies the conditions, we return 0."
      }
    ],
    "topics": [
      "Array",
      "Hash Table",
      "String"
    ],
    "difficulty": "Easy",
    "constraints": [
      "1 <= words.length <= 100",
      "1 <= words[i].length <= 100",
      "words[i] consist of only lowercase English letters."
    ],
    "hints": [
      "How can you check if two strings are similar?",
      "Use a hashSet to store the character of each string."
    ]
  },
  {
    "title": "Minimum Total Cost to Make Arrays Unequal",
    "description": "You are given two 0-indexed integer arrays nums1 and nums2, of equal length n.\nIn one operation, you can swap the values of any two indices of nums1. The cost of this operation is the sum of the indices.\nFind the minimum total cost of performing the given operation any number of times such that nums1[i] != nums2[i] for all 0 <= i <= n - 1 after performing all the operations.\nReturn the minimum total cost such that nums1 and nums2 satisfy the above condition. In case it is not possible, return -1.\n \n",
    "examples": [
      {
        "input": "Input: nums1 = [1,2,3,4,5], nums2 = [1,2,3,4,5]",
        "output": "Output: 10",
        "explanation": "Explanation: "
      },
      {
        "input": "Input: nums1 = [2,2,2,1,3], nums2 = [1,2,2,3,3]",
        "output": "Output: 10",
        "explanation": "Explanation: "
      },
      {
        "input": "Input: nums1 = [1,2,2], nums2 = [1,2,2]",
        "output": "Output: -1",
        "explanation": "Explanation: "
      }
    ],
    "topics": [
      "Array",
      "Hash Table",
      "Greedy",
      "Counting"
    ],
    "difficulty": "Hard",
    "constraints": [
      "n == nums1.length == nums2.length",
      "1 <= n <= 105",
      "1 <= nums1[i], nums2[i] <= n"
    ],
    "hints": [
      "How can we check which indices of nums1 will be considered for swapping? How to minimize the number of such operations?",
      "It can be seen that greedily swapping values of indices where nums1[i] == nums2[i] is the most optimal choice. How many values cannot be swapped this way?",
      "Find which indices we will swap these remaining values with, and if there are enough such indices."
    ]
  },
  {
    "title": "Frog Jump II",
    "description": "You are given a 0-indexed integer array stones sorted in strictly increasing order representing the positions of stones in a river.\nA frog, initially on the first stone, wants to travel to the last stone and then return to the first stone. However, it can jump to any stone at most once.\nThe length of a jump is the absolute difference between the position of the stone the frog is currently on and the position of the stone to which the frog jumps.\n\nMore formally, if the frog is at stones[i] and is jumping to stones[j], the length of the jump is |stones[i] - stones[j]|.\n\nThe cost of a path is the maximum length of a jump among all jumps in the path.\nReturn the minimum cost of a path for the frog.\n \n",
    "examples": [
      {
        "input": "Input: stones = [0,2,5,6,7]",
        "output": "Output: 5",
        "explanation": "Explanation: The above figure represents one of the optimal paths the frog can take."
      },
      {
        "input": "Input: stones = [0,3,9]",
        "output": "Output: 9",
        "explanation": "Explanation: "
      }
    ],
    "topics": [
      "Array",
      "Binary Search",
      "Greedy"
    ],
    "difficulty": "Medium",
    "constraints": [
      "2 <= stones.length <= 105",
      "0 <= stones[i] <= 109",
      "stones[0] == 0",
      "stones is sorted in a strictly increasing order."
    ],
    "hints": [
      "One of the optimal strategies will be to jump to every stone.",
      "Skipping just one stone in every forward jump and jumping to those skipped stones in backward jump can minimize the maximum jump."
    ]
  },
  {
    "title": "Maximum Star Sum of a Graph",
    "description": "There is an undirected graph consisting of n nodes numbered from 0 to n - 1. You are given a 0-indexed integer array vals of length n where vals[i] denotes the value of the ith node.\nYou are also given a 2D integer array edges where edges[i] = [ai, bi] denotes that there exists an undirected edge connecting nodes ai and bi.\nA star graph is a subgraph of the given graph having a center node containing 0 or more neighbors. In other words, it is a subset of edges of the given graph such that there exists a common node for all edges.\nThe image below shows star graphs with 3 and 4 neighbors respectively, centered at the blue node.\n\nThe star sum is the sum of the values of all the nodes present in the star graph.\nGiven an integer k, return the maximum star sum of a star graph containing at most k edges.\n \n",
    "examples": [
      {
        "input": "Input: vals = [1,2,3,4,10,-10,-20], edges = [[0,1],[1,2],[1,3],[3,4],[3,5],[3,6]], k = 2",
        "output": "Output: 16",
        "explanation": "Explanation: The above diagram represents the input graph."
      },
      {
        "input": "Input: vals = [-5], edges = [], k = 0",
        "output": "Output: -5",
        "explanation": "Explanation: There is only one possible star graph, which is node 0 itself."
      }
    ],
    "topics": [
      "Array",
      "Greedy",
      "Graph",
      "Sorting",
      "Heap (Priority Queue)"
    ],
    "difficulty": "Medium",
    "constraints": [
      "n == vals.length",
      "1 <= n <= 105",
      "-104 <= vals[i] <= 104",
      "0 <= edges.length <= min(n * (n - 1) / 2, 105)",
      "edges[i].length == 2",
      "0 <= ai, bi <= n - 1",
      "ai != bi",
      "0 <= k <= n - 1"
    ],
    "hints": [
      "A star graph doesn’t necessarily include all of its neighbors.",
      "For each node, sort its neighbors in descending order and take k max valued neighbors."
    ]
  },
  {
    "title": "Maximum Value of a String in an Array",
    "description": "The value of an alphanumeric string can be defined as:\n\nThe numeric representation of the string in base 10, if it comprises of digits only.\nThe length of the string, otherwise.\n\nGiven an array strs of alphanumeric strings, return the maximum value of any string in strs.\n \n",
    "examples": [
      {
        "input": "Input: strs = [\"alic3\",\"bob\",\"3\",\"4\",\"00000\"]",
        "output": "Output: 5",
        "explanation": "Explanation: "
      },
      {
        "input": "Input: strs = [\"1\",\"01\",\"001\",\"0001\"]",
        "output": "Output: 1",
        "explanation": "Explanation: "
      }
    ],
    "topics": [
      "Array",
      "String"
    ],
    "difficulty": "Easy",
    "constraints": [
      "1 <= strs.length <= 100",
      "1 <= strs[i].length <= 9",
      "strs[i] consists of only lowercase English letters and digits."
    ],
    "hints": [
      "For strings comprising only of digits, convert them into integers.",
      "For all other strings, calculate their length."
    ]
  },
  {
    "title": "Maximum Number of Points From Grid Queries",
    "description": "You are given an m x n integer matrix grid and an array queries of size k.\nFind an array answer of size k such that for each integer queries[i] you start in the top left cell of the matrix and repeat the following process:\n\nIf queries[i] is strictly greater than the value of the current cell that you are in, then you get one point if it is your first time visiting this cell, and you can move to any adjacent cell in all 4 directions: up, down, left, and right.\nOtherwise, you do not get any points, and you end this process.\n\nAfter the process, answer[i] is the maximum number of points you can get. Note that for each query you are allowed to visit the same cell multiple times.\nReturn the resulting array answer.\n \n",
    "examples": [
      {
        "input": "Input: grid = [[1,2,3],[2,5,7],[3,5,1]], queries = [5,6,2]",
        "output": "Output: [5,8,1]",
        "explanation": "Explanation: The diagrams above show which cells we visit to get points for each query."
      },
      {
        "input": "Input: grid = [[5,2,1],[1,1,2]], queries = [3]",
        "output": "Output: [0]",
        "explanation": "Explanation: We can not get any points because the value of the top left cell is already greater than or equal to 3."
      }
    ],
    "topics": [
      "Array",
      "Breadth-First Search",
      "Union Find",
      "Sorting",
      "Heap (Priority Queue)"
    ],
    "difficulty": "Hard",
    "constraints": [
      "m == grid.length",
      "n == grid[i].length",
      "2 <= m, n <= 1000",
      "4 <= m * n <= 105",
      "k == queries.length",
      "1 <= k <= 104",
      "1 <= grid[i][j], queries[i] <= 106"
    ],
    "hints": [
      "The queries are all given to you beforehand so you can answer them in any order you want.",
      "Sort the queries knowing their original order to be able to build the answer array.",
      "Run a BFS on the graph and answer the queries in increasing order."
    ]
  },
  {
    "title": "Design Memory Allocator",
    "description": "You are given an integer n representing the size of a 0-indexed memory array. All memory units are initially free.\nYou have a memory allocator with the following functionalities:\n\nAllocate a block of size consecutive free memory units and assign it the id mID.\nFree all memory units with the given id mID.\n\nNote that:\n\nMultiple blocks can be allocated to the same mID.\nYou should free all the memory units with mID, even if they were allocated in different blocks.\n\nImplement the Allocator class:\n\nAllocator(int n) Initializes an Allocator object with a memory array of size n.\nint allocate(int size, int mID) Find the leftmost block of size consecutive free memory units and allocate it with the id mID. Return the block's first index. If such a block does not exist, return -1.\nint free(int mID) Free all memory units with the id mID. Return the number of memory units you have freed.\n\n \n",
    "examples": [
      {
        "input": "Input\n[\"Allocator\", \"allocate\", \"allocate\", \"allocate\", \"free\", \"allocate\", \"allocate\", \"allocate\", \"free\", \"allocate\", \"free\"]",
        "output": "Output\n[null, 0, 1, 2, 1, 3, 1, 6, 3, -1, 0]",
        "explanation": "Explanation\nAllocator loc = new Allocator(10); // Initialize a memory array of size 10. All memory units are initially free."
      }
    ],
    "topics": [
      "Array",
      "Hash Table",
      "Design",
      "Simulation"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= n, size, mID <= 1000",
      "At most 1000 calls will be made to allocate and free."
    ],
    "hints": [
      "Can you simulate the process?",
      "Use brute force to find the leftmost free block and free each occupied memory unit"
    ]
  },
  {
    "title": "Longest Square Streak in an Array",
    "description": "You are given an integer array nums. A subsequence of nums is called a square streak if:\n\nThe length of the subsequence is at least 2, and\nafter sorting the subsequence, each element (except the first element) is the square of the previous number.\n\nReturn the length of the longest square streak in nums, or return -1 if there is no square streak.\nA subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.\n \n",
    "examples": [
      {
        "input": "Input: nums = [4,3,6,16,8,2]",
        "output": "Output: 3",
        "explanation": "Explanation: Choose the subsequence [4,16,2]. After sorting it, it becomes [2,4,16]."
      },
      {
        "input": "Input: nums = [2,3,5,6,7]",
        "output": "Output: -1",
        "explanation": "Explanation: There is no square streak in nums so return -1."
      }
    ],
    "topics": [
      "Array",
      "Hash Table",
      "Binary Search",
      "Dynamic Programming",
      "Sorting"
    ],
    "difficulty": "Medium",
    "constraints": [
      "2 <= nums.length <= 105",
      "2 <= nums[i] <= 105"
    ],
    "hints": [
      "With the constraints, the length of the longest square streak possible is 5.",
      "Store the elements of nums in a set to quickly check if it exists."
    ]
  },
  {
    "title": "Delete Greatest Value in Each Row",
    "description": "You are given an m x n matrix grid consisting of positive integers.\nPerform the following operation until grid becomes empty:\n\nDelete the element with the greatest value from each row. If multiple such elements exist, delete any of them.\nAdd the maximum of deleted elements to the answer.\n\nNote that the number of columns decreases by one after each operation.\nReturn the answer after performing the operations described above.\n \n",
    "examples": [
      {
        "input": "Input: grid = [[1,2,4],[3,3,1]]",
        "output": "Output: 8",
        "explanation": "Explanation: The diagram above shows the removed values in each step."
      },
      {
        "input": "Input: grid = [[10]]",
        "output": "Output: 10",
        "explanation": "Explanation: The diagram above shows the removed values in each step."
      }
    ],
    "topics": [
      "Array",
      "Sorting",
      "Matrix"
    ],
    "difficulty": "Easy",
    "constraints": [
      "m == grid.length",
      "n == grid[i].length",
      "1 <= m, n <= 50",
      "1 <= grid[i][j] <= 100"
    ],
    "hints": [
      "Iterate from the first to the last row and if there exist some unmarked cells, take a maximum from them and mark that cell as visited.",
      "Add a maximum of newly marked cells to answer and repeat that operation until the whole matrix becomes marked."
    ]
  },
  {
    "title": "Divide Nodes Into the Maximum Number of Groups",
    "description": "You are given a positive integer n representing the number of nodes in an undirected graph. The nodes are labeled from 1 to n.\nYou are also given a 2D integer array edges, where edges[i] = [ai, bi] indicates that there is a bidirectional edge between nodes ai and bi. Notice that the given graph may be disconnected.\nDivide the nodes of the graph into m groups (1-indexed) such that:\n\nEach node in the graph belongs to exactly one group.\nFor every pair of nodes in the graph that are connected by an edge [ai, bi], if ai belongs to the group with index x, and bi belongs to the group with index y, then |y - x| = 1.\n\nReturn the maximum number of groups (i.e., maximum m) into which you can divide the nodes. Return -1 if it is impossible to group the nodes with the given conditions.\n \n",
    "examples": [
      {
        "input": "Input: n = 6, edges = [[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]]",
        "output": "Output: 4",
        "explanation": "Explanation: As shown in the image we:"
      },
      {
        "input": "Input: n = 3, edges = [[1,2],[2,3],[3,1]]",
        "output": "Output: -1",
        "explanation": "Explanation: If we add node 1 to the first group, node 2 to the second group, and node 3 to the third group to satisfy the first two edges, we can see that the third edge will not be satisfied."
      }
    ],
    "topics": [
      "Breadth-First Search",
      "Union Find",
      "Graph"
    ],
    "difficulty": "Hard",
    "constraints": [
      "1 <= n <= 500",
      "1 <= edges.length <= 104",
      "edges[i].length == 2",
      "1 <= ai, bi <= n",
      "ai != bi",
      "There is at most one edge between any pair of vertices."
    ],
    "hints": [
      "If the graph is not bipartite, it is not possible to group the nodes.",
      "Notice that we can solve the problem for each connected component independently, and the final answer will be just the sum of the maximum number of groups in each component.",
      "Finally, to solve the problem for each connected component, we can notice that if for some node v we fix its position to be in the leftmost group, then we can also evaluate the position of every other node. That position is the depth of the node in a bfs tree after rooting at node v."
    ]
  },
  {
    "title": "Minimum Score of a Path Between Two Cities",
    "description": "You are given a positive integer n representing n cities numbered from 1 to n. You are also given a 2D array roads where roads[i] = [ai, bi, distancei] indicates that there is a bidirectional road between cities ai and bi with a distance equal to distancei. The cities graph is not necessarily connected.\nThe score of a path between two cities is defined as the minimum distance of a road in this path.\nReturn the minimum possible score of a path between cities 1 and n.\nNote:\n\nA path is a sequence of roads between two cities.\nIt is allowed for a path to contain the same road multiple times, and you can visit cities 1 and n multiple times along the path.\nThe test cases are generated such that there is at least one path between 1 and n.\n\n \n",
    "examples": [
      {
        "input": "Input: n = 4, roads = [[1,2,9],[2,3,6],[2,4,5],[1,4,7]]",
        "output": "Output: 5",
        "explanation": "Explanation: The path from city 1 to 4 with the minimum score is: 1 -> 2 -> 4. The score of this path is min(9,5) = 5."
      },
      {
        "input": "Input: n = 4, roads = [[1,2,2],[1,3,4],[3,4,7]]",
        "output": "Output: 2",
        "explanation": "Explanation: The path from city 1 to 4 with the minimum score is: 1 -> 2 -> 1 -> 3 -> 4. The score of this path is min(2,2,4,7) = 2."
      }
    ],
    "topics": [
      "Depth-First Search",
      "Breadth-First Search",
      "Union Find",
      "Graph"
    ],
    "difficulty": "Medium",
    "constraints": [
      "2 <= n <= 105",
      "1 <= roads.length <= 105",
      "roads[i].length == 3",
      "1 <= ai, bi <= n",
      "ai != bi",
      "1 <= distancei <= 104",
      "There are no repeated edges.",
      "There is at least one path between 1 and n."
    ],
    "hints": [
      "Can you solve the problem if the whole graph is connected?",
      "Notice that if the graph is connected, you can always use any edge of the graph in your path.",
      "How to solve the general problem in a similar way? Remove all the nodes that are not connected to 1 and n, then apply the previous solution in the new graph."
    ]
  },
  {
    "title": "Divide Players Into Teams of Equal Skill",
    "description": "You are given a positive integer array skill of even length n where skill[i] denotes the skill of the ith player. Divide the players into n / 2 teams of size 2 such that the total skill of each team is equal.\nThe chemistry of a team is equal to the product of the skills of the players on that team.\nReturn the sum of the chemistry of all the teams, or return -1 if there is no way to divide the players into teams such that the total skill of each team is equal.\n \n",
    "examples": [
      {
        "input": "Input: skill = [3,2,5,1,3,4]",
        "output": "Output: 22",
        "explanation": "Explanation: "
      },
      {
        "input": "Input: skill = [3,4]",
        "output": "Output: 12",
        "explanation": "Explanation: "
      },
      {
        "input": "Input: skill = [1,1,2,3]",
        "output": "Output: -1",
        "explanation": "Explanation: "
      }
    ],
    "topics": [
      "Array",
      "Hash Table",
      "Two Pointers",
      "Sorting"
    ],
    "difficulty": "Medium",
    "constraints": [
      "2 <= skill.length <= 105",
      "skill.length is even.",
      "1 <= skill[i] <= 1000"
    ],
    "hints": [
      "Try sorting the skill array.",
      "It is always optimal to pair the weakest available player with the strongest available player."
    ]
  },
  {
    "title": "Circular Sentence",
    "description": "A sentence is a list of words that are separated by a single space with no leading or trailing spaces.\n\nFor example, \"Hello World\", \"HELLO\", \"hello world hello world\" are all sentences.\n\nWords consist of only uppercase and lowercase English letters. Uppercase and lowercase English letters are considered different.\nA sentence is circular if:\n\nThe last character of a word is equal to the first character of the next word.\nThe last character of the last word is equal to the first character of the first word.\n\nFor example, \"leetcode exercises sound delightful\", \"eetcode\", \"leetcode eats soul\" are all circular sentences. However, \"Leetcode is cool\", \"happy Leetcode\", \"Leetcode\" and \"I like Leetcode\" are not circular sentences.\nGiven a string sentence, return true if it is circular. Otherwise, return false.\n \n",
    "examples": [
      {
        "input": "Input: sentence = \"leetcode exercises sound delightful\"",
        "output": "Output: true",
        "explanation": "Explanation: The words in sentence are [\"leetcode\", \"exercises\", \"sound\", \"delightful\"]."
      },
      {
        "input": "Input: sentence = \"eetcode\"",
        "output": "Output: true",
        "explanation": "Explanation: The words in sentence are [\"eetcode\"]."
      },
      {
        "input": "Input: sentence = \"Leetcode is cool\"",
        "output": "Output: false",
        "explanation": "Explanation: The words in sentence are [\"Leetcode\", \"is\", \"cool\"]."
      }
    ],
    "topics": [
      "String"
    ],
    "difficulty": "Easy",
    "constraints": [
      "1 <= sentence.length <= 500",
      "sentence consist of only lowercase and uppercase English letters and spaces.",
      "The words in sentence are separated by a single space.",
      "There are no leading or trailing spaces."
    ],
    "hints": [
      "Check the character before the empty space and the character after the empty space.",
      "Check the first character and the last character of the sentence."
    ]
  },
  {
    "title": "Count Palindromic Subsequences",
    "description": "Given a string of digits s, return the number of palindromic subsequences of s having length 5. Since the answer may be very large, return it modulo 109 + 7.\nNote:\n\nA string is palindromic if it reads the same forward and backward.\nA subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.\n\n \n",
    "examples": [
      {
        "input": "Input: s = \"103301\"",
        "output": "Output: 2",
        "explanation": "Explanation: "
      },
      {
        "input": "Input: s = \"0000000\"",
        "output": "Output: 21",
        "explanation": "Explanation: All 21 subsequences are \"00000\", which is palindromic."
      },
      {
        "input": "Input: s = \"9999900000\"",
        "output": "Output: 2",
        "explanation": "Explanation: The only two palindromic subsequences are \"99999\" and \"00000\"."
      }
    ],
    "topics": [
      "String",
      "Dynamic Programming"
    ],
    "difficulty": "Hard",
    "constraints": [
      "1 <= s.length <= 104",
      "s consists of digits."
    ],
    "hints": [
      "There are 100 possibilities for the first two characters of the palindrome.",
      "Iterate over all characters, letting the current character be the center of the palindrome."
    ]
  },
  {
    "title": "Minimum Penalty for a Shop",
    "description": "You are given the customer visit log of a shop represented by a 0-indexed string customers consisting only of characters 'N' and 'Y':\n\nif the ith character is 'Y', it means that customers come at the ith hour\nwhereas 'N' indicates that no customers come at the ith hour.\n\nIf the shop closes at the jth hour (0 <= j <= n), the penalty is calculated as follows:\n\nFor every hour when the shop is open and no customers come, the penalty increases by 1.\nFor every hour when the shop is closed and customers come, the penalty increases by 1.\n\nReturn the earliest hour at which the shop must be closed to incur a minimum penalty.\nNote that if a shop closes at the jth hour, it means the shop is closed at the hour j.\n \n",
    "examples": [
      {
        "input": "Input: customers = \"YYNY\"",
        "output": "Output: 2",
        "explanation": "Explanation: "
      },
      {
        "input": "Input: customers = \"NNNNN\"",
        "output": "Output: 0",
        "explanation": "Explanation: It is best to close the shop at the 0th hour as no customers arrive."
      },
      {
        "input": "Input: customers = \"YYYY\"",
        "output": "Output: 4",
        "explanation": "Explanation: It is best to close the shop at the 4th hour as customers arrive at each hour."
      }
    ],
    "topics": [
      "String",
      "Prefix Sum"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= customers.length <= 105",
      "customers consists only of characters 'Y' and 'N'."
    ],
    "hints": [
      "At any index, the penalty is the sum of prefix count of ‘N’ and suffix count of ‘Y’.",
      "Enumerate all indices and find the minimum such value."
    ]
  },
  {
    "title": "Minimum Cuts to Divide a Circle",
    "description": "A valid cut in a circle can be:\n\nA cut that is represented by a straight line that touches two points on the edge of the circle and passes through its center, or\nA cut that is represented by a straight line that touches one point on the edge of the circle and its center.\n\nSome valid and invalid cuts are shown in the figures below.\n\nGiven the integer n, return the minimum number of cuts needed to divide a circle into n equal slices.\n \n",
    "examples": [
      {
        "input": "Input: n = 4",
        "output": "Output: 2",
        "explanation": "Explanation: "
      },
      {
        "input": "Input: n = 3",
        "output": "Output: 3",
        "explanation": ""
      }
    ],
    "topics": [
      "Math",
      "Geometry"
    ],
    "difficulty": "Easy",
    "constraints": [
      "1 <= n <= 100"
    ],
    "hints": [
      "Think about odd and even values separately.",
      "When will we not have to cut the circle at all?"
    ]
  },
  {
    "title": "Count Subarrays With Median K",
    "description": "You are given an array nums of size n consisting of distinct integers from 1 to n and a positive integer k.\nReturn the number of non-empty subarrays in nums that have a median equal to k.\nNote:\n\nThe median of an array is the middle element after sorting the array in ascending order. If the array is of even length, the median is the left middle element.\n\n\t\nFor example, the median of [2,3,1,4] is 2, and the median of [8,4,3,5,1] is 4.\n\n\nA subarray is a contiguous part of an array.\n\n \n",
    "examples": [
      {
        "input": "Input: nums = [3,2,1,4,5], k = 4",
        "output": "Output: 3",
        "explanation": "Explanation: The subarrays that have a median equal to 4 are: [4], [4,5] and [1,4,5]."
      },
      {
        "input": "Input: nums = [2,3,1], k = 3",
        "output": "Output: 1",
        "explanation": "Explanation: [3] is the only subarray that has a median equal to 3."
      }
    ],
    "topics": [
      "Array",
      "Hash Table",
      "Prefix Sum"
    ],
    "difficulty": "Hard",
    "constraints": [
      "n == nums.length",
      "1 <= n <= 105",
      "1 <= nums[i], k <= n",
      "The integers in nums are distinct."
    ],
    "hints": [
      "Consider changing the numbers that are strictly greater than k in the array to 1, the numbers that are strictly smaller than k to -1, and k to 0.",
      "After the change, what property does a subarray with median k have in the new array?",
      "An array with median k should have a sum equal to either 0 or 1 in the new array and should contain the element k. How do you count such subarrays?"
    ]
  },
  {
    "title": "Remove Nodes From Linked List",
    "description": "You are given the head of a linked list.\nRemove every node which has a node with a strictly greater value anywhere to the right side of it.\nReturn the head of the modified linked list.\n \n",
    "examples": [
      {
        "input": "Input: head = [5,2,13,3,8]",
        "output": "Output: [13,8]",
        "explanation": "Explanation: The nodes that should be removed are 5, 2 and 3."
      },
      {
        "input": "Input: head = [1,1,1,1]",
        "output": "Output: [1,1,1,1]",
        "explanation": "Explanation: Every node has value 1, so no nodes are removed."
      }
    ],
    "topics": [
      "Linked List",
      "Stack",
      "Recursion",
      "Monotonic Stack"
    ],
    "difficulty": "Medium",
    "constraints": [
      "The number of the nodes in the given list is in the range [1, 105].",
      "1 <= Node.val <= 105"
    ],
    "hints": [
      "Iterate on nodes in reversed order.",
      "When iterating in reversed order, save the maximum value that was passed before."
    ]
  },
  {
    "title": "Append Characters to String to Make Subsequence",
    "description": "You are given two strings s and t consisting of only lowercase English letters.\nReturn the minimum number of characters that need to be appended to the end of s so that t becomes a subsequence of s.\nA subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.\n \n",
    "examples": [
      {
        "input": "Input: s = \"coaching\", t = \"coding\"",
        "output": "Output: 4",
        "explanation": "Explanation: Append the characters \"ding\" to the end of s so that s = \"coachingding\"."
      },
      {
        "input": "Input: s = \"abcde\", t = \"a\"",
        "output": "Output: 0",
        "explanation": "Explanation: t is already a subsequence of s (\"abcde\")."
      },
      {
        "input": "Input: s = \"z\", t = \"abcde\"",
        "output": "Output: 5",
        "explanation": "Explanation: Append the characters \"abcde\" to the end of s so that s = \"zabcde\"."
      }
    ],
    "topics": [
      "Two Pointers",
      "String",
      "Greedy"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= s.length, t.length <= 105",
      "s and t consist only of lowercase English letters."
    ],
    "hints": [
      "Find the longest prefix of t that is a subsequence of s.",
      "Use two variables to keep track of your location in s and t. If the characters match, increment both variables. Otherwise, only increment the variable for s.",
      "The remaining characters in t must be appended to the end of s."
    ]
  },
  {
    "title": "Find the Pivot Integer",
    "description": "Given a positive integer n, find the pivot integer x such that:\n\nThe sum of all elements between 1 and x inclusively equals the sum of all elements between x and n inclusively.\n\nReturn the pivot integer x. If no such integer exists, return -1. It is guaranteed that there will be at most one pivot index for the given input.\n \n",
    "examples": [
      {
        "input": "Input: n = 8",
        "output": "Output: 6",
        "explanation": "Explanation: 6 is the pivot integer since: 1 + 2 + 3 + 4 + 5 + 6 = 6 + 7 + 8 = 21."
      },
      {
        "input": "Input: n = 1",
        "output": "Output: 1",
        "explanation": "Explanation: 1 is the pivot integer since: 1 = 1."
      },
      {
        "input": "Input: n = 4",
        "output": "Output: -1",
        "explanation": "Explanation: It can be proved that no such integer exist."
      }
    ],
    "topics": [
      "Math",
      "Prefix Sum"
    ],
    "difficulty": "Easy",
    "constraints": [
      "1 <= n <= 1000"
    ],
    "hints": [
      "Can you use brute force to check every number from 1 to n if any of them is the pivot integer?",
      "If you know the sum of [1: pivot], how can you efficiently calculate the sum of the other parts?"
    ]
  },
  {
    "title": "Number of Beautiful Partitions",
    "description": "You are given a string s that consists of the digits '1' to '9' and two integers k and minLength.\nA partition of s is called beautiful if:\n\ns is partitioned into k non-intersecting substrings.\nEach substring has a length of at least minLength.\nEach substring starts with a prime digit and ends with a non-prime digit. Prime digits are '2', '3', '5', and '7', and the rest of the digits are non-prime.\n\nReturn the number of beautiful partitions of s. Since the answer may be very large, return it modulo 109 + 7.\nA substring is a contiguous sequence of characters within a string.\n \n",
    "examples": [
      {
        "input": "Input: s = \"23542185131\", k = 3, minLength = 2",
        "output": "Output: 3",
        "explanation": "Explanation: There exists three ways to create a beautiful partition:"
      },
      {
        "input": "Input: s = \"23542185131\", k = 3, minLength = 3",
        "output": "Output: 1",
        "explanation": "Explanation: There exists one way to create a beautiful partition: \"2354 | 218 | 5131\"."
      },
      {
        "input": "Input: s = \"3312958\", k = 3, minLength = 1",
        "output": "Output: 1",
        "explanation": "Explanation: There exists one way to create a beautiful partition: \"331 | 29 | 58\"."
      }
    ],
    "topics": [
      "String",
      "Dynamic Programming"
    ],
    "difficulty": "Hard",
    "constraints": [
      "1 <= k, minLength <= s.length <= 1000",
      "s consists of the digits '1' to '9'."
    ],
    "hints": [
      "Try using a greedy approach where you take as many digits as possible from the left of the string for each partition.",
      "You can also use a dynamic programming approach, let an array dp where dp[i] is the solution of the problem for the prefix of the string ending at index i, the answer of the problem will be dp[n-1]. What are the transitions of this dp?"
    ]
  },
  {
    "title": "Minimum Fuel Cost to Report to the Capital",
    "description": "There is a tree (i.e., a connected, undirected graph with no cycles) structure country network consisting of n cities numbered from 0 to n - 1 and exactly n - 1 roads. The capital city is city 0. You are given a 2D integer array roads where roads[i] = [ai, bi] denotes that there exists a bidirectional road connecting cities ai and bi.\nThere is a meeting for the representatives of each city. The meeting is in the capital city.\nThere is a car in each city. You are given an integer seats that indicates the number of seats in each car.\nA representative can use the car in their city to travel or change the car and ride with another representative. The cost of traveling between two cities is one liter of fuel.\nReturn the minimum number of liters of fuel to reach the capital city.\n \n",
    "examples": [
      {
        "input": "Input: roads = [[0,1],[0,2],[0,3]], seats = 5",
        "output": "Output: 3",
        "explanation": "Explanation: "
      },
      {
        "input": "Input: roads = [[3,1],[3,2],[1,0],[0,4],[0,5],[4,6]], seats = 2",
        "output": "Output: 7",
        "explanation": "Explanation: "
      },
      {
        "input": "Input: roads = [], seats = 1",
        "output": "Output: 0",
        "explanation": "Explanation: No representatives need to travel to the capital city."
      }
    ],
    "topics": [
      "Tree",
      "Depth-First Search",
      "Breadth-First Search",
      "Graph"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= n <= 105",
      "roads.length == n - 1",
      "roads[i].length == 2",
      "0 <= ai, bi < n",
      "ai != bi",
      "roads represents a valid tree.",
      "1 <= seats <= 105"
    ],
    "hints": [
      "Can you record the size of each subtree?",
      "If n people meet on the same node, what is the minimum number of cars needed?"
    ]
  },
  {
    "title": "Closest Nodes Queries in a Binary Search Tree",
    "description": "You are given the root of a binary search tree and an array queries of size n consisting of positive integers.\nFind a 2D array answer of size n where answer[i] = [mini, maxi]:\n\nmini is the largest value in the tree that is smaller than or equal to queries[i]. If a such value does not exist, add -1 instead.\nmaxi is the smallest value in the tree that is greater than or equal to queries[i]. If a such value does not exist, add -1 instead.\n\nReturn the array answer.\n \n",
    "examples": [
      {
        "input": "Input: root = [6,2,13,1,4,9,15,null,null,null,null,null,null,14], queries = [2,5,16]",
        "output": "Output: [[2,2],[4,6],[15,-1]]",
        "explanation": "Explanation: We answer the queries in the following way:"
      },
      {
        "input": "Input: root = [4,null,9], queries = [3]",
        "output": "Output: [[-1,4]]",
        "explanation": "Explanation: The largest number that is smaller or equal to 3 in the tree does not exist, and the smallest number that is greater or equal to 3 is 4. So the answer for the query is [-1,4]."
      }
    ],
    "topics": [
      "Array",
      "Binary Search",
      "Tree",
      "Depth-First Search",
      "Binary Tree"
    ],
    "difficulty": "Medium",
    "constraints": [
      "The number of nodes in the tree is in the range [2, 105].",
      "1 <= Node.val <= 106",
      "n == queries.length",
      "1 <= n <= 105",
      "1 <= queries[i] <= 106"
    ],
    "hints": [
      "Try to first convert the tree into a sorted array.",
      "How do you solve each query in O(log(n)) time using the array of the tree?"
    ]
  },
  {
    "title": "Number of Unequal Triplets in Array",
    "description": "You are given a 0-indexed array of positive integers nums. Find the number of triplets (i, j, k) that meet the following conditions:\n\n0 <= i < j < k < nums.length\nnums[i], nums[j], and nums[k] are pairwise distinct.\n\t\nIn other words, nums[i] != nums[j], nums[i] != nums[k], and nums[j] != nums[k].\n\n\n\nReturn the number of triplets that meet the conditions.\n \n",
    "examples": [
      {
        "input": "Input: nums = [4,4,2,4,3]",
        "output": "Output: 3",
        "explanation": "Explanation: The following triplets meet the conditions:"
      },
      {
        "input": "Input: nums = [1,1,1,1,1]",
        "output": "Output: 0",
        "explanation": "Explanation: No triplets meet the conditions so we return 0."
      }
    ],
    "topics": [
      "Array",
      "Hash Table"
    ],
    "difficulty": "Easy",
    "constraints": [
      "3 <= nums.length <= 100",
      "1 <= nums[i] <= 1000"
    ],
    "hints": [
      "The constraints are very small. Can we try every triplet?",
      "Yes, we can. Use three loops to iterate through all the possible triplets, ensuring the condition i < j < k holds."
    ]
  },
  {
    "title": "Most Profitable Path in a Tree",
    "description": "There is an undirected tree with n nodes labeled from 0 to n - 1, rooted at node 0. You are given a 2D integer array edges of length n - 1 where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree.\nAt every node i, there is a gate. You are also given an array of even integers amount, where amount[i] represents:\n\nthe price needed to open the gate at node i, if amount[i] is negative, or,\nthe cash reward obtained on opening the gate at node i, otherwise.\n\nThe game goes on as follows:\n\nInitially, Alice is at node 0 and Bob is at node bob.\nAt every second, Alice and Bob each move to an adjacent node. Alice moves towards some leaf node, while Bob moves towards node 0.\nFor every node along their path, Alice and Bob either spend money to open the gate at that node, or accept the reward. Note that:\n\t\nIf the gate is already open, no price will be required, nor will there be any cash reward.\nIf Alice and Bob reach the node simultaneously, they share the price/reward for opening the gate there. In other words, if the price to open the gate is c, then both Alice and Bob pay c / 2 each. Similarly, if the reward at the gate is c, both of them receive c / 2 each.\n\n\nIf Alice reaches a leaf node, she stops moving. Similarly, if Bob reaches node 0, he stops moving. Note that these events are independent of each other.\n\nReturn the maximum net income Alice can have if she travels towards the optimal leaf node.\n \n",
    "examples": [
      {
        "input": "Input: edges = [[0,1],[1,2],[1,3],[3,4]], bob = 3, amount = [-2,4,2,-4,6]",
        "output": "Output: 6",
        "explanation": "Explanation: "
      },
      {
        "input": "Input: edges = [[0,1]], bob = 1, amount = [-7280,2350]",
        "output": "Output: -7280",
        "explanation": "Explanation: "
      }
    ],
    "topics": [
      "Array",
      "Tree",
      "Depth-First Search",
      "Breadth-First Search",
      "Graph"
    ],
    "difficulty": "Medium",
    "constraints": [
      "2 <= n <= 105",
      "edges.length == n - 1",
      "edges[i].length == 2",
      "0 <= ai, bi < n",
      "ai != bi",
      "edges represents a valid tree.",
      "1 <= bob < n",
      "amount.length == n",
      "amount[i] is an even integer in the range [-104, 104]."
    ],
    "hints": [
      "Bob travels along a fixed path (from node “bob” to node 0).",
      "Calculate Alice’s distance to each node via DFS.",
      "We can calculate Alice’s score along a path ending at some node easily using Hints 1 and 2."
    ]
  },
  {
    "title": "Split Message Based on Limit",
    "description": "You are given a string, message, and a positive integer, limit.\nYou must split message into one or more parts based on limit. Each resulting part should have the suffix \"<a/b>\", where \"b\" is to be replaced with the total number of parts and \"a\" is to be replaced with the index of the part, starting from 1 and going up to b. Additionally, the length of each resulting part (including its suffix) should be equal to limit, except for the last part whose length can be at most limit.\nThe resulting parts should be formed such that when their suffixes are removed and they are all concatenated in order, they should be equal to message. Also, the result should contain as few parts as possible.\nReturn the parts message would be split into as an array of strings. If it is impossible to split message as required, return an empty array.\n \n",
    "examples": [
      {
        "input": "Input: message = \"this is really a very awesome message\", limit = 9",
        "output": "Output: [\"thi<1/14>\",\"s i<2/14>\",\"s r<3/14>\",\"eal<4/14>\",\"ly <5/14>\",\"a v<6/14>\",\"ery<7/14>\",\" aw<8/14>\",\"eso<9/14>\",\"me<10/14>\",\" m<11/14>\",\"es<12/14>\",\"sa<13/14>\",\"ge<14/14>\"]",
        "explanation": ""
      },
      {
        "input": "Input: message = \"short message\", limit = 15",
        "output": "Output: [\"short mess<1/2>\",\"age<2/2>\"]",
        "explanation": ""
      }
    ],
    "topics": [
      "String",
      "Binary Search"
    ],
    "difficulty": "Hard",
    "constraints": [
      "1 <= message.length <= 104",
      "message consists only of lowercase English letters and ' '.",
      "1 <= limit <= 104"
    ],
    "hints": [
      "Could you solve the problem if you knew how many digits the total number of parts has?",
      "Try all possible lengths of the total number of parts, and see if the string can be split such that the total number of parts has that length.",
      "Binary search can be used for each part length to find the precise number of parts needed."
    ]
  },
  {
    "title": "Count Ways To Build Good Strings",
    "description": "Given the integers zero, one, low, and high, we can construct a string by starting with an empty string, and then at each step perform either of the following:\n\nAppend the character '0' zero times.\nAppend the character '1' one times.\n\nThis can be performed any number of times.\nA good string is a string constructed by the above process having a length between low and high (inclusive).\nReturn the number of different good strings that can be constructed satisfying these properties. Since the answer can be large, return it modulo 109 + 7.\n \n",
    "examples": [
      {
        "input": "Input: low = 3, high = 3, zero = 1, one = 1",
        "output": "Output: 8",
        "explanation": "Explanation: "
      },
      {
        "input": "Input: low = 2, high = 3, zero = 1, one = 2",
        "output": "Output: 5",
        "explanation": "Explanation: The good strings are \"00\", \"11\", \"000\", \"110\", and \"011\"."
      }
    ],
    "topics": [
      "Dynamic Programming"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= low <= high <= 105",
      "1 <= zero, one <= low"
    ],
    "hints": [
      "Calculate the number of good strings with length less or equal to some constant x.",
      "Apply dynamic programming using the group size of consecutive zeros and ones."
    ]
  },
  {
    "title": "Number of Distinct Averages",
    "description": "You are given a 0-indexed integer array nums of even length.\nAs long as nums is not empty, you must repetitively:\n\nFind the minimum number in nums and remove it.\nFind the maximum number in nums and remove it.\nCalculate the average of the two removed numbers.\n\nThe average of two numbers a and b is (a + b) / 2.\n\nFor example, the average of 2 and 3 is (2 + 3) / 2 = 2.5.\n\nReturn the number of distinct averages calculated using the above process.\nNote that when there is a tie for a minimum or maximum number, any can be removed.\n \n",
    "examples": [
      {
        "input": "Input: nums = [4,1,4,0,3,5]",
        "output": "Output: 2",
        "explanation": ""
      },
      {
        "input": "Input: nums = [1,100]",
        "output": "Output: 1",
        "explanation": ""
      }
    ],
    "topics": [
      "Array",
      "Hash Table",
      "Two Pointers",
      "Sorting"
    ],
    "difficulty": "Easy",
    "constraints": [
      "2 <= nums.length <= 100",
      "nums.length is even.",
      "0 <= nums[i] <= 100"
    ],
    "hints": [
      "Try sorting the array.",
      "Store the averages being calculated, and find the distinct ones."
    ]
  },
  {
    "title": "Maximum Number of Non-overlapping Palindrome Substrings",
    "description": "You are given a string s and a positive integer k.\nSelect a set of non-overlapping substrings from the string s that satisfy the following conditions:\n\nThe length of each substring is at least k.\nEach substring is a palindrome.\n\nReturn the maximum number of substrings in an optimal selection.\nA substring is a contiguous sequence of characters within a string.\n \n",
    "examples": [
      {
        "input": "Input: s = \"abaccdbbd\", k = 3",
        "output": "Output: 2",
        "explanation": "Explanation: We can select the substrings underlined in s = \"abaccdbbd\". Both \"aba\" and \"dbbd\" are palindromes and have a length of at least k = 3."
      },
      {
        "input": "Input: s = \"adbcda\", k = 2",
        "output": "Output: 0",
        "explanation": "Explanation: There is no palindrome substring of length at least 2 in the string."
      }
    ],
    "topics": [
      "String",
      "Dynamic Programming"
    ],
    "difficulty": "Hard",
    "constraints": [
      "1 <= k <= s.length <= 2000",
      "s consists of lowercase English letters."
    ],
    "hints": [
      "Try to use dynamic programming to solve the problem.",
      "let dp[i] be the answer for the prefix s[0…i].",
      "The final answer to the problem will be dp[n-1]. How do you compute this dp?"
    ]
  },
  {
    "title": "Minimum Number of Operations to Sort a Binary Tree by Level",
    "description": "You are given the root of a binary tree with unique values.\nIn one operation, you can choose any two nodes at the same level and swap their values.\nReturn the minimum number of operations needed to make the values at each level sorted in a strictly increasing order.\nThe level of a node is the number of edges along the path between it and the root node.\n \n",
    "examples": [
      {
        "input": "Input: root = [1,4,3,7,6,8,5,null,null,null,null,9,null,10]",
        "output": "Output: 3",
        "explanation": ""
      },
      {
        "input": "Input: root = [1,3,2,7,6,5,4]",
        "output": "Output: 3",
        "explanation": ""
      },
      {
        "input": "Input: root = [1,2,3,4,5,6]",
        "output": "Output: 0",
        "explanation": "Explanation: Each level is already sorted in increasing order so return 0."
      }
    ],
    "topics": [
      "Tree",
      "Breadth-First Search",
      "Binary Tree"
    ],
    "difficulty": "Medium",
    "constraints": [
      "The number of nodes in the tree is in the range [1, 105].",
      "1 <= Node.val <= 105",
      "All the values of the tree are unique."
    ],
    "hints": [
      "We can group the values level by level and solve each group independently.",
      "Do BFS to group the value level by level.",
      "Find the minimum number of swaps to sort the array of each level.",
      "While iterating over the array, check the current element, and if not in the correct index, replace that element with the index of the element which should have come."
    ]
  },
  {
    "title": "Number of Subarrays With LCM Equal to K",
    "description": "Given an integer array nums and an integer k, return the number of subarrays of nums where the least common multiple of the subarray's elements is k.\nA subarray is a contiguous non-empty sequence of elements within an array.\nThe least common multiple of an array is the smallest positive integer that is divisible by all the array elements.\n \n",
    "examples": [
      {
        "input": "Input: nums = [3,6,2,7,1], k = 6",
        "output": "Output: 4",
        "explanation": "Explanation: The subarrays of nums where 6 is the least common multiple of all the subarray's elements are:"
      },
      {
        "input": "Input: nums = [3], k = 2",
        "output": "Output: 0",
        "explanation": "Explanation: There are no subarrays of nums where 2 is the least common multiple of all the subarray's elements."
      }
    ],
    "topics": [
      "Array",
      "Math",
      "Number Theory"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= nums.length <= 1000",
      "1 <= nums[i], k <= 1000"
    ],
    "hints": [
      "The constraints on nums.length are small. It is possible to check every subarray.",
      "To calculate LCM, you can use a built-in function or the formula lcm(a, b) = a * b / gcd(a, b).",
      "As you calculate the LCM of more numbers, it can only become greater. Once it becomes greater than k, you know that any larger subarrays containing all the current elements will not work."
    ]
  },
  {
    "title": "Convert the Temperature",
    "description": "You are given a non-negative floating point number rounded to two decimal places celsius, that denotes the temperature in Celsius.\nYou should convert Celsius into Kelvin and Fahrenheit and return it as an array ans = [kelvin, fahrenheit].\nReturn the array ans. Answers within 10-5 of the actual answer will be accepted.\nNote that:\n\nKelvin = Celsius + 273.15\nFahrenheit = Celsius * 1.80 + 32.00\n\n \n",
    "examples": [
      {
        "input": "Input: celsius = 36.50",
        "output": "Output: [309.65000,97.70000]",
        "explanation": "Explanation: Temperature at 36.50 Celsius converted in Kelvin is 309.65 and converted in Fahrenheit is 97.70."
      },
      {
        "input": "Input: celsius = 122.11",
        "output": "Output: [395.26000,251.79800]",
        "explanation": "Explanation: Temperature at 122.11 Celsius converted in Kelvin is 395.26 and converted in Fahrenheit is 251.798."
      }
    ],
    "topics": [
      "Math"
    ],
    "difficulty": "Easy",
    "constraints": [
      "0 <= celsius <= 1000"
    ],
    "hints": [
      "Implement formulas that are given in the statement."
    ]
  },
  {
    "title": "Minimum Total Distance Traveled",
    "description": "There are some robots and factories on the X-axis. You are given an integer array robot where robot[i] is the position of the ith robot. You are also given a 2D integer array factory where factory[j] = [positionj, limitj] indicates that positionj is the position of the jth factory and that the jth factory can repair at most limitj robots.\nThe positions of each robot are unique. The positions of each factory are also unique. Note that a robot can be in the same position as a factory initially.\nAll the robots are initially broken; they keep moving in one direction. The direction could be the negative or the positive direction of the X-axis. When a robot reaches a factory that did not reach its limit, the factory repairs the robot, and it stops moving.\nAt any moment, you can set the initial direction of moving for some robot. Your target is to minimize the total distance traveled by all the robots.\nReturn the minimum total distance traveled by all the robots. The test cases are generated such that all the robots can be repaired.\nNote that\n\nAll robots move at the same speed.\nIf two robots move in the same direction, they will never collide.\nIf two robots move in opposite directions and they meet at some point, they do not collide. They cross each other.\nIf a robot passes by a factory that reached its limits, it crosses it as if it does not exist.\nIf the robot moved from a position x to a position y, the distance it moved is |y - x|.\n\n \n",
    "examples": [
      {
        "input": "Input: robot = [0,4,6], factory = [[2,2],[6,2]]",
        "output": "Output: 4",
        "explanation": "Explanation: As shown in the figure:"
      },
      {
        "input": "Input: robot = [1,-1], factory = [[-2,1],[2,1]]",
        "output": "Output: 2",
        "explanation": "Explanation: As shown in the figure:"
      }
    ],
    "topics": [
      "Array",
      "Dynamic Programming",
      "Sorting"
    ],
    "difficulty": "Hard",
    "constraints": [
      "1 <= robot.length, factory.length <= 100",
      "factory[j].length == 2",
      "-109 <= robot[i], positionj <= 109",
      "0 <= limitj <= robot.length",
      "The input will be generated such that it is always possible to repair every robot."
    ],
    "hints": [
      "Sort robots and factories by their positions.",
      "After sorting, notice that each factory should repair some subsegment of robots.",
      "Find the minimum total distance to repair first i robots with first j factories."
    ]
  },
  {
    "title": "Total Cost to Hire K Workers",
    "description": "You are given a 0-indexed integer array costs where costs[i] is the cost of hiring the ith worker.\nYou are also given two integers k and candidates. We want to hire exactly k workers according to the following rules:\n\nYou will run k sessions and hire exactly one worker in each session.\nIn each hiring session, choose the worker with the lowest cost from either the first candidates workers or the last candidates workers. Break the tie by the smallest index.\n\t\nFor example, if costs = [3,2,7,7,1,2] and candidates = 2, then in the first hiring session, we will choose the 4th worker because they have the lowest cost [3,2,7,7,1,2].\nIn the second hiring session, we will choose 1st worker because they have the same lowest cost as 4th worker but they have the smallest index [3,2,7,7,2]. Please note that the indexing may be changed in the process.\n\n\nIf there are fewer than candidates workers remaining, choose the worker with the lowest cost among them. Break the tie by the smallest index.\nA worker can only be chosen once.\n\nReturn the total cost to hire exactly k workers.\n \n",
    "examples": [
      {
        "input": "Input: costs = [17,12,10,2,7,2,11,20,8], k = 3, candidates = 4",
        "output": "Output: 11",
        "explanation": "Explanation: We hire 3 workers in total. The total cost is initially 0."
      },
      {
        "input": "Input: costs = [1,2,4,1], k = 3, candidates = 3",
        "output": "Output: 4",
        "explanation": "Explanation: We hire 3 workers in total. The total cost is initially 0."
      }
    ],
    "topics": [
      "Array",
      "Two Pointers",
      "Heap (Priority Queue)",
      "Simulation"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= costs.length <= 105 ",
      "1 <= costs[i] <= 105",
      "1 <= k, candidates <= costs.length"
    ],
    "hints": [
      "Maintain two minheaps: one for the left and one for the right.",
      "Compare the top element from two heaps and remove the appropriate one.",
      "Add a new element to the heap and maintain its size as k."
    ]
  },
  {
    "title": "Maximum Sum of Distinct Subarrays With Length K",
    "description": "You are given an integer array nums and an integer k. Find the maximum subarray sum of all the subarrays of nums that meet the following conditions:\n\nThe length of the subarray is k, and\nAll the elements of the subarray are distinct.\n\nReturn the maximum subarray sum of all the subarrays that meet the conditions. If no subarray meets the conditions, return 0.\nA subarray is a contiguous non-empty sequence of elements within an array.\n \n",
    "examples": [
      {
        "input": "Input: nums = [1,5,4,2,9,9,9], k = 3",
        "output": "Output: 15",
        "explanation": "Explanation: The subarrays of nums with length 3 are:"
      },
      {
        "input": "Input: nums = [4,4,4], k = 3",
        "output": "Output: 0",
        "explanation": "Explanation: The subarrays of nums with length 3 are:"
      }
    ],
    "topics": [
      "Array",
      "Hash Table",
      "Sliding Window"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= k <= nums.length <= 105",
      "1 <= nums[i] <= 105"
    ],
    "hints": [
      "Which elements change when moving from the subarray of size k that ends at index i to the subarray of size k that ends at index i + 1?",
      "Only two elements change, the element at i + 1 is added into the subarray, and the element at i - k + 1 gets removed from the subarray.",
      "Iterate through each subarray of size k and keep track of the sum of the subarray and the frequency of each element."
    ]
  },
  {
    "title": "Apply Operations to an Array",
    "description": "You are given a 0-indexed array nums of size n consisting of non-negative integers.\nYou need to apply n - 1 operations to this array where, in the ith operation (0-indexed), you will apply the following on the ith element of nums:\n\nIf nums[i] == nums[i + 1], then multiply nums[i] by 2 and set nums[i + 1] to 0. Otherwise, you skip this operation.\n\nAfter performing all the operations, shift all the 0's to the end of the array.\n\nFor example, the array [1,0,2,0,0,1] after shifting all its 0's to the end, is [1,2,1,0,0,0].\n\nReturn the resulting array.\nNote that the operations are applied sequentially, not all at once.\n \n",
    "examples": [
      {
        "input": "Input: nums = [1,2,2,1,1,0]",
        "output": "Output: [1,4,2,0,0,0]",
        "explanation": "Explanation: We do the following operations:"
      },
      {
        "input": "Input: nums = [0,1]",
        "output": "Output: [1,0]",
        "explanation": "Explanation: No operation can be applied, we just shift the 0 to the end."
      }
    ],
    "topics": [
      "Array",
      "Simulation"
    ],
    "difficulty": "Easy",
    "constraints": [
      "2 <= nums.length <= 2000",
      "0 <= nums[i] <= 1000"
    ],
    "hints": [
      "Iterate over the array and simulate the described process."
    ]
  },
  {
    "title": "Words Within Two Edits of Dictionary",
    "description": "You are given two string arrays, queries and dictionary. All words in each array comprise of lowercase English letters and have the same length.\nIn one edit you can take a word from queries, and change any letter in it to any other letter. Find all words from queries that, after a maximum of two edits, equal some word from dictionary.\nReturn a list of all words from queries, that match with some word from dictionary after a maximum of two edits. Return the words in the same order they appear in queries.\n \n",
    "examples": [
      {
        "input": "Input: queries = [\"word\",\"note\",\"ants\",\"wood\"], dictionary = [\"wood\",\"joke\",\"moat\"]",
        "output": "Output: [\"word\",\"note\",\"wood\"]",
        "explanation": ""
      },
      {
        "input": "Input: queries = [\"yes\"], dictionary = [\"not\"]",
        "output": "Output: []",
        "explanation": ""
      }
    ],
    "topics": [
      "Array",
      "String"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= queries.length, dictionary.length <= 100",
      "n == queries[i].length == dictionary[j].length",
      "1 <= n <= 100",
      "All queries[i] and dictionary[j] are composed of lowercase English letters."
    ],
    "hints": [
      "Try brute-forcing the problem.",
      "For each word in queries, try comparing to each word in dictionary.",
      "If there is a maximum of two edit differences, the word should be present in answer."
    ]
  },
  {
    "title": "Next Greater Element IV",
    "description": "You are given a 0-indexed array of non-negative integers nums. For each integer in nums, you must find its respective second greater integer.\nThe second greater integer of nums[i] is nums[j] such that:\n\nj > i\nnums[j] > nums[i]\nThere exists exactly one index k such that nums[k] > nums[i] and i < k < j.\n\nIf there is no such nums[j], the second greater integer is considered to be -1.\n\nFor example, in the array [1, 2, 4, 3], the second greater integer of 1 is 4, 2 is 3, and that of 3 and 4 is -1.\n\nReturn an integer array answer, where answer[i] is the second greater integer of nums[i].\n \n",
    "examples": [
      {
        "input": "Input: nums = [2,4,0,9,6]",
        "output": "Output: [9,6,6,-1,-1]",
        "explanation": ""
      },
      {
        "input": "Input: nums = [3,3]",
        "output": "Output: [-1,-1]",
        "explanation": ""
      }
    ],
    "topics": [
      "Array",
      "Binary Search",
      "Stack",
      "Sorting",
      "Heap (Priority Queue)",
      "Monotonic Stack"
    ],
    "difficulty": "Hard",
    "constraints": [
      "1 <= nums.length <= 105",
      "0 <= nums[i] <= 109"
    ],
    "hints": [
      "Move forward in nums and store the value in a non-increasing stack for the first greater value.",
      "Move the value in the stack to an ordered data structure for the second greater value.",
      "Move value from the ordered data structure for the answer."
    ]
  },
  {
    "title": "Destroy Sequential Targets",
    "description": "You are given a 0-indexed array nums consisting of positive integers, representing targets on a number line. You are also given an integer space.\nYou have a machine which can destroy targets. Seeding the machine with some nums[i] allows it to destroy all targets with values that can be represented as nums[i] + c * space, where c is any non-negative integer. You want to destroy the maximum number of targets in nums.\nReturn the minimum value of nums[i] you can seed the machine with to destroy the maximum number of targets.\n \n",
    "examples": [
      {
        "input": "Input: nums = [3,7,8,1,1,5], space = 2",
        "output": "Output: 1",
        "explanation": "Explanation: If we seed the machine with nums[3], then we destroy all targets equal to 1,3,5,7,9,... "
      },
      {
        "input": "Input: nums = [1,3,5,2,4,6], space = 2",
        "output": "Output: 1",
        "explanation": "Explanation: Seeding the machine with nums[0], or nums[3] destroys 3 targets. "
      },
      {
        "input": "Input: nums = [6,2,5], space = 100",
        "output": "Output: 2",
        "explanation": "Explanation: Whatever initial seed we select, we can only destroy 1 target. The minimal seed is nums[1]."
      }
    ],
    "topics": [
      "Array",
      "Hash Table",
      "Counting"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= nums.length <= 105",
      "1 <= nums[i] <= 109",
      "1 <= space <= 109"
    ],
    "hints": [
      "Keep track of nums[i] modulo k.",
      "Iterate over nums in sorted order."
    ]
  },
  {
    "title": "Odd String Difference",
    "description": "You are given an array of equal-length strings words. Assume that the length of each string is n.\nEach string words[i] can be converted into a difference integer array difference[i] of length n - 1 where difference[i][j] = words[i][j+1] - words[i][j] where 0 <= j <= n - 2. Note that the difference between two letters is the difference between their positions in the alphabet i.e. the position of 'a' is 0, 'b' is 1, and 'z' is 25.\n\nFor example, for the string \"acb\", the difference integer array is [2 - 0, 1 - 2] = [2, -1].\n\nAll the strings in words have the same difference integer array, except one. You should find that string.\nReturn the string in words that has different difference integer array.\n \n",
    "examples": [
      {
        "input": "Input: words = [\"adc\",\"wzy\",\"abc\"]",
        "output": "Output: \"abc\"",
        "explanation": "Explanation: "
      },
      {
        "input": "Input: words = [\"aaa\",\"bob\",\"ccc\",\"ddd\"]",
        "output": "Output: \"bob\"",
        "explanation": "Explanation: All the integer arrays are [0, 0] except for \"bob\", which corresponds to [13, -13]."
      }
    ],
    "topics": [
      "Hash Table",
      "Math",
      "String"
    ],
    "difficulty": "Easy",
    "constraints": [
      "3 <= words.length <= 100",
      "n == words[i].length",
      "2 <= n <= 20",
      "words[i] consists of lowercase English letters."
    ],
    "hints": [
      "Find the difference integer array for each string.",
      "Compare them to find the odd one out."
    ]
  },
  {
    "title": "Number of Subarrays With GCD Equal to K",
    "description": "Given an integer array nums and an integer k, return the number of subarrays of nums where the greatest common divisor of the subarray's elements is k.\nA subarray is a contiguous non-empty sequence of elements within an array.\nThe greatest common divisor of an array is the largest integer that evenly divides all the array elements.\n \n",
    "examples": [
      {
        "input": "Input: nums = [9,3,1,2,6,3], k = 3",
        "output": "Output: 4",
        "explanation": "Explanation: The subarrays of nums where 3 is the greatest common divisor of all the subarray's elements are:"
      },
      {
        "input": "Input: nums = [4], k = 7",
        "output": "Output: 0",
        "explanation": "Explanation: There are no subarrays of nums where 7 is the greatest common divisor of all the subarray's elements."
      }
    ],
    "topics": [
      "Array",
      "Math",
      "Number Theory"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= nums.length <= 1000",
      "1 <= nums[i], k <= 109"
    ],
    "hints": [
      "The constraints on nums.length are small. It is possible to check every subarray.",
      "To calculate GCD, you can use a built-in function or the Euclidean Algorithm."
    ]
  },
  {
    "title": "Height of Binary Tree After Subtree Removal Queries",
    "description": "You are given the root of a binary tree with n nodes. Each node is assigned a unique value from 1 to n. You are also given an array queries of size m.\nYou have to perform m independent queries on the tree where in the ith query you do the following:\n\nRemove the subtree rooted at the node with the value queries[i] from the tree. It is guaranteed that queries[i] will not be equal to the value of the root.\n\nReturn an array answer of size m where answer[i] is the height of the tree after performing the ith query.\nNote:\n\nThe queries are independent, so the tree returns to its initial state after each query.\nThe height of a tree is the number of edges in the longest simple path from the root to some node in the tree.\n\n \n",
    "examples": [
      {
        "input": "Input: root = [1,3,4,2,null,6,5,null,null,null,null,null,7], queries = [4]",
        "output": "Output: [2]",
        "explanation": "Explanation: The diagram above shows the tree after removing the subtree rooted at node with value 4."
      },
      {
        "input": "Input: root = [5,8,9,2,1,3,7,4,6], queries = [3,2,4,8]",
        "output": "Output: [3,2,3,2]",
        "explanation": "Explanation: We have the following queries:"
      }
    ],
    "topics": [
      "Array",
      "Tree",
      "Depth-First Search",
      "Breadth-First Search",
      "Binary Tree"
    ],
    "difficulty": "Hard",
    "constraints": [
      "The number of nodes in the tree is n.",
      "2 <= n <= 105",
      "1 <= Node.val <= n",
      "All the values in the tree are unique.",
      "m == queries.length",
      "1 <= m <= min(n, 104)",
      "1 <= queries[i] <= n",
      "queries[i] != root.val"
    ],
    "hints": [
      "Try pre-computing the answer for each node from 1 to n, and answer each query in O(1).",
      "The answers can be precomputed in a single tree traversal after computing the height of each subtree."
    ]
  },
  {
    "title": "Minimum Addition to Make Integer Beautiful",
    "description": "You are given two positive integers n and target.\nAn integer is considered beautiful if the sum of its digits is less than or equal to target.\nReturn the minimum non-negative integer x such that n + x is beautiful. The input will be generated such that it is always possible to make n beautiful.\n \n",
    "examples": [
      {
        "input": "Input: n = 16, target = 6",
        "output": "Output: 4",
        "explanation": "Explanation: Initially n is 16 and its digit sum is 1 + 6 = 7. After adding 4, n becomes 20 and digit sum becomes 2 + 0 = 2. It can be shown that we can not make n beautiful with adding non-negative integer less than 4."
      },
      {
        "input": "Input: n = 467, target = 6",
        "output": "Output: 33",
        "explanation": "Explanation: Initially n is 467 and its digit sum is 4 + 6 + 7 = 17. After adding 33, n becomes 500 and digit sum becomes 5 + 0 + 0 = 5. It can be shown that we can not make n beautiful with adding non-negative integer less than 33."
      },
      {
        "input": "Input: n = 1, target = 1",
        "output": "Output: 0",
        "explanation": "Explanation: Initially n is 1 and its digit sum is 1, which is already smaller than or equal to target."
      }
    ],
    "topics": [
      "Math",
      "Greedy"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= n <= 1012",
      "1 <= target <= 150",
      "The input will be generated such that it is always possible to make n beautiful."
    ],
    "hints": [
      "Think about each digit independently.",
      "Turn the rightmost non-zero digit to zero until the digit sum is greater than target."
    ]
  },
  {
    "title": "Most Popular Video Creator",
    "description": "You are given two string arrays creators and ids, and an integer array views, all of length n. The ith video on a platform was created by creator[i], has an id of ids[i], and has views[i] views.\nThe popularity of a creator is the sum of the number of views on all of the creator's videos. Find the creator with the highest popularity and the id of their most viewed video.\n\nIf multiple creators have the highest popularity, find all of them.\nIf multiple videos have the highest view count for a creator, find the lexicographically smallest id.\n\nReturn a 2D array of strings answer where answer[i] = [creatori, idi] means that creatori has the highest popularity and idi is the id of their most popular video. The answer can be returned in any order.\n \n",
    "examples": [
      {
        "input": "Input: creators = [\"alice\",\"bob\",\"alice\",\"chris\"], ids = [\"one\",\"two\",\"three\",\"four\"], views = [5,10,5,4]",
        "output": "Output: [[\"alice\",\"one\"],[\"bob\",\"two\"]]",
        "explanation": ""
      },
      {
        "input": "Input: creators = [\"alice\",\"alice\",\"alice\"], ids = [\"a\",\"b\",\"c\"], views = [1,2,2]",
        "output": "Output: [[\"alice\",\"b\"]]",
        "explanation": ""
      }
    ],
    "topics": [
      "Array",
      "Hash Table",
      "String",
      "Sorting",
      "Heap (Priority Queue)"
    ],
    "difficulty": "Medium",
    "constraints": [
      "n == creators.length == ids.length == views.length",
      "1 <= n <= 105",
      "1 <= creators[i].length, ids[i].length <= 5",
      "creators[i] and ids[i] consist only of lowercase English letters.",
      "0 <= views[i] <= 105"
    ],
    "hints": [
      "Use a hash table to store and categorize videos based on their creator.",
      "For each creator, iterate through all their videos and use three variables to keep track of their popularity, their most popular video, and the id of their most popular video."
    ]
  },
  {
    "title": "Average Value of Even Numbers That Are Divisible by Three",
    "description": "Given an integer array nums of positive integers, return the average value of all even integers that are divisible by 3.\nNote that the average of n elements is the sum of the n elements divided by n and rounded down to the nearest integer.\n \n",
    "examples": [
      {
        "input": "Input: nums = [1,3,6,10,12,15]",
        "output": "Output: 9",
        "explanation": "Explanation: 6 and 12 are even numbers that are divisible by 3. (6 + 12) / 2 = 9."
      },
      {
        "input": "Input: nums = [1,2,4,7,10]",
        "output": "Output: 0",
        "explanation": "Explanation: There is no single number that satisfies the requirement, so return 0."
      }
    ],
    "topics": [
      "Array",
      "Math"
    ],
    "difficulty": "Easy",
    "constraints": [
      "1 <= nums.length <= 1000",
      "1 <= nums[i] <= 1000"
    ],
    "hints": [
      "What is the property of a number if it is divisible by both 2 and 3 at the same time?",
      "It is equivalent to finding all the numbers that are divisible by 6."
    ]
  },
  {
    "title": "Sum of Number and Its Reverse",
    "description": "Given a non-negative integer num, return true if num can be expressed as the sum of any non-negative integer and its reverse, or false otherwise.\n \n",
    "examples": [
      {
        "input": "Input: num = 443",
        "output": "Output: true",
        "explanation": "Explanation: 172 + 271 = 443 so we return true."
      },
      {
        "input": "Input: num = 63",
        "output": "Output: false",
        "explanation": "Explanation: 63 cannot be expressed as the sum of a non-negative integer and its reverse so we return false."
      },
      {
        "input": "Input: num = 181",
        "output": "Output: true",
        "explanation": "Explanation: 140 + 041 = 181 so we return true. Note that when a number is reversed, there may be leading zeros."
      }
    ],
    "topics": [
      "Math",
      "Enumeration"
    ],
    "difficulty": "Medium",
    "constraints": [
      "0 <= num <= 105"
    ],
    "hints": [
      "The constraints are small enough that we can check every number.",
      "To reverse a number, first convert it to a string. Then, create a new string that is the reverse of the first one. Finally, convert the new string back into a number."
    ]
  },
  {
    "title": "Minimum Number of Operations to Make Arrays Similar",
    "description": "You are given two positive integer arrays nums and target, of the same length.\nIn one operation, you can choose any two distinct indices i and j where 0 <= i, j < nums.length and:\n\nset nums[i] = nums[i] + 2 and\nset nums[j] = nums[j] - 2.\n\nTwo arrays are considered to be similar if the frequency of each element is the same.\nReturn the minimum number of operations required to make nums similar to target. The test cases are generated such that nums can always be similar to target.\n \n",
    "examples": [
      {
        "input": "Input: nums = [8,12,6], target = [2,14,10]",
        "output": "Output: 2",
        "explanation": "Explanation: It is possible to make nums similar to target in two operations:"
      },
      {
        "input": "Input: nums = [1,2,5], target = [4,1,3]",
        "output": "Output: 1",
        "explanation": "Explanation: We can make nums similar to target in one operation:"
      },
      {
        "input": "Input: nums = [1,1,1,1,1], target = [1,1,1,1,1]",
        "output": "Output: 0",
        "explanation": "Explanation: The array nums is already similiar to target."
      }
    ],
    "topics": [
      "Array",
      "Greedy",
      "Sorting"
    ],
    "difficulty": "Hard",
    "constraints": [
      "n == nums.length == target.length",
      "1 <= n <= 105",
      "1 <= nums[i], target[i] <= 106",
      "It is possible to make nums similar to target."
    ],
    "hints": [
      "Solve for even and odd numbers separately.",
      "Greedily match smallest even element from nums to smallest even element from target, then similarly next smallest element and so on.",
      "Similarly, match odd elements too."
    ]
  },
  {
    "title": "Minimum Cost to Make Array Equal",
    "description": "You are given two 0-indexed arrays nums and cost consisting each of n positive integers.\nYou can do the following operation any number of times:\n\nIncrease or decrease any element of the array nums by 1.\n\nThe cost of doing one operation on the ith element is cost[i].\nReturn the minimum total cost such that all the elements of the array nums become equal.\n \n",
    "examples": [
      {
        "input": "Input: nums = [1,3,5,2], cost = [2,3,1,14]",
        "output": "Output: 8",
        "explanation": "Explanation: We can make all the elements equal to 2 in the following way:"
      },
      {
        "input": "Input: nums = [2,2,2,2,2], cost = [4,2,8,1,3]",
        "output": "Output: 0",
        "explanation": "Explanation: All the elements are already equal, so no operations are needed."
      }
    ],
    "topics": [
      "Array",
      "Binary Search",
      "Greedy",
      "Sorting",
      "Prefix Sum"
    ],
    "difficulty": "Hard",
    "constraints": [
      "n == nums.length == cost.length",
      "1 <= n <= 105",
      "1 <= nums[i], cost[i] <= 106"
    ],
    "hints": [
      "Changing the elements into one of the numbers already existing in the array nums is optimal.",
      "Try finding the cost of changing the array into each element, and return the minimum value."
    ]
  },
  {
    "title": "Determine if Two Events Have Conflict",
    "description": "You are given two arrays of strings that represent two inclusive events that happened on the same day, event1 and event2, where:\n\nevent1 = [startTime1, endTime1] and\nevent2 = [startTime2, endTime2].\n\nEvent times are valid 24 hours format in the form of HH:MM.\nA conflict happens when two events have some non-empty intersection (i.e., some moment is common to both events).\nReturn true if there is a conflict between two events. Otherwise, return false.\n \n",
    "examples": [
      {
        "input": "Input: event1 = [\"01:15\",\"02:00\"], event2 = [\"02:00\",\"03:00\"]",
        "output": "Output: true",
        "explanation": "Explanation: The two events intersect at time 2:00."
      },
      {
        "input": "Input: event1 = [\"01:00\",\"02:00\"], event2 = [\"01:20\",\"03:00\"]",
        "output": "Output: true",
        "explanation": "Explanation: The two events intersect starting from 01:20 to 02:00."
      },
      {
        "input": "Input: event1 = [\"10:00\",\"11:00\"], event2 = [\"14:00\",\"15:00\"]",
        "output": "Output: false",
        "explanation": "Explanation: The two events do not intersect."
      }
    ],
    "topics": [
      "Array",
      "String"
    ],
    "difficulty": "Easy",
    "constraints": [
      "evnet1.length == event2.length == 2.",
      "event1[i].length == event2[i].length == 5",
      "startTime1 <= endTime1",
      "startTime2 <= endTime2",
      "All the event times follow the HH:MM format."
    ],
    "hints": [
      "Parse time format to some integer interval first",
      "How would you determine if two intervals overlap?"
    ]
  },
  {
    "title": "Bitwise XOR of All Pairings",
    "description": "You are given two 0-indexed arrays, nums1 and nums2, consisting of non-negative integers. There exists another array, nums3, which contains the bitwise XOR of all pairings of integers between nums1 and nums2 (every integer in nums1 is paired with every integer in nums2 exactly once).\nReturn the bitwise XOR of all integers in nums3.\n \n",
    "examples": [
      {
        "input": "Input: nums1 = [2,1,3], nums2 = [10,2,5,0]",
        "output": "Output: 13",
        "explanation": ""
      },
      {
        "input": "Input: nums1 = [1,2], nums2 = [3,4]",
        "output": "Output: 0",
        "explanation": ""
      }
    ],
    "topics": [
      "Array",
      "Bit Manipulation",
      "Brainteaser"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= nums1.length, nums2.length <= 105",
      "0 <= nums1[i], nums2[j] <= 109"
    ],
    "hints": [
      "Think how the count of each individual integer affects the final answer.",
      "If the length of nums1 is m and the length of nums2 is n, then each number in nums1 is repeated n times and each number in nums2 is repeated m times."
    ]
  },
  {
    "title": "Remove Letter To Equalize Frequency",
    "description": "You are given a 0-indexed string word, consisting of lowercase English letters. You need to select one index and remove the letter at that index from word so that the frequency of every letter present in word is equal.\nReturn true if it is possible to remove one letter so that the frequency of all letters in word are equal, and false otherwise.\nNote:\n\nThe frequency of a letter x is the number of times it occurs in the string.\nYou must remove exactly one letter and cannot chose to do nothing.\n\n \n",
    "examples": [
      {
        "input": "Input: word = \"abcc\"",
        "output": "Output: true",
        "explanation": "Explanation: Select index 3 and delete it: word becomes \"abc\" and each character has a frequency of 1."
      },
      {
        "input": "Input: word = \"aazz\"",
        "output": "Output: false",
        "explanation": "Explanation: We must delete a character, so either the frequency of \"a\" is 1 and the frequency of \"z\" is 2, or vice versa. It is impossible to make all present letters have equal frequency."
      }
    ],
    "topics": [
      "Hash Table",
      "String",
      "Counting"
    ],
    "difficulty": "Easy",
    "constraints": [
      "2 <= word.length <= 100",
      "word consists of lowercase English letters only."
    ],
    "hints": [
      "Brute force all letters that could be removed.",
      "Use a frequency array of size 26."
    ]
  },
  {
    "title": "Create Components With Same Value",
    "description": "There is an undirected tree with n nodes labeled from 0 to n - 1.\nYou are given a 0-indexed integer array nums of length n where nums[i] represents the value of the ith node. You are also given a 2D integer array edges of length n - 1 where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree.\nYou are allowed to delete some edges, splitting the tree into multiple connected components. Let the value of a component be the sum of all nums[i] for which node i is in the component.\nReturn the maximum number of edges you can delete, such that every connected component in the tree has the same value.\n \n",
    "examples": [
      {
        "input": "Input: nums = [6,2,2,2,6], edges = [[0,1],[1,2],[1,3],[3,4]] ",
        "output": "Output: 2 ",
        "explanation": "Explanation: The above figure shows how we can delete the edges [0,1] and [3,4]. The created components are nodes [0], [1,2,3] and [4]. The sum of the values in each component equals 6. It can be proven that no better deletion exists, so the answer is 2."
      },
      {
        "input": "Input: nums = [2], edges = []",
        "output": "Output: 0",
        "explanation": "Explanation: There are no edges to be deleted."
      }
    ],
    "topics": [
      "Array",
      "Math",
      "Tree",
      "Depth-First Search",
      "Enumeration"
    ],
    "difficulty": "Hard",
    "constraints": [
      "1 <= n <= 2 * 104",
      "nums.length == n",
      "1 <= nums[i] <= 50",
      "edges.length == n - 1",
      "edges[i].length == 2",
      "0 <= edges[i][0], edges[i][1] <= n - 1",
      "edges represents a valid tree."
    ],
    "hints": [
      "Consider all divisors of the sum of values."
    ]
  },
  {
    "title": "Minimize Maximum of Array",
    "description": "You are given a 0-indexed array nums comprising of n non-negative integers.\nIn one operation, you must:\n\nChoose an integer i such that 1 <= i < n and nums[i] > 0.\nDecrease nums[i] by 1.\nIncrease nums[i - 1] by 1.\n\nReturn the minimum possible value of the maximum integer of nums after performing any number of operations.\n \n",
    "examples": [
      {
        "input": "Input: nums = [3,7,1,6]",
        "output": "Output: 5",
        "explanation": ""
      },
      {
        "input": "Input: nums = [10,1]",
        "output": "Output: 10",
        "explanation": ""
      }
    ],
    "topics": [
      "Array",
      "Binary Search",
      "Dynamic Programming",
      "Greedy",
      "Prefix Sum"
    ],
    "difficulty": "Medium",
    "constraints": [
      "n == nums.length",
      "2 <= n <= 105",
      "0 <= nums[i] <= 109"
    ],
    "hints": [
      "Try a binary search approach.",
      "Perform a binary search over the minimum value that can be achieved for the maximum number of the array.",
      "In each binary search iteration, iterate through the array backwards, greedily decreasing the current element until it is within the limit."
    ]
  },
  {
    "title": "Range Product Queries of Powers",
    "description": "Given a positive integer n, there exists a 0-indexed array called powers, composed of the minimum number of powers of 2 that sum to n. The array is sorted in non-decreasing order, and there is only one way to form the array.\nYou are also given a 0-indexed 2D integer array queries, where queries[i] = [lefti, righti]. Each queries[i] represents a query where you have to find the product of all powers[j] with lefti <= j <= righti.\nReturn an array answers, equal in length to queries, where answers[i] is the answer to the ith query. Since the answer to the ith query may be too large, each answers[i] should be returned modulo 109 + 7.\n \n",
    "examples": [
      {
        "input": "Input: n = 15, queries = [[0,1],[2,2],[0,3]]",
        "output": "Output: [2,4,64]",
        "explanation": ""
      },
      {
        "input": "Input: n = 2, queries = [[0,0]]",
        "output": "Output: [2]",
        "explanation": ""
      }
    ],
    "topics": [
      "Array",
      "Bit Manipulation",
      "Prefix Sum"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= n <= 109",
      "1 <= queries.length <= 105",
      "0 <= starti <= endi < powers.length"
    ],
    "hints": [
      "The powers array can be created using the binary representation of n.",
      "Once powers is formed, the products can be taken using brute force."
    ]
  },
  {
    "title": "Number of Valid Clock Times",
    "description": "You are given a string of length 5 called time, representing the current time on a digital clock in the format \"hh:mm\". The earliest possible time is \"00:00\" and the latest possible time is \"23:59\".\nIn the string time, the digits represented by the ? symbol are unknown, and must be replaced with a digit from 0 to 9.\nReturn an integer answer, the number of valid clock times that can be created by replacing every ? with a digit from 0 to 9.\n \n",
    "examples": [
      {
        "input": "Input: time = \"?5:00\"",
        "output": "Output: 2",
        "explanation": "Explanation: We can replace the ? with either a 0 or 1, producing \"05:00\" or \"15:00\". Note that we cannot replace it with a 2, since the time \"25:00\" is invalid. In total, we have two choices."
      },
      {
        "input": "Input: time = \"0?:0?\"",
        "output": "Output: 100",
        "explanation": "Explanation: Each ? can be replaced by any digit from 0 to 9, so we have 100 total choices."
      },
      {
        "input": "Input: time = \"??:??\"",
        "output": "Output: 1440",
        "explanation": "Explanation: There are 24 possible choices for the hours, and 60 possible choices for the minutes. In total, we have 24 * 60 = 1440 choices."
      }
    ],
    "topics": [
      "String",
      "Enumeration"
    ],
    "difficulty": "Easy",
    "constraints": [
      "time is a valid string of length 5 in the format \"hh:mm\".",
      "\"00\" <= hh <= \"23\"",
      "\"00\" <= mm <= \"59\"",
      "Some of the digits might be replaced with '?' and need to be replaced with digits from 0 to 9."
    ],
    "hints": [
      "Brute force all possible clock times.",
      "Checking if a clock time is valid can be done with Regex."
    ]
  },
  {
    "title": "Count Subarrays With Fixed Bounds",
    "description": "You are given an integer array nums and two integers minK and maxK.\nA fixed-bound subarray of nums is a subarray that satisfies the following conditions:\n\nThe minimum value in the subarray is equal to minK.\nThe maximum value in the subarray is equal to maxK.\n\nReturn the number of fixed-bound subarrays.\nA subarray is a contiguous part of an array.\n \n",
    "examples": [
      {
        "input": "Input: nums = [1,3,5,2,7,5], minK = 1, maxK = 5",
        "output": "Output: 2",
        "explanation": "Explanation: The fixed-bound subarrays are [1,3,5] and [1,3,5,2]."
      },
      {
        "input": "Input: nums = [1,1,1,1], minK = 1, maxK = 1",
        "output": "Output: 10",
        "explanation": "Explanation: Every subarray of nums is a fixed-bound subarray. There are 10 possible subarrays."
      }
    ],
    "topics": [
      "Array",
      "Queue",
      "Sliding Window",
      "Monotonic Queue"
    ],
    "difficulty": "Hard",
    "constraints": [
      "2 <= nums.length <= 105",
      "1 <= nums[i], minK, maxK <= 106"
    ],
    "hints": [
      "Can you solve the problem if all the numbers in the array were between minK and maxK inclusive?",
      "Think of the inclusion-exclusion principle.",
      "Divide the array into multiple subarrays such that each number in each subarray is between minK and maxK inclusive, solve the previous problem for each subarray, and sum all the answers."
    ]
  },
  {
    "title": "Longest Increasing Subsequence II",
    "description": "You are given an integer array nums and an integer k.\nFind the longest subsequence of nums that meets the following requirements:\n\nThe subsequence is strictly increasing and\nThe difference between adjacent elements in the subsequence is at most k.\n\nReturn the length of the longest subsequence that meets the requirements.\nA subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.\n \n",
    "examples": [
      {
        "input": "Input: nums = [4,2,1,4,3,4,5,8,15], k = 3",
        "output": "Output: 5",
        "explanation": ""
      },
      {
        "input": "Input: nums = [7,4,5,1,8,12,4,7], k = 5",
        "output": "Output: 4",
        "explanation": ""
      },
      {
        "input": "Input: nums = [1,5], k = 1",
        "output": "Output: 1",
        "explanation": ""
      }
    ],
    "topics": [
      "Array",
      "Divide and Conquer",
      "Dynamic Programming",
      "Binary Indexed Tree",
      "Segment Tree",
      "Queue",
      "Monotonic Queue"
    ],
    "difficulty": "Hard",
    "constraints": [
      "1 <= nums.length <= 105",
      "1 <= nums[i], k <= 105"
    ],
    "hints": [
      "We can use dynamic programming. Let dp[i][val] be the answer using only the first i + 1 elements, and the last element in the subsequence is equal to val.",
      "The only value that might change between dp[i - 1] and dp[i] are dp[i - 1][val] and dp[i][val].",
      "Try using dp[i - 1] and the fact that the second last element in the subsequence has to fall within a range to calculate dp[i][val].",
      "We can use a segment tree to find the maximum value in dp[i - 1] within a certain range."
    ]
  },
  {
    "title": "Count Number of Distinct Integers After Reverse Operations",
    "description": "You are given an array nums consisting of positive integers.\nYou have to take each integer in the array, reverse its digits, and add it to the end of the array. You should apply this operation to the original integers in nums.\nReturn the number of distinct integers in the final array.\n \n",
    "examples": [
      {
        "input": "Input: nums = [1,13,10,12,31]",
        "output": "Output: 6",
        "explanation": "Explanation: After including the reverse of each number, the resulting array is [1,13,10,12,31,1,31,1,21,13]."
      },
      {
        "input": "Input: nums = [2,2,2]",
        "output": "Output: 1",
        "explanation": "Explanation: After including the reverse of each number, the resulting array is [2,2,2,2,2,2]."
      }
    ],
    "topics": [
      "Array",
      "Hash Table",
      "Math"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= nums.length <= 105",
      "1 <= nums[i] <= 106"
    ],
    "hints": [
      "What data structure allows us to insert numbers and find the number of distinct numbers in it?",
      "Try using a set, insert all the numbers and their reverse into it, and return its size."
    ]
  },
  {
    "title": "Largest Positive Integer That Exists With Its Negative",
    "description": "Given an integer array nums that does not contain any zeros, find the largest positive integer k such that -k also exists in the array.\nReturn the positive integer k. If there is no such integer, return -1.\n \n",
    "examples": [
      {
        "input": "Input: nums = [-1,2,-3,3]",
        "output": "Output: 3",
        "explanation": "Explanation: 3 is the only valid k we can find in the array."
      },
      {
        "input": "Input: nums = [-1,10,6,7,-7,1]",
        "output": "Output: 7",
        "explanation": "Explanation: Both 1 and 7 have their corresponding negative values in the array. 7 has a larger value."
      },
      {
        "input": "Input: nums = [-10,8,6,7,-2,-3]",
        "output": "Output: -1",
        "explanation": "Explanation: There is no a single valid k, we return -1."
      }
    ],
    "topics": [
      "Array",
      "Hash Table",
      "Two Pointers",
      "Sorting"
    ],
    "difficulty": "Easy",
    "constraints": [
      "1 <= nums.length <= 1000",
      "-1000 <= nums[i] <= 1000",
      "nums[i] != 0"
    ],
    "hints": [
      "What data structure can help you to determine if an element exists?",
      "Would a hash table help?"
    ]
  },
  {
    "title": "Paths in Matrix Whose Sum Is Divisible by K",
    "description": "You are given a 0-indexed m x n integer matrix grid and an integer k. You are currently at position (0, 0) and you want to reach position (m - 1, n - 1) moving only down or right.\nReturn the number of paths where the sum of the elements on the path is divisible by k. Since the answer may be very large, return it modulo 109 + 7.\n \n",
    "examples": [
      {
        "input": "Input: grid = [[5,2,4],[3,0,5],[0,7,2]], k = 3",
        "output": "Output: 2",
        "explanation": "Explanation: There are two paths where the sum of the elements on the path is divisible by k."
      },
      {
        "input": "Input: grid = [[0,0]], k = 5",
        "output": "Output: 1",
        "explanation": "Explanation: The path highlighted in red has a sum of 0 + 0 = 0 which is divisible by 5."
      },
      {
        "input": "Input: grid = [[7,3,4,9],[2,3,6,2],[2,3,7,0]], k = 1",
        "output": "Output: 10",
        "explanation": "Explanation: Every integer is divisible by 1 so the sum of the elements on every possible path is divisible by k."
      }
    ],
    "topics": [
      "Array",
      "Dynamic Programming",
      "Matrix"
    ],
    "difficulty": "Hard",
    "constraints": [
      "m == grid.length",
      "n == grid[i].length",
      "1 <= m, n <= 5 * 104",
      "1 <= m * n <= 5 * 104",
      "0 <= grid[i][j] <= 100",
      "1 <= k <= 50"
    ],
    "hints": [
      "The actual numbers in grid do not matter. What matters are the remainders you get when you divide the numbers by k.",
      "We can use dynamic programming to solve this problem. What can we use as states?",
      "Let dp[i][j][value] represent the number of paths where the sum of the elements on the path has a remainder of value when divided by k."
    ]
  },
  {
    "title": "Using a Robot to Print the Lexicographically Smallest String",
    "description": "You are given a string s and a robot that currently holds an empty string t. Apply one of the following operations until s and t are both empty:\n\nRemove the first character of a string s and give it to the robot. The robot will append this character to the string t.\nRemove the last character of a string t and give it to the robot. The robot will write this character on paper.\n\nReturn the lexicographically smallest string that can be written on the paper.\n \n",
    "examples": [
      {
        "input": "Input: s = \"zza\"",
        "output": "Output: \"azz\"",
        "explanation": "Explanation: Let p denote the written string."
      },
      {
        "input": "Input: s = \"bac\"",
        "output": "Output: \"abc\"",
        "explanation": "Explanation: Let p denote the written string."
      },
      {
        "input": "Input: s = \"bdda\"",
        "output": "Output: \"addb\"",
        "explanation": "Explanation: Let p denote the written string."
      }
    ],
    "topics": [
      "Hash Table",
      "String",
      "Stack",
      "Greedy"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= s.length <= 105",
      "s consists of only English lowercase letters."
    ],
    "hints": [
      "If there are some character “a” ’ s in the string, they can be written on paper before anything else.",
      "Every character in the string before the last “a” should be written in reversed order.",
      "After the robot writes every “a” on paper, the same holds for other characters “b”, ”c”, …etc."
    ]
  },
  {
    "title": "Find The Original Array of Prefix Xor",
    "description": "You are given an integer array pref of size n. Find and return the array arr of size n that satisfies:\n\npref[i] = arr[0] ^ arr[1] ^ ... ^ arr[i].\n\nNote that ^ denotes the bitwise-xor operation.\nIt can be proven that the answer is unique.\n \n",
    "examples": [
      {
        "input": "Input: pref = [5,2,0,3,1]",
        "output": "Output: [5,7,2,3,2]",
        "explanation": "Explanation: From the array [5,7,2,3,2] we have the following:"
      },
      {
        "input": "Input: pref = [13]",
        "output": "Output: [13]",
        "explanation": "Explanation: We have pref[0] = arr[0] = 13."
      }
    ],
    "topics": [
      "Array",
      "Bit Manipulation"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= pref.length <= 105",
      "0 <= pref[i] <= 106"
    ],
    "hints": [
      "Consider the following equation: x ^ a = b. How can you find x?",
      "Notice that arr[i] ^ pref[i-1] = pref[i]. This is the same as the previous equation."
    ]
  },
  {
    "title": "The Employee That Worked on the Longest Task",
    "description": "There are n employees, each with a unique id from 0 to n - 1.\nYou are given a 2D integer array logs where logs[i] = [idi, leaveTimei] where:\n\nidi is the id of the employee that worked on the ith task, and\nleaveTimei is the time at which the employee finished the ith task. All the values leaveTimei are unique.\n\nNote that the ith task starts the moment right after the (i - 1)th task ends, and the 0th task starts at time 0.\nReturn the id of the employee that worked the task with the longest time. If there is a tie between two or more employees, return the smallest id among them.\n \n",
    "examples": [
      {
        "input": "Input: n = 10, logs = [[0,3],[2,5],[0,9],[1,15]]",
        "output": "Output: 1",
        "explanation": "Explanation: "
      },
      {
        "input": "Input: n = 26, logs = [[1,1],[3,7],[2,12],[7,17]]",
        "output": "Output: 3",
        "explanation": "Explanation: "
      },
      {
        "input": "Input: n = 2, logs = [[0,10],[1,20]]",
        "output": "Output: 0",
        "explanation": "Explanation: "
      }
    ],
    "topics": [
      "Array"
    ],
    "difficulty": "Easy",
    "constraints": [
      "2 <= n <= 500",
      "1 <= logs.length <= 500",
      "logs[i].length == 2",
      "0 <= idi <= n - 1",
      "1 <= leaveTimei <= 500",
      "idi != idi+1",
      "leaveTimei are sorted in a strictly increasing order."
    ],
    "hints": [
      "Find the time of the longest task",
      "Store each employee’s longest task time in a hash table",
      "For employees that have the same longest task time, we only need the employee with the smallest ID"
    ]
  },
  {
    "title": "Number of Pairs Satisfying Inequality",
    "description": "You are given two 0-indexed integer arrays nums1 and nums2, each of size n, and an integer diff. Find the number of pairs (i, j) such that:\n\n0 <= i < j <= n - 1 and\nnums1[i] - nums1[j] <= nums2[i] - nums2[j] + diff.\n\nReturn the number of pairs that satisfy the conditions.\n \n",
    "examples": [
      {
        "input": "Input: nums1 = [3,2,5], nums2 = [2,2,1], diff = 1",
        "output": "Output: 3",
        "explanation": ""
      },
      {
        "input": "Input: nums1 = [3,-1], nums2 = [-2,2], diff = -1",
        "output": "Output: 0",
        "explanation": ""
      }
    ],
    "topics": [
      "Array",
      "Binary Search",
      "Divide and Conquer",
      "Binary Indexed Tree",
      "Segment Tree",
      "Merge Sort",
      "Ordered Set"
    ],
    "difficulty": "Hard",
    "constraints": [
      "n == nums1.length == nums2.length",
      "2 <= n <= 105",
      "-104 <= nums1[i], nums2[i] <= 104",
      "-104 <= diff <= 104"
    ],
    "hints": [
      "Try rearranging the equation.",
      "Once the equation is rearranged properly, think how a segment tree or a Fenwick tree can be used to solve the rearranged equation.",
      "Iterate through the array backwards."
    ]
  },
  {
    "title": "Longest Uploaded Prefix",
    "description": "You are given a stream of n videos, each represented by a distinct number from 1 to n that you need to \"upload\" to a server. You need to implement a data structure that calculates the length of the longest uploaded prefix at various points in the upload process.\nWe consider i to be an uploaded prefix if all videos in the range 1 to i (inclusive) have been uploaded to the server. The longest uploaded prefix is the maximum value of i that satisfies this definition.\n\nImplement the LUPrefix class:\n\nLUPrefix(int n) Initializes the object for a stream of n videos.\nvoid upload(int video) Uploads video to the server.\nint longest() Returns the length of the longest uploaded prefix defined above.\n\n \n",
    "examples": [
      {
        "input": "Input\n[\"LUPrefix\", \"upload\", \"longest\", \"upload\", \"longest\", \"upload\", \"longest\"]",
        "output": "Output\n[null, null, 0, null, 1, null, 3]",
        "explanation": "Explanation\nLUPrefix server = new LUPrefix(4);   // Initialize a stream of 4 videos."
      }
    ],
    "topics": [
      "Binary Search",
      "Union Find",
      "Design",
      "Binary Indexed Tree",
      "Segment Tree",
      "Heap (Priority Queue)",
      "Ordered Set"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= n <= 105",
      "1 <= video <= n",
      "All values of video are distinct.",
      "At most 2 * 105 calls in total will be made to upload and longest.",
      "At least one call will be made to longest."
    ],
    "hints": [
      "Maintain an array keeping track of whether video “i” has been uploaded yet."
    ]
  },
  {
    "title": "Partition String Into Substrings With Values at Most K",
    "description": "You are given a string s consisting of digits from 1 to 9 and an integer k.\nA partition of a string s is called good if:\n\nEach digit of s is part of exactly one substring.\nThe value of each substring is less than or equal to k.\n\nReturn the minimum number of substrings in a good partition of s. If no good partition of s exists, return -1.\nNote that:\n\nThe value of a string is its result when interpreted as an integer. For example, the value of \"123\" is 123 and the value of \"1\" is 1.\nA substring is a contiguous sequence of characters within a string.\n\n \n",
    "examples": [
      {
        "input": "Input: s = \"165462\", k = 60",
        "output": "Output: 4",
        "explanation": "Explanation: We can partition the string into substrings \"16\", \"54\", \"6\", and \"2\". Each substring has a value less than or equal to k = 60."
      },
      {
        "input": "Input: s = \"238182\", k = 5",
        "output": "Output: -1",
        "explanation": "Explanation: There is no good partition for this string."
      }
    ],
    "topics": [
      "String",
      "Dynamic Programming",
      "Greedy"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= s.length <= 105",
      "s[i] is a digit from '1' to '9'.",
      "1 <= k <= 109"
    ],
    "hints": []
  },
  {
    "title": "Maximum Deletions on a String",
    "description": "You are given a string s consisting of only lowercase English letters. In one operation, you can:\n\nDelete the entire string s, or\nDelete the first i letters of s if the first i letters of s are equal to the following i letters in s, for any i in the range 1 <= i <= s.length / 2.\n\nFor example, if s = \"ababc\", then in one operation, you could delete the first two letters of s to get \"abc\", since the first two letters of s and the following two letters of s are both equal to \"ab\".\nReturn the maximum number of operations needed to delete all of s.\n \n",
    "examples": [
      {
        "input": "Input: s = \"abcabcdabc\"",
        "output": "Output: 2",
        "explanation": ""
      },
      {
        "input": "Input: s = \"aaabaab\"",
        "output": "Output: 4",
        "explanation": ""
      },
      {
        "input": "Input: s = \"aaaaa\"",
        "output": "Output: 5",
        "explanation": "Explanation: In each operation, we can delete the first letter of s."
      }
    ],
    "topics": [
      "String",
      "Dynamic Programming",
      "Rolling Hash",
      "String Matching",
      "Hash Function"
    ],
    "difficulty": "Hard",
    "constraints": [
      "1 <= s.length <= 4000",
      "s consists only of lowercase English letters."
    ],
    "hints": [
      "We can use dynamic programming to find the answer. Create a 0-indexed dp array where dp[i] represents the maximum number of moves needed to remove the first i + 1 letters from s.",
      "What should we do if there is an i where it is impossible to remove the first i + 1 letters?",
      "Use a sentinel value such as -1 to show that it is impossible.",
      "How can we quickly determine if two substrings of s are equal? We can use hashing."
    ]
  },
  {
    "title": "Minimize XOR",
    "description": "Given two positive integers num1 and num2, find the positive integer x such that:\n\nx has the same number of set bits as num2, and\nThe value x XOR num1 is minimal.\n\nNote that XOR is the bitwise XOR operation.\nReturn the integer x. The test cases are generated such that x is uniquely determined.\nThe number of set bits of an integer is the number of 1's in its binary representation.\n \n",
    "examples": [
      {
        "input": "Input: num1 = 3, num2 = 5",
        "output": "Output: 3",
        "explanation": ""
      },
      {
        "input": "Input: num1 = 1, num2 = 12",
        "output": "Output: 3",
        "explanation": ""
      }
    ],
    "topics": [
      "Greedy",
      "Bit Manipulation"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= num1, num2 <= 109"
    ],
    "hints": [
      "To arrive at a small xor, try to turn off some bits from num1",
      "If there are still left bits to set, try to set them from the least significant bit"
    ]
  },
  {
    "title": "Maximum Sum of an Hourglass",
    "description": "You are given an m x n integer matrix grid.\nWe define an hourglass as a part of the matrix with the following form:\n\nReturn the maximum sum of the elements of an hourglass.\nNote that an hourglass cannot be rotated and must be entirely contained within the matrix.\n \n",
    "examples": [
      {
        "input": "Input: grid = [[6,2,1,3],[4,2,1,5],[9,2,8,7],[4,1,2,9]]",
        "output": "Output: 30",
        "explanation": "Explanation: The cells shown above represent the hourglass with the maximum sum: 6 + 2 + 1 + 2 + 9 + 2 + 8 = 30."
      },
      {
        "input": "Input: grid = [[1,2,3],[4,5,6],[7,8,9]]",
        "output": "Output: 35",
        "explanation": "Explanation: There is only one hourglass in the matrix, with the sum: 1 + 2 + 3 + 5 + 7 + 8 + 9 = 35."
      }
    ],
    "topics": [
      "Array",
      "Matrix",
      "Prefix Sum"
    ],
    "difficulty": "Medium",
    "constraints": [
      "m == grid.length",
      "n == grid[i].length",
      "3 <= m, n <= 150",
      "0 <= grid[i][j] <= 106"
    ],
    "hints": [
      "Each 3x3 submatrix has exactly one hourglass.",
      "Find the sum of each hourglass in the matrix and return the largest of these values."
    ]
  },
  {
    "title": "Number of Common Factors",
    "description": "Given two positive integers a and b, return the number of common factors of a and b.\nAn integer x is a common factor of a and b if x divides both a and b.\n \n",
    "examples": [
      {
        "input": "Input: a = 12, b = 6",
        "output": "Output: 4",
        "explanation": "Explanation: The common factors of 12 and 6 are 1, 2, 3, 6."
      },
      {
        "input": "Input: a = 25, b = 30",
        "output": "Output: 2",
        "explanation": "Explanation: The common factors of 25 and 30 are 1, 5."
      }
    ],
    "topics": [
      "Math",
      "Enumeration",
      "Number Theory"
    ],
    "difficulty": "Easy",
    "constraints": [
      "1 <= a, b <= 1000"
    ],
    "hints": [
      "For each integer in range [1,1000], check if it’s divisible by both A and B."
    ]
  },
  {
    "title": "Number of Good Paths",
    "description": "There is a tree (i.e. a connected, undirected graph with no cycles) consisting of n nodes numbered from 0 to n - 1 and exactly n - 1 edges.\nYou are given a 0-indexed integer array vals of length n where vals[i] denotes the value of the ith node. You are also given a 2D integer array edges where edges[i] = [ai, bi] denotes that there exists an undirected edge connecting nodes ai and bi.\nA good path is a simple path that satisfies the following conditions:\n\nThe starting node and the ending node have the same value.\nAll nodes between the starting node and the ending node have values less than or equal to the starting node (i.e. the starting node's value should be the maximum value along the path).\n\nReturn the number of distinct good paths.\nNote that a path and its reverse are counted as the same path. For example, 0 -> 1 is considered to be the same as 1 -> 0. A single node is also considered as a valid path.\n \n",
    "examples": [
      {
        "input": "Input: vals = [1,3,2,1,3], edges = [[0,1],[0,2],[2,3],[2,4]]",
        "output": "Output: 6",
        "explanation": "Explanation: There are 5 good paths consisting of a single node."
      },
      {
        "input": "Input: vals = [1,1,2,2,3], edges = [[0,1],[1,2],[2,3],[2,4]]",
        "output": "Output: 7",
        "explanation": "Explanation: There are 5 good paths consisting of a single node."
      },
      {
        "input": "Input: vals = [1], edges = []",
        "output": "Output: 1",
        "explanation": "Explanation: The tree consists of only one node, so there is one good path."
      }
    ],
    "topics": [
      "Array",
      "Tree",
      "Union Find",
      "Graph"
    ],
    "difficulty": "Hard",
    "constraints": [
      "n == vals.length",
      "1 <= n <= 3 * 104",
      "0 <= vals[i] <= 105",
      "edges.length == n - 1",
      "edges[i].length == 2",
      "0 <= ai, bi < n",
      "ai != bi",
      "edges represents a valid tree."
    ],
    "hints": [
      "Can you process nodes from smallest to largest value?",
      "Try to build the graph from nodes with the smallest value to the largest value.",
      "May union find help?"
    ]
  },
  {
    "title": "Find All Good Indices",
    "description": "You are given a 0-indexed integer array nums of size n and a positive integer k.\nWe call an index i in the range k <= i < n - k good if the following conditions are satisfied:\n\nThe k elements that are just before the index i are in non-increasing order.\nThe k elements that are just after the index i are in non-decreasing order.\n\nReturn an array of all good indices sorted in increasing order.\n \n",
    "examples": [
      {
        "input": "Input: nums = [2,1,1,1,3,4,1], k = 2",
        "output": "Output: [2,3]",
        "explanation": "Explanation: There are two good indices in the array:"
      },
      {
        "input": "Input: nums = [2,1,1,2], k = 2",
        "output": "Output: []",
        "explanation": "Explanation: There are no good indices in this array."
      }
    ],
    "topics": [
      "Array",
      "Dynamic Programming",
      "Prefix Sum"
    ],
    "difficulty": "Medium",
    "constraints": [
      "n == nums.length",
      "3 <= n <= 105",
      "1 <= nums[i] <= 106",
      "1 <= k <= n / 2"
    ],
    "hints": [
      "Iterate over all indices i. How do you quickly check the two conditions?",
      "Precompute for each index whether the conditions are satisfied on the left and the right of the index. You can do that with two iterations, from left to right and right to left."
    ]
  },
  {
    "title": "Longest Subarray With Maximum Bitwise AND",
    "description": "You are given an integer array nums of size n.\nConsider a non-empty subarray from nums that has the maximum possible bitwise AND.\n\nIn other words, let k be the maximum value of the bitwise AND of any subarray of nums. Then, only subarrays with a bitwise AND equal to k should be considered.\n\nReturn the length of the longest such subarray.\nThe bitwise AND of an array is the bitwise AND of all the numbers in it.\nA subarray is a contiguous sequence of elements within an array.\n \n",
    "examples": [
      {
        "input": "Input: nums = [1,2,3,3,2,2]",
        "output": "Output: 2",
        "explanation": ""
      },
      {
        "input": "Input: nums = [1,2,3,4]",
        "output": "Output: 1",
        "explanation": ""
      }
    ],
    "topics": [
      "Array",
      "Bit Manipulation",
      "Brainteaser"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= nums.length <= 105",
      "1 <= nums[i] <= 106"
    ],
    "hints": [
      "Notice that the bitwise AND of two different numbers will always be strictly less than the maximum of those two numbers.",
      "What does that tell us about the nature of the subarray that we should choose?"
    ]
  },
  {
    "title": "Sort the People",
    "description": "You are given an array of strings names, and an array heights that consists of distinct positive integers. Both arrays are of length n.\nFor each index i, names[i] and heights[i] denote the name and height of the ith person.\nReturn names sorted in descending order by the people's heights.\n \n",
    "examples": [
      {
        "input": "Input: names = [\"Mary\",\"John\",\"Emma\"], heights = [180,165,170]",
        "output": "Output: [\"Mary\",\"Emma\",\"John\"]",
        "explanation": "Explanation: Mary is the tallest, followed by Emma and John."
      },
      {
        "input": "Input: names = [\"Alice\",\"Bob\",\"Bob\"], heights = [155,185,150]",
        "output": "Output: [\"Bob\",\"Alice\",\"Bob\"]",
        "explanation": "Explanation: The first Bob is the tallest, followed by Alice and the second Bob."
      }
    ],
    "topics": [
      "Array",
      "Hash Table",
      "String",
      "Sorting"
    ],
    "difficulty": "Easy",
    "constraints": [
      "n == names.length == heights.length",
      "1 <= n <= 103",
      "1 <= names[i].length <= 20",
      "1 <= heights[i] <= 105",
      "names[i] consists of lower and upper case English letters.",
      "All the values of heights are distinct."
    ],
    "hints": [
      "Find the tallest person and swap with the first person, then find the second tallest person and swap with the second person, etc. Repeat until you fix all n people."
    ]
  },
  {
    "title": "Minimum Money Required Before Transactions",
    "description": "You are given a 0-indexed 2D integer array transactions, where transactions[i] = [costi, cashbacki].\nThe array describes transactions, where each transaction must be completed exactly once in some order. At any given moment, you have a certain amount of money. In order to complete transaction i, money >= costi must hold true. After performing a transaction, money becomes money - costi + cashbacki.\nReturn the minimum amount of money required before any transaction so that all of the transactions can be completed regardless of the order of the transactions.\n \n",
    "examples": [
      {
        "input": "Input: transactions = [[2,1],[5,0],[4,2]]",
        "output": "Output: 10",
        "explanation": ""
      },
      {
        "input": "Input: transactions = [[3,0],[0,3]]",
        "output": "Output: 3",
        "explanation": ""
      }
    ],
    "topics": [
      "Array",
      "Greedy",
      "Sorting"
    ],
    "difficulty": "Hard",
    "constraints": [
      "1 <= transactions.length <= 105",
      "transactions[i].length == 2",
      "0 <= costi, cashbacki <= 109"
    ],
    "hints": [
      "Split transactions that have cashback greater or equal to cost apart from transactions that have cashback less than cost. You will always earn money in the first scenario.",
      "For transactions that have cashback greater or equal to cost, sort them by cost in descending order.",
      "For transactions that have cashback less than cost, sort them by cashback in ascending order."
    ]
  },
  {
    "title": "Smallest Subarrays With Maximum Bitwise OR",
    "description": "You are given a 0-indexed array nums of length n, consisting of non-negative integers. For each index i from 0 to n - 1, you must determine the size of the minimum sized non-empty subarray of nums starting at i (inclusive) that has the maximum possible bitwise OR.\n\nIn other words, let Bij be the bitwise OR of the subarray nums[i...j]. You need to find the smallest subarray starting at i, such that bitwise OR of this subarray is equal to max(Bik) where i <= k <= n - 1.\n\nThe bitwise OR of an array is the bitwise OR of all the numbers in it.\nReturn an integer array answer of size n where answer[i] is the length of the minimum sized subarray starting at i with maximum bitwise OR.\nA subarray is a contiguous non-empty sequence of elements within an array.\n \n",
    "examples": [
      {
        "input": "Input: nums = [1,0,2,1,3]",
        "output": "Output: [3,3,2,2,1]",
        "explanation": ""
      },
      {
        "input": "Input: nums = [1,2]",
        "output": "Output: [2,1]",
        "explanation": ""
      }
    ],
    "topics": [
      "Array",
      "Binary Search",
      "Bit Manipulation",
      "Sliding Window"
    ],
    "difficulty": "Medium",
    "constraints": [
      "n == nums.length",
      "1 <= n <= 105",
      "0 <= nums[i] <= 109"
    ],
    "hints": [
      "Consider trying to solve the problem for each bit position separately.",
      "For each bit position, find the position of the next number that has a 1 in that position, if any.",
      "Take the maximum distance to such a number, including the current number.",
      "Iterate backwards to achieve a linear complexity."
    ]
  },
  {
    "title": "Maximum Matching of Players With Trainers",
    "description": "You are given a 0-indexed integer array players, where players[i] represents the ability of the ith player. You are also given a 0-indexed integer array trainers, where trainers[j] represents the training capacity of the jth trainer.\nThe ith player can match with the jth trainer if the player's ability is less than or equal to the trainer's training capacity. Additionally, the ith player can be matched with at most one trainer, and the jth trainer can be matched with at most one player.\nReturn the maximum number of matchings between players and trainers that satisfy these conditions.\n \n",
    "examples": [
      {
        "input": "Input: players = [4,7,9], trainers = [8,2,5,8]",
        "output": "Output: 2",
        "explanation": ""
      },
      {
        "input": "Input: players = [1,1,1], trainers = [10]",
        "output": "Output: 1",
        "explanation": ""
      }
    ],
    "topics": [
      "Array",
      "Two Pointers",
      "Greedy",
      "Sorting"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= players.length, trainers.length <= 105",
      "1 <= players[i], trainers[j] <= 109"
    ],
    "hints": [
      "Sort both the arrays.",
      "Construct the matching greedily."
    ]
  },
  {
    "title": "Count Days Spent Together",
    "description": "Alice and Bob are traveling to Rome for separate business meetings.\nYou are given 4 strings arriveAlice, leaveAlice, arriveBob, and leaveBob. Alice will be in the city from the dates arriveAlice to leaveAlice (inclusive), while Bob will be in the city from the dates arriveBob to leaveBob (inclusive). Each will be a 5-character string in the format \"MM-DD\", corresponding to the month and day of the date.\nReturn the total number of days that Alice and Bob are in Rome together.\nYou can assume that all dates occur in the same calendar year, which is not a leap year. Note that the number of days per month can be represented as: [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31].\n \n",
    "examples": [
      {
        "input": "Input: arriveAlice = \"08-15\", leaveAlice = \"08-18\", arriveBob = \"08-16\", leaveBob = \"08-19\"",
        "output": "Output: 3",
        "explanation": "Explanation: Alice will be in Rome from August 15 to August 18. Bob will be in Rome from August 16 to August 19. They are both in Rome together on August 16th, 17th, and 18th, so the answer is 3."
      },
      {
        "input": "Input: arriveAlice = \"10-01\", leaveAlice = \"10-31\", arriveBob = \"11-01\", leaveBob = \"12-31\"",
        "output": "Output: 0",
        "explanation": "Explanation: There is no day when Alice and Bob are in Rome together, so we return 0."
      }
    ],
    "topics": [
      "Math",
      "String"
    ],
    "difficulty": "Easy",
    "constraints": [
      "All dates are provided in the format \"MM-DD\".",
      "Alice and Bob's arrival dates are earlier than or equal to their leaving dates.",
      "The given dates are valid dates of a non-leap year."
    ],
    "hints": [
      "For a given day, determine if Alice or Bob or both are in Rome.",
      "Brute force all 365 days for both Alice and Bob."
    ]
  },
  {
    "title": "Sum of Prefix Scores of Strings",
    "description": "You are given an array words of size n consisting of non-empty strings.\nWe define the score of a string word as the number of strings words[i] such that word is a prefix of words[i].\n\nFor example, if words = [\"a\", \"ab\", \"abc\", \"cab\"], then the score of \"ab\" is 2, since \"ab\" is a prefix of both \"ab\" and \"abc\".\n\nReturn an array answer of size n where answer[i] is the sum of scores of every non-empty prefix of words[i].\nNote that a string is considered as a prefix of itself.\n \n",
    "examples": [
      {
        "input": "Input: words = [\"abc\",\"ab\",\"bc\",\"b\"]",
        "output": "Output: [5,4,3,2]",
        "explanation": "Explanation: The answer for each string is the following:"
      },
      {
        "input": "Input: words = [\"abcd\"]",
        "output": "Output: [4]",
        "explanation": ""
      }
    ],
    "topics": [
      "Array",
      "String",
      "Trie",
      "Counting"
    ],
    "difficulty": "Hard",
    "constraints": [
      "1 <= words.length <= 1000",
      "1 <= words[i].length <= 1000",
      "words[i] consists of lowercase English letters."
    ],
    "hints": [
      "What data structure will allow you to efficiently keep track of the score of each prefix?",
      "Use a Trie. Insert all the words into it, and keep a counter at each node that will tell you how many times we have visited each prefix."
    ]
  },
  {
    "title": "Reverse Odd Levels of Binary Tree",
    "description": "Given the root of a perfect binary tree, reverse the node values at each odd level of the tree.\n\nFor example, suppose the node values at level 3 are [2,1,3,4,7,11,29,18], then it should become [18,29,11,7,4,3,1,2].\n\nReturn the root of the reversed tree.\nA binary tree is perfect if all parent nodes have two children and all leaves are on the same level.\nThe level of a node is the number of edges along the path between it and the root node.\n \n",
    "examples": [
      {
        "input": "Input: root = [2,3,5,8,13,21,34]",
        "output": "Output: [2,5,3,8,13,21,34]",
        "explanation": "Explanation: "
      },
      {
        "input": "Input: root = [7,13,11]",
        "output": "Output: [7,11,13]",
        "explanation": "Explanation: "
      },
      {
        "input": "Input: root = [0,1,2,0,0,0,0,1,1,1,1,2,2,2,2]",
        "output": "Output: [0,2,1,0,0,0,0,2,2,2,2,1,1,1,1]",
        "explanation": "Explanation: "
      }
    ],
    "topics": [
      "Tree",
      "Depth-First Search",
      "Breadth-First Search",
      "Binary Tree"
    ],
    "difficulty": "Medium",
    "constraints": [
      "The number of nodes in the tree is in the range [1, 214].",
      "0 <= Node.val <= 105",
      "root is a perfect binary tree."
    ],
    "hints": [
      "Try to solve recursively for each level independently.",
      "While performing a depth-first search, pass the left and right nodes (which should be paired) to the next level. If the current level is odd, then reverse their values, or else recursively move to the next level."
    ]
  },
  {
    "title": "Length of the Longest Alphabetical Continuous Substring",
    "description": "An alphabetical continuous string is a string consisting of consecutive letters in the alphabet. In other words, it is any substring of the string \"abcdefghijklmnopqrstuvwxyz\".\n\nFor example, \"abc\" is an alphabetical continuous string, while \"acb\" and \"za\" are not.\n\nGiven a string s consisting of lowercase letters only, return the length of the longest alphabetical continuous substring.\n \n",
    "examples": [
      {
        "input": "Input: s = \"abacaba\"",
        "output": "Output: 2",
        "explanation": "Explanation: There are 4 distinct continuous substrings: \"a\", \"b\", \"c\" and \"ab\"."
      },
      {
        "input": "Input: s = \"abcde\"",
        "output": "Output: 5",
        "explanation": "Explanation: \"abcde\" is the longest continuous substring."
      }
    ],
    "topics": [
      "String"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= s.length <= 105",
      "s consists of only English lowercase letters."
    ],
    "hints": [
      "What is the longest possible continuous substring?",
      "The size of the longest possible continuous substring is at most 26, so we can just brute force the answer."
    ]
  },
  {
    "title": "Smallest Even Multiple",
    "description": "Given a positive integer n, return the smallest positive integer that is a multiple of both 2 and n.\n \n",
    "examples": [
      {
        "input": "Input: n = 5",
        "output": "Output: 10",
        "explanation": "Explanation: The smallest multiple of both 5 and 2 is 10."
      },
      {
        "input": "Input: n = 6",
        "output": "Output: 6",
        "explanation": "Explanation: The smallest multiple of both 6 and 2 is 6. Note that a number is a multiple of itself."
      }
    ],
    "topics": [
      "Math",
      "Number Theory"
    ],
    "difficulty": "Easy",
    "constraints": [
      "1 <= n <= 150"
    ],
    "hints": [
      "A guaranteed way to find a multiple of 2 and n is to multiply them together. When is this the answer, and when is there a smaller answer?",
      "There is a smaller answer when n is even."
    ]
  },
  {
    "title": "Divide Intervals Into Minimum Number of Groups",
    "description": "You are given a 2D integer array intervals where intervals[i] = [lefti, righti] represents the inclusive interval [lefti, righti].\nYou have to divide the intervals into one or more groups such that each interval is in exactly one group, and no two intervals that are in the same group intersect each other.\nReturn the minimum number of groups you need to make.\nTwo intervals intersect if there is at least one common number between them. For example, the intervals [1, 5] and [5, 8] intersect.\n \n",
    "examples": [
      {
        "input": "Input: intervals = [[5,10],[6,8],[1,5],[2,3],[1,10]]",
        "output": "Output: 3",
        "explanation": "Explanation: We can divide the intervals into the following groups:"
      },
      {
        "input": "Input: intervals = [[1,3],[5,6],[8,10],[11,13]]",
        "output": "Output: 1",
        "explanation": "Explanation: None of the intervals overlap, so we can put all of them in one group."
      }
    ],
    "topics": [
      "Array",
      "Two Pointers",
      "Greedy",
      "Sorting",
      "Heap (Priority Queue)",
      "Prefix Sum"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= intervals.length <= 105",
      "intervals[i].length == 2",
      "1 <= lefti <= righti <= 106"
    ],
    "hints": [
      "Can you find a different way to describe the question?",
      "The minimum number of groups we need is equivalent to the maximum number of intervals that overlap at some point. How can you find that?"
    ]
  },
  {
    "title": "Optimal Partition of String",
    "description": "Given a string s, partition the string into one or more substrings such that the characters in each substring are unique. That is, no letter appears in a single substring more than once.\nReturn the minimum number of substrings in such a partition.\nNote that each character should belong to exactly one substring in a partition.\n \n",
    "examples": [
      {
        "input": "Input: s = \"abacaba\"",
        "output": "Output: 4",
        "explanation": ""
      },
      {
        "input": "Input: s = \"ssssss\"",
        "output": "Output: 6",
        "explanation": ""
      }
    ],
    "topics": [
      "Hash Table",
      "String",
      "Greedy"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= s.length <= 105",
      "s consists of only English lowercase letters."
    ],
    "hints": [
      "Try to come up with a greedy approach.",
      "From left to right, extend every substring in the partition as much as possible."
    ]
  },
  {
    "title": "Most Frequent Even Element",
    "description": "Given an integer array nums, return the most frequent even element.\nIf there is a tie, return the smallest one. If there is no such element, return -1.\n \n",
    "examples": [
      {
        "input": "Input: nums = [0,1,2,2,4,4,1]",
        "output": "Output: 2",
        "explanation": ""
      },
      {
        "input": "Input: nums = [4,4,4,9,2,4]",
        "output": "Output: 4",
        "explanation": "Explanation: 4 is the even element appears the most."
      },
      {
        "input": "Input: nums = [29,47,21,41,13,37,25,7]",
        "output": "Output: -1",
        "explanation": "Explanation: There is no even element."
      }
    ],
    "topics": [
      "Array",
      "Hash Table",
      "Counting"
    ],
    "difficulty": "Easy",
    "constraints": [
      "1 <= nums.length <= 2000",
      "0 <= nums[i] <= 105"
    ],
    "hints": [
      "Could you count the frequency of each even element in the array?",
      "Would a hashmap help?"
    ]
  },
  {
    "title": "Task Scheduler II",
    "description": "You are given a 0-indexed array of positive integers tasks, representing tasks that need to be completed in order, where tasks[i] represents the type of the ith task.\nYou are also given a positive integer space, which represents the minimum number of days that must pass after the completion of a task before another task of the same type can be performed.\nEach day, until all tasks have been completed, you must either:\n\nComplete the next task from tasks, or\nTake a break.\n\nReturn the minimum number of days needed to complete all tasks.\n \n",
    "examples": [
      {
        "input": "Input: tasks = [1,2,1,2,3,1], space = 3",
        "output": "Output: 9",
        "explanation": ""
      },
      {
        "input": "Input: tasks = [5,8,8,5], space = 2",
        "output": "Output: 6",
        "explanation": ""
      }
    ],
    "topics": [
      "Array",
      "Hash Table",
      "Simulation"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= tasks.length <= 105",
      "1 <= tasks[i] <= 109",
      "1 <= space <= tasks.length"
    ],
    "hints": [
      "Try taking breaks as late as possible, such that tasks are still spaced appropriately.",
      "Whenever considering whether to complete the next task, if it is not the first task of its type, check how many days ago the previous task was completed and add an appropriate number of breaks."
    ]
  },
  {
    "title": "Maximum Rows Covered by Columns",
    "description": "You are given a 0-indexed m x n binary matrix matrix and an integer numSelect, which denotes the number of distinct columns you must select from matrix.\nLet us consider s = {c1, c2, ...., cnumSelect} as the set of columns selected by you. A row row is covered by s if:\n\nFor each cell matrix[row][col] (0 <= col <= n - 1) where matrix[row][col] == 1, col is present in s or,\nNo cell in row has a value of 1.\n\nYou need to choose numSelect columns such that the number of rows that are covered is maximized.\nReturn the maximum number of rows that can be covered by a set of numSelect columns.\n \n",
    "examples": [
      {
        "input": "Input: matrix = [[0,0,0],[1,0,1],[0,1,1],[0,0,1]], numSelect = 2",
        "output": "Output: 3",
        "explanation": "Explanation: One possible way to cover 3 rows is shown in the diagram above."
      },
      {
        "input": "Input: matrix = [[1],[0]], numSelect = 1",
        "output": "Output: 2",
        "explanation": "Explanation: Selecting the only column will result in both rows being covered since the entire matrix is selected."
      }
    ],
    "topics": [
      "Array",
      "Backtracking",
      "Bit Manipulation",
      "Matrix",
      "Enumeration"
    ],
    "difficulty": "Medium",
    "constraints": [
      "m == matrix.length",
      "n == matrix[i].length",
      "1 <= m, n <= 12",
      "matrix[i][j] is either 0 or 1.",
      "1 <= numSelect <= n"
    ],
    "hints": [
      "Try a brute-force approach.",
      "Iterate through all possible sets of exactly cols columns.",
      "For each valid set, check how many rows are covered, and return the maximum."
    ]
  },
  {
    "title": "Strictly Palindromic Number",
    "description": "An integer n is strictly palindromic if, for every base b between 2 and n - 2 (inclusive), the string representation of the integer n in base b is palindromic.\nGiven an integer n, return true if n is strictly palindromic and false otherwise.\nA string is palindromic if it reads the same forward and backward.\n \n",
    "examples": [
      {
        "input": "Input: n = 9",
        "output": "Output: false",
        "explanation": "Explanation: In base 2: 9 = 1001 (base 2), which is palindromic."
      },
      {
        "input": "Input: n = 4",
        "output": "Output: false",
        "explanation": "Explanation: We only consider base 2: 4 = 100 (base 2), which is not palindromic."
      }
    ],
    "topics": [
      "Math",
      "Two Pointers",
      "Brainteaser"
    ],
    "difficulty": "Medium",
    "constraints": [
      "4 <= n <= 105"
    ],
    "hints": [
      "Consider the representation of the given number in the base n - 2.",
      "The number n in base (n - 2) is always 12, which is not palindromic."
    ]
  },
  {
    "title": "Find Subarrays With Equal Sum",
    "description": "Given a 0-indexed integer array nums, determine whether there exist two subarrays of length 2 with equal sum. Note that the two subarrays must begin at different indices.\nReturn true if these subarrays exist, and false otherwise.\nA subarray is a contiguous non-empty sequence of elements within an array.\n \n",
    "examples": [
      {
        "input": "Input: nums = [4,2,4]",
        "output": "Output: true",
        "explanation": "Explanation: The subarrays with elements [4,2] and [2,4] have the same sum of 6."
      },
      {
        "input": "Input: nums = [1,2,3,4,5]",
        "output": "Output: false",
        "explanation": "Explanation: No two subarrays of size 2 have the same sum."
      },
      {
        "input": "Input: nums = [0,0,0]",
        "output": "Output: true",
        "explanation": "Explanation: The subarrays [nums[0],nums[1]] and [nums[1],nums[2]] have the same sum of 0. "
      }
    ],
    "topics": [
      "Array",
      "Hash Table"
    ],
    "difficulty": "Easy",
    "constraints": [
      "2 <= nums.length <= 1000",
      "-109 <= nums[i] <= 109"
    ],
    "hints": [
      "Use a counter to keep track of the subarray sums.",
      "Use a hashset to check if any two sums are equal."
    ]
  },
  {
    "title": "Meeting Rooms III",
    "description": "You are given an integer n. There are n rooms numbered from 0 to n - 1.\nYou are given a 2D integer array meetings where meetings[i] = [starti, endi] means that a meeting will be held during the half-closed time interval [starti, endi). All the values of starti are unique.\nMeetings are allocated to rooms in the following manner:\n\nEach meeting will take place in the unused room with the lowest number.\nIf there are no available rooms, the meeting will be delayed until a room becomes free. The delayed meeting should have the same duration as the original meeting.\nWhen a room becomes unused, meetings that have an earlier original start time should be given the room.\n\nReturn the number of the room that held the most meetings. If there are multiple rooms, return the room with the lowest number.\nA half-closed interval [a, b) is the interval between a and b including a and not including b.\n \n",
    "examples": [
      {
        "input": "Input: n = 2, meetings = [[0,10],[1,5],[2,7],[3,4]]",
        "output": "Output: 0",
        "explanation": ""
      },
      {
        "input": "Input: n = 3, meetings = [[1,20],[2,10],[3,5],[4,9],[6,8]]",
        "output": "Output: 1",
        "explanation": ""
      }
    ],
    "topics": [
      "Array",
      "Sorting",
      "Heap (Priority Queue)"
    ],
    "difficulty": "Hard",
    "constraints": [
      "1 <= n <= 100",
      "1 <= meetings.length <= 105",
      "meetings[i].length == 2",
      "0 <= starti < endi <= 5 * 105",
      "All the values of starti are unique."
    ],
    "hints": [
      "Sort meetings based on start times.",
      "Use two min heaps, the first one keeps track of the numbers of all the rooms that are free. The second heap keeps track of the end times of all the meetings that are happening and the room that they are in.",
      "Keep track of the number of times each room is used in an array.",
      "With each meeting, check if there are any free rooms. If there are, then use the room with the smallest number. Otherwise, assign the meeting to the room whose meeting will end the soonest."
    ]
  },
  {
    "title": "Longest Nice Subarray",
    "description": "You are given an array nums consisting of positive integers.\nWe call a subarray of nums nice if the bitwise AND of every pair of elements that are in different positions in the subarray is equal to 0.\nReturn the length of the longest nice subarray.\nA subarray is a contiguous part of an array.\nNote that subarrays of length 1 are always considered nice.\n \n",
    "examples": [
      {
        "input": "Input: nums = [1,3,8,48,10]",
        "output": "Output: 3",
        "explanation": "Explanation: The longest nice subarray is [3,8,48]. This subarray satisfies the conditions:"
      },
      {
        "input": "Input: nums = [3,1,5,11,13]",
        "output": "Output: 1",
        "explanation": "Explanation: The length of the longest nice subarray is 1. Any subarray of length 1 can be chosen."
      }
    ],
    "topics": [
      "Array",
      "Bit Manipulation",
      "Sliding Window"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= nums.length <= 105",
      "1 <= nums[i] <= 109"
    ],
    "hints": [
      "What is the maximum possible length of a nice subarray?",
      "The length of the longest nice subarray cannot exceed 30. Why is that?"
    ]
  },
  {
    "title": "Number of Ways to Reach a Position After Exactly k Steps",
    "description": "You are given two positive integers startPos and endPos. Initially, you are standing at position startPos on an infinite number line. With one step, you can move either one position to the left, or one position to the right.\nGiven a positive integer k, return the number of different ways to reach the position endPos starting from startPos, such that you perform exactly k steps. Since the answer may be very large, return it modulo 109 + 7.\nTwo ways are considered different if the order of the steps made is not exactly the same.\nNote that the number line includes negative integers.\n \n",
    "examples": [
      {
        "input": "Input: startPos = 1, endPos = 2, k = 3",
        "output": "Output: 3",
        "explanation": "Explanation: We can reach position 2 from 1 in exactly 3 steps in three ways:"
      },
      {
        "input": "Input: startPos = 2, endPos = 5, k = 10",
        "output": "Output: 0",
        "explanation": "Explanation: It is impossible to reach position 5 from position 2 in exactly 10 steps."
      }
    ],
    "topics": [
      "Math",
      "Dynamic Programming",
      "Combinatorics"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= startPos, endPos, k <= 1000"
    ],
    "hints": [
      "How many steps to the left and to the right do you need to make exactly?",
      "Does the order of the steps matter?",
      "Use combinatorics to find the number of ways to order the steps."
    ]
  },
  {
    "title": "Check Distances Between Same Letters",
    "description": "You are given a 0-indexed string s consisting of only lowercase English letters, where each letter in s appears exactly twice. You are also given a 0-indexed integer array distance of length 26.\nEach letter in the alphabet is numbered from 0 to 25 (i.e. 'a' -> 0, 'b' -> 1, 'c' -> 2, ... , 'z' -> 25).\nIn a well-spaced string, the number of letters between the two occurrences of the ith letter is distance[i]. If the ith letter does not appear in s, then distance[i] can be ignored.\nReturn true if s is a well-spaced string, otherwise return false.\n \n",
    "examples": [
      {
        "input": "Input: s = \"abaccb\", distance = [1,3,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]",
        "output": "Output: true",
        "explanation": ""
      },
      {
        "input": "Input: s = \"aa\", distance = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]",
        "output": "Output: false",
        "explanation": ""
      }
    ],
    "topics": [
      "Array",
      "Hash Table",
      "String"
    ],
    "difficulty": "Easy",
    "constraints": [
      "2 <= s.length <= 52",
      "s consists only of lowercase English letters.",
      "Each letter appears in s exactly twice.",
      "distance.length == 26",
      "0 <= distance[i] <= 50"
    ],
    "hints": [
      "Create an integer array of size 26 to keep track of the first occurrence of each letter.",
      "The number of letters between indices i and j is j - i - 1."
    ]
  },
  {
    "title": "Largest Palindromic Number",
    "description": "You are given a string num consisting of digits only.\nReturn the largest palindromic integer (in the form of a string) that can be formed using digits taken from num. It should not contain leading zeroes.\nNotes:\n\nYou do not need to use all the digits of num, but you must use at least one digit.\nThe digits can be reordered.\n\n \n",
    "examples": [
      {
        "input": "Input: num = \"444947137\"",
        "output": "Output: \"7449447\"",
        "explanation": "Explanation: "
      },
      {
        "input": "Input: num = \"00009\"",
        "output": "Output: \"9\"",
        "explanation": "Explanation: "
      }
    ],
    "topics": [
      "Hash Table",
      "String",
      "Greedy"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= num.length <= 105",
      "num consists of digits."
    ],
    "hints": [
      "In order to form a valid palindrome, other than the middle digit in an odd-length palindrome, every digit needs to exist on both sides.",
      "A longer palindrome implies a larger valued palindrome. For palindromes of the same length, the larger digits should occur first.",
      "We can count the occurrences of each digit and build the palindrome starting from the ends. Starting from the larger digits, if there are still at least 2 occurrences of a digit, we can place these digits on each side.",
      "Make sure to consider the special case for the center digit (if any) and zeroes. There should not be leading zeroes."
    ]
  },
  {
    "title": "Max Sum of a Pair With Equal Sum of Digits",
    "description": "You are given a 0-indexed array nums consisting of positive integers. You can choose two indices i and j, such that i != j, and the sum of digits of the number nums[i] is equal to that of nums[j].\nReturn the maximum value of nums[i] + nums[j] that you can obtain over all possible indices i and j that satisfy the conditions.\n \n",
    "examples": [
      {
        "input": "Input: nums = [18,43,36,13,7]",
        "output": "Output: 54",
        "explanation": "Explanation: The pairs (i, j) that satisfy the conditions are:"
      },
      {
        "input": "Input: nums = [10,12,19,14]",
        "output": "Output: -1",
        "explanation": "Explanation: There are no two numbers that satisfy the conditions, so we return -1."
      }
    ],
    "topics": [
      "Array",
      "Hash Table",
      "Sorting",
      "Heap (Priority Queue)"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= nums.length <= 105",
      "1 <= nums[i] <= 109"
    ],
    "hints": [
      "What is the largest possible sum of digits a number can have?",
      "Group the array elements by the sum of their digits, and find the largest two elements of each group."
    ]
  },
  {
    "title": "Build a Matrix With Conditions",
    "description": "You are given a positive integer k. You are also given:\n\na 2D integer array rowConditions of size n where rowConditions[i] = [abovei, belowi], and\na 2D integer array colConditions of size m where colConditions[i] = [lefti, righti].\n\nThe two arrays contain integers from 1 to k.\nYou have to build a k x k matrix that contains each of the numbers from 1 to k exactly once. The remaining cells should have the value 0.\nThe matrix should also satisfy the following conditions:\n\nThe number abovei should appear in a row that is strictly above the row at which the number belowi appears for all i from 0 to n - 1.\nThe number lefti should appear in a column that is strictly left of the column at which the number righti appears for all i from 0 to m - 1.\n\nReturn any matrix that satisfies the conditions. If no answer exists, return an empty matrix.\n \n",
    "examples": [
      {
        "input": "Input: k = 3, rowConditions = [[1,2],[3,2]], colConditions = [[2,1],[3,2]]",
        "output": "Output: [[3,0,0],[0,0,1],[0,2,0]]",
        "explanation": "Explanation: The diagram above shows a valid example of a matrix that satisfies all the conditions."
      },
      {
        "input": "Input: k = 3, rowConditions = [[1,2],[2,3],[3,1],[2,3]], colConditions = [[2,1]]",
        "output": "Output: []",
        "explanation": "Explanation: From the first two conditions, 3 has to be below 1 but the third conditions needs 3 to be above 1 to be satisfied."
      }
    ],
    "topics": [
      "Array",
      "Graph",
      "Topological Sort",
      "Matrix"
    ],
    "difficulty": "Hard",
    "constraints": [
      "2 <= k <= 400",
      "1 <= rowConditions.length, colConditions.length <= 104",
      "rowConditions[i].length == colConditions[i].length == 2",
      "1 <= abovei, belowi, lefti, righti <= k",
      "abovei != belowi",
      "lefti != righti"
    ],
    "hints": [
      "Can you think of the problem in terms of graphs?",
      "What algorithm allows you to find the order of nodes in a graph?"
    ]
  },
  {
    "title": "Minimum Amount of Time to Collect Garbage",
    "description": "You are given a 0-indexed array of strings garbage where garbage[i] represents the assortment of garbage at the ith house. garbage[i] consists only of the characters 'M', 'P' and 'G' representing one unit of metal, paper and glass garbage respectively. Picking up one unit of any type of garbage takes 1 minute.\nYou are also given a 0-indexed integer array travel where travel[i] is the number of minutes needed to go from house i to house i + 1.\nThere are three garbage trucks in the city, each responsible for picking up one type of garbage. Each garbage truck starts at house 0 and must visit each house in order; however, they do not need to visit every house.\nOnly one garbage truck may be used at any given moment. While one truck is driving or picking up garbage, the other two trucks cannot do anything.\nReturn the minimum number of minutes needed to pick up all the garbage.\n \n",
    "examples": [
      {
        "input": "Input: garbage = [\"G\",\"P\",\"GP\",\"GG\"], travel = [2,4,3]",
        "output": "Output: 21",
        "explanation": ""
      },
      {
        "input": "Input: garbage = [\"MMM\",\"PGM\",\"GP\"], travel = [3,10]",
        "output": "Output: 37",
        "explanation": ""
      }
    ],
    "topics": [
      "Array",
      "String",
      "Prefix Sum"
    ],
    "difficulty": "Medium",
    "constraints": [
      "2 <= garbage.length <= 105",
      "garbage[i] consists of only the letters 'M', 'P', and 'G'.",
      "1 <= garbage[i].length <= 10",
      "travel.length == garbage.length - 1",
      "1 <= travel[i] <= 100"
    ],
    "hints": [
      "Where can we save time? By not visiting all the houses.",
      "For each type of garbage, find the house with the highest index that has at least 1 unit of this type of garbage."
    ]
  },
  {
    "title": "Removing Stars From a String",
    "description": "You are given a string s, which contains stars *.\nIn one operation, you can:\n\nChoose a star in s.\nRemove the closest non-star character to its left, as well as remove the star itself.\n\nReturn the string after all stars have been removed.\nNote:\n\nThe input will be generated such that the operation is always possible.\nIt can be shown that the resulting string will always be unique.\n\n \n",
    "examples": [
      {
        "input": "Input: s = \"leet**cod*e\"",
        "output": "Output: \"lecoe\"",
        "explanation": "Explanation: Performing the removals from left to right:"
      },
      {
        "input": "Input: s = \"erase*****\"",
        "output": "Output: \"\"",
        "explanation": "Explanation: The entire string is removed, so we return an empty string."
      }
    ],
    "topics": [
      "String",
      "Stack",
      "Simulation"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= s.length <= 105",
      "s consists of lowercase English letters and stars *.",
      "The operation above can be performed on s."
    ],
    "hints": [
      "What data structure could we use to efficiently perform these removals?",
      "Use a stack to store the characters. Pop one character off the stack at each star. Otherwise, we push the character onto the stack."
    ]
  },
  {
    "title": "Longest Subsequence With Limited Sum",
    "description": "You are given an integer array nums of length n, and an integer array queries of length m.\nReturn an array answer of length m where answer[i] is the maximum size of a subsequence that you can take from nums such that the sum of its elements is less than or equal to queries[i].\nA subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.\n \n",
    "examples": [
      {
        "input": "Input: nums = [4,5,2,1], queries = [3,10,21]",
        "output": "Output: [2,3,4]",
        "explanation": "Explanation: We answer the queries as follows:"
      },
      {
        "input": "Input: nums = [2,3,4,5], queries = [1]",
        "output": "Output: [0]",
        "explanation": "Explanation: The empty subsequence is the only subsequence that has a sum less than or equal to 1, so answer[0] = 0."
      }
    ],
    "topics": [
      "Array",
      "Binary Search",
      "Greedy",
      "Sorting",
      "Prefix Sum"
    ],
    "difficulty": "Easy",
    "constraints": [
      "n == nums.length",
      "m == queries.length",
      "1 <= n, m <= 1000",
      "1 <= nums[i], queries[i] <= 106"
    ],
    "hints": [
      "Solve each query independently.",
      "When solving a query, which elements of nums should you choose to make the subsequence as long as possible?",
      "Choose the smallest elements in nums that add up to a sum less than the query."
    ]
  },
  {
    "title": "Maximum Segment Sum After Removals",
    "description": "You are given two 0-indexed integer arrays nums and removeQueries, both of length n. For the ith query, the element in nums at the index removeQueries[i] is removed, splitting nums into different segments.\nA segment is a contiguous sequence of positive integers in nums. A segment sum is the sum of every element in a segment.\nReturn an integer array answer, of length n, where answer[i] is the maximum segment sum after applying the ith removal.\nNote: The same index will not be removed more than once.\n \n",
    "examples": [
      {
        "input": "Input: nums = [1,2,5,6,1], removeQueries = [0,3,2,4,1]",
        "output": "Output: [14,7,2,2,0]",
        "explanation": "Explanation: Using 0 to indicate a removed element, the answer is as follows:"
      },
      {
        "input": "Input: nums = [3,2,11,1], removeQueries = [3,2,1,0]",
        "output": "Output: [16,5,3,0]",
        "explanation": "Explanation: Using 0 to indicate a removed element, the answer is as follows:"
      }
    ],
    "topics": [
      "Array",
      "Union Find",
      "Prefix Sum",
      "Ordered Set"
    ],
    "difficulty": "Hard",
    "constraints": [
      "n == nums.length == removeQueries.length",
      "1 <= n <= 105",
      "1 <= nums[i] <= 109",
      "0 <= removeQueries[i] < n",
      "All the values of removeQueries are unique."
    ],
    "hints": [
      "Use a sorted data structure to collect removal points and store the segments.",
      "Use a heap or priority queue to store segment sums and their corresponding boundaries.",
      "Make sure to remove invalid segments from the heap."
    ]
  },
  {
    "title": "Shifting Letters II",
    "description": "You are given a string s of lowercase English letters and a 2D integer array shifts where shifts[i] = [starti, endi, directioni]. For every i, shift the characters in s from the index starti to the index endi (inclusive) forward if directioni = 1, or shift the characters backward if directioni = 0.\nShifting a character forward means replacing it with the next letter in the alphabet (wrapping around so that 'z' becomes 'a'). Similarly, shifting a character backward means replacing it with the previous letter in the alphabet (wrapping around so that 'a' becomes 'z').\nReturn the final string after all such shifts to s are applied.\n \n",
    "examples": [
      {
        "input": "Input: s = \"abc\", shifts = [[0,1,0],[1,2,1],[0,2,1]]",
        "output": "Output: \"ace\"",
        "explanation": "Explanation: Firstly, shift the characters from index 0 to index 1 backward. Now s = \"zac\"."
      },
      {
        "input": "Input: s = \"dztz\", shifts = [[0,0,0],[1,1,1]]",
        "output": "Output: \"catz\"",
        "explanation": "Explanation: Firstly, shift the characters from index 0 to index 0 backward. Now s = \"cztz\"."
      }
    ],
    "topics": [
      "Array",
      "String",
      "Prefix Sum"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= s.length, shifts.length <= 5 * 104",
      "shifts[i].length == 3",
      "0 <= starti <= endi < s.length",
      "0 <= directioni <= 1",
      "s consists of lowercase English letters."
    ],
    "hints": [
      "Instead of shifting every character in each shift, could you keep track of which characters are shifted and by how much across all shifts?",
      "Try marking the start and ends of each shift, then perform a prefix sum of the shifts."
    ]
  },
  {
    "title": "Time Needed to Rearrange a Binary String",
    "description": "You are given a binary string s. In one second, all occurrences of \"01\" are simultaneously replaced with \"10\". This process repeats until no occurrences of \"01\" exist.\nReturn the number of seconds needed to complete this process.\n \n",
    "examples": [
      {
        "input": "Input: s = \"0110101\"",
        "output": "Output: 4",
        "explanation": "Explanation: "
      },
      {
        "input": "Input: s = \"11100\"",
        "output": "Output: 0",
        "explanation": ""
      }
    ],
    "topics": [
      "String",
      "Dynamic Programming",
      "Simulation"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= s.length <= 1000",
      "s[i] is either '0' or '1'.",
      "",
      " ",
      "Follow up:",
      "Can you solve this problem in O(n) time complexity?"
    ],
    "hints": [
      "Try replicating the steps from the problem statement.",
      "Perform the replacements simultaneously, and return the number of times the process repeats."
    ]
  },
  {
    "title": "Minimum Recolors to Get K Consecutive Black Blocks",
    "description": "You are given a 0-indexed string blocks of length n, where blocks[i] is either 'W' or 'B', representing the color of the ith block. The characters 'W' and 'B' denote the colors white and black, respectively.\nYou are also given an integer k, which is the desired number of consecutive black blocks.\nIn one operation, you can recolor a white block such that it becomes a black block.\nReturn the minimum number of operations needed such that there is at least one occurrence of k consecutive black blocks.\n \n",
    "examples": [
      {
        "input": "Input: blocks = \"WBBWWBBWBW\", k = 7",
        "output": "Output: 3",
        "explanation": ""
      },
      {
        "input": "Input: blocks = \"WBWBBBW\", k = 2",
        "output": "Output: 0",
        "explanation": ""
      }
    ],
    "topics": [
      "String",
      "Sliding Window"
    ],
    "difficulty": "Easy",
    "constraints": [
      "n == blocks.length",
      "1 <= n <= 100",
      "blocks[i] is either 'W' or 'B'.",
      "1 <= k <= n"
    ],
    "hints": [
      "Iterate through all possible consecutive substrings of k characters.",
      "Find the number of changes for each substring to make all blocks black, and return the minimum of these."
    ]
  },
  {
    "title": "Find the K-Sum of an Array",
    "description": "You are given an integer array nums and a positive integer k. You can choose any subsequence of the array and sum all of its elements together.\nWe define the K-Sum of the array as the kth largest subsequence sum that can be obtained (not necessarily distinct).\nReturn the K-Sum of the array.\nA subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.\nNote that the empty subsequence is considered to have a sum of 0.\n \n",
    "examples": [
      {
        "input": "Input: nums = [2,4,-2], k = 5",
        "output": "Output: 2",
        "explanation": "Explanation: All the possible subsequence sums that we can obtain are the following sorted in decreasing order:"
      },
      {
        "input": "Input: nums = [1,-2,3,4,-10,12], k = 16",
        "output": "Output: 10",
        "explanation": "Explanation: The 16-Sum of the array is 10."
      }
    ],
    "topics": [
      "Array",
      "Sorting",
      "Heap (Priority Queue)"
    ],
    "difficulty": "Hard",
    "constraints": [
      "n == nums.length",
      "1 <= n <= 105",
      "-109 <= nums[i] <= 109",
      "1 <= k <= min(2000, 2n)"
    ],
    "hints": [
      "Start from the largest sum possible, and keep finding the next largest sum until you reach the kth sum.",
      "Starting from a sum, what are the two next largest sums that you can obtain from it?"
    ]
  },
  {
    "title": "Amount of Time for Binary Tree to Be Infected",
    "description": "You are given the root of a binary tree with unique values, and an integer start. At minute 0, an infection starts from the node with value start.\nEach minute, a node becomes infected if:\n\nThe node is currently uninfected.\nThe node is adjacent to an infected node.\n\nReturn the number of minutes needed for the entire tree to be infected.\n \n",
    "examples": [
      {
        "input": "Input: root = [1,5,3,null,4,10,6,9,2], start = 3",
        "output": "Output: 4",
        "explanation": "Explanation: The following nodes are infected during:"
      },
      {
        "input": "Input: root = [1], start = 1",
        "output": "Output: 0",
        "explanation": "Explanation: At minute 0, the only node in the tree is infected so we return 0."
      }
    ],
    "topics": [
      "Tree",
      "Depth-First Search",
      "Breadth-First Search",
      "Binary Tree"
    ],
    "difficulty": "Medium",
    "constraints": [
      "The number of nodes in the tree is in the range [1, 105].",
      "1 <= Node.val <= 105",
      "Each node has a unique value.",
      "A node with a value of start exists in the tree."
    ],
    "hints": [
      "Convert the tree to an undirected graph to make it easier to handle.",
      "Use BFS starting at the start node to find the distance between each node and the start node. The answer is the maximum distance."
    ]
  },
  {
    "title": "Minimum Hours of Training to Win a Competition",
    "description": "You are entering a competition, and are given two positive integers initialEnergy and initialExperience denoting your initial energy and initial experience respectively.\nYou are also given two 0-indexed integer arrays energy and experience, both of length n.\nYou will face n opponents in order. The energy and experience of the ith opponent is denoted by energy[i] and experience[i] respectively. When you face an opponent, you need to have both strictly greater experience and energy to defeat them and move to the next opponent if available.\nDefeating the ith opponent increases your experience by experience[i], but decreases your energy by energy[i].\nBefore starting the competition, you can train for some number of hours. After each hour of training, you can either choose to increase your initial experience by one, or increase your initial energy by one.\nReturn the minimum number of training hours required to defeat all n opponents.\n \n",
    "examples": [
      {
        "input": "Input: initialEnergy = 5, initialExperience = 3, energy = [1,4,3,2], experience = [2,6,3,1]",
        "output": "Output: 8",
        "explanation": "Explanation: You can increase your energy to 11 after 6 hours of training, and your experience to 5 after 2 hours of training."
      },
      {
        "input": "Input: initialEnergy = 2, initialExperience = 4, energy = [1], experience = [3]",
        "output": "Output: 0",
        "explanation": "Explanation: You do not need any additional energy or experience to win the competition, so we return 0."
      }
    ],
    "topics": [
      "Array",
      "Greedy"
    ],
    "difficulty": "Easy",
    "constraints": [
      "n == energy.length == experience.length",
      "1 <= n <= 100",
      "1 <= initialEnergy, initialExperience, energy[i], experience[i] <= 100"
    ],
    "hints": [
      "Find the minimum number of training hours needed for the energy and experience separately, and sum the results.",
      "Try to increase the energy and experience until you find how much is enough to win the competition."
    ]
  },
  {
    "title": "Count Special Integers",
    "description": "We call a positive integer special if all of its digits are distinct.\nGiven a positive integer n, return the number of special integers that belong to the interval [1, n].\n \n",
    "examples": [
      {
        "input": "Input: n = 20",
        "output": "Output: 19",
        "explanation": "Explanation: All the integers from 1 to 20, except 11, are special. Thus, there are 19 special integers."
      },
      {
        "input": "Input: n = 5",
        "output": "Output: 5",
        "explanation": "Explanation: All the integers from 1 to 5 are special."
      },
      {
        "input": "Input: n = 135",
        "output": "Output: 110",
        "explanation": "Explanation: There are 110 integers from 1 to 135 that are special."
      }
    ],
    "topics": [
      "Math",
      "Dynamic Programming"
    ],
    "difficulty": "Hard",
    "constraints": [
      "1 <= n <= 2 * 109"
    ],
    "hints": [
      "Try to think of dynamic programming.",
      "Use the idea of digit dynamic programming to build the numbers, in addition to a bitmask that will tell which digits you have used so far on the number that you are building."
    ]
  },
  {
    "title": "Construct Smallest Number From DI String",
    "description": "You are given a 0-indexed string pattern of length n consisting of the characters 'I' meaning increasing and 'D' meaning decreasing.\nA 0-indexed string num of length n + 1 is created using the following conditions:\n\nnum consists of the digits '1' to '9', where each digit is used at most once.\nIf pattern[i] == 'I', then num[i] < num[i + 1].\nIf pattern[i] == 'D', then num[i] > num[i + 1].\n\nReturn the lexicographically smallest possible string num that meets the conditions.\n \n",
    "examples": [
      {
        "input": "Input: pattern = \"IIIDIDDD\"",
        "output": "Output: \"123549876\"",
        "explanation": ""
      },
      {
        "input": "Input: pattern = \"DDD\"",
        "output": "Output: \"4321\"",
        "explanation": ""
      }
    ],
    "topics": [
      "String",
      "Backtracking",
      "Stack",
      "Greedy"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= pattern.length <= 8",
      "pattern consists of only the letters 'I' and 'D'."
    ],
    "hints": [
      "With the constraints, could we generate every possible string?",
      "Yes we can. Now we just need to check if the string meets all the conditions."
    ]
  },
  {
    "title": "Node With Highest Edge Score",
    "description": "You are given a directed graph with n nodes labeled from 0 to n - 1, where each node has exactly one outgoing edge.\nThe graph is represented by a given 0-indexed integer array edges of length n, where edges[i] indicates that there is a directed edge from node i to node edges[i].\nThe edge score of a node i is defined as the sum of the labels of all the nodes that have an edge pointing to i.\nReturn the node with the highest edge score. If multiple nodes have the same edge score, return the node with the smallest index.\n \n",
    "examples": [
      {
        "input": "Input: edges = [1,0,0,0,0,7,7,5]",
        "output": "Output: 7",
        "explanation": ""
      },
      {
        "input": "Input: edges = [2,0,0,2]",
        "output": "Output: 0",
        "explanation": ""
      }
    ],
    "topics": [
      "Hash Table",
      "Graph"
    ],
    "difficulty": "Medium",
    "constraints": [
      "n == edges.length",
      "2 <= n <= 105",
      "0 <= edges[i] < n",
      "edges[i] != i"
    ],
    "hints": [
      "Create an array arr where arr[i] is the edge score for node i.",
      "How does the edge score for node edges[i] change? It increases by i.",
      "The edge score may not fit within a standard 32-bit integer."
    ]
  },
  {
    "title": "Largest Local Values in a Matrix",
    "description": "You are given an n x n integer matrix grid.\nGenerate an integer matrix maxLocal of size (n - 2) x (n - 2) such that:\n\nmaxLocal[i][j] is equal to the largest value of the 3 x 3 matrix in grid centered around row i + 1 and column j + 1.\n\nIn other words, we want to find the largest value in every contiguous 3 x 3 matrix in grid.\nReturn the generated matrix.\n \n",
    "examples": [
      {
        "input": "Input: grid = [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]",
        "output": "Output: [[9,9],[8,6]]",
        "explanation": "Explanation: The diagram above shows the original matrix and the generated matrix."
      },
      {
        "input": "Input: grid = [[1,1,1,1,1],[1,1,1,1,1],[1,1,2,1,1],[1,1,1,1,1],[1,1,1,1,1]]",
        "output": "Output: [[2,2,2],[2,2,2],[2,2,2]]",
        "explanation": "Explanation: Notice that the 2 is contained within every contiguous 3 x 3 matrix in grid."
      }
    ],
    "topics": [
      "Array",
      "Matrix"
    ],
    "difficulty": "Easy",
    "constraints": [
      "n == grid.length == grid[i].length",
      "3 <= n <= 100",
      "1 <= grid[i][j] <= 100"
    ],
    "hints": [
      "Use nested loops to run through all possible 3 x 3 windows in the matrix.",
      "For each 3 x 3 window, iterate through the values to get the maximum value within the window."
    ]
  },
  {
    "title": "Minimum Replacements to Sort the Array",
    "description": "You are given a 0-indexed integer array nums. In one operation you can replace any element of the array with any two elements that sum to it.\n\nFor example, consider nums = [5,6,7]. In one operation, we can replace nums[1] with 2 and 4 and convert nums to [5,2,4,7].\n\nReturn the minimum number of operations to make an array that is sorted in non-decreasing order.\n \n",
    "examples": [
      {
        "input": "Input: nums = [3,9,3]",
        "output": "Output: 2",
        "explanation": "Explanation: Here are the steps to sort the array in non-decreasing order:"
      },
      {
        "input": "Input: nums = [1,2,3,4,5]",
        "output": "Output: 0",
        "explanation": "Explanation: The array is already in non-decreasing order. Therefore, we return 0. "
      }
    ],
    "topics": [
      "Array",
      "Math",
      "Greedy"
    ],
    "difficulty": "Hard",
    "constraints": [
      "1 <= nums.length <= 105",
      "1 <= nums[i] <= 109"
    ],
    "hints": [
      "It is optimal to never make an operation to the last element of the array.",
      "You can iterate from the second last element to the first. If the current value is greater than the previous bound, we want to break it into pieces so that the smaller one is as large as possible but not larger than the previous one."
    ]
  },
  {
    "title": "Maximum Number of Robots Within Budget",
    "description": "You have n robots. You are given two 0-indexed integer arrays, chargeTimes and runningCosts, both of length n. The ith robot costs chargeTimes[i] units to charge and costs runningCosts[i] units to run. You are also given an integer budget.\nThe total cost of running k chosen robots is equal to max(chargeTimes) + k * sum(runningCosts), where max(chargeTimes) is the largest charge cost among the k robots and sum(runningCosts) is the sum of running costs among the k robots.\nReturn the maximum number of consecutive robots you can run such that the total cost does not exceed budget.\n \n",
    "examples": [
      {
        "input": "Input: chargeTimes = [3,6,1,3,4], runningCosts = [2,1,3,4,5], budget = 25",
        "output": "Output: 3",
        "explanation": "Explanation: "
      },
      {
        "input": "Input: chargeTimes = [11,12,19], runningCosts = [10,8,7], budget = 19",
        "output": "Output: 0",
        "explanation": "Explanation: No robot can be run that does not exceed the budget, so we return 0."
      }
    ],
    "topics": [
      "Array",
      "Binary Search",
      "Queue",
      "Sliding Window",
      "Heap (Priority Queue)",
      "Prefix Sum"
    ],
    "difficulty": "Hard",
    "constraints": [
      "chargeTimes.length == runningCosts.length == n",
      "1 <= n <= 5 * 104",
      "1 <= chargeTimes[i], runningCosts[i] <= 105",
      "1 <= budget <= 1015"
    ],
    "hints": [
      "Use binary search to convert the problem into checking if we can find a specific number of consecutive robots within the budget.",
      "Maintain a sliding window of the consecutive robots being considered.",
      "Use either a map, deque, or heap to find the maximum charge times in the window efficiently."
    ]
  },
  {
    "title": "Count Number of Bad Pairs",
    "description": "You are given a 0-indexed integer array nums. A pair of indices (i, j) is a bad pair if i < j and j - i != nums[j] - nums[i].\nReturn the total number of bad pairs in nums.\n \n",
    "examples": [
      {
        "input": "Input: nums = [4,1,3,3]",
        "output": "Output: 5",
        "explanation": "Explanation: The pair (0, 1) is a bad pair since 1 - 0 != 1 - 4."
      },
      {
        "input": "Input: nums = [1,2,3,4,5]",
        "output": "Output: 0",
        "explanation": "Explanation: There are no bad pairs."
      }
    ],
    "topics": [
      "Array",
      "Hash Table"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= nums.length <= 105",
      "1 <= nums[i] <= 109"
    ],
    "hints": [
      "Would it be easier to count the number of pairs that are not bad pairs?",
      "Notice that (j - i != nums[j] - nums[i]) is the same as (nums[i] - i != nums[j] - j).",
      "Keep a counter of nums[i] - i. To be efficient, use a HashMap."
    ]
  },
  {
    "title": "Merge Similar Items",
    "description": "You are given two 2D integer arrays, items1 and items2, representing two sets of items. Each array items has the following properties:\n\nitems[i] = [valuei, weighti] where valuei represents the value and weighti represents the weight of the ith item.\nThe value of each item in items is unique.\n\nReturn a 2D integer array ret where ret[i] = [valuei, weighti], with weighti being the sum of weights of all items with value valuei.\nNote: ret should be returned in ascending order by value.\n \n",
    "examples": [
      {
        "input": "Input: items1 = [[1,1],[4,5],[3,8]], items2 = [[3,1],[1,5]]",
        "output": "Output: [[1,6],[3,9],[4,5]]",
        "explanation": "Explanation: "
      },
      {
        "input": "Input: items1 = [[1,1],[3,2],[2,3]], items2 = [[2,1],[3,2],[1,3]]",
        "output": "Output: [[1,4],[2,4],[3,4]]",
        "explanation": "Explanation: "
      },
      {
        "input": "Input: items1 = [[1,3],[2,2]], items2 = [[7,1],[2,2],[1,4]]",
        "output": "Output: [[1,7],[2,4],[7,1]]",
        "explanation": ""
      }
    ],
    "topics": [
      "Array",
      "Hash Table",
      "Sorting",
      "Ordered Set"
    ],
    "difficulty": "Easy",
    "constraints": [
      "1 <= items1.length, items2.length <= 1000",
      "items1[i].length == items2[i].length == 2",
      "1 <= valuei, weighti <= 1000",
      "Each valuei in items1 is unique.",
      "Each valuei in items2 is unique."
    ],
    "hints": [
      "Map the weights using the corresponding values as keys.",
      "Make sure your output is sorted in ascending order by value."
    ]
  },
  {
    "title": "Reachable Nodes With Restrictions",
    "description": "There is an undirected tree with n nodes labeled from 0 to n - 1 and n - 1 edges.\nYou are given a 2D integer array edges of length n - 1 where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree. You are also given an integer array restricted which represents restricted nodes.\nReturn the maximum number of nodes you can reach from node 0 without visiting a restricted node.\nNote that node 0 will not be a restricted node.\n \n",
    "examples": [
      {
        "input": "Input: n = 7, edges = [[0,1],[1,2],[3,1],[4,0],[0,5],[5,6]], restricted = [4,5]",
        "output": "Output: 4",
        "explanation": "Explanation: The diagram above shows the tree."
      },
      {
        "input": "Input: n = 7, edges = [[0,1],[0,2],[0,5],[0,4],[3,2],[6,5]], restricted = [4,2,1]",
        "output": "Output: 3",
        "explanation": "Explanation: The diagram above shows the tree."
      }
    ],
    "topics": [
      "Array",
      "Hash Table",
      "Tree",
      "Depth-First Search",
      "Breadth-First Search",
      "Graph"
    ],
    "difficulty": "Medium",
    "constraints": [
      "2 <= n <= 105",
      "edges.length == n - 1",
      "edges[i].length == 2",
      "0 <= ai, bi < n",
      "ai != bi",
      "edges represents a valid tree.",
      "1 <= restricted.length < n",
      "1 <= restricted[i] < n",
      "All the values of restricted are unique."
    ],
    "hints": [
      "Can we find all the reachable nodes in a single traversal?",
      "Traverse the graph from node 0 while avoiding the nodes in restricted and do not revisit nodes that have been visited.",
      "Keep count of how many nodes are visited in total."
    ]
  },
  {
    "title": "Longest Ideal Subsequence",
    "description": "You are given a string s consisting of lowercase letters and an integer k. We call a string t ideal if the following conditions are satisfied:\n\nt is a subsequence of the string s.\nThe absolute difference in the alphabet order of every two adjacent letters in t is less than or equal to k.\n\nReturn the length of the longest ideal string.\nA subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.\nNote that the alphabet order is not cyclic. For example, the absolute difference in the alphabet order of 'a' and 'z' is 25, not 1.\n \n",
    "examples": [
      {
        "input": "Input: s = \"acfgbd\", k = 2",
        "output": "Output: 4",
        "explanation": "Explanation: The longest ideal string is \"acbd\". The length of this string is 4, so 4 is returned."
      },
      {
        "input": "Input: s = \"abcd\", k = 3",
        "output": "Output: 4",
        "explanation": "Explanation: The longest ideal string is \"abcd\". The length of this string is 4, so 4 is returned."
      }
    ],
    "topics": [
      "Hash Table",
      "String",
      "Dynamic Programming"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= s.length <= 105",
      "0 <= k <= 25",
      "s consists of lowercase English letters."
    ],
    "hints": [
      "How can you calculate the longest ideal subsequence that ends at a specific index i?",
      "Can you calculate it for all positions i? How can you use previously calculated answers to calculate the answer for the next position?"
    ]
  },
  {
    "title": "Check if There is a Valid Partition For The Array",
    "description": "You are given a 0-indexed integer array nums. You have to partition the array into one or more contiguous subarrays.\nWe call a partition of the array valid if each of the obtained subarrays satisfies one of the following conditions:\n\nThe subarray consists of exactly 2 equal elements. For example, the subarray [2,2] is good.\nThe subarray consists of exactly 3 equal elements. For example, the subarray [4,4,4] is good.\nThe subarray consists of exactly 3 consecutive increasing elements, that is, the difference between adjacent elements is 1. For example, the subarray [3,4,5] is good, but the subarray [1,3,5] is not.\n\nReturn true if the array has at least one valid partition. Otherwise, return false.\n \n",
    "examples": [
      {
        "input": "Input: nums = [4,4,4,5,6]",
        "output": "Output: true",
        "explanation": "Explanation: The array can be partitioned into the subarrays [4,4] and [4,5,6]."
      },
      {
        "input": "Input: nums = [1,1,1,2]",
        "output": "Output: false",
        "explanation": "Explanation: There is no valid partition for this array."
      }
    ],
    "topics": [
      "Array",
      "Dynamic Programming"
    ],
    "difficulty": "Medium",
    "constraints": [
      "2 <= nums.length <= 105",
      "1 <= nums[i] <= 106"
    ],
    "hints": [
      "How can you reduce the problem to checking if there is a valid partition for a smaller array?",
      "Use dynamic programming to reduce the problem until you have an empty array."
    ]
  },
  {
    "title": "Number of Arithmetic Triplets",
    "description": "You are given a 0-indexed, strictly increasing integer array nums and a positive integer diff. A triplet (i, j, k) is an arithmetic triplet if the following conditions are met:\n\ni < j < k,\nnums[j] - nums[i] == diff, and\nnums[k] - nums[j] == diff.\n\nReturn the number of unique arithmetic triplets.\n \n",
    "examples": [
      {
        "input": "Input: nums = [0,1,4,6,7,10], diff = 3",
        "output": "Output: 2",
        "explanation": ""
      },
      {
        "input": "Input: nums = [4,5,6,7,8,9], diff = 2",
        "output": "Output: 2",
        "explanation": ""
      }
    ],
    "topics": [
      "Array",
      "Hash Table",
      "Two Pointers",
      "Enumeration"
    ],
    "difficulty": "Easy",
    "constraints": [
      "3 <= nums.length <= 200",
      "0 <= nums[i] <= 200",
      "1 <= diff <= 50",
      "nums is strictly increasing."
    ],
    "hints": [
      "Are the constraints small enough for brute force?",
      "We can use three loops, each iterating through the array to go through every possible triplet. Be sure to not count duplicates."
    ]
  },
  {
    "title": "Longest Cycle in a Graph",
    "description": "You are given a directed graph of n nodes numbered from 0 to n - 1, where each node has at most one outgoing edge.\nThe graph is represented with a given 0-indexed array edges of size n, indicating that there is a directed edge from node i to node edges[i]. If there is no outgoing edge from node i, then edges[i] == -1.\nReturn the length of the longest cycle in the graph. If no cycle exists, return -1.\nA cycle is a path that starts and ends at the same node.\n \n",
    "examples": [
      {
        "input": "Input: edges = [3,3,4,2,3]",
        "output": "Output: 3",
        "explanation": "Explanation: The longest cycle in the graph is the cycle: 2 -> 4 -> 3 -> 2."
      },
      {
        "input": "Input: edges = [2,-1,3,1]",
        "output": "Output: -1",
        "explanation": "Explanation: There are no cycles in this graph."
      }
    ],
    "topics": [
      "Depth-First Search",
      "Graph",
      "Topological Sort"
    ],
    "difficulty": "Hard",
    "constraints": [
      "n == edges.length",
      "2 <= n <= 105",
      "-1 <= edges[i] < n",
      "edges[i] != i"
    ],
    "hints": [
      "How many cycles can each node at most be part of?",
      "Each node can be part of at most one cycle. Start from each node and find the cycle that it is part of if there is any. Save the already visited nodes to not repeat visiting the same cycle multiple times."
    ]
  },
  {
    "title": "Find Closest Node to Given Two Nodes",
    "description": "You are given a directed graph of n nodes numbered from 0 to n - 1, where each node has at most one outgoing edge.\nThe graph is represented with a given 0-indexed array edges of size n, indicating that there is a directed edge from node i to node edges[i]. If there is no outgoing edge from i, then edges[i] == -1.\nYou are also given two integers node1 and node2.\nReturn the index of the node that can be reached from both node1 and node2, such that the maximum between the distance from node1 to that node, and from node2 to that node is minimized. If there are multiple answers, return the node with the smallest index, and if no possible answer exists, return -1.\nNote that edges may contain cycles.\n \n",
    "examples": [
      {
        "input": "Input: edges = [2,2,3,-1], node1 = 0, node2 = 1",
        "output": "Output: 2",
        "explanation": "Explanation: The distance from node 0 to node 2 is 1, and the distance from node 1 to node 2 is 1."
      },
      {
        "input": "Input: edges = [1,2,-1], node1 = 0, node2 = 2",
        "output": "Output: 2",
        "explanation": "Explanation: The distance from node 0 to node 2 is 2, and the distance from node 2 to itself is 0."
      }
    ],
    "topics": [
      "Depth-First Search",
      "Graph"
    ],
    "difficulty": "Medium",
    "constraints": [
      "n == edges.length",
      "2 <= n <= 105",
      "-1 <= edges[i] < n",
      "edges[i] != i",
      "0 <= node1, node2 < n"
    ],
    "hints": [
      "How can you find the shortest distance from one node to all nodes in the graph?",
      "Use BFS to find the shortest distance from both node1 and node2 to all nodes in the graph. Then iterate over all nodes, and find the node with the minimum max distance."
    ]
  },
  {
    "title": "Maximum Number of Groups Entering a Competition",
    "description": "You are given a positive integer array grades which represents the grades of students in a university. You would like to enter all these students into a competition in ordered non-empty groups, such that the ordering meets the following conditions:\n\nThe sum of the grades of students in the ith group is less than the sum of the grades of students in the (i + 1)th group, for all groups (except the last).\nThe total number of students in the ith group is less than the total number of students in the (i + 1)th group, for all groups (except the last).\n\nReturn the maximum number of groups that can be formed.\n \n",
    "examples": [
      {
        "input": "Input: grades = [10,6,12,7,3,5]",
        "output": "Output: 3",
        "explanation": "Explanation: The following is a possible way to form 3 groups of students:"
      },
      {
        "input": "Input: grades = [8,8]",
        "output": "Output: 1",
        "explanation": "Explanation: We can only form 1 group, since forming 2 groups would lead to an equal number of students in both groups."
      }
    ],
    "topics": [
      "Array",
      "Math",
      "Binary Search",
      "Greedy"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= grades.length <= 105",
      "1 <= grades[i] <= 105"
    ],
    "hints": [
      "Would it be easier to place the students into valid groups after sorting them based on their grades in ascending order?",
      "Notice that, after sorting, we can separate them into groups of sizes 1, 2, 3, and so on.",
      "If the last group is invalid, we can merge it with the previous group.",
      "This creates the maximum number of groups because we always greedily form the smallest possible group."
    ]
  },
  {
    "title": "Make Array Zero by Subtracting Equal Amounts",
    "description": "You are given a non-negative integer array nums. In one operation, you must:\n\nChoose a positive integer x such that x is less than or equal to the smallest non-zero element in nums.\nSubtract x from every positive element in nums.\n\nReturn the minimum number of operations to make every element in nums equal to 0.\n \n",
    "examples": [
      {
        "input": "Input: nums = [1,5,0,3,5]",
        "output": "Output: 3",
        "explanation": ""
      },
      {
        "input": "Input: nums = [0]",
        "output": "Output: 0",
        "explanation": "Explanation: Each element in nums is already 0 so no operations are needed."
      }
    ],
    "topics": [
      "Array",
      "Hash Table",
      "Greedy",
      "Sorting",
      "Heap (Priority Queue)",
      "Simulation"
    ],
    "difficulty": "Easy",
    "constraints": [
      "1 <= nums.length <= 100",
      "0 <= nums[i] <= 100"
    ],
    "hints": [
      "It is always best to set x as the smallest non-zero element in nums.",
      "Elements with the same value will always take the same number of operations to become 0. Contrarily, elements with different values will always take a different number of operations to become 0.",
      "The answer is the number of unique non-zero numbers in nums."
    ]
  },
  {
    "title": "Shortest Impossible Sequence of Rolls",
    "description": "You are given an integer array rolls of length n and an integer k. You roll a k sided dice numbered from 1 to k, n times, where the result of the ith roll is rolls[i].\nReturn the length of the shortest sequence of rolls that cannot be taken from rolls.\nA sequence of rolls of length len is the result of rolling a k sided dice len times.\nNote that the sequence taken does not have to be consecutive as long as it is in order.\n \n",
    "examples": [
      {
        "input": "Input: rolls = [4,2,1,2,3,3,2,4,1], k = 4",
        "output": "Output: 3",
        "explanation": "Explanation: Every sequence of rolls of length 1, [1], [2], [3], [4], can be taken from rolls."
      },
      {
        "input": "Input: rolls = [1,1,2,2], k = 2",
        "output": "Output: 2",
        "explanation": "Explanation: Every sequence of rolls of length 1, [1], [2], can be taken from rolls."
      },
      {
        "input": "Input: rolls = [1,1,3,2,2,2,3,3], k = 4",
        "output": "Output: 1",
        "explanation": "Explanation: The sequence [4] cannot be taken from rolls, so we return 1."
      }
    ],
    "topics": [
      "Array",
      "Hash Table",
      "Greedy"
    ],
    "difficulty": "Hard",
    "constraints": [
      "n == rolls.length",
      "1 <= n <= 105",
      "1 <= rolls[i] <= k <= 105"
    ],
    "hints": [
      "How can you find the minimum index such that all sequences of length 1 can be formed from the start until that index?",
      "Starting from the previous minimum index, what is the next index such that all sequences of length 2 can be formed?",
      "Can you extend the idea to sequences of length 3 and more?"
    ]
  },
  {
    "title": "Design a Number Container System",
    "description": "Design a number container system that can do the following:\n\nInsert or Replace a number at the given index in the system.\nReturn the smallest index for the given number in the system.\n\nImplement the NumberContainers class:\n\nNumberContainers() Initializes the number container system.\nvoid change(int index, int number) Fills the container at index with the number. If there is already a number at that index, replace it.\nint find(int number) Returns the smallest index for the given number, or -1 if there is no index that is filled by number in the system.\n\n \n",
    "examples": [
      {
        "input": "Input\n[\"NumberContainers\", \"find\", \"change\", \"change\", \"change\", \"change\", \"find\", \"change\", \"find\"]",
        "output": "Output\n[null, -1, null, null, null, null, 1, null, 2]",
        "explanation": "Explanation\nNumberContainers nc = new NumberContainers();"
      }
    ],
    "topics": [
      "Hash Table",
      "Design",
      "Heap (Priority Queue)",
      "Ordered Set"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= index, number <= 109",
      "At most 105 calls will be made in total to change and find."
    ],
    "hints": [
      "Use a hash table to efficiently map each number to all of its indices in the container and to map each index to their current number.",
      "In addition, you can use ordered set to store all of the indices for each number to solve the find method. Do not forget to update the ordered set according to the change method."
    ]
  },
  {
    "title": "Best Poker Hand",
    "description": "You are given an integer array ranks and a character array suits. You have 5 cards where the ith card has a rank of ranks[i] and a suit of suits[i].\nThe following are the types of poker hands you can make from best to worst:\n\n\"Flush\": Five cards of the same suit.\n\"Three of a Kind\": Three cards of the same rank.\n\"Pair\": Two cards of the same rank.\n\"High Card\": Any single card.\n\nReturn a string representing the best type of poker hand you can make with the given cards.\nNote that the return values are case-sensitive.\n \n",
    "examples": [
      {
        "input": "Input: ranks = [13,2,3,1,9], suits = [\"a\",\"a\",\"a\",\"a\",\"a\"]",
        "output": "Output: \"Flush\"",
        "explanation": "Explanation: The hand with all the cards consists of 5 cards with the same suit, so we have a \"Flush\"."
      },
      {
        "input": "Input: ranks = [4,4,2,4,4], suits = [\"d\",\"a\",\"a\",\"b\",\"c\"]",
        "output": "Output: \"Three of a Kind\"",
        "explanation": "Explanation: The hand with the first, second, and fourth card consists of 3 cards with the same rank, so we have a \"Three of a Kind\"."
      },
      {
        "input": "Input: ranks = [10,10,2,12,9], suits = [\"a\",\"b\",\"c\",\"a\",\"d\"]",
        "output": "Output: \"Pair\"",
        "explanation": "Explanation: The hand with the first and second card consists of 2 cards with the same rank, so we have a \"Pair\"."
      }
    ],
    "topics": [
      "Array",
      "Hash Table",
      "Counting"
    ],
    "difficulty": "Easy",
    "constraints": [
      "ranks.length == suits.length == 5",
      "1 <= ranks[i] <= 13",
      "'a' <= suits[i] <= 'd'",
      "No two cards have the same rank and suit."
    ],
    "hints": [
      "Sequentially check the conditions 1 through 4, and return the outcome corresponding to the first met condition."
    ]
  },
  {
    "title": "Number of Zero-Filled Subarrays",
    "description": "Given an integer array nums, return the number of subarrays filled with 0.\nA subarray is a contiguous non-empty sequence of elements within an array.\n \n",
    "examples": [
      {
        "input": "Input: nums = [1,3,0,0,2,0,0,4]",
        "output": "Output: 6",
        "explanation": "Explanation: "
      },
      {
        "input": "Input: nums = [0,0,0,2,0,0]",
        "output": "Output: 9",
        "explanation": ""
      },
      {
        "input": "Input: nums = [2,10,2019]",
        "output": "Output: 0",
        "explanation": "Explanation: There is no subarray filled with 0. Therefore, we return 0."
      }
    ],
    "topics": [
      "Array",
      "Math"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= nums.length <= 105",
      "-109 <= nums[i] <= 109"
    ],
    "hints": [
      "For each zero, you can calculate the number of zero-filled subarrays that end on that index, which is the number of consecutive zeros behind the current element + 1.",
      "Maintain the number of consecutive zeros behind the current element, count the number of zero-filled subarrays that end on each index, sum it up to get the answer."
    ]
  },
  {
    "title": "Number of Excellent Pairs",
    "description": "You are given a 0-indexed positive integer array nums and a positive integer k.\nA pair of numbers (num1, num2) is called excellent if the following conditions are satisfied:\n\nBoth the numbers num1 and num2 exist in the array nums.\nThe sum of the number of set bits in num1 OR num2 and num1 AND num2 is greater than or equal to k, where OR is the bitwise OR operation and AND is the bitwise AND operation.\n\nReturn the number of distinct excellent pairs.\nTwo pairs (a, b) and (c, d) are considered distinct if either a != c or b != d. For example, (1, 2) and (2, 1) are distinct.\nNote that a pair (num1, num2) such that num1 == num2 can also be excellent if you have at least one occurrence of num1 in the array.\n \n",
    "examples": [
      {
        "input": "Input: nums = [1,2,3,1], k = 3",
        "output": "Output: 5",
        "explanation": "Explanation: The excellent pairs are the following:"
      },
      {
        "input": "Input: nums = [5,1,1], k = 10",
        "output": "Output: 0",
        "explanation": "Explanation: There are no excellent pairs for this array."
      }
    ],
    "topics": [
      "Array",
      "Hash Table",
      "Binary Search",
      "Bit Manipulation"
    ],
    "difficulty": "Hard",
    "constraints": [
      "1 <= nums.length <= 105",
      "1 <= nums[i] <= 109",
      "1 <= k <= 60"
    ],
    "hints": [
      "Can you find a different way to describe the second condition?",
      "The sum of the number of set bits in (num1 OR num2) and (num1 AND num2) is equal to the sum of the number of set bits in num1 and num2."
    ]
  },
  {
    "title": "Design a Food Rating System",
    "description": "Design a food rating system that can do the following:\n\nModify the rating of a food item listed in the system.\nReturn the highest-rated food item for a type of cuisine in the system.\n\nImplement the FoodRatings class:\n\nFoodRatings(String[] foods, String[] cuisines, int[] ratings) Initializes the system. The food items are described by foods, cuisines and ratings, all of which have a length of n.\n\n\t\nfoods[i] is the name of the ith food,\ncuisines[i] is the type of cuisine of the ith food, and\nratings[i] is the initial rating of the ith food.\n\n\nvoid changeRating(String food, int newRating) Changes the rating of the food item with the name food.\nString highestRated(String cuisine) Returns the name of the food item that has the highest rating for the given type of cuisine. If there is a tie, return the item with the lexicographically smaller name.\n\nNote that a string x is lexicographically smaller than string y if x comes before y in dictionary order, that is, either x is a prefix of y, or if i is the first position such that x[i] != y[i], then x[i] comes before y[i] in alphabetic order.\n \n",
    "examples": [
      {
        "input": "Input\n[\"FoodRatings\", \"highestRated\", \"highestRated\", \"changeRating\", \"highestRated\", \"changeRating\", \"highestRated\"]",
        "output": "Output\n[null, \"kimchi\", \"ramen\", null, \"sushi\", null, \"ramen\"]",
        "explanation": "Explanation\nFoodRatings foodRatings = new FoodRatings([\"kimchi\", \"miso\", \"sushi\", \"moussaka\", \"ramen\", \"bulgogi\"], [\"korean\", \"japanese\", \"japanese\", \"greek\", \"japanese\", \"korean\"], [9, 12, 8, 15, 14, 7]);"
      }
    ],
    "topics": [
      "Hash Table",
      "Design",
      "Heap (Priority Queue)",
      "Ordered Set"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= n <= 2 * 104",
      "n == foods.length == cuisines.length == ratings.length",
      "1 <= foods[i].length, cuisines[i].length <= 10",
      "foods[i], cuisines[i] consist of lowercase English letters.",
      "1 <= ratings[i] <= 108",
      "All the strings in foods are distinct.",
      "food will be the name of a food item in the system across all calls to changeRating.",
      "cuisine will be a type of cuisine of at least one food item in the system across all calls to highestRated.",
      "At most 2 * 104 calls in total will be made to changeRating and highestRated."
    ],
    "hints": [
      "The key to solving this problem is to properly store the data using the right data structures.",
      "Firstly, a hash table is needed to efficiently map each food item to its cuisine and current rating.",
      "In addition, another hash table is needed to map cuisines to foods within each cuisine stored in an ordered set according to their ratings."
    ]
  },
  {
    "title": "Equal Row and Column Pairs",
    "description": "Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.\nA row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).\n \n",
    "examples": [
      {
        "input": "Input: grid = [[3,2,1],[1,7,6],[2,7,7]]",
        "output": "Output: 1",
        "explanation": "Explanation: There is 1 equal row and column pair:"
      },
      {
        "input": "Input: grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]",
        "output": "Output: 3",
        "explanation": "Explanation: There are 3 equal row and column pairs:"
      }
    ],
    "topics": [
      "Array",
      "Hash Table",
      "Matrix",
      "Simulation"
    ],
    "difficulty": "Medium",
    "constraints": [
      "n == grid.length == grid[i].length",
      "1 <= n <= 200",
      "1 <= grid[i][j] <= 105"
    ],
    "hints": [
      "We can use nested loops to compare every row against every column.",
      "Another loop is necessary to compare the row and column element by element.",
      "It is also possible to hash the arrays and compare the hashed values instead."
    ]
  },
  {
    "title": "First Letter to Appear Twice",
    "description": "Given a string s consisting of lowercase English letters, return the first letter to appear twice.\nNote:\n\nA letter a appears twice before another letter b if the second occurrence of a is before the second occurrence of b.\ns will contain at least one letter that appears twice.\n\n \n",
    "examples": [
      {
        "input": "Input: s = \"abccbaacz\"",
        "output": "Output: \"c\"",
        "explanation": ""
      },
      {
        "input": "Input: s = \"abcdd\"",
        "output": "Output: \"d\"",
        "explanation": ""
      }
    ],
    "topics": [
      "Hash Table",
      "String",
      "Counting"
    ],
    "difficulty": "Easy",
    "constraints": [
      "2 <= s.length <= 100",
      "s consists of lowercase English letters.",
      "s has at least one repeated letter."
    ],
    "hints": [
      "Iterate through the string from left to right. Keep track of the elements you have already seen in a set.",
      "If the current element is already in the set, return that element."
    ]
  },
  {
    "title": "Minimum Deletions to Make Array Divisible",
    "description": "You are given two positive integer arrays nums and numsDivide. You can delete any number of elements from nums.\nReturn the minimum number of deletions such that the smallest element in nums divides all the elements of numsDivide. If this is not possible, return -1.\nNote that an integer x divides y if y % x == 0.\n \n",
    "examples": [
      {
        "input": "Input: nums = [2,3,2,4,3], numsDivide = [9,6,9,3,15]",
        "output": "Output: 2",
        "explanation": "Explanation: "
      },
      {
        "input": "Input: nums = [4,3,6], numsDivide = [8,2,6,10]",
        "output": "Output: -1",
        "explanation": "Explanation: "
      }
    ],
    "topics": [
      "Array",
      "Math",
      "Sorting",
      "Heap (Priority Queue)",
      "Number Theory"
    ],
    "difficulty": "Hard",
    "constraints": [
      "1 <= nums.length, numsDivide.length <= 105",
      "1 <= nums[i], numsDivide[i] <= 109"
    ],
    "hints": [
      "How can we find an integer x that divides all the elements of numsDivide?",
      "Will finding GCD (Greatest Common Divisor) help here?"
    ]
  },
  {
    "title": "Query Kth Smallest Trimmed Number",
    "description": "You are given a 0-indexed array of strings nums, where each string is of equal length and consists of only digits.\nYou are also given a 0-indexed 2D integer array queries where queries[i] = [ki, trimi]. For each queries[i], you need to:\n\nTrim each number in nums to its rightmost trimi digits.\nDetermine the index of the kith smallest trimmed number in nums. If two trimmed numbers are equal, the number with the lower index is considered to be smaller.\nReset each number in nums to its original length.\n\nReturn an array answer of the same length as queries, where answer[i] is the answer to the ith query.\nNote:\n\nTo trim to the rightmost x digits means to keep removing the leftmost digit, until only x digits remain.\nStrings in nums may contain leading zeros.\n\n \n",
    "examples": [
      {
        "input": "Input: nums = [\"102\",\"473\",\"251\",\"814\"], queries = [[1,1],[2,3],[4,2],[1,2]]",
        "output": "Output: [2,2,1,0]",
        "explanation": ""
      },
      {
        "input": "Input: nums = [\"24\",\"37\",\"96\",\"04\"], queries = [[2,1],[2,2]]",
        "output": "Output: [3,0]",
        "explanation": ""
      }
    ],
    "topics": [
      "Array",
      "String",
      "Divide and Conquer",
      "Sorting",
      "Heap (Priority Queue)",
      "Radix Sort",
      "Quickselect"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= nums.length <= 100",
      "1 <= nums[i].length <= 100",
      "nums[i] consists of only digits.",
      "All nums[i].length are equal.",
      "1 <= queries.length <= 100",
      "queries[i].length == 2",
      "1 <= ki <= nums.length",
      "1 <= trimi <= nums[i].length",
      "",
      " ",
      "Follow up: Could you use the Radix Sort Algorithm to solve this problem? What will be the complexity of that solution?"
    ],
    "hints": [
      "Run a simulation to follow the requirement of each query."
    ]
  },
  {
    "title": "Maximum Number of Pairs in Array",
    "description": "You are given a 0-indexed integer array nums. In one operation, you may do the following:\n\nChoose two integers in nums that are equal.\nRemove both integers from nums, forming a pair.\n\nThe operation is done on nums as many times as possible.\nReturn a 0-indexed integer array answer of size 2 where answer[0] is the number of pairs that are formed and answer[1] is the number of leftover integers in nums after doing the operation as many times as possible.\n \n",
    "examples": [
      {
        "input": "Input: nums = [1,3,2,1,3,2,2]",
        "output": "Output: [3,1]",
        "explanation": ""
      },
      {
        "input": "Input: nums = [1,1]",
        "output": "Output: [1,0]",
        "explanation": "Explanation: Form a pair with nums[0] and nums[1] and remove them from nums. Now, nums = []."
      },
      {
        "input": "Input: nums = [0]",
        "output": "Output: [0,1]",
        "explanation": "Explanation: No pairs can be formed, and there is 1 number leftover in nums."
      }
    ],
    "topics": [
      "Array",
      "Hash Table",
      "Counting"
    ],
    "difficulty": "Easy",
    "constraints": [
      "1 <= nums.length <= 100",
      "0 <= nums[i] <= 100"
    ],
    "hints": [
      "What do we need to know to find how many pairs we can make? We need to know the frequency of each integer.",
      "When will there be a leftover number? When the frequency of an integer is an odd number."
    ]
  },
  {
    "title": "Subarray With Elements Greater Than Varying Threshold",
    "description": "You are given an integer array nums and an integer threshold.\nFind any subarray of nums of length k such that every element in the subarray is greater than threshold / k.\nReturn the size of any such subarray. If there is no such subarray, return -1.\nA subarray is a contiguous non-empty sequence of elements within an array.\n \n",
    "examples": [
      {
        "input": "Input: nums = [1,3,4,3,1], threshold = 6",
        "output": "Output: 3",
        "explanation": "Explanation: The subarray [3,4,3] has a size of 3, and every element is greater than 6 / 3 = 2."
      },
      {
        "input": "Input: nums = [6,5,6,5,8], threshold = 7",
        "output": "Output: 1",
        "explanation": "Explanation: The subarray [8] has a size of 1, and 8 > 7 / 1 = 7. So 1 is returned."
      }
    ],
    "topics": [
      "Array",
      "Stack",
      "Union Find",
      "Monotonic Stack"
    ],
    "difficulty": "Hard",
    "constraints": [
      "1 <= nums.length <= 105",
      "1 <= nums[i], threshold <= 109"
    ],
    "hints": [
      "For all elements to be greater than the threshold/length, the minimum element in the subarray must be greater than the threshold/length.",
      "For a given index, could you find the largest subarray such that the given index is the minimum element?",
      "Could you use a monotonic stack to get the next and previous smallest element for every index?"
    ]
  },
  {
    "title": "Minimum Sum of Squared Difference",
    "description": "You are given two positive 0-indexed integer arrays nums1 and nums2, both of length n.\nThe sum of squared difference of arrays nums1 and nums2 is defined as the sum of (nums1[i] - nums2[i])2 for each 0 <= i < n.\nYou are also given two positive integers k1 and k2. You can modify any of the elements of nums1 by +1 or -1 at most k1 times. Similarly, you can modify any of the elements of nums2 by +1 or -1 at most k2 times.\nReturn the minimum sum of squared difference after modifying array nums1 at most k1 times and modifying array nums2 at most k2 times.\nNote: You are allowed to modify the array elements to become negative integers.\n \n",
    "examples": [
      {
        "input": "Input: nums1 = [1,2,3,4], nums2 = [2,10,20,19], k1 = 0, k2 = 0",
        "output": "Output: 579",
        "explanation": "Explanation: The elements in nums1 and nums2 cannot be modified because k1 = 0 and k2 = 0. "
      },
      {
        "input": "Input: nums1 = [1,4,10,12], nums2 = [5,8,6,9], k1 = 1, k2 = 1",
        "output": "Output: 43",
        "explanation": "Explanation: One way to obtain the minimum sum of square difference is: "
      }
    ],
    "topics": [
      "Array",
      "Math",
      "Sorting",
      "Heap (Priority Queue)"
    ],
    "difficulty": "Medium",
    "constraints": [
      "n == nums1.length == nums2.length",
      "1 <= n <= 105",
      "0 <= nums1[i], nums2[i] <= 105",
      "0 <= k1, k2 <= 109"
    ],
    "hints": [
      "There is no difference between the purpose of k1 and k2. Adding +1 to one element in nums1 is same as performing -1 to one element in nums2, and vice versa.",
      "Reduce the sum of squared difference greedily. One operation of k should use the index that has the current maximum difference.",
      "Binary search the maximum difference for the final result."
    ]
  },
  {
    "title": "The Latest Time to Catch a Bus",
    "description": "You are given a 0-indexed integer array buses of length n, where buses[i] represents the departure time of the ith bus. You are also given a 0-indexed integer array passengers of length m, where passengers[j] represents the arrival time of the jth passenger. All bus departure times are unique. All passenger arrival times are unique.\nYou are given an integer capacity, which represents the maximum number of passengers that can get on each bus.\nWhen a passenger arrives, they will wait in line for the next available bus. You can get on a bus that departs at x minutes if you arrive at y minutes where y <= x, and the bus is not full. Passengers with the earliest arrival times get on the bus first.\nMore formally when a bus arrives, either:\n\nIf capacity or fewer passengers are waiting for a bus, they will all get on the bus, or\nThe capacity passengers with the earliest arrival times will get on the bus.\n\nReturn the latest time you may arrive at the bus station to catch a bus. You cannot arrive at the same time as another passenger.\nNote: The arrays buses and passengers are not necessarily sorted.\n \n",
    "examples": [
      {
        "input": "Input: buses = [10,20], passengers = [2,17,18,19], capacity = 2",
        "output": "Output: 16",
        "explanation": "Explanation: Suppose you arrive at time 16."
      },
      {
        "input": "Input: buses = [20,30,10], passengers = [19,13,26,4,25,11,21], capacity = 2",
        "output": "Output: 20",
        "explanation": "Explanation: Suppose you arrive at time 20."
      }
    ],
    "topics": [
      "Array",
      "Two Pointers",
      "Binary Search",
      "Sorting"
    ],
    "difficulty": "Medium",
    "constraints": [
      "n == buses.length",
      "m == passengers.length",
      "1 <= n, m, capacity <= 105",
      "2 <= buses[i], passengers[i] <= 109",
      "Each element in buses is unique.",
      "Each element in passengers is unique."
    ],
    "hints": [
      "Sort the buses and passengers arrays.",
      "Use 2 pointers to traverse buses and passengers with a simulation of passengers getting on a particular bus."
    ]
  },
  {
    "title": "Evaluate Boolean Binary Tree",
    "description": "You are given the root of a full binary tree with the following properties:\n\nLeaf nodes have either the value 0 or 1, where 0 represents False and 1 represents True.\nNon-leaf nodes have either the value 2 or 3, where 2 represents the boolean OR and 3 represents the boolean AND.\n\nThe evaluation of a node is as follows:\n\nIf the node is a leaf node, the evaluation is the value of the node, i.e. True or False.\nOtherwise, evaluate the node's two children and apply the boolean operation of its value with the children's evaluations.\n\nReturn the boolean result of evaluating the root node.\nA full binary tree is a binary tree where each node has either 0 or 2 children.\nA leaf node is a node that has zero children.\n \n",
    "examples": [
      {
        "input": "Input: root = [2,1,3,null,null,0,1]",
        "output": "Output: true",
        "explanation": "Explanation: The above diagram illustrates the evaluation process."
      },
      {
        "input": "Input: root = [0]",
        "output": "Output: false",
        "explanation": "Explanation: The root node is a leaf node and it evaluates to false, so we return false."
      }
    ],
    "topics": [
      "Tree",
      "Depth-First Search",
      "Binary Tree"
    ],
    "difficulty": "Easy",
    "constraints": [
      "The number of nodes in the tree is in the range [1, 1000].",
      "0 <= Node.val <= 3",
      "Every node has either 0 or 2 children.",
      "Leaf nodes have a value of 0 or 1.",
      "Non-leaf nodes have a value of 2 or 3."
    ],
    "hints": [
      "Traverse the tree using depth-first search in post-order.",
      "Can you use recursion to solve this easily?"
    ]
  },
  {
    "title": "Count the Number of Ideal Arrays",
    "description": "You are given two integers n and maxValue, which are used to describe an ideal array.\nA 0-indexed integer array arr of length n is considered ideal if the following conditions hold:\n\nEvery arr[i] is a value from 1 to maxValue, for 0 <= i < n.\nEvery arr[i] is divisible by arr[i - 1], for 0 < i < n.\n\nReturn the number of distinct ideal arrays of length n. Since the answer may be very large, return it modulo 109 + 7.\n \n",
    "examples": [
      {
        "input": "Input: n = 2, maxValue = 5",
        "output": "Output: 10",
        "explanation": "Explanation: The following are the possible ideal arrays:"
      },
      {
        "input": "Input: n = 5, maxValue = 3",
        "output": "Output: 11",
        "explanation": "Explanation: The following are the possible ideal arrays:"
      }
    ],
    "topics": [
      "Math",
      "Dynamic Programming",
      "Combinatorics",
      "Number Theory"
    ],
    "difficulty": "Hard",
    "constraints": [
      "2 <= n <= 104",
      "1 <= maxValue <= 104"
    ],
    "hints": [
      "Notice that an ideal array is non-decreasing.",
      "Consider an alternative problem: where an ideal array must also be strictly increasing. Can you use DP to solve it?",
      "Will combinatorics help to get an answer from the alternative problem to the actual problem?"
    ]
  },
  {
    "title": "Move Pieces to Obtain a String",
    "description": "You are given two strings start and target, both of length n. Each string consists only of the characters 'L', 'R', and '_' where:\n\nThe characters 'L' and 'R' represent pieces, where a piece 'L' can move to the left only if there is a blank space directly to its left, and a piece 'R' can move to the right only if there is a blank space directly to its right.\nThe character '_' represents a blank space that can be occupied by any of the 'L' or 'R' pieces.\n\nReturn true if it is possible to obtain the string target by moving the pieces of the string start any number of times. Otherwise, return false.\n \n",
    "examples": [
      {
        "input": "Input: start = \"_L__R__R_\", target = \"L______RR\"",
        "output": "Output: true",
        "explanation": "Explanation: We can obtain the string target from start by doing the following moves:"
      },
      {
        "input": "Input: start = \"R_L_\", target = \"__LR\"",
        "output": "Output: false",
        "explanation": "Explanation: The 'R' piece in the string start can move one step to the right to obtain \"_RL_\"."
      },
      {
        "input": "Input: start = \"_R\", target = \"R_\"",
        "output": "Output: false",
        "explanation": "Explanation: The piece in the string start can move only to the right, so it is impossible to obtain the string target from start."
      }
    ],
    "topics": [
      "Two Pointers",
      "String"
    ],
    "difficulty": "Medium",
    "constraints": [
      "n == start.length == target.length",
      "1 <= n <= 105",
      "start and target consist of the characters 'L', 'R', and '_'."
    ],
    "hints": [
      "After some sequence of moves, can the order of the pieces change?",
      "Try to match each piece in s with a piece in e."
    ]
  },
  {
    "title": "Smallest Number in Infinite Set",
    "description": "You have a set which contains all positive integers [1, 2, 3, 4, 5, ...].\nImplement the SmallestInfiniteSet class:\n\nSmallestInfiniteSet() Initializes the SmallestInfiniteSet object to contain all positive integers.\nint popSmallest() Removes and returns the smallest integer contained in the infinite set.\nvoid addBack(int num) Adds a positive integer num back into the infinite set, if it is not already in the infinite set.\n\n \n",
    "examples": [
      {
        "input": "Input\n[\"SmallestInfiniteSet\", \"addBack\", \"popSmallest\", \"popSmallest\", \"popSmallest\", \"addBack\", \"popSmallest\", \"popSmallest\", \"popSmallest\"]",
        "output": "Output\n[null, null, 1, 2, 3, null, 1, 4, 5]",
        "explanation": "Explanation\nSmallestInfiniteSet smallestInfiniteSet = new SmallestInfiniteSet();"
      }
    ],
    "topics": [
      "Hash Table",
      "Design",
      "Heap (Priority Queue)"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= num <= 1000",
      "At most 1000 calls will be made in total to popSmallest and addBack."
    ],
    "hints": [
      "Based on the constraints, what is the maximum element that can possibly be popped?",
      "Maintain whether elements are in or not in the set. How many elements do we consider?"
    ]
  },
  {
    "title": "Minimum Amount of Time to Fill Cups",
    "description": "You have a water dispenser that can dispense cold, warm, and hot water. Every second, you can either fill up 2 cups with different types of water, or 1 cup of any type of water.\nYou are given a 0-indexed integer array amount of length 3 where amount[0], amount[1], and amount[2] denote the number of cold, warm, and hot water cups you need to fill respectively. Return the minimum number of seconds needed to fill up all the cups.\n \n",
    "examples": [
      {
        "input": "Input: amount = [1,4,2]",
        "output": "Output: 4",
        "explanation": "Explanation: One way to fill up the cups is:"
      },
      {
        "input": "Input: amount = [5,4,4]",
        "output": "Output: 7",
        "explanation": "Explanation: One way to fill up the cups is:"
      },
      {
        "input": "Input: amount = [5,0,0]",
        "output": "Output: 5",
        "explanation": "Explanation: Every second, we fill up a cold cup."
      }
    ],
    "topics": [
      "Array",
      "Greedy",
      "Sorting",
      "Heap (Priority Queue)"
    ],
    "difficulty": "Easy",
    "constraints": [
      "amount.length == 3",
      "0 <= amount[i] <= 100"
    ],
    "hints": [
      "To minimize the amount of time needed, you want to fill up as many cups as possible in each second. This means that you want to maximize the number of seconds where you are filling up two cups.",
      "You always want to fill up the two types of water with the most unfilled cups."
    ]
  },
  {
    "title": "Spiral Matrix IV",
    "description": "You are given two integers m and n, which represent the dimensions of a matrix.\nYou are also given the head of a linked list of integers.\nGenerate an m x n matrix that contains the integers in the linked list presented in spiral order (clockwise), starting from the top-left of the matrix. If there are remaining empty spaces, fill them with -1.\nReturn the generated matrix.\n \n",
    "examples": [
      {
        "input": "Input: m = 3, n = 5, head = [3,0,2,6,8,1,7,9,4,2,5,5,0]",
        "output": "Output: [[3,0,2,6,8],[5,0,-1,-1,1],[5,2,4,9,7]]",
        "explanation": "Explanation: The diagram above shows how the values are printed in the matrix."
      },
      {
        "input": "Input: m = 1, n = 4, head = [0,1,2]",
        "output": "Output: [[0,1,2,-1]]",
        "explanation": "Explanation: The diagram above shows how the values are printed from left to right in the matrix."
      }
    ],
    "topics": [
      "Array",
      "Linked List",
      "Matrix",
      "Simulation"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= m, n <= 105",
      "1 <= m * n <= 105",
      "The number of nodes in the list is in the range [1, m * n].",
      "0 <= Node.val <= 1000"
    ],
    "hints": [
      "First, generate an m x n matrix filled with -1s.",
      "Navigate within the matrix at (i, j) with the help of a direction vector ⟨di, dj⟩. At (i, j), you need to decide if you can keep going in the current direction.",
      "If you cannot keep going, rotate the direction vector clockwise by 90 degrees."
    ]
  },
  {
    "title": "Number of Increasing Paths in a Grid",
    "description": "You are given an m x n integer matrix grid, where you can move from a cell to any adjacent cell in all 4 directions.\nReturn the number of strictly increasing paths in the grid such that you can start from any cell and end at any cell. Since the answer may be very large, return it modulo 109 + 7.\nTwo paths are considered different if they do not have exactly the same sequence of visited cells.\n \n",
    "examples": [
      {
        "input": "Input: grid = [[1,1],[3,4]]",
        "output": "Output: 8",
        "explanation": "Explanation: The strictly increasing paths are:"
      },
      {
        "input": "Input: grid = [[1],[2]]",
        "output": "Output: 3",
        "explanation": "Explanation: The strictly increasing paths are:"
      }
    ],
    "topics": [
      "Array",
      "Dynamic Programming",
      "Depth-First Search",
      "Breadth-First Search",
      "Graph",
      "Topological Sort",
      "Memoization",
      "Matrix"
    ],
    "difficulty": "Hard",
    "constraints": [
      "m == grid.length",
      "n == grid[i].length",
      "1 <= m, n <= 1000",
      "1 <= m * n <= 105",
      "1 <= grid[i][j] <= 105"
    ],
    "hints": [
      "How can you calculate the number of increasing paths that start from a cell (i, j)? Think about dynamic programming.",
      "Define f(i, j) as the number of increasing paths starting from cell (i, j). Try to find how f(i, j) is related to each of f(i, j+1), f(i, j-1), f(i+1, j) and f(i-1, j)."
    ]
  },
  {
    "title": "Number of People Aware of a Secret",
    "description": "On day 1, one person discovers a secret.\nYou are given an integer delay, which means that each person will share the secret with a new person every day, starting from delay days after discovering the secret. You are also given an integer forget, which means that each person will forget the secret forget days after discovering it. A person cannot share the secret on the same day they forgot it, or on any day afterwards.\nGiven an integer n, return the number of people who know the secret at the end of day n. Since the answer may be very large, return it modulo 109 + 7.\n \n",
    "examples": [
      {
        "input": "Input: n = 6, delay = 2, forget = 4",
        "output": "Output: 5",
        "explanation": ""
      },
      {
        "input": "Input: n = 4, delay = 1, forget = 3",
        "output": "Output: 6",
        "explanation": ""
      }
    ],
    "topics": [
      "Dynamic Programming",
      "Queue",
      "Simulation"
    ],
    "difficulty": "Medium",
    "constraints": [
      "2 <= n <= 1000",
      "1 <= delay < forget <= n"
    ],
    "hints": [
      "Let dp[i][j] be the number of people who have known the secret for exactly j + 1 days, at day i.",
      "If j > 0, dp[i][j] = dp[i – 1][j – 1].",
      "dp[i][0] = sum(dp[i – 1][j]) for j in [delay – 1, forget – 2]."
    ]
  },
  {
    "title": "Decode the Message",
    "description": "You are given the strings key and message, which represent a cipher key and a secret message, respectively. The steps to decode message are as follows:\n\nUse the first appearance of all 26 lowercase English letters in key as the order of the substitution table.\nAlign the substitution table with the regular English alphabet.\nEach letter in message is then substituted using the table.\nSpaces ' ' are transformed to themselves.\n\n\nFor example, given key = \"happy boy\" (actual key would have at least one instance of each letter in the alphabet), we have the partial substitution table of ('h' -> 'a', 'a' -> 'b', 'p' -> 'c', 'y' -> 'd', 'b' -> 'e', 'o' -> 'f').\n\nReturn the decoded message.\n \n",
    "examples": [
      {
        "input": "Input: key = \"the quick brown fox jumps over the lazy dog\", message = \"vkbs bs t suepuv\"",
        "output": "Output: \"this is a secret\"",
        "explanation": "Explanation: The diagram above shows the substitution table."
      },
      {
        "input": "Input: key = \"eljuxhpwnyrdgtqkviszcfmabo\", message = \"zwx hnfx lqantp mnoeius ycgk vcnjrdb\"",
        "output": "Output: \"the five boxing wizards jump quickly\"",
        "explanation": "Explanation: The diagram above shows the substitution table."
      }
    ],
    "topics": [
      "Hash Table",
      "String"
    ],
    "difficulty": "Easy",
    "constraints": [
      "26 <= key.length <= 2000",
      "key consists of lowercase English letters and ' '.",
      "key contains every letter in the English alphabet ('a' to 'z') at least once.",
      "1 <= message.length <= 2000",
      "message consists of lowercase English letters and ' '."
    ],
    "hints": [
      "Iterate through the characters in the key to construct a mapping to the English alphabet.",
      "Make sure to check that the current character is not already in the mapping (only the first appearance is considered).",
      "Map the characters in the message according to the constructed mapping."
    ]
  },
  {
    "title": "Number of Distinct Roll Sequences",
    "description": "You are given an integer n. You roll a fair 6-sided dice n times. Determine the total number of distinct sequences of rolls possible such that the following conditions are satisfied:\n\nThe greatest common divisor of any adjacent values in the sequence is equal to 1.\nThere is at least a gap of 2 rolls between equal valued rolls. More formally, if the value of the ith roll is equal to the value of the jth roll, then abs(i - j) > 2.\n\nReturn the total number of distinct sequences possible. Since the answer may be very large, return it modulo 109 + 7.\nTwo sequences are considered distinct if at least one element is different.\n \n",
    "examples": [
      {
        "input": "Input: n = 4",
        "output": "Output: 184",
        "explanation": "Explanation: Some of the possible sequences are (1, 2, 3, 4), (6, 1, 2, 3), (1, 2, 3, 1), etc."
      },
      {
        "input": "Input: n = 2",
        "output": "Output: 22",
        "explanation": "Explanation: Some of the possible sequences are (1, 2), (2, 1), (3, 2)."
      }
    ],
    "topics": [
      "Dynamic Programming",
      "Memoization"
    ],
    "difficulty": "Hard",
    "constraints": [
      "1 <= n <= 104"
    ],
    "hints": [
      "Can you think of a DP solution?",
      "Consider a state that remembers the last 1 or 2 rolls.",
      "Do you need to consider the last 3 rolls?"
    ]
  },
  {
    "title": "Count Unreachable Pairs of Nodes in an Undirected Graph",
    "description": "You are given an integer n. There is an undirected graph with n nodes, numbered from 0 to n - 1. You are given a 2D integer array edges where edges[i] = [ai, bi] denotes that there exists an undirected edge connecting nodes ai and bi.\nReturn the number of pairs of different nodes that are unreachable from each other.\n \n",
    "examples": [
      {
        "input": "Input: n = 3, edges = [[0,1],[0,2],[1,2]]",
        "output": "Output: 0",
        "explanation": "Explanation: There are no pairs of nodes that are unreachable from each other. Therefore, we return 0."
      },
      {
        "input": "Input: n = 7, edges = [[0,2],[0,5],[2,4],[1,6],[5,4]]",
        "output": "Output: 14",
        "explanation": "Explanation: There are 14 pairs of nodes that are unreachable from each other:"
      }
    ],
    "topics": [
      "Depth-First Search",
      "Breadth-First Search",
      "Union Find",
      "Graph"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= n <= 105",
      "0 <= edges.length <= 2 * 105",
      "edges[i].length == 2",
      "0 <= ai, bi < n",
      "ai != bi",
      "There are no repeated edges."
    ],
    "hints": [
      "Find the connected components of the graph. To find connected components, you can use Union Find (Disjoint Sets), BFS, or DFS.",
      "For a node u, the number of nodes that are unreachable from u is the number of nodes that are not in the same connected component as u.",
      "The number of unreachable nodes from node u will be the same for the number of nodes that are unreachable from node v if nodes u and v belong to the same connected component."
    ]
  },
  {
    "title": "Maximum XOR After Operations ",
    "description": "You are given a 0-indexed integer array nums. In one operation, select any non-negative integer x and an index i, then update nums[i] to be equal to nums[i] AND (nums[i] XOR x).\nNote that AND is the bitwise AND operation and XOR is the bitwise XOR operation.\nReturn the maximum possible bitwise XOR of all elements of nums after applying the operation any number of times.\n \n",
    "examples": [
      {
        "input": "Input: nums = [3,2,4,6]",
        "output": "Output: 7",
        "explanation": "Explanation: Apply the operation with x = 4 and i = 3, num[3] = 6 AND (6 XOR 4) = 6 AND 2 = 2."
      },
      {
        "input": "Input: nums = [1,2,3,9,2]",
        "output": "Output: 11",
        "explanation": "Explanation: Apply the operation zero times."
      }
    ],
    "topics": [
      "Array",
      "Math",
      "Bit Manipulation"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= nums.length <= 105",
      "0 <= nums[i] <= 108"
    ],
    "hints": [
      "Consider what it means to be able to choose any x for the operation and which integers could be obtained from a given nums[i].",
      "The given operation can unset any bit in nums[i].",
      "The nth bit of the XOR of all the elements is 1 if the nth bit is 1 for an odd number of elements. When can we ensure it is odd?",
      "Try to set every bit of the result to 1 if possible."
    ]
  },
  {
    "title": "Count Asterisks",
    "description": "You are given a string s, where every two consecutive vertical bars '|' are grouped into a pair. In other words, the 1st and 2nd '|' make a pair, the 3rd and 4th '|' make a pair, and so forth.\nReturn the number of '*' in s, excluding the '*' between each pair of '|'.\nNote that each '|' will belong to exactly one pair.\n \n",
    "examples": [
      {
        "input": "Input: s = \"l|*e*et|c**o|*de|\"",
        "output": "Output: 2",
        "explanation": "Explanation: The considered characters are underlined: \"l|*e*et|c**o|*de|\"."
      },
      {
        "input": "Input: s = \"iamprogrammer\"",
        "output": "Output: 0",
        "explanation": "Explanation: In this example, there are no asterisks in s. Therefore, we return 0."
      },
      {
        "input": "Input: s = \"yo|uar|e**|b|e***au|tifu|l\"",
        "output": "Output: 5",
        "explanation": "Explanation: The considered characters are underlined: \"yo|uar|e**|b|e***au|tifu|l\". There are 5 asterisks considered. Therefore, we return 5."
      }
    ],
    "topics": [
      "String"
    ],
    "difficulty": "Easy",
    "constraints": [
      "1 <= s.length <= 1000",
      "s consists of lowercase English letters, vertical bars '|', and asterisks '*'.",
      "s contains an even number of vertical bars '|'."
    ],
    "hints": [
      "Iterate through each character, while maintaining whether we are currently between a pair of ‘|’ or not.",
      "If we are not in between a pair of ‘|’ and there is a ‘*’, increment the answer by 1."
    ]
  },
  {
    "title": "Minimum Score After Removals on a Tree",
    "description": "There is an undirected connected tree with n nodes labeled from 0 to n - 1 and n - 1 edges.\nYou are given a 0-indexed integer array nums of length n where nums[i] represents the value of the ith node. You are also given a 2D integer array edges of length n - 1 where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree.\nRemove two distinct edges of the tree to form three connected components. For a pair of removed edges, the following steps are defined:\n\nGet the XOR of all the values of the nodes for each of the three components respectively.\nThe difference between the largest XOR value and the smallest XOR value is the score of the pair.\n\n\nFor example, say the three components have the node values: [4,5,7], [1,9], and [3,3,3]. The three XOR values are 4 ^ 5 ^ 7 = 6, 1 ^ 9 = 8, and 3 ^ 3 ^ 3 = 3. The largest XOR value is 8 and the smallest XOR value is 3. The score is then 8 - 3 = 5.\n\nReturn the minimum score of any possible pair of edge removals on the given tree.\n \n",
    "examples": [
      {
        "input": "Input: nums = [1,5,5,4,11], edges = [[0,1],[1,2],[1,3],[3,4]]",
        "output": "Output: 9",
        "explanation": "Explanation: The diagram above shows a way to make a pair of removals."
      },
      {
        "input": "Input: nums = [5,5,2,4,4,2], edges = [[0,1],[1,2],[5,2],[4,3],[1,3]]",
        "output": "Output: 0",
        "explanation": "Explanation: The diagram above shows a way to make a pair of removals."
      }
    ],
    "topics": [
      "Array",
      "Bit Manipulation",
      "Tree",
      "Depth-First Search"
    ],
    "difficulty": "Hard",
    "constraints": [
      "n == nums.length",
      "3 <= n <= 1000",
      "1 <= nums[i] <= 108",
      "edges.length == n - 1",
      "edges[i].length == 2",
      "0 <= ai, bi < n",
      "ai != bi",
      "edges represents a valid tree."
    ],
    "hints": [
      "Consider iterating over the first edge to remove, and then doing some precalculations on the 2 resulting connected components.",
      "Will calculating the XOR of each subtree help?"
    ]
  },
  {
    "title": "Check if Matrix Is X-Matrix",
    "description": "A square matrix is said to be an X-Matrix if both of the following conditions hold:\n\nAll the elements in the diagonals of the matrix are non-zero.\nAll other elements are 0.\n\nGiven a 2D integer array grid of size n x n representing a square matrix, return true if grid is an X-Matrix. Otherwise, return false.\n \n",
    "examples": [
      {
        "input": "Input: grid = [[2,0,0,1],[0,3,1,0],[0,5,2,0],[4,0,0,2]]",
        "output": "Output: true",
        "explanation": "Explanation: Refer to the diagram above. "
      },
      {
        "input": "Input: grid = [[5,7,0],[0,3,1],[0,5,0]]",
        "output": "Output: false",
        "explanation": "Explanation: Refer to the diagram above."
      }
    ],
    "topics": [
      "Array",
      "Matrix"
    ],
    "difficulty": "Easy",
    "constraints": [
      "n == grid.length == grid[i].length",
      "3 <= n <= 100",
      "0 <= grid[i][j] <= 105"
    ],
    "hints": [
      "Assuming a 0-indexed matrix, for a given cell on row i and column j, it is in a diagonal if and only if i == j or i == n - 1 - j.",
      "We can then iterate through the elements in the matrix to check if all the elements in the diagonals are non-zero and all other elements are zero."
    ]
  },
  {
    "title": "Count Number of Ways to Place Houses",
    "description": "There is a street with n * 2 plots, where there are n plots on each side of the street. The plots on each side are numbered from 1 to n. On each plot, a house can be placed.\nReturn the number of ways houses can be placed such that no two houses are adjacent to each other on the same side of the street. Since the answer may be very large, return it modulo 109 + 7.\nNote that if a house is placed on the ith plot on one side of the street, a house can also be placed on the ith plot on the other side of the street.\n \n",
    "examples": [
      {
        "input": "Input: n = 1",
        "output": "Output: 4",
        "explanation": "Explanation: "
      },
      {
        "input": "Input: n = 2",
        "output": "Output: 9",
        "explanation": "Explanation: The 9 possible arrangements are shown in the diagram above."
      }
    ],
    "topics": [
      "Dynamic Programming"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= n <= 104"
    ],
    "hints": [
      "Try coming up with a DP solution for one side of the street.",
      "The DP for one side of the street will bear resemblance to the Fibonacci sequence.",
      "The number of different arrangements on both side of the street is the same."
    ]
  },
  {
    "title": "Longest Binary Subsequence Less Than or Equal to K",
    "description": "You are given a binary string s and a positive integer k.\nReturn the length of the longest subsequence of s that makes up a binary number less than or equal to k.\nNote:\n\nThe subsequence can contain leading zeroes.\nThe empty string is considered to be equal to 0.\nA subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.\n\n \n",
    "examples": [
      {
        "input": "Input: s = \"1001010\", k = 5",
        "output": "Output: 5",
        "explanation": "Explanation: The longest subsequence of s that makes up a binary number less than or equal to 5 is \"00010\", as this number is equal to 2 in decimal."
      },
      {
        "input": "Input: s = \"00101001\", k = 1",
        "output": "Output: 6",
        "explanation": "Explanation: \"000001\" is the longest subsequence of s that makes up a binary number less than or equal to 1, as this number is equal to 1 in decimal."
      }
    ],
    "topics": [
      "String",
      "Dynamic Programming",
      "Greedy",
      "Memoization"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= s.length <= 1000",
      "s[i] is either '0' or '1'.",
      "1 <= k <= 109"
    ],
    "hints": [
      "Choosing a subsequence from the string is equivalent to deleting all the other digits.",
      "If you were to remove a digit, which one should you remove to reduce the value of the string?"
    ]
  },
  {
    "title": "Count Subarrays With Score Less Than K",
    "description": "The score of an array is defined as the product of its sum and its length.\n\nFor example, the score of [1, 2, 3, 4, 5] is (1 + 2 + 3 + 4 + 5) * 5 = 75.\n\nGiven a positive integer array nums and an integer k, return the number of non-empty subarrays of nums whose score is strictly less than k.\nA subarray is a contiguous sequence of elements within an array.\n \n",
    "examples": [
      {
        "input": "Input: nums = [2,1,4,3,5], k = 10",
        "output": "Output: 6",
        "explanation": ""
      },
      {
        "input": "Input: nums = [1,1,1], k = 5",
        "output": "Output: 5",
        "explanation": ""
      }
    ],
    "topics": [
      "Array",
      "Binary Search",
      "Sliding Window",
      "Prefix Sum"
    ],
    "difficulty": "Hard",
    "constraints": [
      "1 <= nums.length <= 105",
      "1 <= nums[i] <= 105",
      "1 <= k <= 1015"
    ],
    "hints": [
      "If we add an element to a list of elements, how will the score change?",
      "How can we use this to determine the number of subarrays with score less than k in a given range?",
      "How can we use “Two Pointers” to generalize the solution, and thus count all possible subarrays?"
    ]
  },
  {
    "title": "Match Substring After Replacement",
    "description": "You are given two strings s and sub. You are also given a 2D character array mappings where mappings[i] = [oldi, newi] indicates that you may perform the following operation any number of times:\n\nReplace a character oldi of sub with newi.\n\nEach character in sub cannot be replaced more than once.\nReturn true if it is possible to make sub a substring of s by replacing zero or more characters according to mappings. Otherwise, return false.\nA substring is a contiguous non-empty sequence of characters within a string.\n \n",
    "examples": [
      {
        "input": "Input: s = \"fool3e7bar\", sub = \"leet\", mappings = [[\"e\",\"3\"],[\"t\",\"7\"],[\"t\",\"8\"]]",
        "output": "Output: true",
        "explanation": "Explanation: Replace the first 'e' in sub with '3' and 't' in sub with '7'."
      },
      {
        "input": "Input: s = \"fooleetbar\", sub = \"f00l\", mappings = [[\"o\",\"0\"]]",
        "output": "Output: false",
        "explanation": "Explanation: The string \"f00l\" is not a substring of s and no replacements can be made."
      },
      {
        "input": "Input: s = \"Fool33tbaR\", sub = \"leetd\", mappings = [[\"e\",\"3\"],[\"t\",\"7\"],[\"t\",\"8\"],[\"d\",\"b\"],[\"p\",\"b\"]]",
        "output": "Output: true",
        "explanation": "Explanation: Replace the first and second 'e' in sub with '3' and 'd' in sub with 'b'."
      }
    ],
    "topics": [
      "Array",
      "Hash Table",
      "String",
      "String Matching"
    ],
    "difficulty": "Hard",
    "constraints": [
      "1 <= sub.length <= s.length <= 5000",
      "0 <= mappings.length <= 1000",
      "mappings[i].length == 2",
      "oldi != newi",
      "s and sub consist of uppercase and lowercase English letters and digits.",
      "oldi and newi are either uppercase or lowercase English letters or digits."
    ],
    "hints": [
      "Enumerate all substrings of s with the same length as sub, and compare each substring to sub for equality.",
      "How can you quickly tell if a character of s can result from replacing the corresponding character in sub?"
    ]
  },
  {
    "title": "Successful Pairs of Spells and Potions",
    "description": "You are given two positive integer arrays spells and potions, of length n and m respectively, where spells[i] represents the strength of the ith spell and potions[j] represents the strength of the jth potion.\nYou are also given an integer success. A spell and potion pair is considered successful if the product of their strengths is at least success.\nReturn an integer array pairs of length n where pairs[i] is the number of potions that will form a successful pair with the ith spell.\n \n",
    "examples": [
      {
        "input": "Input: spells = [5,1,3], potions = [1,2,3,4,5], success = 7",
        "output": "Output: [4,0,3]",
        "explanation": ""
      },
      {
        "input": "Input: spells = [3,1,2], potions = [8,5,8], success = 16",
        "output": "Output: [2,0,2]",
        "explanation": ""
      }
    ],
    "topics": [
      "Array",
      "Two Pointers",
      "Binary Search",
      "Sorting"
    ],
    "difficulty": "Medium",
    "constraints": [
      "n == spells.length",
      "m == potions.length",
      "1 <= n, m <= 105",
      "1 <= spells[i], potions[i] <= 105",
      "1 <= success <= 1010"
    ],
    "hints": [
      "Notice that if a spell and potion pair is successful, then the spell and all stronger potions will be successful too.",
      "Thus, for each spell, we need to find the potion with the least strength that will form a successful pair.",
      "We can efficiently do this by sorting the potions based on strength and using binary search."
    ]
  },
  {
    "title": "Strong Password Checker II",
    "description": "A password is said to be strong if it satisfies all the following criteria:\n\nIt has at least 8 characters.\nIt contains at least one lowercase letter.\nIt contains at least one uppercase letter.\nIt contains at least one digit.\nIt contains at least one special character. The special characters are the characters in the following string: \"!@#$%^&*()-+\".\nIt does not contain 2 of the same character in adjacent positions (i.e., \"aab\" violates this condition, but \"aba\" does not).\n\nGiven a string password, return true if it is a strong password. Otherwise, return false.\n \n",
    "examples": [
      {
        "input": "Input: password = \"IloveLe3tcode!\"",
        "output": "Output: true",
        "explanation": "Explanation: The password meets all the requirements. Therefore, we return true."
      },
      {
        "input": "Input: password = \"Me+You--IsMyDream\"",
        "output": "Output: false",
        "explanation": "Explanation: The password does not contain a digit and also contains 2 of the same character in adjacent positions. Therefore, we return false."
      },
      {
        "input": "Input: password = \"1aB!\"",
        "output": "Output: false",
        "explanation": "Explanation: The password does not meet the length requirement. Therefore, we return false."
      }
    ],
    "topics": [
      "String"
    ],
    "difficulty": "Easy",
    "constraints": [
      "1 <= password.length <= 100",
      "password consists of letters, digits, and special characters: \"!@#$%^&*()-+\"."
    ],
    "hints": [
      "You can use a boolean flag to define certain types of characters seen in the string.",
      "In the end, check if all boolean flags have ended up True, and do not forget to check the \"adjacent\" and \"length\" criteria."
    ]
  },
  {
    "title": "Naming a Company",
    "description": "You are given an array of strings ideas that represents a list of names to be used in the process of naming a company. The process of naming a company is as follows:\n\nChoose 2 distinct names from ideas, call them ideaA and ideaB.\nSwap the first letters of ideaA and ideaB with each other.\nIf both of the new names are not found in the original ideas, then the name ideaA ideaB (the concatenation of ideaA and ideaB, separated by a space) is a valid company name.\nOtherwise, it is not a valid name.\n\nReturn the number of distinct valid names for the company.\n \n",
    "examples": [
      {
        "input": "Input: ideas = [\"coffee\",\"donuts\",\"time\",\"toffee\"]",
        "output": "Output: 6",
        "explanation": "Explanation: The following selections are valid:"
      },
      {
        "input": "Input: ideas = [\"lack\",\"back\"]",
        "output": "Output: 0",
        "explanation": "Explanation: There are no valid selections. Therefore, 0 is returned."
      }
    ],
    "topics": [
      "Array",
      "Hash Table",
      "String",
      "Bit Manipulation",
      "Enumeration"
    ],
    "difficulty": "Hard",
    "constraints": [
      "2 <= ideas.length <= 5 * 104",
      "1 <= ideas[i].length <= 10",
      "ideas[i] consists of lowercase English letters.",
      "All the strings in ideas are unique."
    ],
    "hints": [
      "How can we divide the ideas into groups to make it easier to find valid pairs?",
      "Group ideas that share the same suffix (all characters except the first) together and notice that a pair of ideas from the same group is invalid. What about pairs of ideas from different groups?",
      "The first letter of the idea in the first group must not be the first letter of an idea in the second group and vice versa.",
      "We can efficiently count the valid pairings for an idea if we already know how many ideas starting with a letter x are within a group that does not contain any ideas with starting letter y for all letters x and y."
    ]
  },
  {
    "title": "Design a Text Editor",
    "description": "Design a text editor with a cursor that can do the following:\n\nAdd text to where the cursor is.\nDelete text from where the cursor is (simulating the backspace key).\nMove the cursor either left or right.\n\nWhen deleting text, only characters to the left of the cursor will be deleted. The cursor will also remain within the actual text and cannot be moved beyond it. More formally, we have that 0 <= cursor.position <= currentText.length always holds.\nImplement the TextEditor class:\n\nTextEditor() Initializes the object with empty text.\nvoid addText(string text) Appends text to where the cursor is. The cursor ends to the right of text.\nint deleteText(int k) Deletes k characters to the left of the cursor. Returns the number of characters actually deleted.\nstring cursorLeft(int k) Moves the cursor to the left k times. Returns the last min(10, len) characters to the left of the cursor, where len is the number of characters to the left of the cursor.\nstring cursorRight(int k) Moves the cursor to the right k times. Returns the last min(10, len) characters to the left of the cursor, where len is the number of characters to the left of the cursor.\n\n \n",
    "examples": [
      {
        "input": "Input\n[\"TextEditor\", \"addText\", \"deleteText\", \"addText\", \"cursorRight\", \"cursorLeft\", \"deleteText\", \"cursorLeft\", \"cursorRight\"]",
        "output": "Output\n[null, null, 4, null, \"etpractice\", \"leet\", 4, \"\", \"practi\"]",
        "explanation": "Explanation\nTextEditor textEditor = new TextEditor(); // The current text is \"|\". (The '|' character represents the cursor)"
      }
    ],
    "topics": [
      "Linked List",
      "String",
      "Stack",
      "Design",
      "Simulation",
      "Doubly-Linked List"
    ],
    "difficulty": "Hard",
    "constraints": [
      "1 <= text.length, k <= 40",
      "text consists of lowercase English letters.",
      "At most 2 * 104 calls in total will be made to addText, deleteText, cursorLeft and cursorRight.",
      "",
      " ",
      "Follow-up: Could you find a solution with time complexity of O(k) per call?"
    ],
    "hints": [
      "Making changes in the middle of some data structures is generally harder than changing the front/back of the same data structure.",
      "Can you partition your data structure (text with cursor) into two parts, such that each part changes only near its ends?",
      "Can you think of a data structure that supports efficient removals/additions to the front/back?",
      "Try to solve the problem with two deques by maintaining the prefix and the suffix separately."
    ]
  },
  {
    "title": "Replace Elements in an Array",
    "description": "You are given a 0-indexed array nums that consists of n distinct positive integers. Apply m operations to this array, where in the ith operation you replace the number operations[i][0] with operations[i][1].\nIt is guaranteed that in the ith operation:\n\noperations[i][0] exists in nums.\noperations[i][1] does not exist in nums.\n\nReturn the array obtained after applying all the operations.\n \n",
    "examples": [
      {
        "input": "Input: nums = [1,2,4,6], operations = [[1,3],[4,7],[6,1]]",
        "output": "Output: [3,2,7,1]",
        "explanation": "Explanation: We perform the following operations on nums:"
      },
      {
        "input": "Input: nums = [1,2], operations = [[1,3],[2,1],[3,2]]",
        "output": "Output: [2,1]",
        "explanation": "Explanation: We perform the following operations to nums:"
      }
    ],
    "topics": [
      "Array",
      "Hash Table",
      "Simulation"
    ],
    "difficulty": "Medium",
    "constraints": [
      "n == nums.length",
      "m == operations.length",
      "1 <= n, m <= 105",
      "All the values of nums are distinct.",
      "operations[i].length == 2",
      "1 <= nums[i], operations[i][0], operations[i][1] <= 106",
      "operations[i][0] will exist in nums when applying the ith operation.",
      "operations[i][1] will not exist in nums when applying the ith operation."
    ],
    "hints": [
      "Can you think of a data structure that will allow you to store the position of each number?",
      "Use that data structure to instantly replace a number with its new value."
    ]
  },
  {
    "title": "Partition Array Such That Maximum Difference Is K",
    "description": "You are given an integer array nums and an integer k. You may partition nums into one or more subsequences such that each element in nums appears in exactly one of the subsequences.\nReturn the minimum number of subsequences needed such that the difference between the maximum and minimum values in each subsequence is at most k.\nA subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.\n \n",
    "examples": [
      {
        "input": "Input: nums = [3,6,1,2,5], k = 2",
        "output": "Output: 2",
        "explanation": ""
      },
      {
        "input": "Input: nums = [1,2,3], k = 1",
        "output": "Output: 2",
        "explanation": ""
      },
      {
        "input": "Input: nums = [2,2,4,5], k = 0",
        "output": "Output: 3",
        "explanation": ""
      }
    ],
    "topics": [
      "Array",
      "Greedy",
      "Sorting"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= nums.length <= 105",
      "0 <= nums[i] <= 105",
      "0 <= k <= 105"
    ],
    "hints": [
      "Which values in each subsequence matter? The only values that matter are the maximum and minimum values.",
      "Let the maximum and minimum values of a subsequence be Max and Min. It is optimal to place all values in between Max and Min in the original array in the same subsequence as Max and Min.",
      "Sort the array."
    ]
  },
  {
    "title": "Min Max Game",
    "description": "You are given a 0-indexed integer array nums whose length is a power of 2.\nApply the following algorithm on nums:\n\nLet n be the length of nums. If n == 1, end the process. Otherwise, create a new 0-indexed integer array newNums of length n / 2.\nFor every even index i where 0 <= i < n / 2, assign the value of newNums[i] as min(nums[2 * i], nums[2 * i + 1]).\nFor every odd index i where 0 <= i < n / 2, assign the value of newNums[i] as max(nums[2 * i], nums[2 * i + 1]).\nReplace the array nums with newNums.\nRepeat the entire process starting from step 1.\n\nReturn the last number that remains in nums after applying the algorithm.\n \n",
    "examples": [
      {
        "input": "Input: nums = [1,3,5,2,4,8,2,2]",
        "output": "Output: 1",
        "explanation": "Explanation: The following arrays are the results of applying the algorithm repeatedly."
      },
      {
        "input": "Input: nums = [3]",
        "output": "Output: 3",
        "explanation": "Explanation: 3 is already the last remaining number, so we return 3."
      }
    ],
    "topics": [
      "Array",
      "Simulation"
    ],
    "difficulty": "Easy",
    "constraints": [
      "1 <= nums.length <= 1024",
      "1 <= nums[i] <= 109",
      "nums.length is a power of 2."
    ],
    "hints": [
      "Simply simulate the algorithm.",
      "Note that the size of the array decreases exponentially, so the process will terminate after just O(log n) steps."
    ]
  },
  {
    "title": "Root Equals Sum of Children",
    "description": "You are given the root of a binary tree that consists of exactly 3 nodes: the root, its left child, and its right child.\nReturn true if the value of the root is equal to the sum of the values of its two children, or false otherwise.\n \n",
    "examples": [
      {
        "input": "Input: root = [10,4,6]",
        "output": "Output: true",
        "explanation": "Explanation: The values of the root, its left child, and its right child are 10, 4, and 6, respectively."
      },
      {
        "input": "Input: root = [5,3,1]",
        "output": "Output: false",
        "explanation": "Explanation: The values of the root, its left child, and its right child are 5, 3, and 1, respectively."
      }
    ],
    "topics": [
      "Tree",
      "Binary Tree"
    ],
    "difficulty": "Easy",
    "constraints": [
      "The tree consists only of the root, its left child, and its right child.",
      "-100 <= Node.val <= 100"
    ],
    "hints": []
  },
  {
    "title": "Add Two Integers",
    "description": "Given two integers num1 and num2, return the sum of the two integers.\n \n",
    "examples": [
      {
        "input": "Input: num1 = 12, num2 = 5",
        "output": "Output: 17",
        "explanation": "Explanation: num1 is 12, num2 is 5, and their sum is 12 + 5 = 17, so 17 is returned."
      },
      {
        "input": "Input: num1 = -10, num2 = 4",
        "output": "Output: -6",
        "explanation": "Explanation: num1 + num2 = -6, so -6 is returned."
      }
    ],
    "topics": [
      "Math"
    ],
    "difficulty": "Easy",
    "constraints": [
      "-100 <= num1, num2 <= 100"
    ],
    "hints": []
  },
  {
    "title": "Booking Concert Tickets in Groups",
    "description": "A concert hall has n rows numbered from 0 to n - 1, each with m seats, numbered from 0 to m - 1. You need to design a ticketing system that can allocate seats in the following cases:\n\nIf a group of k spectators can sit together in a row.\nIf every member of a group of k spectators can get a seat. They may or may not sit together.\n\nNote that the spectators are very picky. Hence:\n\nThey will book seats only if each member of their group can get a seat with row number less than or equal to maxRow. maxRow can vary from group to group.\nIn case there are multiple rows to choose from, the row with the smallest number is chosen. If there are multiple seats to choose in the same row, the seat with the smallest number is chosen.\n\nImplement the BookMyShow class:\n\nBookMyShow(int n, int m) Initializes the object with n as number of rows and m as number of seats per row.\nint[] gather(int k, int maxRow) Returns an array of length 2 denoting the row and seat number (respectively) of the first seat being allocated to the k members of the group, who must sit together. In other words, it returns the smallest possible r and c such that all [c, c + k - 1] seats are valid and empty in row r, and r <= maxRow. Returns [] in case it is not possible to allocate seats to the group.\nboolean scatter(int k, int maxRow) Returns true if all k members of the group can be allocated seats in rows 0 to maxRow, who may or may not sit together. If the seats can be allocated, it allocates k seats to the group with the smallest row numbers, and the smallest possible seat numbers in each row. Otherwise, returns false.\n\n \n",
    "examples": [
      {
        "input": "Input\n[\"BookMyShow\", \"gather\", \"gather\", \"scatter\", \"scatter\"]",
        "output": "Output\n[null, [0, 0], [], true, false]",
        "explanation": "Explanation\nBookMyShow bms = new BookMyShow(2, 5); // There are 2 rows with 5 seats each "
      }
    ],
    "topics": [
      "Binary Search",
      "Design",
      "Binary Indexed Tree",
      "Segment Tree"
    ],
    "difficulty": "Hard",
    "constraints": [
      "1 <= n <= 5 * 104",
      "1 <= m, k <= 109",
      "0 <= maxRow <= n - 1",
      "At most 5 * 104 calls in total will be made to gather and scatter."
    ],
    "hints": [
      "Since seats are allocated by smallest row and then by smallest seat numbers, how can we keep a record of the smallest seat number vacant in each row?",
      "How can range max query help us to check if contiguous seats can be allocated in a range?",
      "Similarly, can range sum query help us to check if enough seats are available in a range?",
      "Which data structure can be used to implement the above?"
    ]
  },
  {
    "title": "Maximum Total Importance of Roads",
    "description": "You are given an integer n denoting the number of cities in a country. The cities are numbered from 0 to n - 1.\nYou are also given a 2D integer array roads where roads[i] = [ai, bi] denotes that there exists a bidirectional road connecting cities ai and bi.\nYou need to assign each city with an integer value from 1 to n, where each value can only be used once. The importance of a road is then defined as the sum of the values of the two cities it connects.\nReturn the maximum total importance of all roads possible after assigning the values optimally.\n \n",
    "examples": [
      {
        "input": "Input: n = 5, roads = [[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]]",
        "output": "Output: 43",
        "explanation": "Explanation: The figure above shows the country and the assigned values of [2,4,5,3,1]."
      },
      {
        "input": "Input: n = 5, roads = [[0,3],[2,4],[1,3]]",
        "output": "Output: 20",
        "explanation": "Explanation: The figure above shows the country and the assigned values of [4,3,2,5,1]."
      }
    ],
    "topics": [
      "Greedy",
      "Graph",
      "Sorting",
      "Heap (Priority Queue)"
    ],
    "difficulty": "Medium",
    "constraints": [
      "2 <= n <= 5 * 104",
      "1 <= roads.length <= 5 * 104",
      "roads[i].length == 2",
      "0 <= ai, bi <= n - 1",
      "ai != bi",
      "There are no duplicate roads."
    ],
    "hints": [
      "Consider what each city contributes to the total importance of all roads.",
      "Based on that, how can you sort the cities such that assigning them values in that order will yield the maximum total importance?"
    ]
  },
  {
    "title": "Sender With Largest Word Count",
    "description": "You have a chat log of n messages. You are given two string arrays messages and senders where messages[i] is a message sent by senders[i].\nA message is list of words that are separated by a single space with no leading or trailing spaces. The word count of a sender is the total number of words sent by the sender. Note that a sender may send more than one message.\nReturn the sender with the largest word count. If there is more than one sender with the largest word count, return the one with the lexicographically largest name.\nNote:\n\nUppercase letters come before lowercase letters in lexicographical order.\n\"Alice\" and \"alice\" are distinct.\n\n \n",
    "examples": [
      {
        "input": "Input: messages = [\"Hello userTwooo\",\"Hi userThree\",\"Wonderful day Alice\",\"Nice day userThree\"], senders = [\"Alice\",\"userTwo\",\"userThree\",\"Alice\"]",
        "output": "Output: \"Alice\"",
        "explanation": "Explanation: Alice sends a total of 2 + 3 = 5 words."
      },
      {
        "input": "Input: messages = [\"How is leetcode for everyone\",\"Leetcode is useful for practice\"], senders = [\"Bob\",\"Charlie\"]",
        "output": "Output: \"Charlie\"",
        "explanation": "Explanation: Bob sends a total of 5 words."
      }
    ],
    "topics": [
      "Array",
      "Hash Table",
      "String",
      "Counting"
    ],
    "difficulty": "Medium",
    "constraints": [
      "n == messages.length == senders.length",
      "1 <= n <= 104",
      "1 <= messages[i].length <= 100",
      "1 <= senders[i].length <= 10",
      "messages[i] consists of uppercase and lowercase English letters and ' '.",
      "All the words in messages[i] are separated by a single space.",
      "messages[i] does not have leading or trailing spaces.",
      "senders[i] consists of uppercase and lowercase English letters only."
    ],
    "hints": [
      "The number of words in a message is equal to the number of spaces + 1.",
      "Use a hash map to count the total number of words from each sender."
    ]
  },
  {
    "title": "Check if Number Has Equal Digit Count and Digit Value",
    "description": "You are given a 0-indexed string num of length n consisting of digits.\nReturn true if for every index i in the range 0 <= i < n, the digit i occurs num[i] times in num, otherwise return false.\n \n",
    "examples": [
      {
        "input": "Input: num = \"1210\"",
        "output": "Output: true",
        "explanation": ""
      },
      {
        "input": "Input: num = \"030\"",
        "output": "Output: false",
        "explanation": ""
      }
    ],
    "topics": [
      "Hash Table",
      "String",
      "Counting"
    ],
    "difficulty": "Easy",
    "constraints": [
      "n == num.length",
      "1 <= n <= 10",
      "num consists of digits."
    ],
    "hints": [
      "Count the frequency of each digit in num."
    ]
  },
  {
    "title": "Minimum Obstacle Removal to Reach Corner",
    "description": "You are given a 0-indexed 2D integer array grid of size m x n. Each cell has one of two values:\n\n0 represents an empty cell,\n1 represents an obstacle that may be removed.\n\nYou can move up, down, left, or right from and to an empty cell.\nReturn the minimum number of obstacles to remove so you can move from the upper left corner (0, 0) to the lower right corner (m - 1, n - 1).\n \n",
    "examples": [
      {
        "input": "Input: grid = [[0,1,1],[1,1,0],[1,1,0]]",
        "output": "Output: 2",
        "explanation": "Explanation: We can remove the obstacles at (0, 1) and (0, 2) to create a path from (0, 0) to (2, 2)."
      },
      {
        "input": "Input: grid = [[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]]",
        "output": "Output: 0",
        "explanation": "Explanation: We can move from (0, 0) to (2, 4) without removing any obstacles, so we return 0."
      }
    ],
    "topics": [
      "Array",
      "Breadth-First Search",
      "Graph",
      "Heap (Priority Queue)",
      "Matrix",
      "Shortest Path"
    ],
    "difficulty": "Hard",
    "constraints": [
      "m == grid.length",
      "n == grid[i].length",
      "1 <= m, n <= 105",
      "2 <= m * n <= 105",
      "grid[i][j] is either 0 or 1.",
      "grid[0][0] == grid[m - 1][n - 1] == 0"
    ],
    "hints": [
      "Model the grid as a graph where cells are nodes and edges are between adjacent cells. Edges to cells with obstacles have a cost of 1 and all other edges have a cost of 0.",
      "Could you use 0-1 Breadth-First Search or Dijkstra’s algorithm?"
    ]
  },
  {
    "title": "Steps to Make Array Non-decreasing",
    "description": "You are given a 0-indexed integer array nums. In one step, remove all elements nums[i] where nums[i - 1] > nums[i] for all 0 < i < nums.length.\nReturn the number of steps performed until nums becomes a non-decreasing array.\n \n",
    "examples": [
      {
        "input": "Input: nums = [5,3,4,4,7,3,6,11,8,5,11]",
        "output": "Output: 3",
        "explanation": "Explanation: The following are the steps performed:"
      },
      {
        "input": "Input: nums = [4,5,7,7,13]",
        "output": "Output: 0",
        "explanation": "Explanation: nums is already a non-decreasing array. Therefore, we return 0."
      }
    ],
    "topics": [
      "Array",
      "Linked List",
      "Stack",
      "Monotonic Stack"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= nums.length <= 105",
      "1 <= nums[i] <= 109"
    ],
    "hints": [
      "Notice that an element will be removed if and only if there exists a strictly greater element to the left of it in the array.",
      "For each element, we need to find the number of rounds it will take for it to be removed. The answer is the maximum number of rounds for all elements. Build an array dp to hold this information where the answer is the maximum value of dp.",
      "Use a stack of the indices. While processing element nums[i], remove from the stack all the indices of elements that are smaller than nums[i]. dp[i] should be set to the maximum of dp[i] + 1 and dp[removed index]."
    ]
  },
  {
    "title": "Apply Discount to Prices",
    "description": "A sentence is a string of single-space separated words where each word can contain digits, lowercase letters, and the dollar sign '$'. A word represents a price if it is a sequence of digits preceded by a dollar sign.\n\nFor example, \"$100\", \"$23\", and \"$6\" represent prices while \"100\", \"$\", and \"$1e5\" do not.\n\nYou are given a string sentence representing a sentence and an integer discount. For each word representing a price, apply a discount of discount% on the price and update the word in the sentence. All updated prices should be represented with exactly two decimal places.\nReturn a string representing the modified sentence.\nNote that all prices will contain at most 10 digits.\n \n",
    "examples": [
      {
        "input": "Input: sentence = \"there are $1 $2 and 5$ candies in the shop\", discount = 50",
        "output": "Output: \"there are $0.50 $1.00 and 5$ candies in the shop\"",
        "explanation": "Explanation: "
      },
      {
        "input": "Input: sentence = \"1 2 $3 4 $5 $6 7 8$ $9 $10$\", discount = 100",
        "output": "Output: \"1 2 $0.00 4 $0.00 $0.00 7 8$ $0.00 $10$\"",
        "explanation": "Explanation: "
      }
    ],
    "topics": [
      "String"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= sentence.length <= 105",
      "sentence consists of lowercase English letters, digits, ' ', and '$'.",
      "sentence does not have leading or trailing spaces.",
      "All words in sentence are separated by a single space.",
      "All prices will be positive numbers without leading zeros.",
      "All prices will have at most 10 digits.",
      "0 <= discount <= 100"
    ],
    "hints": [
      "Extract each word from the sentence and check if it represents a price.",
      "For each price, apply the given discount to it and update it."
    ]
  },
  {
    "title": "Rearrange Characters to Make Target String",
    "description": "You are given two 0-indexed strings s and target. You can take some letters from s and rearrange them to form new strings.\nReturn the maximum number of copies of target that can be formed by taking letters from s and rearranging them.\n \n",
    "examples": [
      {
        "input": "Input: s = \"ilovecodingonleetcode\", target = \"code\"",
        "output": "Output: 2",
        "explanation": ""
      },
      {
        "input": "Input: s = \"abcba\", target = \"abc\"",
        "output": "Output: 1",
        "explanation": ""
      },
      {
        "input": "Input: s = \"abbaccaddaeea\", target = \"aaaaa\"",
        "output": "Output: 1",
        "explanation": ""
      }
    ],
    "topics": [
      "Hash Table",
      "String",
      "Counting"
    ],
    "difficulty": "Easy",
    "constraints": [
      "1 <= s.length <= 100",
      "1 <= target.length <= 10",
      "s and target consist of lowercase English letters."
    ],
    "hints": [
      "Count the frequency of each character in s and target.",
      "Consider each letter one at a time. If there are x occurrences of a letter in s and y occurrences of the same letter in target, how many copies of this letter can we make?",
      "We can make floor(x / y) copies of the letter."
    ]
  },
  {
    "title": "Sum of Total Strength of Wizards",
    "description": "As the ruler of a kingdom, you have an army of wizards at your command.\nYou are given a 0-indexed integer array strength, where strength[i] denotes the strength of the ith wizard. For a contiguous group of wizards (i.e. the wizards' strengths form a subarray of strength), the total strength is defined as the product of the following two values:\n\nThe strength of the weakest wizard in the group.\nThe total of all the individual strengths of the wizards in the group.\n\nReturn the sum of the total strengths of all contiguous groups of wizards. Since the answer may be very large, return it modulo 109 + 7.\nA subarray is a contiguous non-empty sequence of elements within an array.\n \n",
    "examples": [
      {
        "input": "Input: strength = [1,3,1,2]",
        "output": "Output: 44",
        "explanation": "Explanation: The following are all the contiguous groups of wizards:"
      },
      {
        "input": "Input: strength = [5,4,6]",
        "output": "Output: 213",
        "explanation": "Explanation: The following are all the contiguous groups of wizards: "
      }
    ],
    "topics": [
      "Array",
      "Stack",
      "Monotonic Stack",
      "Prefix Sum"
    ],
    "difficulty": "Hard",
    "constraints": [
      "1 <= strength.length <= 105",
      "1 <= strength[i] <= 109"
    ],
    "hints": [
      "Consider the contribution of each wizard to the answer.",
      "Can you efficiently calculate the total contribution to the answer for all subarrays that end at each index?",
      "Denote the total contribution of all subarrays ending at index i as solve[i]. Can you express solve[i] in terms of solve[m] for some m < i?"
    ]
  },
  {
    "title": "Minimum Lines to Represent a Line Chart",
    "description": "You are given a 2D integer array stockPrices where stockPrices[i] = [dayi, pricei] indicates the price of the stock on day dayi is pricei. A line chart is created from the array by plotting the points on an XY plane with the X-axis representing the day and the Y-axis representing the price and connecting adjacent points. One such example is shown below:\n\nReturn the minimum number of lines needed to represent the line chart.\n \n",
    "examples": [
      {
        "input": "Input: stockPrices = [[1,7],[2,6],[3,5],[4,4],[5,4],[6,3],[7,2],[8,1]]",
        "output": "Output: 3",
        "explanation": ""
      },
      {
        "input": "Input: stockPrices = [[3,4],[1,2],[7,8],[2,3]]",
        "output": "Output: 1",
        "explanation": ""
      }
    ],
    "topics": [
      "Array",
      "Math",
      "Geometry",
      "Sorting",
      "Number Theory"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= stockPrices.length <= 105",
      "stockPrices[i].length == 2",
      "1 <= dayi, pricei <= 109",
      "All dayi are distinct."
    ],
    "hints": [
      "When will three adjacent points lie on the same line? How can we generalize this for all points?",
      "Will calculating the slope of lines connecting adjacent points help us find the answer?"
    ]
  },
  {
    "title": "Maximum Bags With Full Capacity of Rocks",
    "description": "You have n bags numbered from 0 to n - 1. You are given two 0-indexed integer arrays capacity and rocks. The ith bag can hold a maximum of capacity[i] rocks and currently contains rocks[i] rocks. You are also given an integer additionalRocks, the number of additional rocks you can place in any of the bags.\nReturn the maximum number of bags that could have full capacity after placing the additional rocks in some bags.\n \n",
    "examples": [
      {
        "input": "Input: capacity = [2,3,4,5], rocks = [1,2,4,4], additionalRocks = 2",
        "output": "Output: 3",
        "explanation": ""
      },
      {
        "input": "Input: capacity = [10,2,2], rocks = [2,2,0], additionalRocks = 100",
        "output": "Output: 3",
        "explanation": ""
      }
    ],
    "topics": [
      "Array",
      "Greedy",
      "Sorting"
    ],
    "difficulty": "Medium",
    "constraints": [
      "n == capacity.length == rocks.length",
      "1 <= n <= 5 * 104",
      "1 <= capacity[i] <= 109",
      "0 <= rocks[i] <= capacity[i]",
      "1 <= additionalRocks <= 109"
    ],
    "hints": [
      "Which bag should you fill completely first?",
      "Can you think of a greedy solution?"
    ]
  },
  {
    "title": "Percentage of Letter in String",
    "description": "Given a string s and a character letter, return the percentage of characters in s that equal letter rounded down to the nearest whole percent.\n \n",
    "examples": [
      {
        "input": "Input: s = \"foobar\", letter = \"o\"",
        "output": "Output: 33",
        "explanation": ""
      },
      {
        "input": "Input: s = \"jjjj\", letter = \"k\"",
        "output": "Output: 0",
        "explanation": ""
      }
    ],
    "topics": [
      "String"
    ],
    "difficulty": "Easy",
    "constraints": [
      "1 <= s.length <= 100",
      "s consists of lowercase English letters.",
      "letter is a lowercase English letter."
    ],
    "hints": [
      "Can we count the number of occurrences of letter in s?",
      "Recall that the percentage is calculated as (occurrences / total) * 100."
    ]
  },
  {
    "title": "Longest Path With Different Adjacent Characters",
    "description": "You are given a tree (i.e. a connected, undirected graph that has no cycles) rooted at node 0 consisting of n nodes numbered from 0 to n - 1. The tree is represented by a 0-indexed array parent of size n, where parent[i] is the parent of node i. Since node 0 is the root, parent[0] == -1.\nYou are also given a string s of length n, where s[i] is the character assigned to node i.\nReturn the length of the longest path in the tree such that no pair of adjacent nodes on the path have the same character assigned to them.\n \n",
    "examples": [
      {
        "input": "Input: parent = [-1,0,0,1,1,2], s = \"abacbe\"",
        "output": "Output: 3",
        "explanation": "Explanation: The longest path where each two adjacent nodes have different characters in the tree is the path: 0 -> 1 -> 3. The length of this path is 3, so 3 is returned."
      },
      {
        "input": "Input: parent = [-1,0,0,0], s = \"aabc\"",
        "output": "Output: 3",
        "explanation": "Explanation: The longest path where each two adjacent nodes have different characters is the path: 2 -> 0 -> 3. The length of this path is 3, so 3 is returned."
      }
    ],
    "topics": [
      "Array",
      "String",
      "Tree",
      "Depth-First Search",
      "Graph",
      "Topological Sort"
    ],
    "difficulty": "Hard",
    "constraints": [
      "n == parent.length == s.length",
      "1 <= n <= 105",
      "0 <= parent[i] <= n - 1 for all i >= 1",
      "parent[0] == -1",
      "parent represents a valid tree.",
      "s consists of only lowercase English letters."
    ],
    "hints": [
      "Do a DFS from the root. At each node, calculate the longest path we can make from two branches of that subtree.",
      "To do that, we need to find the length of the longest path from each of the node’s children."
    ]
  },
  {
    "title": "Maximum Trailing Zeros in a Cornered Path",
    "description": "You are given a 2D integer array grid of size m x n, where each cell contains a positive integer.\nA cornered path is defined as a set of adjacent cells with at most one turn. More specifically, the path should exclusively move either horizontally or vertically up to the turn (if there is one), without returning to a previously visited cell. After the turn, the path will then move exclusively in the alternate direction: move vertically if it moved horizontally, and vice versa, also without returning to a previously visited cell.\nThe product of a path is defined as the product of all the values in the path.\nReturn the maximum number of trailing zeros in the product of a cornered path found in grid.\nNote:\n\nHorizontal movement means moving in either the left or right direction.\nVertical movement means moving in either the up or down direction.\n\n \n",
    "examples": [
      {
        "input": "Input: grid = [[23,17,15,3,20],[8,1,20,27,11],[9,4,6,2,21],[40,9,1,10,6],[22,7,4,5,3]]",
        "output": "Output: 3",
        "explanation": "Explanation: The grid on the left shows a valid cornered path."
      },
      {
        "input": "Input: grid = [[4,3,2],[7,6,1],[8,8,8]]",
        "output": "Output: 0",
        "explanation": "Explanation: The grid is shown in the figure above."
      }
    ],
    "topics": [
      "Array",
      "Matrix",
      "Prefix Sum"
    ],
    "difficulty": "Medium",
    "constraints": [
      "m == grid.length",
      "n == grid[i].length",
      "1 <= m, n <= 105",
      "1 <= m * n <= 105",
      "1 <= grid[i][j] <= 1000"
    ],
    "hints": [
      "What actually tells us the trailing zeros of the product of a path?",
      "It is the sum of the exponents of 2 and sum of the exponents of 5 of the prime factorizations of the numbers on that path. The smaller of the two is the answer for that path.",
      "We can then treat each cell as the elbow point and calculate the largest minimum (sum of 2 exponents, sum of 5 exponents) from the combination of top-left, top-right, bottom-left and bottom-right.",
      "To do this efficiently, we should use the prefix sum technique."
    ]
  },
  {
    "title": "Minimum Rounds to Complete All Tasks",
    "description": "You are given a 0-indexed integer array tasks, where tasks[i] represents the difficulty level of a task. In each round, you can complete either 2 or 3 tasks of the same difficulty level.\nReturn the minimum rounds required to complete all the tasks, or -1 if it is not possible to complete all the tasks.\n \n",
    "examples": [
      {
        "input": "Input: tasks = [2,2,3,3,2,4,4,4,4,4]",
        "output": "Output: 4",
        "explanation": "Explanation: To complete all the tasks, a possible plan is:"
      },
      {
        "input": "Input: tasks = [2,3,3]",
        "output": "Output: -1",
        "explanation": "Explanation: There is only 1 task of difficulty level 2, but in each round, you can only complete either 2 or 3 tasks of the same difficulty level. Hence, you cannot complete all the tasks, and the answer is -1."
      }
    ],
    "topics": [
      "Array",
      "Hash Table",
      "Greedy",
      "Counting"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= tasks.length <= 105",
      "1 <= tasks[i] <= 109"
    ],
    "hints": [
      "Which data structure can you use to store the number of tasks of each difficulty level?",
      "For any particular difficulty level, what can be the optimal strategy to complete the tasks using minimum rounds?",
      "When can we not complete all tasks of a difficulty level?"
    ]
  },
  {
    "title": "Calculate Digit Sum of a String",
    "description": "You are given a string s consisting of digits and an integer k.\nA round can be completed if the length of s is greater than k. In one round, do the following:\n\nDivide s into consecutive groups of size k such that the first k characters are in the first group, the next k characters are in the second group, and so on. Note that the size of the last group can be smaller than k.\nReplace each group of s with a string representing the sum of all its digits. For example, \"346\" is replaced with \"13\" because 3 + 4 + 6 = 13.\nMerge consecutive groups together to form a new string. If the length of the string is greater than k, repeat from step 1.\n\nReturn s after all rounds have been completed.\n \n",
    "examples": [
      {
        "input": "Input: s = \"11111222223\", k = 3",
        "output": "Output: \"135\"",
        "explanation": "Explanation: "
      },
      {
        "input": "Input: s = \"00000000\", k = 3",
        "output": "Output: \"000\"",
        "explanation": "Explanation: "
      }
    ],
    "topics": [
      "String",
      "Simulation"
    ],
    "difficulty": "Easy",
    "constraints": [
      "1 <= s.length <= 100",
      "2 <= k <= 100",
      "s consists of digits only."
    ],
    "hints": [
      "Try simulating the entire process to find the final answer."
    ]
  },
  {
    "title": "Substring With Largest Variance",
    "description": "The variance of a string is defined as the largest difference between the number of occurrences of any 2 characters present in the string. Note the two characters may or may not be the same.\nGiven a string s consisting of lowercase English letters only, return the largest variance possible among all substrings of s.\nA substring is a contiguous sequence of characters within a string.\n \n",
    "examples": [
      {
        "input": "Input: s = \"aababbb\"",
        "output": "Output: 3",
        "explanation": ""
      },
      {
        "input": "Input: s = \"abcde\"",
        "output": "Output: 0",
        "explanation": ""
      }
    ],
    "topics": [
      "Array",
      "Dynamic Programming"
    ],
    "difficulty": "Hard",
    "constraints": [
      "1 <= s.length <= 104",
      "s consists of lowercase English letters."
    ],
    "hints": [
      "Think about how to solve the problem if the string had only two distinct characters.",
      "If we replace all occurrences of the first character by +1 and those of the second character by -1, can we efficiently calculate the largest possible variance of a string with only two distinct characters?",
      "Now, try finding the optimal answer by taking all possible pairs of characters into consideration."
    ]
  },
  {
    "title": "Maximum White Tiles Covered by a Carpet",
    "description": "You are given a 2D integer array tiles where tiles[i] = [li, ri] represents that every tile j in the range li <= j <= ri is colored white.\nYou are also given an integer carpetLen, the length of a single carpet that can be placed anywhere.\nReturn the maximum number of white tiles that can be covered by the carpet.\n \n",
    "examples": [
      {
        "input": "Input: tiles = [[1,5],[10,11],[12,18],[20,25],[30,32]], carpetLen = 10",
        "output": "Output: 9",
        "explanation": "Explanation: Place the carpet starting on tile 10. "
      },
      {
        "input": "Input: tiles = [[10,11],[1,1]], carpetLen = 2",
        "output": "Output: 2",
        "explanation": "Explanation: Place the carpet starting on tile 10. "
      }
    ],
    "topics": [
      "Array",
      "Binary Search",
      "Greedy",
      "Sorting",
      "Prefix Sum"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= tiles.length <= 5 * 104",
      "tiles[i].length == 2",
      "1 <= li <= ri <= 109",
      "1 <= carpetLen <= 109",
      "The tiles are non-overlapping."
    ],
    "hints": [
      "Think about the potential placements of the carpet in an optimal solution.",
      "Can we use Prefix Sum and Binary Search to determine how many tiles are covered for a given placement?"
    ]
  },
  {
    "title": "Number of Ways to Split Array",
    "description": "You are given a 0-indexed integer array nums of length n.\nnums contains a valid split at index i if the following are true:\n\nThe sum of the first i + 1 elements is greater than or equal to the sum of the last n - i - 1 elements.\nThere is at least one element to the right of i. That is, 0 <= i < n - 1.\n\nReturn the number of valid splits in nums.\n \n",
    "examples": [
      {
        "input": "Input: nums = [10,4,-8,7]",
        "output": "Output: 2",
        "explanation": "Explanation: "
      },
      {
        "input": "Input: nums = [2,3,1,0]",
        "output": "Output: 2",
        "explanation": "Explanation: "
      }
    ],
    "topics": [
      "Array",
      "Prefix Sum"
    ],
    "difficulty": "Medium",
    "constraints": [
      "2 <= nums.length <= 105",
      "-105 <= nums[i] <= 105"
    ],
    "hints": [
      "For any index i, how can we find the sum of the first (i+1) elements from the sum of the first i elements?",
      "If the total sum of the array is known, how can we check if the sum of the first (i+1) elements greater than or equal to the remaining elements?"
    ]
  },
  {
    "title": "Count Integers in Intervals",
    "description": "Given an empty set of intervals, implement a data structure that can:\n\nAdd an interval to the set of intervals.\nCount the number of integers that are present in at least one interval.\n\nImplement the CountIntervals class:\n\nCountIntervals() Initializes the object with an empty set of intervals.\nvoid add(int left, int right) Adds the interval [left, right] to the set of intervals.\nint count() Returns the number of integers that are present in at least one interval.\n\nNote that an interval [left, right] denotes all the integers x where left <= x <= right.\n \n",
    "examples": [
      {
        "input": "Input\n[\"CountIntervals\", \"add\", \"add\", \"count\", \"add\", \"count\"]",
        "output": "Output\n[null, null, null, 6, null, 8]",
        "explanation": "Explanation\nCountIntervals countIntervals = new CountIntervals(); // initialize the object with an empty set of intervals. "
      }
    ],
    "topics": [
      "Design",
      "Segment Tree",
      "Ordered Set"
    ],
    "difficulty": "Hard",
    "constraints": [
      "1 <= left <= right <= 109",
      "At most 105 calls in total will be made to add and count.",
      "At least one call will be made to count."
    ],
    "hints": [
      "How can you efficiently add intervals to the set of intervals? Can a data structure like a Binary Search Tree help?",
      "How can you ensure that the intervals present in the set are non-overlapping? Try merging the overlapping intervals whenever a new interval is added.",
      "How can you update the count of integers present in at least one interval when a new interval is added to the set?"
    ]
  },
  {
    "title": "Largest Combination With Bitwise AND Greater Than Zero",
    "description": "The bitwise AND of an array nums is the bitwise AND of all integers in nums.\n\nFor example, for nums = [1, 5, 3], the bitwise AND is equal to 1 & 5 & 3 = 1.\nAlso, for nums = [7], the bitwise AND is 7.\n\nYou are given an array of positive integers candidates. Evaluate the bitwise AND of every combination of numbers of candidates. Each number in candidates may only be used once in each combination.\nReturn the size of the largest combination of candidates with a bitwise AND greater than 0.\n \n",
    "examples": [
      {
        "input": "Input: candidates = [16,17,71,62,12,24,14]",
        "output": "Output: 4",
        "explanation": "Explanation: The combination [16,17,62,24] has a bitwise AND of 16 & 17 & 62 & 24 = 16 > 0."
      },
      {
        "input": "Input: candidates = [8,8]",
        "output": "Output: 2",
        "explanation": "Explanation: The largest combination [8,8] has a bitwise AND of 8 & 8 = 8 > 0."
      }
    ],
    "topics": [
      "Array",
      "Hash Table",
      "Bit Manipulation",
      "Counting"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= candidates.length <= 105",
      "1 <= candidates[i] <= 107"
    ],
    "hints": [
      "For the bitwise AND to be greater than zero, at least one bit should be 1 for every number in the combination.",
      "The candidates are 24 bits long, so for every bit position, we can calculate the size of the largest combination such that the bitwise AND will have a 1 at that bit position."
    ]
  },
  {
    "title": "Maximum Consecutive Floors Without Special Floors",
    "description": "Alice manages a company and has rented some floors of a building as office space. Alice has decided some of these floors should be special floors, used for relaxation only.\nYou are given two integers bottom and top, which denote that Alice has rented all the floors from bottom to top (inclusive). You are also given the integer array special, where special[i] denotes a special floor that Alice has designated for relaxation.\nReturn the maximum number of consecutive floors without a special floor.\n \n",
    "examples": [
      {
        "input": "Input: bottom = 2, top = 9, special = [4,6]",
        "output": "Output: 3",
        "explanation": "Explanation: The following are the ranges (inclusive) of consecutive floors without a special floor:"
      },
      {
        "input": "Input: bottom = 6, top = 8, special = [7,6,8]",
        "output": "Output: 0",
        "explanation": "Explanation: Every floor rented is a special floor, so we return 0."
      }
    ],
    "topics": [
      "Array",
      "Sorting"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= special.length <= 105",
      "1 <= bottom <= special[i] <= top <= 109",
      "All the values of special are unique."
    ],
    "hints": [
      "Say we have a pair of special floors (x, y) with no other special floors in between. There are x - y - 1 consecutive floors in between them without a special floor.",
      "Say there are n special floors. After sorting special, we have answer = max(answer, special[i] – special[i – 1] – 1) for all 0 < i ≤ n.",
      "However, there are two special cases left to consider: the floors before special[0] and after special[n-1].",
      "To consider these cases, we have answer = max(answer, special[0] – bottom, top – special[n-1])."
    ]
  },
  {
    "title": "Maximum Score of a Node Sequence",
    "description": "There is an undirected graph with n nodes, numbered from 0 to n - 1.\nYou are given a 0-indexed integer array scores of length n where scores[i] denotes the score of node i. You are also given a 2D integer array edges where edges[i] = [ai, bi] denotes that there exists an undirected edge connecting nodes ai and bi.\nA node sequence is valid if it meets the following conditions:\n\nThere is an edge connecting every pair of adjacent nodes in the sequence.\nNo node appears more than once in the sequence.\n\nThe score of a node sequence is defined as the sum of the scores of the nodes in the sequence.\nReturn the maximum score of a valid node sequence with a length of 4. If no such sequence exists, return -1.\n \n",
    "examples": [
      {
        "input": "Input: scores = [5,2,9,8,4], edges = [[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]]",
        "output": "Output: 24",
        "explanation": "Explanation: The figure above shows the graph and the chosen node sequence [0,1,2,3]."
      },
      {
        "input": "Input: scores = [9,20,6,4,11,12], edges = [[0,3],[5,3],[2,4],[1,3]]",
        "output": "Output: -1",
        "explanation": "Explanation: The figure above shows the graph."
      }
    ],
    "topics": [
      "Array",
      "Graph",
      "Sorting",
      "Enumeration"
    ],
    "difficulty": "Hard",
    "constraints": [
      "n == scores.length",
      "4 <= n <= 5 * 104",
      "1 <= scores[i] <= 108",
      "0 <= edges.length <= 5 * 104",
      "edges[i].length == 2",
      "0 <= ai, bi <= n - 1",
      "ai != bi",
      "There are no duplicate edges."
    ],
    "hints": [
      "For every node sequence of length 4, there are 3 relevant edges. How can we consider valid triplets of edges?",
      "Fix the middle 2 nodes connected by an edge in the node sequence. Can you determine the other 2 nodes that will give the highest possible score?",
      "The other 2 nodes must each be connected to one of the middle nodes. If we only consider nodes with the highest scores, how many should we store to ensure we don’t choose duplicate nodes?",
      "For each node, we should store the 3 adjacent nodes with the highest scores to ensure we can find a sequence with no duplicate nodes via the method above."
    ]
  },
  {
    "title": "Design an ATM Machine",
    "description": "There is an ATM machine that stores banknotes of 5 denominations: 20, 50, 100, 200, and 500 dollars. Initially the ATM is empty. The user can use the machine to deposit or withdraw any amount of money.\nWhen withdrawing, the machine prioritizes using banknotes of larger values.\n\nFor example, if you want to withdraw $300 and there are 2 $50 banknotes, 1 $100 banknote, and 1 $200 banknote, then the machine will use the $100 and $200 banknotes.\nHowever, if you try to withdraw $600 and there are 3 $200 banknotes and 1 $500 banknote, then the withdraw request will be rejected because the machine will first try to use the $500 banknote and then be unable to use banknotes to complete the remaining $100. Note that the machine is not allowed to use the $200 banknotes instead of the $500 banknote.\n\nImplement the ATM class:\n\nATM() Initializes the ATM object.\nvoid deposit(int[] banknotesCount) Deposits new banknotes in the order $20, $50, $100, $200, and $500.\nint[] withdraw(int amount) Returns an array of length 5 of the number of banknotes that will be handed to the user in the order $20, $50, $100, $200, and $500, and update the number of banknotes in the ATM after withdrawing. Returns [-1] if it is not possible (do not withdraw any banknotes in this case).\n\n \n",
    "examples": [
      {
        "input": "Input\n[\"ATM\", \"deposit\", \"withdraw\", \"deposit\", \"withdraw\", \"withdraw\"]",
        "output": "Output\n[null, null, [0,0,1,0,1], null, [-1], [0,1,0,0,1]]",
        "explanation": "Explanation\nATM atm = new ATM();"
      }
    ],
    "topics": [
      "Array",
      "Greedy",
      "Design"
    ],
    "difficulty": "Medium",
    "constraints": [
      "banknotesCount.length == 5",
      "0 <= banknotesCount[i] <= 109",
      "1 <= amount <= 109",
      "At most 5000 calls in total will be made to withdraw and deposit.",
      "At least one call will be made to each function withdraw and deposit."
    ],
    "hints": [
      "Store the number of banknotes of each denomination.",
      "Can you use math to quickly evaluate a withdrawal request?"
    ]
  },
  {
    "title": "Number of Ways to Buy Pens and Pencils",
    "description": "You are given an integer total indicating the amount of money you have. You are also given two integers cost1 and cost2 indicating the price of a pen and pencil respectively. You can spend part or all of your money to buy multiple quantities (or none) of each kind of writing utensil.\nReturn the number of distinct ways you can buy some number of pens and pencils.\n \n",
    "examples": [
      {
        "input": "Input: total = 20, cost1 = 10, cost2 = 5",
        "output": "Output: 9",
        "explanation": "Explanation: The price of a pen is 10 and the price of a pencil is 5."
      },
      {
        "input": "Input: total = 5, cost1 = 10, cost2 = 10",
        "output": "Output: 1",
        "explanation": "Explanation: The price of both pens and pencils are 10, which cost more than total, so you cannot buy any writing utensils. Therefore, there is only 1 way: buy 0 pens and 0 pencils."
      }
    ],
    "topics": [
      "Math",
      "Enumeration"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= total, cost1, cost2 <= 106"
    ],
    "hints": [
      "Fix the number of pencils purchased and calculate the number of ways to buy pens.",
      "Sum up the number of ways to buy pens for each amount of pencils purchased to get the answer."
    ]
  },
  {
    "title": "Find Closest Number to Zero",
    "description": "Given an integer array nums of size n, return the number with the value closest to 0 in nums. If there are multiple answers, return the number with the largest value.\n \n",
    "examples": [
      {
        "input": "Input: nums = [-4,-2,1,4,8]",
        "output": "Output: 1",
        "explanation": ""
      },
      {
        "input": "Input: nums = [2,-1,1]",
        "output": "Output: 1",
        "explanation": "Explanation: 1 and -1 are both the closest numbers to 0, so 1 being larger is returned."
      }
    ],
    "topics": [
      "Array"
    ],
    "difficulty": "Easy",
    "constraints": [
      "1 <= n <= 1000",
      "-105 <= nums[i] <= 105"
    ],
    "hints": [
      "Keep track of the number closest to 0 as you iterate through the array.",
      "Ensure that if multiple numbers are closest to 0, you store the one with the largest value."
    ]
  },
  {
    "title": " Check if There Is a Valid Parentheses String Path",
    "description": "A parentheses string is a non-empty string consisting only of '(' and ')'. It is valid if any of the following conditions is true:\n\nIt is ().\nIt can be written as AB (A concatenated with B), where A and B are valid parentheses strings.\nIt can be written as (A), where A is a valid parentheses string.\n\nYou are given an m x n matrix of parentheses grid. A valid parentheses string path in the grid is a path satisfying all of the following conditions:\n\nThe path starts from the upper left cell (0, 0).\nThe path ends at the bottom-right cell (m - 1, n - 1).\nThe path only ever moves down or right.\nThe resulting parentheses string formed by the path is valid.\n\nReturn true if there exists a valid parentheses string path in the grid. Otherwise, return false.\n \n",
    "examples": [
      {
        "input": "Input: grid = [[\"(\",\"(\",\"(\"],[\")\",\"(\",\")\"],[\"(\",\"(\",\")\"],[\"(\",\"(\",\")\"]]",
        "output": "Output: true",
        "explanation": "Explanation: The above diagram shows two possible paths that form valid parentheses strings."
      },
      {
        "input": "Input: grid = [[\")\",\")\"],[\"(\",\"(\"]]",
        "output": "Output: false",
        "explanation": "Explanation: The two possible paths form the parentheses strings \"))(\" and \")((\". Since neither of them are valid parentheses strings, we return false."
      }
    ],
    "topics": [
      "Array",
      "Dynamic Programming",
      "Matrix"
    ],
    "difficulty": "Hard",
    "constraints": [
      "m == grid.length",
      "n == grid[i].length",
      "1 <= m, n <= 100",
      "grid[i][j] is either '(' or ')'."
    ],
    "hints": [
      "What observations can you make about the number of open brackets and close brackets for any prefix of a valid bracket sequence?",
      "The number of open brackets must always be greater than or equal to the number of close brackets.",
      "Could you use dynamic programming?"
    ]
  },
  {
    "title": "Count Number of Texts",
    "description": "Alice is texting Bob using her phone. The mapping of digits to letters is shown in the figure below.\n\nIn order to add a letter, Alice has to press the key of the corresponding digit i times, where i is the position of the letter in the key.\n\nFor example, to add the letter 's', Alice has to press '7' four times. Similarly, to add the letter 'k', Alice has to press '5' twice.\nNote that the digits '0' and '1' do not map to any letters, so Alice does not use them.\n\nHowever, due to an error in transmission, Bob did not receive Alice's text message but received a string of pressed keys instead.\n\nFor example, when Alice sent the message \"bob\", Bob received the string \"2266622\".\n\nGiven a string pressedKeys representing the string received by Bob, return the total number of possible text messages Alice could have sent.\nSince the answer may be very large, return it modulo 109 + 7.\n \n",
    "examples": [
      {
        "input": "Input: pressedKeys = \"22233\"",
        "output": "Output: 8",
        "explanation": ""
      },
      {
        "input": "Input: pressedKeys = \"222222222222222222222222222222222222\"",
        "output": "Output: 82876089",
        "explanation": ""
      }
    ],
    "topics": [
      "Hash Table",
      "Math",
      "String",
      "Dynamic Programming"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= pressedKeys.length <= 105",
      "pressedKeys only consists of digits from '2' - '9'."
    ],
    "hints": [
      "For a substring consisting of the same digit, how can we count the number of texts it could have originally represented?",
      "How can dynamic programming help us calculate the required answer?"
    ]
  },
  {
    "title": "Count Nodes Equal to Average of Subtree",
    "description": "Given the root of a binary tree, return the number of nodes where the value of the node is equal to the average of the values in its subtree.\nNote:\n\nThe average of n elements is the sum of the n elements divided by n and rounded down to the nearest integer.\nA subtree of root is a tree consisting of root and all of its descendants.\n\n \n",
    "examples": [
      {
        "input": "Input: root = [4,8,5,0,1,null,6]",
        "output": "Output: 5",
        "explanation": "Explanation: "
      },
      {
        "input": "Input: root = [1]",
        "output": "Output: 1",
        "explanation": "Explanation: For the node with value 1: The average of its subtree is 1 / 1 = 1."
      }
    ],
    "topics": [
      "Tree",
      "Depth-First Search",
      "Binary Tree"
    ],
    "difficulty": "Medium",
    "constraints": [
      "The number of nodes in the tree is in the range [1, 1000].",
      "0 <= Node.val <= 1000"
    ],
    "hints": [
      "What information do we need to calculate the average? We need the sum of the values and the number of values.",
      "Create a recursive function that returns the size of a node’s subtree, and the sum of the values of its subtree."
    ]
  },
  {
    "title": "Largest 3-Same-Digit Number in String",
    "description": "You are given a string num representing a large integer. An integer is good if it meets the following conditions:\n\nIt is a substring of num with length 3.\nIt consists of only one unique digit.\n\nReturn the maximum good integer as a string or an empty string \"\" if no such integer exists.\nNote:\n\nA substring is a contiguous sequence of characters within a string.\nThere may be leading zeroes in num or a good integer.\n\n \n",
    "examples": [
      {
        "input": "Input: num = \"6777133339\"",
        "output": "Output: \"777\"",
        "explanation": "Explanation: There are two distinct good integers: \"777\" and \"333\"."
      },
      {
        "input": "Input: num = \"2300019\"",
        "output": "Output: \"000\"",
        "explanation": "Explanation: \"000\" is the only good integer."
      },
      {
        "input": "Input: num = \"42352338\"",
        "output": "Output: \"\"",
        "explanation": "Explanation: No substring of length 3 consists of only one unique digit. Therefore, there are no good integers."
      }
    ],
    "topics": [
      "String"
    ],
    "difficulty": "Easy",
    "constraints": [
      "3 <= num.length <= 1000",
      "num only consists of digits."
    ],
    "hints": [
      "We can sequentially check if “999”, “888”, “777”, … , “000” exists in num in that order. The first to be found is the maximum good integer.",
      "If we cannot find any of the above integers, we return an empty string “”."
    ]
  },
  {
    "title": "Minimum Number of Operations to Convert Time",
    "description": "You are given two strings current and correct representing two 24-hour times.\n24-hour times are formatted as \"HH:MM\", where HH is between 00 and 23, and MM is between 00 and 59. The earliest 24-hour time is 00:00, and the latest is 23:59.\nIn one operation you can increase the time current by 1, 5, 15, or 60 minutes. You can perform this operation any number of times.\nReturn the minimum number of operations needed to convert current to correct.\n \n",
    "examples": [
      {
        "input": "Input: current = \"02:30\", correct = \"04:35\"",
        "output": "Output: 3",
        "explanation": ""
      },
      {
        "input": "Input: current = \"11:00\", correct = \"11:01\"",
        "output": "Output: 1",
        "explanation": "Explanation: We only have to add one minute to current, so the minimum number of operations needed is 1."
      }
    ],
    "topics": [
      "String",
      "Greedy"
    ],
    "difficulty": "Easy",
    "constraints": [
      "current and correct are in the format \"HH:MM\"",
      "current <= correct"
    ],
    "hints": [
      "Convert the times to minutes.",
      "Use the operation with the biggest value possible at each step."
    ]
  },
  {
    "title": "Escape the Spreading Fire",
    "description": "You are given a 0-indexed 2D integer array grid of size m x n which represents a field. Each cell has one of three values:\n\n0 represents grass,\n1 represents fire,\n2 represents a wall that you and fire cannot pass through.\n\nYou are situated in the top-left cell, (0, 0), and you want to travel to the safehouse at the bottom-right cell, (m - 1, n - 1). Every minute, you may move to an adjacent grass cell. After your move, every fire cell will spread to all adjacent cells that are not walls.\nReturn the maximum number of minutes that you can stay in your initial position before moving while still safely reaching the safehouse. If this is impossible, return -1. If you can always reach the safehouse regardless of the minutes stayed, return 109.\nNote that even if the fire spreads to the safehouse immediately after you have reached it, it will be counted as safely reaching the safehouse.\nA cell is adjacent to another cell if the former is directly north, east, south, or west of the latter (i.e., their sides are touching).\n \n",
    "examples": [
      {
        "input": "Input: grid = [[0,2,0,0,0,0,0],[0,0,0,2,2,1,0],[0,2,0,0,1,2,0],[0,0,2,2,2,0,2],[0,0,0,0,0,0,0]]",
        "output": "Output: 3",
        "explanation": "Explanation: The figure above shows the scenario where you stay in the initial position for 3 minutes."
      },
      {
        "input": "Input: grid = [[0,0,0,0],[0,1,2,0],[0,2,0,0]]",
        "output": "Output: -1",
        "explanation": "Explanation: The figure above shows the scenario where you immediately move towards the safehouse."
      },
      {
        "input": "Input: grid = [[0,0,0],[2,2,0],[1,2,0]]",
        "output": "Output: 1000000000",
        "explanation": "Explanation: The figure above shows the initial grid."
      }
    ],
    "topics": [
      "Array",
      "Binary Search",
      "Breadth-First Search",
      "Matrix"
    ],
    "difficulty": "Hard",
    "constraints": [
      "m == grid.length",
      "n == grid[i].length",
      "2 <= m, n <= 300",
      "4 <= m * n <= 2 * 104",
      "grid[i][j] is either 0, 1, or 2.",
      "grid[0][0] == grid[m - 1][n - 1] == 0"
    ],
    "hints": [
      "For some tile (x, y), how can we determine when, if ever, the fire will reach it?",
      "We can use multi-source BFS to find the earliest time the fire will reach each cell.",
      "Then, starting with a given t minutes of staying in the initial position, we can check if there is a safe path to the safehouse using the obtained information about the fire.",
      "We can use binary search to efficiently find the maximum t that allows us to reach the safehouse."
    ]
  },
  {
    "title": "Count Unguarded Cells in the Grid",
    "description": "You are given two integers m and n representing a 0-indexed m x n grid. You are also given two 2D integer arrays guards and walls where guards[i] = [rowi, coli] and walls[j] = [rowj, colj] represent the positions of the ith guard and jth wall respectively.\nA guard can see every cell in the four cardinal directions (north, east, south, or west) starting from their position unless obstructed by a wall or another guard. A cell is guarded if there is at least one guard that can see it.\nReturn the number of unoccupied cells that are not guarded.\n \n",
    "examples": [
      {
        "input": "Input: m = 4, n = 6, guards = [[0,0],[1,1],[2,3]], walls = [[0,1],[2,2],[1,4]]",
        "output": "Output: 7",
        "explanation": "Explanation: The guarded and unguarded cells are shown in red and green respectively in the above diagram."
      },
      {
        "input": "Input: m = 3, n = 3, guards = [[1,1]], walls = [[0,1],[1,0],[2,1],[1,2]]",
        "output": "Output: 4",
        "explanation": "Explanation: The unguarded cells are shown in green in the above diagram."
      }
    ],
    "topics": [
      "Array",
      "Matrix",
      "Simulation"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= m, n <= 105",
      "2 <= m * n <= 105",
      "1 <= guards.length, walls.length <= 5 * 104",
      "2 <= guards.length + walls.length <= m * n",
      "guards[i].length == walls[j].length == 2",
      "0 <= rowi, rowj < m",
      "0 <= coli, colj < n",
      "All the positions in guards and walls are unique."
    ],
    "hints": [
      "Create a 2D array to represent the grid. Can you mark the tiles that can be seen by a guard?",
      "Iterate over the guards, and for each of the 4 directions, advance the current tile and mark the tile. When should you stop advancing?"
    ]
  },
  {
    "title": "Minimum Average Difference",
    "description": "You are given a 0-indexed integer array nums of length n.\nThe average difference of the index i is the absolute difference between the average of the first i + 1 elements of nums and the average of the last n - i - 1 elements. Both averages should be rounded down to the nearest integer.\nReturn the index with the minimum average difference. If there are multiple such indices, return the smallest one.\nNote:\n\nThe absolute difference of two numbers is the absolute value of their difference.\nThe average of n elements is the sum of the n elements divided (integer division) by n.\nThe average of 0 elements is considered to be 0.\n\n \n",
    "examples": [
      {
        "input": "Input: nums = [2,5,3,9,5,3]",
        "output": "Output: 3",
        "explanation": ""
      },
      {
        "input": "Input: nums = [0]",
        "output": "Output: 0",
        "explanation": ""
      }
    ],
    "topics": [
      "Array",
      "Prefix Sum"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= nums.length <= 105",
      "0 <= nums[i] <= 105"
    ],
    "hints": [
      "How can we use precalculation to efficiently calculate the average difference at an index?",
      "Create a prefix and/or suffix sum array."
    ]
  },
  {
    "title": "Count Prefixes of a Given String",
    "description": "You are given a string array words and a string s, where words[i] and s comprise only of lowercase English letters.\nReturn the number of strings in words that are a prefix of s.\nA prefix of a string is a substring that occurs at the beginning of the string. A substring is a contiguous sequence of characters within a string.\n \n",
    "examples": [
      {
        "input": "Input: words = [\"a\",\"b\",\"c\",\"ab\",\"bc\",\"abc\"], s = \"abc\"",
        "output": "Output: 3",
        "explanation": ""
      },
      {
        "input": "Input: words = [\"a\",\"a\"], s = \"aa\"",
        "output": "Output: 2",
        "explanation": ""
      }
    ],
    "topics": [
      "Array",
      "String"
    ],
    "difficulty": "Easy",
    "constraints": [
      "1 <= words.length <= 1000",
      "1 <= words[i].length, s.length <= 10",
      "words[i] and s consist of lowercase English letters only."
    ],
    "hints": [
      "For each string in words, check if it is a prefix of s. If true, increment the answer by 1."
    ]
  },
  {
    "title": "Total Appeal of A String",
    "description": "The appeal of a string is the number of distinct characters found in the string.\n\nFor example, the appeal of \"abbca\" is 3 because it has 3 distinct characters: 'a', 'b', and 'c'.\n\nGiven a string s, return the total appeal of all of its substrings.\nA substring is a contiguous sequence of characters within a string.\n \n",
    "examples": [
      {
        "input": "Input: s = \"abbca\"",
        "output": "Output: 28",
        "explanation": "Explanation: The following are the substrings of \"abbca\":"
      },
      {
        "input": "Input: s = \"code\"",
        "output": "Output: 20",
        "explanation": "Explanation: The following are the substrings of \"code\":"
      }
    ],
    "topics": [
      "Hash Table",
      "String",
      "Dynamic Programming"
    ],
    "difficulty": "Hard",
    "constraints": [
      "1 <= s.length <= 105",
      "s consists of lowercase English letters."
    ],
    "hints": [
      "Consider the set of substrings that end at a certain index i. Then, consider a specific alphabetic character. How do you count the number of substrings ending at index i that contain that character?",
      "The number of substrings that contain the alphabetic character is equivalent to 1 plus the index of the last occurrence of the character before index i + 1.",
      "The total appeal of all substrings ending at index i is the total sum of the number of substrings that contain each alphabetic character.",
      "To find the total appeal of all substrings, we simply sum up the total appeal for each index."
    ]
  },
  {
    "title": "K Divisible Elements Subarrays",
    "description": "Given an integer array nums and two integers k and p, return the number of distinct subarrays which have at most k elements divisible by p.\nTwo arrays nums1 and nums2 are said to be distinct if:\n\nThey are of different lengths, or\nThere exists at least one index i where nums1[i] != nums2[i].\n\nA subarray is defined as a non-empty contiguous sequence of elements in an array.\n \n",
    "examples": [
      {
        "input": "Input: nums = [2,3,3,2,2], k = 2, p = 2",
        "output": "Output: 11",
        "explanation": ""
      },
      {
        "input": "Input: nums = [1,2,3,4], k = 4, p = 1",
        "output": "Output: 10",
        "explanation": ""
      }
    ],
    "topics": [
      "Array",
      "Hash Table",
      "Trie",
      "Rolling Hash",
      "Hash Function",
      "Enumeration"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= nums.length <= 200",
      "1 <= nums[i], p <= 200",
      "1 <= k <= nums.length",
      "",
      " ",
      "Follow up:",
      "Can you solve this problem in O(n2) time complexity?"
    ],
    "hints": [
      "Enumerate all subarrays and find the ones that satisfy all the conditions.",
      "Use any suitable method to hash the subarrays to avoid duplicates."
    ]
  },
  {
    "title": "Minimum Consecutive Cards to Pick Up",
    "description": "You are given an integer array cards where cards[i] represents the value of the ith card. A pair of cards are matching if the cards have the same value.\nReturn the minimum number of consecutive cards you have to pick up to have a pair of matching cards among the picked cards. If it is impossible to have matching cards, return -1.\n \n",
    "examples": [
      {
        "input": "Input: cards = [3,4,2,3,4,7]",
        "output": "Output: 4",
        "explanation": "Explanation: We can pick up the cards [3,4,2,3] which contain a matching pair of cards with value 3. Note that picking up the cards [4,2,3,4] is also optimal."
      },
      {
        "input": "Input: cards = [1,0,5,3]",
        "output": "Output: -1",
        "explanation": "Explanation: There is no way to pick up a set of consecutive cards that contain a pair of matching cards."
      }
    ],
    "topics": [
      "Array",
      "Hash Table",
      "Sliding Window"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= cards.length <= 105",
      "0 <= cards[i] <= 106"
    ],
    "hints": [
      "Iterate through the cards and store the location of the last occurrence of each number.",
      "What data structure could you use to get the last occurrence of a number in O(1) or O(log n)?"
    ]
  },
  {
    "title": "Remove Digit From Number to Maximize Result",
    "description": "You are given a string number representing a positive integer and a character digit.\nReturn the resulting string after removing exactly one occurrence of digit from number such that the value of the resulting string in decimal form is maximized. The test cases are generated such that digit occurs at least once in number.\n \n",
    "examples": [
      {
        "input": "Input: number = \"123\", digit = \"3\"",
        "output": "Output: \"12\"",
        "explanation": "Explanation: There is only one '3' in \"123\". After removing '3', the result is \"12\"."
      },
      {
        "input": "Input: number = \"1231\", digit = \"1\"",
        "output": "Output: \"231\"",
        "explanation": "Explanation: We can remove the first '1' to get \"231\" or remove the second '1' to get \"123\"."
      },
      {
        "input": "Input: number = \"551\", digit = \"5\"",
        "output": "Output: \"51\"",
        "explanation": "Explanation: We can remove either the first or second '5' from \"551\"."
      }
    ],
    "topics": [
      "String",
      "Greedy",
      "Enumeration"
    ],
    "difficulty": "Easy",
    "constraints": [
      "2 <= number.length <= 100",
      "number consists of digits from '1' to '9'.",
      "digit is a digit from '1' to '9'.",
      "digit occurs at least once in number."
    ],
    "hints": [
      "The maximum length of number is really small.",
      "Iterate through the digits of number and every time we see digit, try removing it.",
      "To remove a character at index i, concatenate the substring from index 0 to i - 1 and the substring from index i + 1 to number.length - 1."
    ]
  },
  {
    "title": "Number of Flowers in Full Bloom",
    "description": "You are given a 0-indexed 2D integer array flowers, where flowers[i] = [starti, endi] means the ith flower will be in full bloom from starti to endi (inclusive). You are also given a 0-indexed integer array people of size n, where poeple[i] is the time that the ith person will arrive to see the flowers.\nReturn an integer array answer of size n, where answer[i] is the number of flowers that are in full bloom when the ith person arrives.\n \n",
    "examples": [
      {
        "input": "Input: flowers = [[1,6],[3,7],[9,12],[4,13]], poeple = [2,3,7,11]",
        "output": "Output: [1,2,2,2]",
        "explanation": "Explanation: The figure above shows the times when the flowers are in full bloom and when the people arrive."
      },
      {
        "input": "Input: flowers = [[1,10],[3,3]], poeple = [3,3,2]",
        "output": "Output: [2,2,1]",
        "explanation": "Explanation: The figure above shows the times when the flowers are in full bloom and when the people arrive."
      }
    ],
    "topics": [
      "Array",
      "Hash Table",
      "Binary Search",
      "Sorting",
      "Prefix Sum",
      "Ordered Set"
    ],
    "difficulty": "Hard",
    "constraints": [
      "1 <= flowers.length <= 5 * 104",
      "flowers[i].length == 2",
      "1 <= starti <= endi <= 109",
      "1 <= people.length <= 5 * 104",
      "1 <= people[i] <= 109"
    ],
    "hints": [
      "Notice that for any given time t, the number of flowers blooming at time t is equal to the number of flowers that have started blooming minus the number of flowers that have already stopped blooming.",
      "We can obtain these values efficiently using binary search.",
      "We can store the starting times in sorted order, which then allows us to binary search to find how many flowers have started blooming for a given time t.",
      "We do the same for the ending times to find how many flowers have stopped blooming at time t."
    ]
  },
  {
    "title": "Count Number of Rectangles Containing Each Point",
    "description": "You are given a 2D integer array rectangles where rectangles[i] = [li, hi] indicates that ith rectangle has a length of li and a height of hi. You are also given a 2D integer array points where points[j] = [xj, yj] is a point with coordinates (xj, yj).\nThe ith rectangle has its bottom-left corner point at the coordinates (0, 0) and its top-right corner point at (li, hi).\nReturn an integer array count of length points.length where count[j] is the number of rectangles that contain the jth point.\nThe ith rectangle contains the jth point if 0 <= xj <= li and 0 <= yj <= hi. Note that points that lie on the edges of a rectangle are also considered to be contained by that rectangle.\n \n",
    "examples": [
      {
        "input": "Input: rectangles = [[1,2],[2,3],[2,5]], points = [[2,1],[1,4]]",
        "output": "Output: [2,1]",
        "explanation": "Explanation: "
      },
      {
        "input": "Input: rectangles = [[1,1],[2,2],[3,3]], points = [[1,3],[1,1]]",
        "output": "Output: [1,3]",
        "explanation": ""
      }
    ],
    "topics": [
      "Array",
      "Binary Search",
      "Binary Indexed Tree",
      "Sorting"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= rectangles.length, points.length <= 5 * 104",
      "rectangles[i].length == points[j].length == 2",
      "1 <= li, xj <= 109",
      "1 <= hi, yj <= 100",
      "All the rectangles are unique.",
      "All the points are unique."
    ],
    "hints": [
      "The heights of the rectangles and the y-coordinates of the points are only at most 100, so for each point, we can iterate over the possible heights of the rectangles that contain a given point.",
      "For a given point and height, can we efficiently count how many rectangles with that height contain our point?",
      "Sort the rectangles at each height and use binary search."
    ]
  },
  {
    "title": "Count Lattice Points Inside a Circle",
    "description": "Given a 2D integer array circles where circles[i] = [xi, yi, ri] represents the center (xi, yi) and radius ri of the ith circle drawn on a grid, return the number of lattice points that are present inside at least one circle.\nNote:\n\nA lattice point is a point with integer coordinates.\nPoints that lie on the circumference of a circle are also considered to be inside it.\n\n \n",
    "examples": [
      {
        "input": "Input: circles = [[2,2,1]]",
        "output": "Output: 5",
        "explanation": ""
      },
      {
        "input": "Input: circles = [[2,2,2],[3,4,1]]",
        "output": "Output: 16",
        "explanation": ""
      }
    ],
    "topics": [
      "Array",
      "Hash Table",
      "Math",
      "Geometry",
      "Enumeration"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= circles.length <= 200",
      "circles[i].length == 3",
      "1 <= xi, yi <= 100",
      "1 <= ri <= min(xi, yi)"
    ],
    "hints": [
      "For each circle, how can you check whether or not a lattice point lies inside it?",
      "Since you need to reduce the search space, consider the minimum and maximum possible values of the coordinates of a lattice point contained in any circle."
    ]
  },
  {
    "title": "Intersection of Multiple Arrays",
    "description": "Given a 2D integer array nums where nums[i] is a non-empty array of distinct positive integers, return the list of integers that are present in each array of nums sorted in ascending order.\n \n",
    "examples": [
      {
        "input": "Input: nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]",
        "output": "Output: [3,4]",
        "explanation": "Explanation: "
      },
      {
        "input": "Input: nums = [[1,2,3],[4,5,6]]",
        "output": "Output: []",
        "explanation": "Explanation: "
      }
    ],
    "topics": [
      "Array",
      "Hash Table",
      "Counting"
    ],
    "difficulty": "Easy",
    "constraints": [
      "1 <= nums.length <= 1000",
      "1 <= sum(nums[i].length) <= 1000",
      "1 <= nums[i][j] <= 1000",
      "All the values of nums[i] are unique."
    ],
    "hints": [
      "Keep a count of the number of times each integer occurs in nums.",
      "Since all integers of nums[i] are distinct, if an integer is present in each array, its count will be equal to the total number of arrays."
    ]
  },
  {
    "title": "Maximum Total Beauty of the Gardens",
    "description": "Alice is a caretaker of n gardens and she wants to plant flowers to maximize the total beauty of all her gardens.\nYou are given a 0-indexed integer array flowers of size n, where flowers[i] is the number of flowers already planted in the ith garden. Flowers that are already planted cannot be removed. You are then given another integer newFlowers, which is the maximum number of flowers that Alice can additionally plant. You are also given the integers target, full, and partial.\nA garden is considered complete if it has at least target flowers. The total beauty of the gardens is then determined as the sum of the following:\n\nThe number of complete gardens multiplied by full.\nThe minimum number of flowers in any of the incomplete gardens multiplied by partial. If there are no incomplete gardens, then this value will be 0.\n\nReturn the maximum total beauty that Alice can obtain after planting at most newFlowers flowers.\n \n",
    "examples": [
      {
        "input": "Input: flowers = [1,3,1,1], newFlowers = 7, target = 6, full = 12, partial = 1",
        "output": "Output: 14",
        "explanation": "Explanation: Alice can plant"
      },
      {
        "input": "Input: flowers = [2,4,5,3], newFlowers = 10, target = 5, full = 2, partial = 6",
        "output": "Output: 30",
        "explanation": "Explanation: Alice can plant"
      }
    ],
    "topics": [
      "Array",
      "Two Pointers",
      "Binary Search",
      "Greedy",
      "Sorting"
    ],
    "difficulty": "Hard",
    "constraints": [
      "1 <= flowers.length <= 105",
      "1 <= flowers[i], target <= 105",
      "1 <= newFlowers <= 1010",
      "1 <= full, partial <= 105"
    ],
    "hints": [
      "Say we choose k gardens to be complete, is there an optimal way of choosing which gardens to plant more flowers to achieve this?",
      "For a given k, we should greedily fill-up the k gardens with the most flowers planted already. This gives us the most remaining flowers to fill up the other gardens.",
      "After sorting flowers, we can thus try every possible k and what is left is to find the highest minimum flowers we can obtain by planting the remaining flowers in the other gardens.",
      "To find the highest minimum in the other gardens, we can use binary search to find the most optimal way of planting."
    ]
  },
  {
    "title": "Maximum Product After K Increments",
    "description": "You are given an array of non-negative integers nums and an integer k. In one operation, you may choose any element from nums and increment it by 1.\nReturn the maximum product of nums after at most k operations. Since the answer may be very large, return it modulo 109 + 7. Note that you should maximize the product before taking the modulo. \n \n",
    "examples": [
      {
        "input": "Input: nums = [0,4], k = 5",
        "output": "Output: 20",
        "explanation": "Explanation: Increment the first number 5 times."
      },
      {
        "input": "Input: nums = [6,3,3,2], k = 2",
        "output": "Output: 216",
        "explanation": "Explanation: Increment the second number 1 time and increment the fourth number 1 time."
      }
    ],
    "topics": [
      "Array",
      "Greedy",
      "Heap (Priority Queue)"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= nums.length, k <= 105",
      "0 <= nums[i] <= 106"
    ],
    "hints": [
      "If you can increment only once, which number should you increment?",
      "We should always prioritize the smallest number. What kind of data structure could we use?",
      "Use a min heap to hold all the numbers. Each time we do an operation, replace the top of the heap x by x + 1."
    ]
  },
  {
    "title": "Minimize Result by Adding Parentheses to Expression",
    "description": "You are given a 0-indexed string expression of the form \"<num1>+<num2>\" where <num1> and <num2> represent positive integers.\nAdd a pair of parentheses to expression such that after the addition of parentheses, expression is a valid mathematical expression and evaluates to the smallest possible value. The left parenthesis must be added to the left of '+' and the right parenthesis must be added to the right of '+'.\nReturn expression after adding a pair of parentheses such that expression evaluates to the smallest possible value. If there are multiple answers that yield the same result, return any of them.\nThe input has been generated such that the original value of expression, and the value of expression after adding any pair of parentheses that meets the requirements fits within a signed 32-bit integer.\n \n",
    "examples": [
      {
        "input": "Input: expression = \"247+38\"",
        "output": "Output: \"2(47+38)\"",
        "explanation": "Explanation: The expression evaluates to 2 * (47 + 38) = 2 * 85 = 170."
      },
      {
        "input": "Input: expression = \"12+34\"",
        "output": "Output: \"1(2+3)4\"",
        "explanation": "Explanation: The expression evaluates to 1 * (2 + 3) * 4 = 1 * 5 * 4 = 20."
      },
      {
        "input": "Input: expression = \"999+999\"",
        "output": "Output: \"(999+999)\"",
        "explanation": "Explanation: The expression evaluates to 999 + 999 = 1998."
      }
    ],
    "topics": [
      "String",
      "Enumeration"
    ],
    "difficulty": "Medium",
    "constraints": [
      "3 <= expression.length <= 10",
      "expression consists of digits from '1' to '9' and '+'.",
      "expression starts and ends with digits.",
      "expression contains exactly one '+'.",
      "The original value of expression, and the value of expression after adding any pair of parentheses that meets the requirements fits within a signed 32-bit integer."
    ],
    "hints": [
      "The maximum length of expression is very low. We can try every possible spot to place the parentheses.",
      "Every possibility of expression is of the form a * (b + c) * d where a, b, c, d represent integers. Note the edge cases where a and/or d do not exist, in which case use 1 instead of them."
    ]
  },
  {
    "title": "Largest Number After Digit Swaps by Parity",
    "description": "You are given a positive integer num. You may swap any two digits of num that have the same parity (i.e. both odd digits or both even digits).\nReturn the largest possible value of num after any number of swaps.\n \n",
    "examples": [
      {
        "input": "Input: num = 1234",
        "output": "Output: 3412",
        "explanation": "Explanation: Swap the digit 3 with the digit 1, this results in the number 3214."
      },
      {
        "input": "Input: num = 65875",
        "output": "Output: 87655",
        "explanation": "Explanation: Swap the digit 8 with the digit 6, this results in the number 85675."
      }
    ],
    "topics": [
      "Sorting",
      "Heap (Priority Queue)"
    ],
    "difficulty": "Easy",
    "constraints": [
      "1 <= num <= 109"
    ],
    "hints": [
      "The bigger digit should appear first (more to the left) because it contributes more to the value of the number.",
      "Get all the even digits, as well as odd digits. Sort them separately.",
      "Reconstruct the number by giving the earlier digits the highest available digit of the same parity."
    ]
  },
  {
    "title": "Sum of Scores of Built Strings",
    "description": "You are building a string s of length n one character at a time, prepending each new character to the front of the string. The strings are labeled from 1 to n, where the string with length i is labeled si.\n\nFor example, for s = \"abaca\", s1 == \"a\", s2 == \"ca\", s3 == \"aca\", etc.\n\nThe score of si is the length of the longest common prefix between si and sn (Note that s == sn).\nGiven the final string s, return the sum of the score of every si.\n \n",
    "examples": [
      {
        "input": "Input: s = \"babab\"",
        "output": "Output: 9",
        "explanation": ""
      },
      {
        "input": "Input: s = \"azbazbzaz\"",
        "output": "Output: 14",
        "explanation": "Explanation: "
      }
    ],
    "topics": [
      "String",
      "Binary Search",
      "Rolling Hash",
      "Suffix Array",
      "String Matching",
      "Hash Function"
    ],
    "difficulty": "Hard",
    "constraints": [
      "1 <= s.length <= 105",
      "s consists of lowercase English letters."
    ],
    "hints": [
      "Each s_i is a suffix of the string s, so consider algorithms that can determine the longest prefix that is also a suffix.",
      "Could you use the Z array from the Z algorithm to find the score of each s_i?"
    ]
  },
  {
    "title": "Number of Ways to Select Buildings",
    "description": "You are given a 0-indexed binary string s which represents the types of buildings along a street where:\n\ns[i] = '0' denotes that the ith building is an office and\ns[i] = '1' denotes that the ith building is a restaurant.\n\nAs a city official, you would like to select 3 buildings for random inspection. However, to ensure variety, no two consecutive buildings out of the selected buildings can be of the same type.\n\nFor example, given s = \"001101\", we cannot select the 1st, 3rd, and 5th buildings as that would form \"011\" which is not allowed due to having two consecutive buildings of the same type.\n\nReturn the number of valid ways to select 3 buildings.\n \n",
    "examples": [
      {
        "input": "Input: s = \"001101\"",
        "output": "Output: 6",
        "explanation": "Explanation: "
      },
      {
        "input": "Input: s = \"11100\"",
        "output": "Output: 0",
        "explanation": "Explanation: It can be shown that there are no valid selections."
      }
    ],
    "topics": [
      "String",
      "Dynamic Programming",
      "Prefix Sum"
    ],
    "difficulty": "Medium",
    "constraints": [
      "3 <= s.length <= 105",
      "s[i] is either '0' or '1'."
    ],
    "hints": [
      "There are only 2 valid patterns: ‘101’ and ‘010’. Think about how we can construct these 2 patterns from smaller patterns.",
      "Count the number of subsequences of the form ‘01’ or ‘10’ first. Let n01[i] be the number of ‘01’ subsequences that exist in the prefix of s up to the ith building. How can you compute n01[i]?",
      "Let n0[i] and n1[i] be the number of ‘0’s and ‘1’s that exists in the prefix of s up to i respectively. Then n01[i] = n01[i – 1] if s[i] == ‘0’, otherwise n01[i] = n01[i – 1] + n0[i – 1].",
      "The same logic applies to building the n10 array and subsequently the n101 and n010 arrays for the number of ‘101’ and ‘010‘ subsequences."
    ]
  },
  {
    "title": "Find Triangular Sum of an Array",
    "description": "You are given a 0-indexed integer array nums, where nums[i] is a digit between 0 and 9 (inclusive).\nThe triangular sum of nums is the value of the only element present in nums after the following process terminates:\n\nLet nums comprise of n elements. If n == 1, end the process. Otherwise, create a new 0-indexed integer array newNums of length n - 1.\nFor each index i, where 0 <= i < n - 1, assign the value of newNums[i] as (nums[i] + nums[i+1]) % 10, where % denotes modulo operator.\nReplace the array nums with newNums.\nRepeat the entire process starting from step 1.\n\nReturn the triangular sum of nums.\n \n",
    "examples": [
      {
        "input": "Input: nums = [1,2,3,4,5]",
        "output": "Output: 8",
        "explanation": ""
      },
      {
        "input": "Input: nums = [5]",
        "output": "Output: 5",
        "explanation": ""
      }
    ],
    "topics": [
      "Array",
      "Math",
      "Simulation",
      "Combinatorics"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= nums.length <= 1000",
      "0 <= nums[i] <= 9"
    ],
    "hints": [
      "Try simulating the entire process.",
      "To reduce space, use a temporary array to update nums in every step instead of creating a new array at each step."
    ]
  },
  {
    "title": "Minimum Bit Flips to Convert Number",
    "description": "A bit flip of a number x is choosing a bit in the binary representation of x and flipping it from either 0 to 1 or 1 to 0.\n\nFor example, for x = 7, the binary representation is 111 and we may choose any bit (including any leading zeros not shown) and flip it. We can flip the first bit from the right to get 110, flip the second bit from the right to get 101, flip the fifth bit from the right (a leading zero) to get 10111, etc.\n\nGiven two integers start and goal, return the minimum number of bit flips to convert start to goal.\n \n",
    "examples": [
      {
        "input": "Input: start = 10, goal = 7",
        "output": "Output: 3",
        "explanation": "Explanation: The binary representation of 10 and 7 are 1010 and 0111 respectively. We can convert 10 to 7 in 3 steps:"
      },
      {
        "input": "Input: start = 3, goal = 4",
        "output": "Output: 3",
        "explanation": "Explanation: The binary representation of 3 and 4 are 011 and 100 respectively. We can convert 3 to 4 in 3 steps:"
      }
    ],
    "topics": [
      "Bit Manipulation"
    ],
    "difficulty": "Easy",
    "constraints": [
      "0 <= start, goal <= 109"
    ],
    "hints": [
      "If the value of a bit in start and goal differ, then we need to flip that bit.",
      "Consider using the XOR operation to determine which bits need a bit flip."
    ]
  },
  {
    "title": "Minimum Weighted Subgraph With the Required Paths",
    "description": "You are given an integer n denoting the number of nodes of a weighted directed graph. The nodes are numbered from 0 to n - 1.\nYou are also given a 2D integer array edges where edges[i] = [fromi, toi, weighti] denotes that there exists a directed edge from fromi to toi with weight weighti.\nLastly, you are given three distinct integers src1, src2, and dest denoting three distinct nodes of the graph.\nReturn the minimum weight of a subgraph of the graph such that it is possible to reach dest from both src1 and src2 via a set of edges of this subgraph. In case such a subgraph does not exist, return -1.\nA subgraph is a graph whose vertices and edges are subsets of the original graph. The weight of a subgraph is the sum of weights of its constituent edges.\n \n",
    "examples": [
      {
        "input": "Input: n = 6, edges = [[0,2,2],[0,5,6],[1,0,3],[1,4,5],[2,1,1],[2,3,3],[2,3,4],[3,4,2],[4,5,1]], src1 = 0, src2 = 1, dest = 5",
        "output": "Output: 9",
        "explanation": ""
      },
      {
        "input": "Input: n = 3, edges = [[0,1,1],[2,1,1]], src1 = 0, src2 = 1, dest = 2",
        "output": "Output: -1",
        "explanation": ""
      }
    ],
    "topics": [
      "Graph",
      "Shortest Path"
    ],
    "difficulty": "Hard",
    "constraints": [
      "3 <= n <= 105",
      "0 <= edges.length <= 105",
      "edges[i].length == 3",
      "0 <= fromi, toi, src1, src2, dest <= n - 1",
      "fromi != toi",
      "src1, src2, and dest are pairwise distinct.",
      "1 <= weight[i] <= 105"
    ],
    "hints": [
      "Consider what the paths from src1 to dest and src2 to dest would look like in the optimal solution.",
      "It can be shown that in an optimal solution, the two paths from src1 and src2 will coincide at one node, and the remaining part to dest will be the same for both paths. Now consider how to find the node where the paths will coincide.",
      "How can algorithms for finding the shortest path between two nodes help us?"
    ]
  },
  {
    "title": "Find All K-Distant Indices in an Array",
    "description": "You are given a 0-indexed integer array nums and two integers key and k. A k-distant index is an index i of nums for which there exists at least one index j such that |i - j| <= k and nums[j] == key.\nReturn a list of all k-distant indices sorted in increasing order.\n \n",
    "examples": [
      {
        "input": "Input: nums = [3,4,9,1,3,9,5], key = 9, k = 1",
        "output": "Output: [1,2,3,4,5,6]",
        "explanation": "Explanation: Here, nums[2] == key and nums[5] == key."
      },
      {
        "input": "Input: nums = [2,2,2,2,2], key = 2, k = 2",
        "output": "Output: [0,1,2,3,4]",
        "explanation": "Explanation: For all indices i in nums, there exists some index j such that |i - j| <= k and nums[j] == key, so every index is a k-distant index. "
      }
    ],
    "topics": [
      "Array"
    ],
    "difficulty": "Easy",
    "constraints": [
      "1 <= nums.length <= 1000",
      "1 <= nums[i] <= 1000",
      "key is an integer from the array nums.",
      "1 <= k <= nums.length"
    ],
    "hints": [
      "For every occurrence of key in nums, find all indices within distance k from it.",
      "Use a hash table to remove duplicate indices."
    ]
  },
  {
    "title": "Longest Substring of One Repeating Character",
    "description": "You are given a 0-indexed string s. You are also given a 0-indexed string queryCharacters of length k and a 0-indexed array of integer indices queryIndices of length k, both of which are used to describe k queries.\nThe ith query updates the character in s at index queryIndices[i] to the character queryCharacters[i].\nReturn an array lengths of length k where lengths[i] is the length of the longest substring of s consisting of only one repeating character after the ith query is performed.\n \n",
    "examples": [
      {
        "input": "Input: s = \"babacc\", queryCharacters = \"bcb\", queryIndices = [1,3,3]",
        "output": "Output: [3,3,4]",
        "explanation": "Explanation: "
      },
      {
        "input": "Input: s = \"abyzz\", queryCharacters = \"aa\", queryIndices = [2,1]",
        "output": "Output: [2,3]",
        "explanation": ""
      }
    ],
    "topics": [
      "Array",
      "String",
      "Segment Tree",
      "Ordered Set"
    ],
    "difficulty": "Hard",
    "constraints": [
      "1 <= s.length <= 105",
      "s consists of lowercase English letters.",
      "k == queryCharacters.length == queryIndices.length",
      "1 <= k <= 105",
      "queryCharacters consists of lowercase English letters.",
      "0 <= queryIndices[i] < s.length"
    ],
    "hints": [
      "Use a segment tree to perform fast point updates and range queries.",
      "We need each segment tree node to store the length of the longest substring of that segment consisting of only 1 repeating character.",
      "We will also have each segment tree node store the leftmost and rightmost character of the segment, the max length of a prefix substring consisting of only 1 repeating character, and the max length of a suffix substring consisting of only 1 repeating character.",
      "Use this information to properly merge the two segment tree nodes together."
    ]
  },
  {
    "title": "Maximum Points in an Archery Competition",
    "description": "Alice and Bob are opponents in an archery competition. The competition has set the following rules:\n\nAlice first shoots numArrows arrows and then Bob shoots numArrows arrows.\nThe points are then calculated as follows:\n\t\nThe target has integer scoring sections ranging from 0 to 11 inclusive.\nFor each section of the target with score k (in between 0 to 11), say Alice and Bob have shot ak and bk arrows on that section respectively. If ak >= bk, then Alice takes k points. If ak < bk, then Bob takes k points.\nHowever, if ak == bk == 0, then nobody takes k points.\n\n\n\n\n\nFor example, if Alice and Bob both shot 2 arrows on the section with score 11, then Alice takes 11 points. On the other hand, if Alice shot 0 arrows on the section with score 11 and Bob shot 2 arrows on that same section, then Bob takes 11 points.\n\n\nYou are given the integer numArrows and an integer array aliceArrows of size 12, which represents the number of arrows Alice shot on each scoring section from 0 to 11. Now, Bob wants to maximize the total number of points he can obtain.\nReturn the array bobArrows which represents the number of arrows Bob shot on each scoring section from 0 to 11. The sum of the values in bobArrows should equal numArrows.\nIf there are multiple ways for Bob to earn the maximum total points, return any one of them.\n \n",
    "examples": [
      {
        "input": "Input: numArrows = 9, aliceArrows = [1,1,0,1,0,0,2,1,0,1,2,0]",
        "output": "Output: [0,0,0,0,1,1,0,0,1,2,3,1]",
        "explanation": "Explanation: The table above shows how the competition is scored. "
      },
      {
        "input": "Input: numArrows = 3, aliceArrows = [0,0,1,0,0,0,0,0,0,0,0,2]",
        "output": "Output: [0,0,0,0,0,0,0,0,1,1,1,0]",
        "explanation": "Explanation: The table above shows how the competition is scored."
      }
    ],
    "topics": [
      "Array",
      "Bit Manipulation",
      "Recursion",
      "Enumeration"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= numArrows <= 105",
      "aliceArrows.length == bobArrows.length == 12",
      "0 <= aliceArrows[i], bobArrows[i] <= numArrows",
      "sum(aliceArrows[i]) == numArrows"
    ],
    "hints": [
      "To obtain points for some certain section x, what is the minimum number of arrows Bob must shoot?",
      "Given the small number of sections, can we brute force which sections Bob wants to win?",
      "For every set of sections Bob wants to win, check if we have the required amount of arrows. If we do, it is a valid selection."
    ]
  },
  {
    "title": "Count Collisions on a Road",
    "description": "There are n cars on an infinitely long road. The cars are numbered from 0 to n - 1 from left to right and each car is present at a unique point.\nYou are given a 0-indexed string directions of length n. directions[i] can be either 'L', 'R', or 'S' denoting whether the ith car is moving towards the left, towards the right, or staying at its current point respectively. Each moving car has the same speed.\nThe number of collisions can be calculated as follows:\n\nWhen two cars moving in opposite directions collide with each other, the number of collisions increases by 2.\nWhen a moving car collides with a stationary car, the number of collisions increases by 1.\n\nAfter a collision, the cars involved can no longer move and will stay at the point where they collided. Other than that, cars cannot change their state or direction of motion.\nReturn the total number of collisions that will happen on the road.\n \n",
    "examples": [
      {
        "input": "Input: directions = \"RLRSLL\"",
        "output": "Output: 5",
        "explanation": ""
      },
      {
        "input": "Input: directions = \"LLRR\"",
        "output": "Output: 0",
        "explanation": ""
      }
    ],
    "topics": [
      "String",
      "Stack"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= directions.length <= 105",
      "directions[i] is either 'L', 'R', or 'S'."
    ],
    "hints": [
      "In what circumstances does a moving car not collide with another car?",
      "If we disregard the moving cars that do not collide with another car, what does each moving car contribute to the answer?",
      "Will stationary cars contribute towards the answer?"
    ]
  },
  {
    "title": "Count Hills and Valleys in an Array",
    "description": "You are given a 0-indexed integer array nums. An index i is part of a hill in nums if the closest non-equal neighbors of i are smaller than nums[i]. Similarly, an index i is part of a valley in nums if the closest non-equal neighbors of i are larger than nums[i]. Adjacent indices i and j are part of the same hill or valley if nums[i] == nums[j].\nNote that for an index to be part of a hill or valley, it must have a non-equal neighbor on both the left and right of the index.\nReturn the number of hills and valleys in nums.\n \n",
    "examples": [
      {
        "input": "Input: nums = [2,4,1,1,6,5]",
        "output": "Output: 3",
        "explanation": ""
      },
      {
        "input": "Input: nums = [6,6,5,5,4,1]",
        "output": "Output: 0",
        "explanation": ""
      }
    ],
    "topics": [
      "Array"
    ],
    "difficulty": "Easy",
    "constraints": [
      "3 <= nums.length <= 100",
      "1 <= nums[i] <= 100"
    ],
    "hints": [
      "For each index, could you find the closest non-equal neighbors?",
      "Ensure that adjacent indices that are part of the same hill or valley are not double-counted."
    ]
  },
  {
    "title": "Most Frequent Number Following Key In an Array",
    "description": "You are given a 0-indexed integer array nums. You are also given an integer key, which is present in nums.\nFor every unique integer target in nums, count the number of times target immediately follows an occurrence of key in nums. In other words, count the number of indices i such that:\n\n0 <= i <= nums.length - 2,\nnums[i] == key and,\nnums[i + 1] == target.\n\nReturn the target with the maximum count. The test cases will be generated such that the target with maximum count is unique.\n \n",
    "examples": [
      {
        "input": "Input: nums = [1,100,200,1,100], key = 1",
        "output": "Output: 100",
        "explanation": "Explanation: For target = 100, there are 2 occurrences at indices 1 and 4 which follow an occurrence of key."
      },
      {
        "input": "Input: nums = [2,2,2,2,3], key = 2",
        "output": "Output: 2",
        "explanation": "Explanation: For target = 2, there are 3 occurrences at indices 1, 2, and 3 which follow an occurrence of key."
      }
    ],
    "topics": [
      "Array",
      "Hash Table",
      "Counting"
    ],
    "difficulty": "Easy",
    "constraints": [
      "2 <= nums.length <= 1000",
      "1 <= nums[i] <= 1000",
      "The test cases will be generated such that the answer is unique."
    ],
    "hints": [
      "Count the number of times each target value follows the key in the array.",
      "Choose the target with the maximum count and return it."
    ]
  },
  {
    "title": "Minimum White Tiles After Covering With Carpets",
    "description": "You are given a 0-indexed binary string floor, which represents the colors of tiles on a floor:\n\nfloor[i] = '0' denotes that the ith tile of the floor is colored black.\nOn the other hand, floor[i] = '1' denotes that the ith tile of the floor is colored white.\n\nYou are also given numCarpets and carpetLen. You have numCarpets black carpets, each of length carpetLen tiles. Cover the tiles with the given carpets such that the number of white tiles still visible is minimum. Carpets may overlap one another.\nReturn the minimum number of white tiles still visible.\n \n",
    "examples": [
      {
        "input": "Input: floor = \"10110101\", numCarpets = 2, carpetLen = 2",
        "output": "Output: 2",
        "explanation": "Explanation: "
      },
      {
        "input": "Input: floor = \"11111\", numCarpets = 2, carpetLen = 3",
        "output": "Output: 0",
        "explanation": "Explanation: "
      }
    ],
    "topics": [
      "String",
      "Dynamic Programming",
      "Prefix Sum"
    ],
    "difficulty": "Hard",
    "constraints": [
      "1 <= carpetLen <= floor.length <= 1000",
      "floor[i] is either '0' or '1'.",
      "1 <= numCarpets <= 1000"
    ],
    "hints": [
      "Can you think of a DP solution?",
      "Let DP[i][j] denote the minimum number of white tiles still visible from indices i to floor.length-1 after covering with at most j carpets.",
      "The transition will be whether to put down the carpet at position i (if possible), or not."
    ]
  },
  {
    "title": "Minimum Operations to Halve Array Sum",
    "description": "You are given an array nums of positive integers. In one operation, you can choose any number from nums and reduce it to exactly half the number. (Note that you may choose this reduced number in future operations.)\nReturn the minimum number of operations to reduce the sum of nums by at least half.\n \n",
    "examples": [
      {
        "input": "Input: nums = [5,19,8,1]",
        "output": "Output: 3",
        "explanation": "Explanation: The initial sum of nums is equal to 5 + 19 + 8 + 1 = 33."
      },
      {
        "input": "Input: nums = [3,8,20]",
        "output": "Output: 3",
        "explanation": "Explanation: The initial sum of nums is equal to 3 + 8 + 20 = 31."
      }
    ],
    "topics": [
      "Array",
      "Greedy",
      "Heap (Priority Queue)"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= nums.length <= 105",
      "1 <= nums[i] <= 107"
    ],
    "hints": [
      "It is always optimal to halve the largest element.",
      "What data structure allows for an efficient query of the maximum element?",
      "Use a heap or priority queue to maintain the current elements."
    ]
  },
  {
    "title": "Maximize Number of Subsequences in a String",
    "description": "You are given a 0-indexed string text and another 0-indexed string pattern of length 2, both of which consist of only lowercase English letters.\nYou can add either pattern[0] or pattern[1] anywhere in text exactly once. Note that the character can be added even at the beginning or at the end of text.\nReturn the maximum number of times pattern can occur as a subsequence of the modified text.\nA subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.\n \n",
    "examples": [
      {
        "input": "Input: text = \"abdcdbc\", pattern = \"ac\"",
        "output": "Output: 4",
        "explanation": ""
      },
      {
        "input": "Input: text = \"aabb\", pattern = \"ab\"",
        "output": "Output: 6",
        "explanation": ""
      }
    ],
    "topics": [
      "String",
      "Greedy",
      "Prefix Sum"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= text.length <= 105",
      "pattern.length == 2",
      "text and pattern consist only of lowercase English letters."
    ],
    "hints": [
      "Find the optimal position to add pattern[0] so that the number of subsequences is maximized. Similarly, find the optimal position to add pattern[1].",
      "For each of the above cases, count the number of times the pattern occurs as a subsequence in text. The larger count is the required answer."
    ]
  },
  {
    "title": "Divide Array Into Equal Pairs",
    "description": "You are given an integer array nums consisting of 2 * n integers.\nYou need to divide nums into n pairs such that:\n\nEach element belongs to exactly one pair.\nThe elements present in a pair are equal.\n\nReturn true if nums can be divided into n pairs, otherwise return false.\n \n",
    "examples": [
      {
        "input": "Input: nums = [3,2,3,2,2,2]",
        "output": "Output: true",
        "explanation": "Explanation: "
      },
      {
        "input": "Input: nums = [1,2,3,4]",
        "output": "Output: false",
        "explanation": "Explanation: "
      }
    ],
    "topics": [
      "Array",
      "Hash Table",
      "Bit Manipulation",
      "Counting"
    ],
    "difficulty": "Easy",
    "constraints": [
      "nums.length == 2 * n",
      "1 <= n <= 500",
      "1 <= nums[i] <= 500"
    ],
    "hints": [
      "For any number x in the range [1, 500], count the number of elements in nums whose values are equal to x.",
      "The elements with equal value can be divided completely into pairs if and only if their count is even."
    ]
  },
  {
    "title": "Replace Non-Coprime Numbers in Array",
    "description": "You are given an array of integers nums. Perform the following steps:\n\nFind any two adjacent numbers in nums that are non-coprime.\nIf no such numbers are found, stop the process.\nOtherwise, delete the two numbers and replace them with their LCM (Least Common Multiple).\nRepeat this process as long as you keep finding two adjacent non-coprime numbers.\n\nReturn the final modified array. It can be shown that replacing adjacent non-coprime numbers in any arbitrary order will lead to the same result.\nThe test cases are generated such that the values in the final array are less than or equal to 108.\nTwo values x and y are non-coprime if GCD(x, y) > 1 where GCD(x, y) is the Greatest Common Divisor of x and y.\n \n",
    "examples": [
      {
        "input": "Input: nums = [6,4,3,2,7,6,2]",
        "output": "Output: [12,7,6]",
        "explanation": "Explanation: "
      },
      {
        "input": "Input: nums = [2,2,1,1,3,3,3]",
        "output": "Output: [2,1,1,3]",
        "explanation": "Explanation: "
      }
    ],
    "topics": [
      "Array",
      "Math",
      "Stack",
      "Number Theory"
    ],
    "difficulty": "Hard",
    "constraints": [
      "1 <= nums.length <= 105",
      "1 <= nums[i] <= 105",
      "The test cases are generated such that the values in the final array are less than or equal to 108."
    ],
    "hints": [
      "Notice that the order of merging two numbers into their LCM does not matter so we can greedily merge elements to its left if possible.",
      "If a new value is formed, we should recursively check if it can be merged with the value to its left.",
      "To simulate the merge efficiently, we can maintain a stack that stores processed elements. When we iterate through the array, we only compare with the top of the stack (which is the value to its left)."
    ]
  },
  {
    "title": "Create Binary Tree From Descriptions",
    "description": "You are given a 2D integer array descriptions where descriptions[i] = [parenti, childi, isLefti] indicates that parenti is the parent of childi in a binary tree of unique values. Furthermore,\n\nIf isLefti == 1, then childi is the left child of parenti.\nIf isLefti == 0, then childi is the right child of parenti.\n\nConstruct the binary tree described by descriptions and return its root.\nThe test cases will be generated such that the binary tree is valid.\n \n",
    "examples": [
      {
        "input": "Input: descriptions = [[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]",
        "output": "Output: [50,20,80,15,17,19]",
        "explanation": "Explanation: The root node is the node with value 50 since it has no parent."
      },
      {
        "input": "Input: descriptions = [[1,2,1],[2,3,0],[3,4,1]]",
        "output": "Output: [1,2,null,null,3,4]",
        "explanation": "Explanation: The root node is the node with value 1 since it has no parent."
      }
    ],
    "topics": [
      "Array",
      "Hash Table",
      "Tree",
      "Depth-First Search",
      "Breadth-First Search",
      "Binary Tree"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= descriptions.length <= 104",
      "descriptions[i].length == 3",
      "1 <= parenti, childi <= 105",
      "0 <= isLefti <= 1",
      "The binary tree described by descriptions is valid."
    ],
    "hints": [
      "Could you represent and store the descriptions more efficiently?",
      "Could you find the root node?",
      "The node that is not a child in any of the descriptions is the root node."
    ]
  },
  {
    "title": "Append K Integers With Minimal Sum",
    "description": "You are given an integer array nums and an integer k. Append k unique positive integers that do not appear in nums to nums such that the resulting total sum is minimum.\nReturn the sum of the k integers appended to nums.\n \n",
    "examples": [
      {
        "input": "Input: nums = [1,4,25,10,25], k = 2",
        "output": "Output: 5",
        "explanation": "Explanation: The two unique positive integers that do not appear in nums which we append are 2 and 3."
      },
      {
        "input": "Input: nums = [5,6], k = 6",
        "output": "Output: 25",
        "explanation": "Explanation: The six unique positive integers that do not appear in nums which we append are 1, 2, 3, 4, 7, and 8."
      }
    ],
    "topics": [
      "Array",
      "Math",
      "Greedy",
      "Sorting"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= nums.length <= 105",
      "1 <= nums[i] <= 109",
      "1 <= k <= 108"
    ],
    "hints": [
      "The k smallest numbers that do not appear in nums will result in the minimum sum.",
      "Recall that the sum of the first n positive numbers is equal to n * (n+1) / 2.",
      "Initialize the answer as the sum of 1 to k. Then, adjust the answer depending on the values in nums."
    ]
  },
  {
    "title": "Cells in a Range on an Excel Sheet",
    "description": "A cell (r, c) of an excel sheet is represented as a string \"<col><row>\" where:\n\n<col> denotes the column number c of the cell. It is represented by alphabetical letters.\n\n\t\nFor example, the 1st column is denoted by 'A', the 2nd by 'B', the 3rd by 'C', and so on.\n\n\n<row> is the row number r of the cell. The rth row is represented by the integer r.\n\nYou are given a string s in the format \"<col1><row1>:<col2><row2>\", where <col1> represents the column c1, <row1> represents the row r1, <col2> represents the column c2, and <row2> represents the row r2, such that r1 <= r2 and c1 <= c2.\nReturn the list of cells (x, y) such that r1 <= x <= r2 and c1 <= y <= c2. The cells should be represented as strings in the format mentioned above and be sorted in non-decreasing order first by columns and then by rows.\n \n",
    "examples": [
      {
        "input": "Input: s = \"K1:L2\"",
        "output": "Output: [\"K1\",\"K2\",\"L1\",\"L2\"]",
        "explanation": ""
      },
      {
        "input": "Input: s = \"A1:F1\"",
        "output": "Output: [\"A1\",\"B1\",\"C1\",\"D1\",\"E1\",\"F1\"]",
        "explanation": ""
      }
    ],
    "topics": [
      "String"
    ],
    "difficulty": "Easy",
    "constraints": [
      "s.length == 5",
      "'A' <= s[0] <= s[3] <= 'Z'",
      "'1' <= s[1] <= s[4] <= '9'",
      "s consists of uppercase English letters, digits and ':'."
    ],
    "hints": [
      "From the given string, find the corresponding rows and columns.",
      "Iterate through the columns in ascending order and for each column, iterate through the rows in ascending order to obtain the required cells in sorted order."
    ]
  },
  {
    "title": "Count Array Pairs Divisible by K",
    "description": "Given a 0-indexed integer array nums of length n and an integer k, return the number of pairs (i, j) such that:\n\n0 <= i < j <= n - 1 and\nnums[i] * nums[j] is divisible by k.\n\n \n",
    "examples": [
      {
        "input": "Input: nums = [1,2,3,4,5], k = 2",
        "output": "Output: 7",
        "explanation": "Explanation: "
      },
      {
        "input": "Input: nums = [1,2,3,4], k = 5",
        "output": "Output: 0",
        "explanation": "Explanation: There does not exist any pair of indices whose corresponding product is divisible by 5."
      }
    ],
    "topics": [
      "Array",
      "Math",
      "Number Theory"
    ],
    "difficulty": "Hard",
    "constraints": [
      "1 <= nums.length <= 105",
      "1 <= nums[i], k <= 105"
    ],
    "hints": [
      "For any element in the array, what is the smallest number it should be multiplied with such that the product is divisible by k?",
      "The smallest number which should be multiplied with nums[i] so that the product is divisible by k is k / gcd(k, nums[i]). Now think about how you can store and update the count of such numbers present in the array efficiently."
    ]
  },
  {
    "title": "Construct String With Repeat Limit",
    "description": "You are given a string s and an integer repeatLimit. Construct a new string repeatLimitedString using the characters of s such that no letter appears more than repeatLimit times in a row. You do not have to use all characters from s.\nReturn the lexicographically largest repeatLimitedString possible.\nA string a is lexicographically larger than a string b if in the first position where a and b differ, string a has a letter that appears later in the alphabet than the corresponding letter in b. If the first min(a.length, b.length) characters do not differ, then the longer string is the lexicographically larger one.\n \n",
    "examples": [
      {
        "input": "Input: s = \"cczazcc\", repeatLimit = 3",
        "output": "Output: \"zzcccac\"",
        "explanation": "Explanation: We use all of the characters from s to construct the repeatLimitedString \"zzcccac\"."
      },
      {
        "input": "Input: s = \"aababab\", repeatLimit = 2",
        "output": "Output: \"bbabaa\"",
        "explanation": "Explanation: We use only some of the characters from s to construct the repeatLimitedString \"bbabaa\". "
      }
    ],
    "topics": [
      "String",
      "Greedy",
      "Heap (Priority Queue)",
      "Counting"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= repeatLimit <= s.length <= 105",
      "s consists of lowercase English letters."
    ],
    "hints": [
      "Start constructing the string in descending order of characters.",
      "When repeatLimit is reached, pick the next largest character."
    ]
  },
  {
    "title": "Merge Nodes in Between Zeros",
    "description": "You are given the head of a linked list, which contains a series of integers separated by 0's. The beginning and end of the linked list will have Node.val == 0.\nFor every two consecutive 0's, merge all the nodes lying in between them into a single node whose value is the sum of all the merged nodes. The modified list should not contain any 0's.\nReturn the head of the modified linked list.\n \n",
    "examples": [
      {
        "input": "Input: head = [0,3,1,0,4,5,2,0]",
        "output": "Output: [4,11]",
        "explanation": "Explanation: "
      },
      {
        "input": "Input: head = [0,1,0,3,0,2,2,0]",
        "output": "Output: [1,3,4]",
        "explanation": "Explanation: "
      }
    ],
    "topics": [
      "Linked List",
      "Simulation"
    ],
    "difficulty": "Medium",
    "constraints": [
      "The number of nodes in the list is in the range [3, 2 * 105].",
      "0 <= Node.val <= 1000",
      "There are no two consecutive nodes with Node.val == 0.",
      "The beginning and end of the linked list have Node.val == 0."
    ],
    "hints": [
      "How can you use two pointers to modify the original list into the new list?",
      "Have a pointer traverse the entire linked list, while another pointer looks at a node that is currently being modified.",
      "Keep on summing the values of the nodes between the traversal pointer and the modifying pointer until the former comes across a ‘0’. In that case, the modifying pointer is incremented to modify the next node.",
      "Do not forget to have the next pointer of the final node of the modified list point to null."
    ]
  },
  {
    "title": "Count Integers With Even Digit Sum",
    "description": "Given a positive integer num, return the number of positive integers less than or equal to num whose digit sums are even.\nThe digit sum of a positive integer is the sum of all its digits.\n \n",
    "examples": [
      {
        "input": "Input: num = 4",
        "output": "Output: 2",
        "explanation": ""
      },
      {
        "input": "Input: num = 30",
        "output": "Output: 14",
        "explanation": ""
      }
    ],
    "topics": [
      "Math",
      "Simulation"
    ],
    "difficulty": "Easy",
    "constraints": [
      "1 <= num <= 1000"
    ],
    "hints": [
      "Iterate through all integers from 1 to num.",
      "For any integer, extract the individual digits to compute their sum and check if it is even."
    ]
  },
  {
    "title": "Minimum Time to Finish the Race",
    "description": "You are given a 0-indexed 2D integer array tires where tires[i] = [fi, ri] indicates that the ith tire can finish its xth successive lap in fi * ri(x-1) seconds.\n\nFor example, if fi = 3 and ri = 2, then the tire would finish its 1st lap in 3 seconds, its 2nd lap in 3 * 2 = 6 seconds, its 3rd lap in 3 * 22 = 12 seconds, etc.\n\nYou are also given an integer changeTime and an integer numLaps.\nThe race consists of numLaps laps and you may start the race with any tire. You have an unlimited supply of each tire and after every lap, you may change to any given tire (including the current tire type) if you wait changeTime seconds.\nReturn the minimum time to finish the race.\n \n",
    "examples": [
      {
        "input": "Input: tires = [[2,3],[3,4]], changeTime = 5, numLaps = 4",
        "output": "Output: 21",
        "explanation": "Explanation: "
      },
      {
        "input": "Input: tires = [[1,10],[2,2],[3,4]], changeTime = 6, numLaps = 5",
        "output": "Output: 25",
        "explanation": "Explanation: "
      }
    ],
    "topics": [
      "Array",
      "Dynamic Programming"
    ],
    "difficulty": "Hard",
    "constraints": [
      "1 <= tires.length <= 105",
      "tires[i].length == 2",
      "1 <= fi, changeTime <= 105",
      "2 <= ri <= 105",
      "1 <= numLaps <= 1000"
    ],
    "hints": [
      "What is the maximum number of times we would want to go around the track without changing tires?",
      "Can we precompute the minimum time to go around the track x times without changing tires?",
      "Can we use dynamic programming to solve this efficiently using the precomputed values?"
    ]
  },
  {
    "title": "Minimum Time to Complete Trips",
    "description": "You are given an array time where time[i] denotes the time taken by the ith bus to complete one trip.\nEach bus can make multiple trips successively; that is, the next trip can start immediately after completing the current trip. Also, each bus operates independently; that is, the trips of one bus do not influence the trips of any other bus.\nYou are also given an integer totalTrips, which denotes the number of trips all buses should make in total. Return the minimum time required for all buses to complete at least totalTrips trips.\n \n",
    "examples": [
      {
        "input": "Input: time = [1,2,3], totalTrips = 5",
        "output": "Output: 3",
        "explanation": ""
      },
      {
        "input": "Input: time = [2], totalTrips = 1",
        "output": "Output: 2",
        "explanation": ""
      }
    ],
    "topics": [
      "Array",
      "Binary Search"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= time.length <= 105",
      "1 <= time[i], totalTrips <= 107"
    ],
    "hints": [
      "For a given amount of time, how can we count the total number of trips completed by all buses within that time?",
      "Consider using binary search."
    ]
  },
  {
    "title": "Minimum Number of Steps to Make Two Strings Anagram II",
    "description": "You are given two strings s and t. In one step, you can append any character to either s or t.\nReturn the minimum number of steps to make s and t anagrams of each other.\nAn anagram of a string is a string that contains the same characters with a different (or the same) ordering.\n \n",
    "examples": [
      {
        "input": "Input: s = \"leetcode\", t = \"coats\"",
        "output": "Output: 7",
        "explanation": "Explanation: "
      },
      {
        "input": "Input: s = \"night\", t = \"thing\"",
        "output": "Output: 0",
        "explanation": "Explanation: The given strings are already anagrams of each other. Thus, we do not need any further steps."
      }
    ],
    "topics": [
      "Hash Table",
      "String",
      "Counting"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= s.length, t.length <= 2 * 105",
      "s and t consist of lowercase English letters."
    ],
    "hints": [
      "Notice that for anagrams, the order of the letters is irrelevant.",
      "For each letter, we can count its frequency in s and t.",
      "For each letter, its contribution to the answer is the absolute difference between its frequency in s and t."
    ]
  },
  {
    "title": "Counting Words With a Given Prefix",
    "description": "You are given an array of strings words and a string pref.\nReturn the number of strings in words that contain pref as a prefix.\nA prefix of a string s is any leading contiguous substring of s.\n \n",
    "examples": [
      {
        "input": "Input: words = [\"pay\",\"attention\",\"practice\",\"attend\"], pref = \"at\"",
        "output": "Output: 2",
        "explanation": "Explanation: The 2 strings that contain \"at\" as a prefix are: \"attention\" and \"attend\"."
      },
      {
        "input": "Input: words = [\"leetcode\",\"win\",\"loops\",\"success\"], pref = \"code\"",
        "output": "Output: 0",
        "explanation": "Explanation: There are no strings that contain \"code\" as a prefix."
      }
    ],
    "topics": [
      "Array",
      "String"
    ],
    "difficulty": "Easy",
    "constraints": [
      "1 <= words.length <= 100",
      "1 <= words[i].length, pref.length <= 100",
      "words[i] and pref consist of lowercase English letters."
    ],
    "hints": [
      "Go through each word in words and increment the answer if pref is a prefix of the word."
    ]
  },
  {
    "title": "Maximum AND Sum of Array",
    "description": "You are given an integer array nums of length n and an integer numSlots such that 2 * numSlots >= n. There are numSlots slots numbered from 1 to numSlots.\nYou have to place all n integers into the slots such that each slot contains at most two numbers. The AND sum of a given placement is the sum of the bitwise AND of every number with its respective slot number.\n\nFor example, the AND sum of placing the numbers [1, 3] into slot 1 and [4, 6] into slot 2 is equal to (1 AND 1) + (3 AND 1) + (4 AND 2) + (6 AND 2) = 1 + 1 + 0 + 2 = 4.\n\nReturn the maximum possible AND sum of nums given numSlots slots.\n \n",
    "examples": [
      {
        "input": "Input: nums = [1,2,3,4,5,6], numSlots = 3",
        "output": "Output: 9",
        "explanation": "Explanation: One possible placement is [1, 4] into slot 1, [2, 6] into slot 2, and [3, 5] into slot 3. "
      },
      {
        "input": "Input: nums = [1,3,10,4,7,1], numSlots = 9",
        "output": "Output: 24",
        "explanation": "Explanation: One possible placement is [1, 1] into slot 1, [3] into slot 3, [4] into slot 4, [7] into slot 7, and [10] into slot 9."
      }
    ],
    "topics": [
      "Array",
      "Dynamic Programming",
      "Bit Manipulation",
      "Bitmask"
    ],
    "difficulty": "Hard",
    "constraints": [
      "n == nums.length",
      "1 <= numSlots <= 9",
      "1 <= n <= 2 * numSlots",
      "1 <= nums[i] <= 15"
    ],
    "hints": [
      "Can you think of a dynamic programming solution to this problem?",
      "Can you use a bitmask to represent the state of the slots?"
    ]
  },
  {
    "title": "Removing Minimum Number of Magic Beans",
    "description": "You are given an array of positive integers beans, where each integer represents the number of magic beans found in a particular magic bag.\nRemove any number of beans (possibly none) from each bag such that the number of beans in each remaining non-empty bag (still containing at least one bean) is equal. Once a bean has been removed from a bag, you are not allowed to return it to any of the bags.\nReturn the minimum number of magic beans that you have to remove.\n \n",
    "examples": [
      {
        "input": "Input: beans = [4,1,6,5]",
        "output": "Output: 4",
        "explanation": "Explanation: "
      },
      {
        "input": "Input: beans = [2,10,3,2]",
        "output": "Output: 7",
        "explanation": ""
      }
    ],
    "topics": [
      "Array",
      "Sorting",
      "Prefix Sum"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= beans.length <= 105",
      "1 <= beans[i] <= 105"
    ],
    "hints": [
      "Notice that if we choose to make x bags of beans empty, we should choose the x bags with the least amount of beans.",
      "Notice that if the minimum number of beans in a non-empty bag is m, then the best way to make all bags have an equal amount of beans is to reduce all the bags to have m beans.",
      "Can we iterate over how many bags we should remove and choose the one that minimizes the total amount of beans to remove?",
      "Sort the bags of beans first."
    ]
  },
  {
    "title": "Minimum Operations to Make the Array Alternating",
    "description": "You are given a 0-indexed array nums consisting of n positive integers.\nThe array nums is called alternating if:\n\nnums[i - 2] == nums[i], where 2 <= i <= n - 1.\nnums[i - 1] != nums[i], where 1 <= i <= n - 1.\n\nIn one operation, you can choose an index i and change nums[i] into any positive integer.\nReturn the minimum number of operations required to make the array alternating.\n \n",
    "examples": [
      {
        "input": "Input: nums = [3,1,3,2,4,3]",
        "output": "Output: 3",
        "explanation": ""
      },
      {
        "input": "Input: nums = [1,2,2,2,2]",
        "output": "Output: 2",
        "explanation": ""
      }
    ],
    "topics": [
      "Array",
      "Hash Table",
      "Greedy",
      "Counting"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= nums.length <= 105",
      "1 <= nums[i] <= 105"
    ],
    "hints": [
      "Count the frequency of each element in odd positions in the array. Do the same for elements in even positions.",
      "To minimize the number of operations we need to maximize the number of elements we keep from the original array.",
      "What are the possible combinations of elements we can choose from odd indices and even indices so that the number of unchanged elements is maximized?"
    ]
  },
  {
    "title": "Count Operations to Obtain Zero",
    "description": "You are given two non-negative integers num1 and num2.\nIn one operation, if num1 >= num2, you must subtract num2 from num1, otherwise subtract num1 from num2.\n\nFor example, if num1 = 5 and num2 = 4, subtract num2 from num1, thus obtaining num1 = 1 and num2 = 4. However, if num1 = 4 and num2 = 5, after one operation, num1 = 4 and num2 = 1.\n\nReturn the number of operations required to make either num1 = 0 or num2 = 0.\n \n",
    "examples": [
      {
        "input": "Input: num1 = 2, num2 = 3",
        "output": "Output: 3",
        "explanation": "Explanation: "
      },
      {
        "input": "Input: num1 = 10, num2 = 10",
        "output": "Output: 1",
        "explanation": "Explanation: "
      }
    ],
    "topics": [
      "Math",
      "Simulation"
    ],
    "difficulty": "Easy",
    "constraints": [
      "0 <= num1, num2 <= 105"
    ],
    "hints": [
      "Try simulating the process until either of the two integers is zero.",
      "Count the number of operations done."
    ]
  },
  {
    "title": "Minimum Time to Remove All Cars Containing Illegal Goods",
    "description": "You are given a 0-indexed binary string s which represents a sequence of train cars. s[i] = '0' denotes that the ith car does not contain illegal goods and s[i] = '1' denotes that the ith car does contain illegal goods.\nAs the train conductor, you would like to get rid of all the cars containing illegal goods. You can do any of the following three operations any number of times:\n\nRemove a train car from the left end (i.e., remove s[0]) which takes 1 unit of time.\nRemove a train car from the right end (i.e., remove s[s.length - 1]) which takes 1 unit of time.\nRemove a train car from anywhere in the sequence which takes 2 units of time.\n\nReturn the minimum time to remove all the cars containing illegal goods.\nNote that an empty sequence of cars is considered to have no cars containing illegal goods.\n \n",
    "examples": [
      {
        "input": "Input: s = \"1100101\"",
        "output": "Output: 5",
        "explanation": "Explanation: "
      },
      {
        "input": "Input: s = \"0010\"",
        "output": "Output: 2",
        "explanation": ""
      }
    ],
    "topics": [
      "String",
      "Dynamic Programming"
    ],
    "difficulty": "Hard",
    "constraints": [
      "1 <= s.length <= 2 * 105",
      "s[i] is either '0' or '1'."
    ],
    "hints": [
      "Build an array withoutFirst where withoutFirst[i] stores the minimum time to remove all the cars containing illegal goods from the ‘suffix’ of the sequence starting from the ith car without using any type 1 operations.",
      "Next, build an array onlyFirst where onlyFirst[i] stores the minimum time to remove all the cars containing illegal goods from the ‘prefix’ of the sequence ending on the ith car using only type 1 operations.",
      "Finally, we can compare the best way to split the operations amongst these two types by finding the minimum time across all onlyFirst[i] + withoutFirst[i + 1]."
    ]
  },
  {
    "title": "Design Bitset",
    "description": "A Bitset is a data structure that compactly stores bits.\nImplement the Bitset class:\n\nBitset(int size) Initializes the Bitset with size bits, all of which are 0.\nvoid fix(int idx) Updates the value of the bit at the index idx to 1. If the value was already 1, no change occurs.\nvoid unfix(int idx) Updates the value of the bit at the index idx to 0. If the value was already 0, no change occurs.\nvoid flip() Flips the values of each bit in the Bitset. In other words, all bits with value 0 will now have value 1 and vice versa.\nboolean all() Checks if the value of each bit in the Bitset is 1. Returns true if it satisfies the condition, false otherwise.\nboolean one() Checks if there is at least one bit in the Bitset with value 1. Returns true if it satisfies the condition, false otherwise.\nint count() Returns the total number of bits in the Bitset which have value 1.\nString toString() Returns the current composition of the Bitset. Note that in the resultant string, the character at the ith index should coincide with the value at the ith bit of the Bitset.\n\n \n",
    "examples": [
      {
        "input": "Input\n[\"Bitset\", \"fix\", \"fix\", \"flip\", \"all\", \"unfix\", \"flip\", \"one\", \"unfix\", \"count\", \"toString\"]",
        "output": "Output\n[null, null, null, null, false, null, null, true, null, 2, \"01010\"]",
        "explanation": "Explanation\nBitset bs = new Bitset(5); // bitset = \"00000\"."
      }
    ],
    "topics": [
      "Array",
      "Hash Table",
      "Design"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= size <= 105",
      "0 <= idx <= size - 1",
      "At most 105 calls will be made in total to fix, unfix, flip, all, one, count, and toString.",
      "At least one call will be made to all, one, count, or toString.",
      "At most 5 calls will be made to toString."
    ],
    "hints": [
      "Note that flipping a bit twice does nothing.",
      "In order to determine the value of a bit, consider how you can efficiently count the number of flips made on the bit since its latest update."
    ]
  },
  {
    "title": "Smallest Value of the Rearranged Number",
    "description": "You are given an integer num. Rearrange the digits of num such that its value is minimized and it does not contain any leading zeros.\nReturn the rearranged number with minimal value.\nNote that the sign of the number does not change after rearranging the digits.\n \n",
    "examples": [
      {
        "input": "Input: num = 310",
        "output": "Output: 103",
        "explanation": "Explanation: The possible arrangements for the digits of 310 are 013, 031, 103, 130, 301, 310. "
      },
      {
        "input": "Input: num = -7605",
        "output": "Output: -7650",
        "explanation": "Explanation: Some possible arrangements for the digits of -7605 are -7650, -6705, -5076, -0567."
      }
    ],
    "topics": [
      "Math",
      "Sorting"
    ],
    "difficulty": "Medium",
    "constraints": [
      "-1015 <= num <= 1015"
    ],
    "hints": [
      "For positive numbers, the leading digit should be the smallest nonzero digit. Then the remaining digits follow in ascending order.",
      "For negative numbers, the digits should be arranged in descending order."
    ]
  },
  {
    "title": "Sort Even and Odd Indices Independently",
    "description": "You are given a 0-indexed integer array nums. Rearrange the values of nums according to the following rules:\n\nSort the values at odd indices of nums in non-increasing order.\n\n\t\nFor example, if nums = [4,1,2,3] before this step, it becomes [4,3,2,1] after. The values at odd indices 1 and 3 are sorted in non-increasing order.\n\n\nSort the values at even indices of nums in non-decreasing order.\n\t\nFor example, if nums = [4,1,2,3] before this step, it becomes [2,1,4,3] after. The values at even indices 0 and 2 are sorted in non-decreasing order.\n\n\n\nReturn the array formed after rearranging the values of nums.\n \n",
    "examples": [
      {
        "input": "Input: nums = [4,1,2,3]",
        "output": "Output: [2,3,4,1]",
        "explanation": "Explanation: "
      },
      {
        "input": "Input: nums = [2,1]",
        "output": "Output: [2,1]",
        "explanation": "Explanation: "
      }
    ],
    "topics": [
      "Array",
      "Sorting"
    ],
    "difficulty": "Easy",
    "constraints": [
      "1 <= nums.length <= 100",
      "1 <= nums[i] <= 100"
    ],
    "hints": [
      "Try to separate the elements at odd indices from the elements at even indices.",
      "Sort the two groups of elements individually.",
      "Combine them to form the resultant array."
    ]
  },
  {
    "title": "Count Good Triplets in an Array",
    "description": "You are given two 0-indexed arrays nums1 and nums2 of length n, both of which are permutations of [0, 1, ..., n - 1].\nA good triplet is a set of 3 distinct values which are present in increasing order by position both in nums1 and nums2. In other words, if we consider pos1v as the index of the value v in nums1 and pos2v as the index of the value v in nums2, then a good triplet will be a set (x, y, z) where 0 <= x, y, z <= n - 1, such that pos1x < pos1y < pos1z and pos2x < pos2y < pos2z.\nReturn the total number of good triplets.\n \n",
    "examples": [
      {
        "input": "Input: nums1 = [2,0,1,3], nums2 = [0,1,2,3]",
        "output": "Output: 1",
        "explanation": "Explanation: "
      },
      {
        "input": "Input: nums1 = [4,0,1,3,2], nums2 = [4,1,0,2,3]",
        "output": "Output: 4",
        "explanation": "Explanation: The 4 good triplets are (4,0,3), (4,0,2), (4,1,3), and (4,1,2)."
      }
    ],
    "topics": [
      "Array",
      "Binary Search",
      "Divide and Conquer",
      "Binary Indexed Tree",
      "Segment Tree",
      "Merge Sort",
      "Ordered Set"
    ],
    "difficulty": "Hard",
    "constraints": [
      "n == nums1.length == nums2.length",
      "3 <= n <= 105",
      "0 <= nums1[i], nums2[i] <= n - 1",
      "nums1 and nums2 are permutations of [0, 1, ..., n - 1]."
    ],
    "hints": [
      "For every value y, how can you find the number of values x  (0 ≤ x, y ≤ n - 1) such that x appears before y in both of the arrays?",
      "Similarly, for every value y, try finding the number of values z (0 ≤ y, z ≤ n - 1) such that z appears after y in both of the arrays.",
      "Now, for every value y, count the number of good triplets that can be formed if y is considered as the middle element."
    ]
  },
  {
    "title": "Maximum Split of Positive Even Integers",
    "description": "You are given an integer finalSum. Split it into a sum of a maximum number of unique positive even integers.\n\nFor example, given finalSum = 12, the following splits are valid (unique positive even integers summing up to finalSum): (12), (2 + 10), (2 + 4 + 6), and (4 + 8). Among them, (2 + 4 + 6) contains the maximum number of integers. Note that finalSum cannot be split into (2 + 2 + 4 + 4) as all the numbers should be unique.\n\nReturn a list of integers that represent a valid split containing a maximum number of integers. If no valid split exists for finalSum, return an empty list. You may return the integers in any order.\n \n",
    "examples": [
      {
        "input": "Input: finalSum = 12",
        "output": "Output: [2,4,6]",
        "explanation": "Explanation: The following are valid splits: (12), (2 + 10), (2 + 4 + 6), and (4 + 8)."
      },
      {
        "input": "Input: finalSum = 7",
        "output": "Output: []",
        "explanation": "Explanation: There are no valid splits for the given finalSum."
      },
      {
        "input": "Input: finalSum = 28",
        "output": "Output: [6,8,2,12]",
        "explanation": "Explanation: The following are valid splits: (2 + 26), (6 + 8 + 2 + 12), and (4 + 24). "
      }
    ],
    "topics": [
      "Math",
      "Backtracking",
      "Greedy"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= finalSum <= 1010"
    ],
    "hints": [
      "First, check if finalSum is divisible by 2. If it isn’t, then we cannot split it into even integers.",
      "Let k be the number of elements in our split. As we want the maximum number of elements, we should try to use the first k - 1 even elements to grow our sum as slowly as possible.",
      "Thus, we find the maximum sum of the first k - 1 even elements which is less than finalSum.",
      "We then add the difference over to the kth element."
    ]
  },
  {
    "title": "Find Three Consecutive Integers That Sum to a Given Number",
    "description": "Given an integer num, return three consecutive integers (as a sorted array) that sum to num. If num cannot be expressed as the sum of three consecutive integers, return an empty array.\n \n",
    "examples": [
      {
        "input": "Input: num = 33",
        "output": "Output: [10,11,12]",
        "explanation": "Explanation: 33 can be expressed as 10 + 11 + 12 = 33."
      },
      {
        "input": "Input: num = 4",
        "output": "Output: []",
        "explanation": "Explanation: There is no way to express 4 as the sum of 3 consecutive integers."
      }
    ],
    "topics": [
      "Math",
      "Simulation"
    ],
    "difficulty": "Medium",
    "constraints": [
      "0 <= num <= 1015"
    ],
    "hints": [
      "Notice that if a solution exists, we can represent them as x-1, x, x+1. What does this tell us about the number?",
      "Notice the sum of the numbers will be 3x. Can you solve for x?"
    ]
  },
  {
    "title": "Count Equal and Divisible Pairs in an Array",
    "description": "Given a 0-indexed integer array nums of length n and an integer k, return the number of pairs (i, j) where 0 <= i < j < n, such that nums[i] == nums[j] and (i * j) is divisible by k.\n \n",
    "examples": [
      {
        "input": "Input: nums = [3,1,2,2,2,1,3], k = 2",
        "output": "Output: 4",
        "explanation": ""
      },
      {
        "input": "Input: nums = [1,2,3,4], k = 1",
        "output": "Output: 0",
        "explanation": "Explanation: Since no value in nums is repeated, there are no pairs (i,j) that meet all the requirements."
      }
    ],
    "topics": [
      "Array"
    ],
    "difficulty": "Easy",
    "constraints": [
      "1 <= nums.length <= 100",
      "1 <= nums[i], k <= 100"
    ],
    "hints": [
      "For every possible pair of indices (i, j) where i < j, check if it satisfies the given conditions."
    ]
  },
  {
    "title": "Groups of Strings",
    "description": "You are given a 0-indexed array of strings words. Each string consists of lowercase English letters only. No letter occurs more than once in any string of words.\nTwo strings s1 and s2 are said to be connected if the set of letters of s2 can be obtained from the set of letters of s1 by any one of the following operations:\n\nAdding exactly one letter to the set of the letters of s1.\nDeleting exactly one letter from the set of the letters of s1.\nReplacing exactly one letter from the set of the letters of s1 with any letter, including itself.\n\nThe array words can be divided into one or more non-intersecting groups. A string belongs to a group if any one of the following is true:\n\nIt is connected to at least one other string of the group.\nIt is the only string present in the group.\n\nNote that the strings in words should be grouped in such a manner that a string belonging to a group cannot be connected to a string present in any other group. It can be proved that such an arrangement is always unique.\nReturn an array ans of size 2 where:\n\nans[0] is the maximum number of groups words can be divided into, and\nans[1] is the size of the largest group.\n\n \n",
    "examples": [
      {
        "input": "Input: words = [\"a\",\"b\",\"ab\",\"cde\"]",
        "output": "Output: [2,3]",
        "explanation": ""
      },
      {
        "input": "Input: words = [\"a\",\"ab\",\"abc\"]",
        "output": "Output: [1,3]",
        "explanation": ""
      }
    ],
    "topics": [
      "String",
      "Bit Manipulation",
      "Union Find"
    ],
    "difficulty": "Hard",
    "constraints": [
      "1 <= words.length <= 2 * 104",
      "1 <= words[i].length <= 26",
      "words[i] consists of lowercase English letters only.",
      "No letter occurs more than once in words[i]."
    ],
    "hints": [
      "Can we build a graph from words, where there exists an edge between nodes i and j if words[i] and words[j] are connected?",
      "The problem now boils down to finding the total number of components and the size of the largest component in the graph.",
      "How can we use bit masking to reduce the search space while adding edges to node i?"
    ]
  },
  {
    "title": "Find Substring With Given Hash Value",
    "description": "The hash of a 0-indexed string s of length k, given integers p and m, is computed using the following function:\n\nhash(s, p, m) = (val(s[0]) * p0 + val(s[1]) * p1 + ... + val(s[k-1]) * pk-1) mod m.\n\nWhere val(s[i]) represents the index of s[i] in the alphabet from val('a') = 1 to val('z') = 26.\nYou are given a string s and the integers power, modulo, k, and hashValue. Return sub, the first substring of s of length k such that hash(sub, power, modulo) == hashValue.\nThe test cases will be generated such that an answer always exists.\nA substring is a contiguous non-empty sequence of characters within a string.\n \n",
    "examples": [
      {
        "input": "Input: s = \"leetcode\", power = 7, modulo = 20, k = 2, hashValue = 0",
        "output": "Output: \"ee\"",
        "explanation": "Explanation: The hash of \"ee\" can be computed to be hash(\"ee\", 7, 20) = (5 * 1 + 5 * 7) mod 20 = 40 mod 20 = 0. "
      },
      {
        "input": "Input: s = \"fbxzaad\", power = 31, modulo = 100, k = 3, hashValue = 32",
        "output": "Output: \"fbx\"",
        "explanation": "Explanation: The hash of \"fbx\" can be computed to be hash(\"fbx\", 31, 100) = (6 * 1 + 2 * 31 + 24 * 312) mod 100 = 23132 mod 100 = 32. "
      }
    ],
    "topics": [
      "String",
      "Sliding Window",
      "Rolling Hash",
      "Hash Function"
    ],
    "difficulty": "Hard",
    "constraints": [
      "1 <= k <= s.length <= 2 * 104",
      "1 <= power, modulo <= 109",
      "0 <= hashValue < modulo",
      "s consists of lowercase English letters only.",
      "The test cases are generated such that an answer always exists."
    ],
    "hints": [
      "How can we update the hash value efficiently while iterating instead of recalculating it each time?",
      "Use the rolling hash method."
    ]
  },
  {
    "title": "Keep Multiplying Found Values by Two",
    "description": "You are given an array of integers nums. You are also given an integer original which is the first number that needs to be searched for in nums.\nYou then do the following steps:\n\nIf original is found in nums, multiply it by two (i.e., set original = 2 * original).\nOtherwise, stop the process.\nRepeat this process with the new number as long as you keep finding the number.\n\nReturn the final value of original.\n \n",
    "examples": [
      {
        "input": "Input: nums = [5,3,6,1,12], original = 3",
        "output": "Output: 24",
        "explanation": "Explanation: "
      },
      {
        "input": "Input: nums = [2,7,9], original = 4",
        "output": "Output: 4",
        "explanation": ""
      }
    ],
    "topics": [
      "Array",
      "Hash Table",
      "Sorting",
      "Simulation"
    ],
    "difficulty": "Easy",
    "constraints": [
      "1 <= nums.length <= 1000",
      "1 <= nums[i], original <= 1000"
    ],
    "hints": [
      "Repeatedly iterate through the array and check if the current value of original is in the array.",
      "If original is not found, stop and return its current value.",
      "Otherwise, multiply original by 2 and repeat the process.",
      "Use set data structure to check the existence faster."
    ]
  },
  {
    "title": "Maximum Good People Based on Statements",
    "description": "There are two types of persons:\n\nThe good person: The person who always tells the truth.\nThe bad person: The person who might tell the truth and might lie.\n\nYou are given a 0-indexed 2D integer array statements of size n x n that represents the statements made by n people about each other. More specifically, statements[i][j] could be one of the following:\n\n0 which represents a statement made by person i that person j is a bad person.\n1 which represents a statement made by person i that person j is a good person.\n2 represents that no statement is made by person i about person j.\n\nAdditionally, no person ever makes a statement about themselves. Formally, we have that statements[i][i] = 2 for all 0 <= i < n.\nReturn the maximum number of people who can be good based on the statements made by the n people.\n \n",
    "examples": [
      {
        "input": "Input: statements = [[2,1,2],[1,2,2],[2,0,2]]",
        "output": "Output: 2",
        "explanation": "Explanation: Each person makes a single statement."
      },
      {
        "input": "Input: statements = [[2,0],[0,2]]",
        "output": "Output: 1",
        "explanation": "Explanation: Each person makes a single statement."
      }
    ],
    "topics": [
      "Array",
      "Backtracking",
      "Bit Manipulation",
      "Enumeration"
    ],
    "difficulty": "Hard",
    "constraints": [
      "n == statements.length == statements[i].length",
      "2 <= n <= 15",
      "statements[i][j] is either 0, 1, or 2.",
      "statements[i][i] == 2"
    ],
    "hints": [
      "You should test every possible assignment of good and bad people, using a bitmask.",
      "In each bitmask, if the person i is good, then his statements should be consistent with the bitmask in order for the assignment to be valid.",
      "If the assignment is valid, count how many people are good and keep track of the maximum."
    ]
  },
  {
    "title": "Rearrange Array Elements by Sign",
    "description": "You are given a 0-indexed integer array nums of even length consisting of an equal number of positive and negative integers.\nYou should rearrange the elements of nums such that the modified array follows the given conditions:\n\nEvery consecutive pair of integers have opposite signs.\nFor all integers with the same sign, the order in which they were present in nums is preserved.\nThe rearranged array begins with a positive integer.\n\nReturn the modified array after rearranging the elements to satisfy the aforementioned conditions.\n \n",
    "examples": [
      {
        "input": "Input: nums = [3,1,-2,-5,2,-4]",
        "output": "Output: [3,-2,1,-5,2,-4]",
        "explanation": ""
      },
      {
        "input": "Input: nums = [-1,1]",
        "output": "Output: [1,-1]",
        "explanation": ""
      }
    ],
    "topics": [
      "Array",
      "Two Pointers",
      "Simulation"
    ],
    "difficulty": "Medium",
    "constraints": [
      "2 <= nums.length <= 2 * 105",
      "nums.length is even",
      "1 <= |nums[i]| <= 105",
      "nums consists of equal number of positive and negative integers."
    ],
    "hints": [
      "Divide the array into two parts- one comprising of only positive integers and the other of negative integers.",
      "Merge the two parts to get the resultant array."
    ]
  },
  {
    "title": "Find All Lonely Numbers in the Array",
    "description": "You are given an integer array nums. A number x is lonely when it appears only once, and no adjacent numbers (i.e. x + 1 and x - 1) appear in the array.\nReturn all lonely numbers in nums. You may return the answer in any order.\n \n",
    "examples": [
      {
        "input": "Input: nums = [10,6,5,8]",
        "output": "Output: [10,8]",
        "explanation": "Explanation: "
      },
      {
        "input": "Input: nums = [1,3,5,3]",
        "output": "Output: [1,5]",
        "explanation": "Explanation: "
      }
    ],
    "topics": [
      "Array",
      "Hash Table",
      "Counting"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= nums.length <= 105",
      "0 <= nums[i] <= 106"
    ],
    "hints": [
      "For a given element x, how can you quickly check if x - 1 and x + 1 are present in the array without reiterating through the entire array?",
      "Use a set or a hash map."
    ]
  },
  {
    "title": "Count Elements With Strictly Smaller and Greater Elements ",
    "description": "Given an integer array nums, return the number of elements that have both a strictly smaller and a strictly greater element appear in nums.\n \n",
    "examples": [
      {
        "input": "Input: nums = [11,7,2,15]",
        "output": "Output: 2",
        "explanation": "Explanation: The element 7 has the element 2 strictly smaller than it and the element 11 strictly greater than it."
      },
      {
        "input": "Input: nums = [-3,3,3,90]",
        "output": "Output: 2",
        "explanation": "Explanation: The element 3 has the element -3 strictly smaller than it and the element 90 strictly greater than it."
      }
    ],
    "topics": [
      "Array",
      "Sorting"
    ],
    "difficulty": "Easy",
    "constraints": [
      "1 <= nums.length <= 100",
      "-105 <= nums[i] <= 105"
    ],
    "hints": [
      "All the elements in the array should be counted except for the minimum and maximum elements.",
      "If the array has n elements, the answer will be n - count(min(nums)) - count(max(nums))",
      "This formula will not work in case the array has all the elements equal, why?"
    ]
  },
  {
    "title": "Minimum Difference in Sums After Removal of Elements",
    "description": "You are given a 0-indexed integer array nums consisting of 3 * n elements.\nYou are allowed to remove any subsequence of elements of size exactly n from nums. The remaining 2 * n elements will be divided into two equal parts:\n\nThe first n elements belonging to the first part and their sum is sumfirst.\nThe next n elements belonging to the second part and their sum is sumsecond.\n\nThe difference in sums of the two parts is denoted as sumfirst - sumsecond.\n\nFor example, if sumfirst = 3 and sumsecond = 2, their difference is 1.\nSimilarly, if sumfirst = 2 and sumsecond = 3, their difference is -1.\n\nReturn the minimum difference possible between the sums of the two parts after the removal of n elements.\n \n",
    "examples": [
      {
        "input": "Input: nums = [3,1,2]",
        "output": "Output: -1",
        "explanation": "Explanation: Here, nums has 3 elements, so n = 1. "
      },
      {
        "input": "Input: nums = [7,9,5,8,1,3]",
        "output": "Output: 1",
        "explanation": "Explanation: Here n = 2. So we must remove 2 elements and divide the remaining array into two parts containing two elements each."
      }
    ],
    "topics": [
      "Array",
      "Dynamic Programming",
      "Heap (Priority Queue)"
    ],
    "difficulty": "Hard",
    "constraints": [
      "nums.length == 3 * n",
      "1 <= n <= 105",
      "1 <= nums[i] <= 105"
    ],
    "hints": [
      "The lowest possible difference can be obtained when the sum of the first n elements in the resultant array is minimum, and the sum of the next n elements is maximum.",
      "For every index i, think about how you can find the minimum possible sum of n elements with indices lesser or equal to i, if possible.",
      "Similarly, for every index i, try to find the maximum possible sum of n elements with indices greater or equal to i, if possible.",
      "Now for all indices, check if we can consider it as the partitioning index and hence find the answer."
    ]
  },
  {
    "title": "Minimum Cost to Set Cooking Time",
    "description": "A generic microwave supports cooking times for:\n\nat least 1 second.\nat most 99 minutes and 99 seconds.\n\nTo set the cooking time, you push at most four digits. The microwave normalizes what you push as four digits by prepending zeroes. It interprets the first two digits as the minutes and the last two digits as the seconds. It then adds them up as the cooking time. For example,\n\nYou push 9 5 4 (three digits). It is normalized as 0954 and interpreted as 9 minutes and 54 seconds.\nYou push 0 0 0 8 (four digits). It is interpreted as 0 minutes and 8 seconds.\nYou push 8 0 9 0. It is interpreted as 80 minutes and 90 seconds.\nYou push 8 1 3 0. It is interpreted as 81 minutes and 30 seconds.\n\nYou are given integers startAt, moveCost, pushCost, and targetSeconds. Initially, your finger is on the digit startAt. Moving the finger above any specific digit costs moveCost units of fatigue. Pushing the digit below the finger once costs pushCost units of fatigue.\nThere can be multiple ways to set the microwave to cook for targetSeconds seconds but you are interested in the way with the minimum cost.\nReturn the minimum cost to set targetSeconds seconds of cooking time.\nRemember that one minute consists of 60 seconds.\n \n",
    "examples": [
      {
        "input": "Input: startAt = 1, moveCost = 2, pushCost = 1, targetSeconds = 600",
        "output": "Output: 6",
        "explanation": "Explanation: The following are the possible ways to set the cooking time."
      },
      {
        "input": "Input: startAt = 0, moveCost = 1, pushCost = 2, targetSeconds = 76",
        "output": "Output: 6",
        "explanation": "Explanation: The optimal way is to push two digits: 7 6, interpreted as 76 seconds."
      }
    ],
    "topics": [
      "Math",
      "Enumeration"
    ],
    "difficulty": "Medium",
    "constraints": [
      "0 <= startAt <= 9",
      "1 <= moveCost, pushCost <= 105",
      "1 <= targetSeconds <= 6039"
    ],
    "hints": [
      "Define a separate function Cost(mm, ss) where 0 <= mm <= 99 and 0 <= ss <= 99. This function should calculate the cost of setting the cocking time to mm minutes and ss seconds",
      "The range of the minutes is small (i.e., [0, 99]), how can you use that?",
      "For every mm in [0, 99], calculate the needed ss to make mm:ss equal to targetSeconds and minimize the cost of setting the cocking time to mm:ss",
      "Be careful in some cases when ss is not in the valid range [0, 99]."
    ]
  },
  {
    "title": "Partition Array According to Given Pivot",
    "description": "You are given a 0-indexed integer array nums and an integer pivot. Rearrange nums such that the following conditions are satisfied:\n\nEvery element less than pivot appears before every element greater than pivot.\nEvery element equal to pivot appears in between the elements less than and greater than pivot.\nThe relative order of the elements less than pivot and the elements greater than pivot is maintained.\n\t\nMore formally, consider every pi, pj where pi is the new position of the ith element and pj is the new position of the jth element. For elements less than pivot, if i < j and nums[i] < pivot and nums[j] < pivot, then pi < pj. Similarly for elements greater than pivot, if i < j and nums[i] > pivot and nums[j] > pivot, then pi < pj.\n\n\n\nReturn nums after the rearrangement.\n \n",
    "examples": [
      {
        "input": "Input: nums = [9,12,5,10,14,3,10], pivot = 10",
        "output": "Output: [9,5,3,10,10,12,14]",
        "explanation": "Explanation: "
      },
      {
        "input": "Input: nums = [-3,4,3,2], pivot = 2",
        "output": "Output: [-3,2,4,3]",
        "explanation": "Explanation: "
      }
    ],
    "topics": [
      "Array",
      "Two Pointers",
      "Simulation"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= nums.length <= 105",
      "-106 <= nums[i] <= 106",
      "pivot equals to an element of nums."
    ],
    "hints": [
      "Could you put the elements smaller than the pivot and greater than the pivot in a separate list as in the sequence that they occur?",
      "With the separate lists generated, could you then generate the result?"
    ]
  },
  {
    "title": "Minimum Sum of Four Digit Number After Splitting Digits",
    "description": "You are given a positive integer num consisting of exactly four digits. Split num into two new integers new1 and new2 by using the digits found in num. Leading zeros are allowed in new1 and new2, and all the digits found in num must be used.\n\nFor example, given num = 2932, you have the following digits: two 2's, one 9 and one 3. Some of the possible pairs [new1, new2] are [22, 93], [23, 92], [223, 9] and [2, 329].\n\nReturn the minimum possible sum of new1 and new2.\n \n",
    "examples": [
      {
        "input": "Input: num = 2932",
        "output": "Output: 52",
        "explanation": "Explanation: Some possible pairs [new1, new2] are [29, 23], [223, 9], etc."
      },
      {
        "input": "Input: num = 4009",
        "output": "Output: 13",
        "explanation": "Explanation: Some possible pairs [new1, new2] are [0, 49], [490, 0], etc. "
      }
    ],
    "topics": [
      "Math",
      "Greedy",
      "Sorting"
    ],
    "difficulty": "Easy",
    "constraints": [
      "1000 <= num <= 9999"
    ],
    "hints": [
      "Notice that the most optimal way to obtain the minimum possible sum using 4 digits is by summing up two 2-digit numbers.",
      "We can use the two smallest digits out of the four as the digits found in the tens place respectively.",
      "Similarly, we use the final 2 larger digits as the digits found in the ones place."
    ]
  },
  {
    "title": "Maximum Running Time of N Computers",
    "description": "You have n computers. You are given the integer n and a 0-indexed integer array batteries where the ith battery can run a computer for batteries[i] minutes. You are interested in running all n computers simultaneously using the given batteries.\nInitially, you can insert at most one battery into each computer. After that and at any integer time moment, you can remove a battery from a computer and insert another battery any number of times. The inserted battery can be a totally new battery or a battery from another computer. You may assume that the removing and inserting processes take no time.\nNote that the batteries cannot be recharged.\nReturn the maximum number of minutes you can run all the n computers simultaneously.\n \n",
    "examples": [
      {
        "input": "Input: n = 2, batteries = [3,3,3]",
        "output": "Output: 4",
        "explanation": "Explanation: "
      },
      {
        "input": "Input: n = 2, batteries = [1,1,1,1]",
        "output": "Output: 2",
        "explanation": "Explanation: "
      }
    ],
    "topics": [
      "Array",
      "Binary Search",
      "Greedy",
      "Sorting"
    ],
    "difficulty": "Hard",
    "constraints": [
      "1 <= n <= batteries.length <= 105",
      "1 <= batteries[i] <= 109"
    ],
    "hints": [
      "For a given running time, can you determine if it is possible to run all n computers simultaneously?",
      "Try to use Binary Search to find the maximal running time"
    ]
  },
  {
    "title": "Solving Questions With Brainpower",
    "description": "You are given a 0-indexed 2D integer array questions where questions[i] = [pointsi, brainpoweri].\nThe array describes the questions of an exam, where you have to process the questions in order (i.e., starting from question 0) and make a decision whether to solve or skip each question. Solving question i will earn you pointsi points but you will be unable to solve each of the next brainpoweri questions. If you skip question i, you get to make the decision on the next question.\n\nFor example, given questions = [[3, 2], [4, 3], [4, 4], [2, 5]]:\n\n\t\nIf question 0 is solved, you will earn 3 points but you will be unable to solve questions 1 and 2.\nIf instead, question 0 is skipped and question 1 is solved, you will earn 4 points but you will be unable to solve questions 2 and 3.\n\n\n\nReturn the maximum points you can earn for the exam.\n \n",
    "examples": [
      {
        "input": "Input: questions = [[3,2],[4,3],[4,4],[2,5]]",
        "output": "Output: 5",
        "explanation": "Explanation: The maximum points can be earned by solving questions 0 and 3."
      },
      {
        "input": "Input: questions = [[1,1],[2,2],[3,3],[4,4],[5,5]]",
        "output": "Output: 7",
        "explanation": "Explanation: The maximum points can be earned by solving questions 1 and 4."
      }
    ],
    "topics": [
      "Array",
      "Dynamic Programming"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= questions.length <= 105",
      "questions[i].length == 2",
      "1 <= pointsi, brainpoweri <= 105"
    ],
    "hints": [
      "For each question, we can either solve it or skip it. How can we use Dynamic Programming to decide the most optimal option for each problem?",
      "We store for each question the maximum points we can earn if we started the exam on that question.",
      "If we skip a question, then the answer for it will be the same as the answer for the next question.",
      "If we solve a question, then the answer for it will be the points of the current question plus the answer for the next solvable question.",
      "The maximum of these two values will be the answer to the current question."
    ]
  },
  {
    "title": "All Divisions With the Highest Score of a Binary Array",
    "description": "You are given a 0-indexed binary array nums of length n. nums can be divided at index i (where 0 <= i <= n) into two arrays (possibly empty) numsleft and numsright:\n\nnumsleft has all the elements of nums between index 0 and i - 1 (inclusive), while numsright has all the elements of nums between index i and n - 1 (inclusive).\nIf i == 0, numsleft is empty, while numsright has all the elements of nums.\nIf i == n, numsleft has all the elements of nums, while numsright is empty.\n\nThe division score of an index i is the sum of the number of 0's in numsleft and the number of 1's in numsright.\nReturn all distinct indices that have the highest possible division score. You may return the answer in any order.\n \n",
    "examples": [
      {
        "input": "Input: nums = [0,0,1,0]",
        "output": "Output: [2,4]",
        "explanation": "Explanation: Division at index"
      },
      {
        "input": "Input: nums = [0,0,0]",
        "output": "Output: [3]",
        "explanation": "Explanation: Division at index"
      },
      {
        "input": "Input: nums = [1,1]",
        "output": "Output: [0]",
        "explanation": "Explanation: Division at index"
      }
    ],
    "topics": [
      "Array"
    ],
    "difficulty": "Medium",
    "constraints": [
      "n == nums.length",
      "1 <= n <= 105",
      "nums[i] is either 0 or 1."
    ],
    "hints": [
      "When you iterate the array, maintain the number of zeros and ones on the left side. Can you quickly calculate the number of ones on the right side?",
      "The number of ones on the right side equals the number of ones in the whole array minus the number of ones on the left side.",
      "Alternatively, you can quickly calculate it by using a prefix sum array."
    ]
  },
  {
    "title": "Divide a String Into Groups of Size k",
    "description": "A string s can be partitioned into groups of size k using the following procedure:\n\nThe first group consists of the first k characters of the string, the second group consists of the next k characters of the string, and so on. Each character can be a part of exactly one group.\nFor the last group, if the string does not have k characters remaining, a character fill is used to complete the group.\n\nNote that the partition is done so that after removing the fill character from the last group (if it exists) and concatenating all the groups in order, the resultant string should be s.\nGiven the string s, the size of each group k and the character fill, return a string array denoting the composition of every group s has been divided into, using the above procedure.\n \n",
    "examples": [
      {
        "input": "Input: s = \"abcdefghi\", k = 3, fill = \"x\"",
        "output": "Output: [\"abc\",\"def\",\"ghi\"]",
        "explanation": ""
      },
      {
        "input": "Input: s = \"abcdefghij\", k = 3, fill = \"x\"",
        "output": "Output: [\"abc\",\"def\",\"ghi\",\"jxx\"]",
        "explanation": ""
      }
    ],
    "topics": [
      "String",
      "Simulation"
    ],
    "difficulty": "Easy",
    "constraints": [
      "1 <= s.length <= 100",
      "s consists of lowercase English letters only.",
      "1 <= k <= 100",
      "fill is a lowercase English letter."
    ],
    "hints": [
      "Using the length of the string and k, can you count the number of groups the string can be divided into?",
      "Try completing each group using characters from the string. If there aren’t enough characters for the last group, use the fill character to complete the group."
    ]
  },
  {
    "title": "Earliest Possible Day of Full Bloom",
    "description": "You have n flower seeds. Every seed must be planted first before it can begin to grow, then bloom. Planting a seed takes time and so does the growth of a seed. You are given two 0-indexed integer arrays plantTime and growTime, of length n each:\n\nplantTime[i] is the number of full days it takes you to plant the ith seed. Every day, you can work on planting exactly one seed. You do not have to work on planting the same seed on consecutive days, but the planting of a seed is not complete until you have worked plantTime[i] days on planting it in total.\ngrowTime[i] is the number of full days it takes the ith seed to grow after being completely planted. After the last day of its growth, the flower blooms and stays bloomed forever.\n\nFrom the beginning of day 0, you can plant the seeds in any order.\nReturn the earliest possible day where all seeds are blooming.\n \n",
    "examples": [
      {
        "input": "Input: plantTime = [1,4,3], growTime = [2,3,1]",
        "output": "Output: 9",
        "explanation": "Explanation: The grayed out pots represent planting days, colored pots represent growing days, and the flower represents the day it blooms."
      },
      {
        "input": "Input: plantTime = [1,2,3,2], growTime = [2,1,2,1]",
        "output": "Output: 9",
        "explanation": "Explanation: The grayed out pots represent planting days, colored pots represent growing days, and the flower represents the day it blooms."
      },
      {
        "input": "Input: plantTime = [1], growTime = [1]",
        "output": "Output: 2",
        "explanation": "Explanation: On day 0, plant the 0th seed. The seed grows for 1 full day and blooms on day 2."
      }
    ],
    "topics": [
      "Array",
      "Greedy",
      "Sorting"
    ],
    "difficulty": "Hard",
    "constraints": [
      "n == plantTime.length == growTime.length",
      "1 <= n <= 105",
      "1 <= plantTime[i], growTime[i] <= 104"
    ],
    "hints": [
      "List the planting like the diagram above shows, where a row represents the timeline of a seed. A row i is above another row j if the last day planting seed i is ahead of the last day for seed j. Does it have any advantage to spend some days to plant seed j before completely planting seed i?",
      "No. It does not help seed j but could potentially delay the completion of seed i, resulting in a worse final answer. Remaining focused is a part of the optimal solution.",
      "Sort the seeds by their growTime in descending order. Can you prove why this strategy is the other part of the optimal solution? Note the bloom time of a seed is the sum of plantTime of all seeds preceding this seed plus the growTime of this seed.",
      "There is no way to improve this strategy. The seed to bloom last dominates the final answer. Exchanging the planting of this seed with another seed with either a larger or smaller growTime will result in a potentially worse answer."
    ]
  },
  {
    "title": "Count Words Obtained After Adding a Letter",
    "description": "You are given two 0-indexed arrays of strings startWords and targetWords. Each string consists of lowercase English letters only.\nFor each string in targetWords, check if it is possible to choose a string from startWords and perform a conversion operation on it to be equal to that from targetWords.\nThe conversion operation is described in the following two steps:\n\nAppend any lowercase letter that is not present in the string to its end.\n\n\t\nFor example, if the string is \"abc\", the letters 'd', 'e', or 'y' can be added to it, but not 'a'. If 'd' is added, the resulting string will be \"abcd\".\n\n\nRearrange the letters of the new string in any arbitrary order.\n\t\nFor example, \"abcd\" can be rearranged to \"acbd\", \"bacd\", \"cbda\", and so on. Note that it can also be rearranged to \"abcd\" itself.\n\n\n\nReturn the number of strings in targetWords that can be obtained by performing the operations on any string of startWords.\nNote that you will only be verifying if the string in targetWords can be obtained from a string in startWords by performing the operations. The strings in startWords do not actually change during this process.\n \n",
    "examples": [
      {
        "input": "Input: startWords = [\"ant\",\"act\",\"tack\"], targetWords = [\"tack\",\"act\",\"acti\"]",
        "output": "Output: 2",
        "explanation": ""
      },
      {
        "input": "Input: startWords = [\"ab\",\"a\"], targetWords = [\"abc\",\"abcd\"]",
        "output": "Output: 1",
        "explanation": ""
      }
    ],
    "topics": [
      "Array",
      "Hash Table",
      "String",
      "Bit Manipulation",
      "Sorting"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= startWords.length, targetWords.length <= 5 * 104",
      "1 <= startWords[i].length, targetWords[j].length <= 26",
      "Each string of startWords and targetWords consists of lowercase English letters only.",
      "No letter occurs more than once in any string of startWords or targetWords."
    ],
    "hints": [
      "Which data structure can be used to efficiently check if a string exists in startWords?",
      "After appending a letter, all letters of a string can be rearranged in any possible way. How can we use this to reduce our search space while checking if a string in targetWords can be obtained from a string in startWords?"
    ]
  },
  {
    "title": "Minimum Swaps to Group All 1's Together II",
    "description": "A swap is defined as taking two distinct positions in an array and swapping the values in them.\nA circular array is defined as an array where we consider the first element and the last element to be adjacent.\nGiven a binary circular array nums, return the minimum number of swaps required to group all 1's present in the array together at any location.\n \n",
    "examples": [
      {
        "input": "Input: nums = [0,1,0,1,1,0,0]",
        "output": "Output: 1",
        "explanation": "Explanation: Here are a few of the ways to group all the 1's together:"
      },
      {
        "input": "Input: nums = [0,1,1,1,0,0,1,1,0]",
        "output": "Output: 2",
        "explanation": "Explanation: Here are a few of the ways to group all the 1's together:"
      },
      {
        "input": "Input: nums = [1,1,0,0,1]",
        "output": "Output: 0",
        "explanation": "Explanation: All the 1's are already grouped together due to the circular property of the array."
      }
    ],
    "topics": [
      "Array",
      "Sliding Window"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= nums.length <= 105",
      "nums[i] is either 0 or 1."
    ],
    "hints": [
      "Notice that the number of 1’s to be grouped together is fixed. It is the number of 1's the whole array has.",
      "Call this number total. We should then check for every subarray of size total (possibly wrapped around), how many swaps are required to have the subarray be all 1’s.",
      "The number of swaps required is the number of 0’s in the subarray.",
      "To eliminate the circular property of the array, we can append the original array to itself. Then, we check each subarray of length total.",
      "How do we avoid recounting the number of 0’s in the subarray each time? The Sliding Window technique can help."
    ]
  },
  {
    "title": "Check if Every Row and Column Contains All Numbers",
    "description": "An n x n matrix is valid if every row and every column contains all the integers from 1 to n (inclusive).\nGiven an n x n integer matrix matrix, return true if the matrix is valid. Otherwise, return false.\n \n",
    "examples": [
      {
        "input": "Input: matrix = [[1,2,3],[3,1,2],[2,3,1]]",
        "output": "Output: true",
        "explanation": "Explanation: In this case, n = 3, and every row and column contains the numbers 1, 2, and 3."
      },
      {
        "input": "Input: matrix = [[1,1,1],[1,2,3],[1,2,3]]",
        "output": "Output: false",
        "explanation": "Explanation: In this case, n = 3, but the first row and the first column do not contain the numbers 2 or 3."
      }
    ],
    "topics": [
      "Array",
      "Hash Table",
      "Matrix"
    ],
    "difficulty": "Easy",
    "constraints": [
      "n == matrix.length == matrix[i].length",
      "1 <= n <= 100",
      "1 <= matrix[i][j] <= n"
    ],
    "hints": [
      "Use for loops to check each row for every number from 1 to n. Similarly, do the same for each column.",
      "For each check, you can keep a set of the unique elements in the checked row/col. By the end of the check, the size of the set should be n."
    ]
  },
  {
    "title": "Number of Ways to Divide a Long Corridor",
    "description": "Along a long library corridor, there is a line of seats and decorative plants. You are given a 0-indexed string corridor of length n consisting of letters 'S' and 'P' where each 'S' represents a seat and each 'P' represents a plant.\nOne room divider has already been installed to the left of index 0, and another to the right of index n - 1. Additional room dividers can be installed. For each position between indices i - 1 and i (1 <= i <= n - 1), at most one divider can be installed.\nDivide the corridor into non-overlapping sections, where each section has exactly two seats with any number of plants. There may be multiple ways to perform the division. Two ways are different if there is a position with a room divider installed in the first way but not in the second way.\nReturn the number of ways to divide the corridor. Since the answer may be very large, return it modulo 109 + 7. If there is no way, return 0.\n \n",
    "examples": [
      {
        "input": "Input: corridor = \"SSPPSPS\"",
        "output": "Output: 3",
        "explanation": "Explanation: There are 3 different ways to divide the corridor."
      },
      {
        "input": "Input: corridor = \"PPSPSP\"",
        "output": "Output: 1",
        "explanation": "Explanation: There is only 1 way to divide the corridor, by not installing any additional dividers."
      },
      {
        "input": "Input: corridor = \"S\"",
        "output": "Output: 0",
        "explanation": "Explanation: There is no way to divide the corridor because there will always be a section that does not have exactly two seats."
      }
    ],
    "topics": [
      "Math",
      "String",
      "Dynamic Programming"
    ],
    "difficulty": "Hard",
    "constraints": [
      "n == corridor.length",
      "1 <= n <= 105",
      "corridor[i] is either 'S' or 'P'."
    ],
    "hints": [
      "Divide the corridor into segments. Each segment has two seats, starts precisely with one seat, and ends precisely with the other seat.",
      "How many dividers can you install between two adjacent segments? You must install precisely one. Otherwise, you would have created a section with not exactly two seats.",
      "If there are k plants between two adjacent segments, there are k + 1 positions (ways) you could install the divider you must install.",
      "The problem now becomes: Find the product of all possible positions between every two adjacent segments."
    ]
  },
  {
    "title": "K Highest Ranked Items Within a Price Range",
    "description": "You are given a 0-indexed 2D integer array grid of size m x n that represents a map of the items in a shop. The integers in the grid represent the following:\n\n0 represents a wall that you cannot pass through.\n1 represents an empty cell that you can freely move to and from.\nAll other positive integers represent the price of an item in that cell. You may also freely move to and from these item cells.\n\nIt takes 1 step to travel between adjacent grid cells.\nYou are also given integer arrays pricing and start where pricing = [low, high] and start = [row, col] indicates that you start at the position (row, col) and are interested only in items with a price in the range of [low, high] (inclusive). You are further given an integer k.\nYou are interested in the positions of the k highest-ranked items whose prices are within the given price range. The rank is determined by the first of these criteria that is different:\n\nDistance, defined as the length of the shortest path from the start (shorter distance has a higher rank).\nPrice (lower price has a higher rank, but it must be in the price range).\nThe row number (smaller row number has a higher rank).\nThe column number (smaller column number has a higher rank).\n\nReturn the k highest-ranked items within the price range sorted by their rank (highest to lowest). If there are fewer than k reachable items within the price range, return all of them.\n \n",
    "examples": [
      {
        "input": "Input: grid = [[1,2,0,1],[1,3,0,1],[0,2,5,1]], pricing = [2,5], start = [0,0], k = 3",
        "output": "Output: [[0,1],[1,1],[2,1]]",
        "explanation": "Explanation: You start at (0,0)."
      },
      {
        "input": "Input: grid = [[1,2,0,1],[1,3,3,1],[0,2,5,1]], pricing = [2,3], start = [2,3], k = 2",
        "output": "Output: [[2,1],[1,2]]",
        "explanation": "Explanation: You start at (2,3)."
      },
      {
        "input": "Input: grid = [[1,1,1],[0,0,1],[2,3,4]], pricing = [2,3], start = [0,0], k = 3",
        "output": "Output: [[2,1],[2,0]]",
        "explanation": "Explanation: You start at (0,0)."
      }
    ],
    "topics": [
      "Array",
      "Breadth-First Search",
      "Sorting",
      "Heap (Priority Queue)",
      "Matrix"
    ],
    "difficulty": "Medium",
    "constraints": [
      "m == grid.length",
      "n == grid[i].length",
      "1 <= m, n <= 105",
      "1 <= m * n <= 105",
      "0 <= grid[i][j] <= 105",
      "pricing.length == 2",
      "2 <= low <= high <= 105",
      "start.length == 2",
      "0 <= row <= m - 1",
      "0 <= col <= n - 1",
      "grid[row][col] > 0",
      "1 <= k <= m * n"
    ],
    "hints": [
      "Could you determine the rank of every item efficiently?",
      "We can perform a breadth-first search from the starting position and know the length of the shortest path from start to every item.",
      "Sort all the items according to the conditions listed in the problem, and return the first k (or all if less than k exist) items as the answer."
    ]
  },
  {
    "title": "Count the Hidden Sequences",
    "description": "You are given a 0-indexed array of n integers differences, which describes the differences between each pair of consecutive integers of a hidden sequence of length (n + 1). More formally, call the hidden sequence hidden, then we have that differences[i] = hidden[i + 1] - hidden[i].\nYou are further given two integers lower and upper that describe the inclusive range of values [lower, upper] that the hidden sequence can contain.\n\nFor example, given differences = [1, -3, 4], lower = 1, upper = 6, the hidden sequence is a sequence of length 4 whose elements are in between 1 and 6 (inclusive).\n\n\t\n[3, 4, 1, 5] and [4, 5, 2, 6] are possible hidden sequences.\n[5, 6, 3, 7] is not possible since it contains an element greater than 6.\n[1, 2, 3, 4] is not possible since the differences are not correct.\n\n\n\nReturn the number of possible hidden sequences there are. If there are no possible sequences, return 0.\n \n",
    "examples": [
      {
        "input": "Input: differences = [1,-3,4], lower = 1, upper = 6",
        "output": "Output: 2",
        "explanation": "Explanation: The possible hidden sequences are:"
      },
      {
        "input": "Input: differences = [3,-4,5,1,-2], lower = -4, upper = 5",
        "output": "Output: 4",
        "explanation": "Explanation: The possible hidden sequences are:"
      },
      {
        "input": "Input: differences = [4,-7,2], lower = 3, upper = 6",
        "output": "Output: 0",
        "explanation": "Explanation: There are no possible hidden sequences. Thus, we return 0."
      }
    ],
    "topics": [
      "Array",
      "Prefix Sum"
    ],
    "difficulty": "Medium",
    "constraints": [
      "n == differences.length",
      "1 <= n <= 105",
      "-105 <= differences[i] <= 105",
      "-105 <= lower <= upper <= 105"
    ],
    "hints": [
      "Fix the first element of the hidden sequence to any value x and ignore the given bounds. Notice that we can then determine all the other elements of the sequence by using the differences array.",
      "We will also be able to determine the difference between the minimum and maximum elements of the sequence. Notice that the value of x does not affect this.",
      "We now have the ‘range’ of the sequence (difference between min and max element), we can then calculate how many ways there are to fit this range into the given range of lower to upper.",
      "Answer is (upper - lower + 1) - (range of sequence)"
    ]
  },
  {
    "title": "Minimum Cost of Buying Candies With Discount",
    "description": "A shop is selling candies at a discount. For every two candies sold, the shop gives a third candy for free.\nThe customer can choose any candy to take away for free as long as the cost of the chosen candy is less than or equal to the minimum cost of the two candies bought.\n\nFor example, if there are 4 candies with costs 1, 2, 3, and 4, and the customer buys candies with costs 2 and 3, they can take the candy with cost 1 for free, but not the candy with cost 4.\n\nGiven a 0-indexed integer array cost, where cost[i] denotes the cost of the ith candy, return the minimum cost of buying all the candies.\n \n",
    "examples": [
      {
        "input": "Input: cost = [1,2,3]",
        "output": "Output: 5",
        "explanation": "Explanation: We buy the candies with costs 2 and 3, and take the candy with cost 1 for free."
      },
      {
        "input": "Input: cost = [6,5,7,9,2,2]",
        "output": "Output: 23",
        "explanation": "Explanation: The way in which we can get the minimum cost is described below:"
      },
      {
        "input": "Input: cost = [5,5]",
        "output": "Output: 10",
        "explanation": "Explanation: Since there are only 2 candies, we buy both of them. There is not a third candy we can take for free."
      }
    ],
    "topics": [
      "Array",
      "Greedy",
      "Sorting"
    ],
    "difficulty": "Easy",
    "constraints": [
      "1 <= cost.length <= 100",
      "1 <= cost[i] <= 100"
    ],
    "hints": [
      "If we consider costs from high to low, what is the maximum cost of a single candy that we can get for free?",
      "How can we generalize this approach to maximize the costs of the candies we get for free?",
      "Can “sorting” the array help us find the minimum cost?"
    ]
  },
  {
    "title": "Maximum Employees to Be Invited to a Meeting",
    "description": "A company is organizing a meeting and has a list of n employees, waiting to be invited. They have arranged for a large circular table, capable of seating any number of employees.\nThe employees are numbered from 0 to n - 1. Each employee has a favorite person and they will attend the meeting only if they can sit next to their favorite person at the table. The favorite person of an employee is not themself.\nGiven a 0-indexed integer array favorite, where favorite[i] denotes the favorite person of the ith employee, return the maximum number of employees that can be invited to the meeting.\n \n",
    "examples": [
      {
        "input": "Input: favorite = [2,2,1,2]",
        "output": "Output: 3",
        "explanation": ""
      },
      {
        "input": "Input: favorite = [1,2,0]",
        "output": "Output: 3",
        "explanation": "Explanation: "
      },
      {
        "input": "Input: favorite = [3,0,1,4,1]",
        "output": "Output: 4",
        "explanation": ""
      }
    ],
    "topics": [
      "Depth-First Search",
      "Graph",
      "Topological Sort"
    ],
    "difficulty": "Hard",
    "constraints": [
      "n == favorite.length",
      "2 <= n <= 105",
      "0 <= favorite[i] <= n - 1",
      "favorite[i] != i"
    ],
    "hints": [
      "From the given array favorite, create a graph where for every index i, there is a directed edge from favorite[i] to i. The graph will be a combination of cycles and chains of acyclic edges. Now, what are the ways in which we can choose employees to sit at the table?",
      "The first way by which we can choose employees is by selecting a cycle of the graph. It can be proven that in this case, the employees that do not lie in the cycle can never be seated at the table.",
      "The second way is by combining acyclic chains. At most two chains can be combined by a cycle of length 2, where each chain ends on one of the employees in the cycle."
    ]
  },
  {
    "title": "Destroying Asteroids",
    "description": "You are given an integer mass, which represents the original mass of a planet. You are further given an integer array asteroids, where asteroids[i] is the mass of the ith asteroid.\nYou can arrange for the planet to collide with the asteroids in any arbitrary order. If the mass of the planet is greater than or equal to the mass of the asteroid, the asteroid is destroyed and the planet gains the mass of the asteroid. Otherwise, the planet is destroyed.\nReturn true if all asteroids can be destroyed. Otherwise, return false.\n \n",
    "examples": [
      {
        "input": "Input: mass = 10, asteroids = [3,9,19,5,21]",
        "output": "Output: true",
        "explanation": "Explanation: One way to order the asteroids is [9,19,5,3,21]:"
      },
      {
        "input": "Input: mass = 5, asteroids = [4,9,23,4]",
        "output": "Output: false",
        "explanation": "Explanation: "
      }
    ],
    "topics": [
      "Array",
      "Greedy",
      "Sorting"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= mass <= 105",
      "1 <= asteroids.length <= 105",
      "1 <= asteroids[i] <= 105"
    ],
    "hints": [
      "Choosing the asteroid to collide with can be done greedily.",
      "If an asteroid will destroy the planet, then every bigger asteroid will also destroy the planet.",
      "You only need to check the smallest asteroid at each collision. If it will destroy the planet, then every other asteroid will also destroy the planet.",
      "Sort the asteroids in non-decreasing order by mass, then greedily try to collide with the asteroids in that order."
    ]
  },
  {
    "title": "Number of Laser Beams in a Bank",
    "description": "Anti-theft security devices are activated inside a bank. You are given a 0-indexed binary string array bank representing the floor plan of the bank, which is an m x n 2D matrix. bank[i] represents the ith row, consisting of '0's and '1's. '0' means the cell is empty, while'1' means the cell has a security device.\nThere is one laser beam between any two security devices if both conditions are met:\n\nThe two devices are located on two different rows: r1 and r2, where r1 < r2.\nFor each row i where r1 < i < r2, there are no security devices in the ith row.\n\nLaser beams are independent, i.e., one beam does not interfere nor join with another.\nReturn the total number of laser beams in the bank.\n \n",
    "examples": [
      {
        "input": "Input: bank = [\"011001\",\"000000\",\"010100\",\"001000\"]",
        "output": "Output: 8",
        "explanation": "Explanation: Between each of the following device pairs, there is one beam. In total, there are 8 beams:"
      },
      {
        "input": "Input: bank = [\"000\",\"111\",\"000\"]",
        "output": "Output: 0",
        "explanation": "Explanation: There does not exist two devices located on two different rows."
      }
    ],
    "topics": [
      "Array",
      "Math",
      "String",
      "Matrix"
    ],
    "difficulty": "Medium",
    "constraints": [
      "m == bank.length",
      "n == bank[i].length",
      "1 <= m, n <= 500",
      "bank[i][j] is either '0' or '1'."
    ],
    "hints": [
      "What is the commonality between security devices on the same row?",
      "Each device on the same row has the same number of beams pointing towards the devices on the next row with devices.",
      "If you were given an integer array where each element is the number of security devices on each row, can you solve it?",
      "Convert the input to such an array, skip any row with no security device, then find the sum of the product between adjacent elements."
    ]
  },
  {
    "title": "Check if All A's Appears Before All B's",
    "description": "Given a string s consisting of only the characters 'a' and 'b', return true if every 'a' appears before every 'b' in the string. Otherwise, return false.\n \n",
    "examples": [
      {
        "input": "Input: s = \"aaabbb\"",
        "output": "Output: true",
        "explanation": ""
      },
      {
        "input": "Input: s = \"abab\"",
        "output": "Output: false",
        "explanation": ""
      },
      {
        "input": "Input: s = \"bbb\"",
        "output": "Output: true",
        "explanation": ""
      }
    ],
    "topics": [
      "String"
    ],
    "difficulty": "Easy",
    "constraints": [
      "1 <= s.length <= 100",
      "s[i] is either 'a' or 'b'."
    ],
    "hints": [
      "You can check the opposite: check if there is a ‘b’ before an ‘a’. Then, negate and return that answer.",
      "s should not have any occurrences of “ba” as a substring."
    ]
  },
  {
    "title": "Recover the Original Array",
    "description": "Alice had a 0-indexed array arr consisting of n positive integers. She chose an arbitrary positive integer k and created two new 0-indexed integer arrays lower and higher in the following manner:\n\nlower[i] = arr[i] - k, for every index i where 0 <= i < n\nhigher[i] = arr[i] + k, for every index i where 0 <= i < n\n\nUnfortunately, Alice lost all three arrays. However, she remembers the integers that were present in the arrays lower and higher, but not the array each integer belonged to. Help Alice and recover the original array.\nGiven an array nums consisting of 2n integers, where exactly n of the integers were present in lower and the remaining in higher, return the original array arr. In case the answer is not unique, return any valid array.\nNote: The test cases are generated such that there exists at least one valid array arr.\n \n",
    "examples": [
      {
        "input": "Input: nums = [2,10,6,4,8,12]",
        "output": "Output: [3,7,11]",
        "explanation": ""
      },
      {
        "input": "Input: nums = [1,1,3,3]",
        "output": "Output: [2,2]",
        "explanation": ""
      },
      {
        "input": "Input: nums = [5,435]",
        "output": "Output: [220]",
        "explanation": ""
      }
    ],
    "topics": [
      "Array",
      "Hash Table",
      "Sorting",
      "Enumeration"
    ],
    "difficulty": "Hard",
    "constraints": [
      "2 * n == nums.length",
      "1 <= n <= 1000",
      "1 <= nums[i] <= 109",
      "The test cases are generated such that there exists at least one valid array arr."
    ],
    "hints": [
      "If we fix the value of k, how can we check if an original array exists for the fixed k?",
      "The smallest value of nums is obtained by subtracting k from the smallest value of the original array. How can we use this to reduce the search space for finding a valid k?",
      "You can compute every possible k by using the smallest value of nums (as lower[i]) against every other value in nums (as the corresponding higher[i]).",
      "For every computed k, greedily pair up the values in nums. This can be done sorting nums, then using a map to store previous values and searching that map for a corresponding lower[i] for the current nums[j] (as higher[i])."
    ]
  },
  {
    "title": "Intervals Between Identical Elements",
    "description": "You are given a 0-indexed array of n integers arr.\nThe interval between two elements in arr is defined as the absolute difference between their indices. More formally, the interval between arr[i] and arr[j] is |i - j|.\nReturn an array intervals of length n where intervals[i] is the sum of intervals between arr[i] and each element in arr with the same value as arr[i].\nNote: |x| is the absolute value of x.\n \n",
    "examples": [
      {
        "input": "Input: arr = [2,1,3,1,2,3,3]",
        "output": "Output: [4,2,7,2,4,4,5]",
        "explanation": ""
      },
      {
        "input": "Input: arr = [10,5,10,10]",
        "output": "Output: [5,0,3,4]",
        "explanation": ""
      }
    ],
    "topics": [
      "Array",
      "Hash Table",
      "Prefix Sum"
    ],
    "difficulty": "Medium",
    "constraints": [
      "n == arr.length",
      "1 <= n <= 105",
      "1 <= arr[i] <= 105"
    ],
    "hints": [
      "For each unique value found in the array, store a sorted list of indices of elements that have this value in the array.",
      "One way of doing this is to use a HashMap that maps the values to their list of indices. Update this mapping as you iterate through the array.",
      "Process each list of indices separately and get the sum of intervals for the elements of that value by utilizing prefix sums.",
      "For each element, keep track of the sum of indices of the identical elements that have come before and that will come after respectively. Use this to calculate the sum of intervals for that element to the rest of the elements with identical values."
    ]
  },
  {
    "title": "Execution of All Suffix Instructions Staying in a Grid",
    "description": "There is an n x n grid, with the top-left cell at (0, 0) and the bottom-right cell at (n - 1, n - 1). You are given the integer n and an integer array startPos where startPos = [startrow, startcol] indicates that a robot is initially at cell (startrow, startcol).\nYou are also given a 0-indexed string s of length m where s[i] is the ith instruction for the robot: 'L' (move left), 'R' (move right), 'U' (move up), and 'D' (move down).\nThe robot can begin executing from any ith instruction in s. It executes the instructions one by one towards the end of s but it stops if either of these conditions is met:\n\nThe next instruction will move the robot off the grid.\nThere are no more instructions left to execute.\n\nReturn an array answer of length m where answer[i] is the number of instructions the robot can execute if the robot begins executing from the ith instruction in s.\n \n",
    "examples": [
      {
        "input": "Input: n = 3, startPos = [0,1], s = \"RRDDLU\"",
        "output": "Output: [1,5,4,3,1,0]",
        "explanation": "Explanation: Starting from startPos and beginning execution from the ith instruction:"
      },
      {
        "input": "Input: n = 2, startPos = [1,1], s = \"LURD\"",
        "output": "Output: [4,1,0,0]",
        "explanation": ""
      },
      {
        "input": "Input: n = 1, startPos = [0,0], s = \"LRUD\"",
        "output": "Output: [0,0,0,0]",
        "explanation": "Explanation: No matter which instruction the robot begins execution from, it would move off the grid."
      }
    ],
    "topics": [
      "String",
      "Simulation"
    ],
    "difficulty": "Medium",
    "constraints": [
      "m == s.length",
      "1 <= n, m <= 500",
      "startPos.length == 2",
      "0 <= startrow, startcol < n",
      "s consists of 'L', 'R', 'U', and 'D'."
    ],
    "hints": [
      "The constraints are not very large. Can we simulate the execution by starting from each index of s?",
      "Before any of the stopping conditions is met, stop the simulation for that index and set the answer for that index."
    ]
  },
  {
    "title": "A Number After a Double Reversal",
    "description": "Reversing an integer means to reverse all its digits.\n\nFor example, reversing 2021 gives 1202. Reversing 12300 gives 321 as the leading zeros are not retained.\n\nGiven an integer num, reverse num to get reversed1, then reverse reversed1 to get reversed2. Return true if reversed2 equals num. Otherwise return false.\n \n",
    "examples": [
      {
        "input": "Input: num = 526",
        "output": "Output: true",
        "explanation": "Explanation: Reverse num to get 625, then reverse 625 to get 526, which equals num."
      },
      {
        "input": "Input: num = 1800",
        "output": "Output: false",
        "explanation": "Explanation: Reverse num to get 81, then reverse 81 to get 18, which does not equal num."
      },
      {
        "input": "Input: num = 0",
        "output": "Output: true",
        "explanation": "Explanation: Reverse num to get 0, then reverse 0 to get 0, which equals num."
      }
    ],
    "topics": [
      "Math"
    ],
    "difficulty": "Easy",
    "constraints": [
      "0 <= num <= 106"
    ],
    "hints": [
      "Other than the number 0 itself, any number that ends with 0 would lose some digits permanently when reversed."
    ]
  },
  {
    "title": "Longest Palindrome by Concatenating Two Letter Words",
    "description": "You are given an array of strings words. Each element of words consists of two lowercase English letters.\nCreate the longest possible palindrome by selecting some elements from words and concatenating them in any order. Each element can be selected at most once.\nReturn the length of the longest palindrome that you can create. If it is impossible to create any palindrome, return 0.\nA palindrome is a string that reads the same forward and backward.\n \n",
    "examples": [
      {
        "input": "Input: words = [\"lc\",\"cl\",\"gg\"]",
        "output": "Output: 6",
        "explanation": "Explanation: One longest palindrome is \"lc\" + \"gg\" + \"cl\" = \"lcggcl\", of length 6."
      },
      {
        "input": "Input: words = [\"ab\",\"ty\",\"yt\",\"lc\",\"cl\",\"ab\"]",
        "output": "Output: 8",
        "explanation": "Explanation: One longest palindrome is \"ty\" + \"lc\" + \"cl\" + \"yt\" = \"tylcclyt\", of length 8."
      },
      {
        "input": "Input: words = [\"cc\",\"ll\",\"xx\"]",
        "output": "Output: 2",
        "explanation": "Explanation: One longest palindrome is \"cc\", of length 2."
      }
    ],
    "topics": [
      "Array",
      "Hash Table",
      "String",
      "Greedy",
      "Counting"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= words.length <= 105",
      "words[i].length == 2",
      "words[i] consists of lowercase English letters."
    ],
    "hints": [
      "A palindrome must be mirrored over the center. Suppose we have a palindrome. If we prepend the word \"ab\" on the left, what must we append on the right to keep it a palindrome?",
      "We must append \"ba\" on the right. The number of times we can do this is the minimum of (occurrences of \"ab\") and (occurrences of \"ba\").",
      "For words that are already palindromes, e.g. \"aa\", we can prepend and append these in pairs as described in the previous hint. We can also use exactly one in the middle to form an even longer palindrome."
    ]
  },
  {
    "title": "Maximum Twin Sum of a Linked List",
    "description": "In a linked list of size n, where n is even, the ith node (0-indexed) of the linked list is known as the twin of the (n-1-i)th node, if 0 <= i <= (n / 2) - 1.\n\nFor example, if n = 4, then node 0 is the twin of node 3, and node 1 is the twin of node 2. These are the only nodes with twins for n = 4.\n\nThe twin sum is defined as the sum of a node and its twin.\nGiven the head of a linked list with even length, return the maximum twin sum of the linked list.\n \n",
    "examples": [
      {
        "input": "Input: head = [5,4,2,1]",
        "output": "Output: 6",
        "explanation": ""
      },
      {
        "input": "Input: head = [4,2,2,3]",
        "output": "Output: 7",
        "explanation": ""
      },
      {
        "input": "Input: head = [1,100000]",
        "output": "Output: 100001",
        "explanation": ""
      }
    ],
    "topics": [
      "Linked List",
      "Two Pointers",
      "Stack"
    ],
    "difficulty": "Medium",
    "constraints": [
      "The number of nodes in the list is an even integer in the range [2, 105].",
      "1 <= Node.val <= 105"
    ],
    "hints": [
      "How can \"reversing\" a part of the linked list help find the answer?",
      "We know that the nodes of the first half are twins of nodes in the second half, so try dividing the linked list in half and reverse the second half.",
      "How can two pointers be used to find every twin sum optimally?",
      "Use two different pointers pointing to the first nodes of the two halves of the linked list. The second pointer will point to the first node of the reversed half, which is the (n-1-i)th node in the original linked list. By moving both pointers forward at the same time, we find all twin sums."
    ]
  },
  {
    "title": "Capitalize the Title",
    "description": "You are given a string title consisting of one or more words separated by a single space, where each word consists of English letters. Capitalize the string by changing the capitalization of each word such that:\n\nIf the length of the word is 1 or 2 letters, change all letters to lowercase.\nOtherwise, change the first letter to uppercase and the remaining letters to lowercase.\n\nReturn the capitalized title.\n \n",
    "examples": [
      {
        "input": "Input: title = \"capiTalIze tHe titLe\"",
        "output": "Output: \"Capitalize The Title\"",
        "explanation": ""
      },
      {
        "input": "Input: title = \"First leTTeR of EACH Word\"",
        "output": "Output: \"First Letter of Each Word\"",
        "explanation": ""
      },
      {
        "input": "Input: title = \"i lOve leetcode\"",
        "output": "Output: \"i Love Leetcode\"",
        "explanation": ""
      }
    ],
    "topics": [
      "String"
    ],
    "difficulty": "Easy",
    "constraints": [
      "1 <= title.length <= 100",
      "title consists of words separated by a single space without any leading or trailing spaces.",
      "Each word consists of uppercase and lowercase English letters and is non-empty."
    ],
    "hints": [
      "Firstly, try to find all the words present in the string.",
      "On the basis of each word's lengths, simulate the process explained in Problem."
    ]
  },
  {
    "title": "Minimum Operations to Make the Array K-Increasing",
    "description": "You are given a 0-indexed array arr consisting of n positive integers, and a positive integer k.\nThe array arr is called K-increasing if arr[i-k] <= arr[i] holds for every index i, where k <= i <= n-1.\n\nFor example, arr = [4, 1, 5, 2, 6, 2] is K-increasing for k = 2 because:\n\n\t\narr[0] <= arr[2] (4 <= 5)\narr[1] <= arr[3] (1 <= 2)\narr[2] <= arr[4] (5 <= 6)\narr[3] <= arr[5] (2 <= 2)\n\n\nHowever, the same arr is not K-increasing for k = 1 (because arr[0] > arr[1]) or k = 3 (because arr[0] > arr[3]).\n\nIn one operation, you can choose an index i and change arr[i] into any positive integer.\nReturn the minimum number of operations required to make the array K-increasing for the given k.\n \n",
    "examples": [
      {
        "input": "Input: arr = [5,4,3,2,1], k = 1",
        "output": "Output: 4",
        "explanation": ""
      },
      {
        "input": "Input: arr = [4,1,5,2,6,2], k = 2",
        "output": "Output: 0",
        "explanation": ""
      },
      {
        "input": "Input: arr = [4,1,5,2,6,2], k = 3",
        "output": "Output: 2",
        "explanation": ""
      }
    ],
    "topics": [
      "Array",
      "Binary Search"
    ],
    "difficulty": "Hard",
    "constraints": [
      "1 <= arr.length <= 105",
      "1 <= arr[i], k <= arr.length"
    ],
    "hints": [
      "Can we divide the array into non-overlapping subsequences and simplify the problem?",
      "In the final array, arr[i-k] ≤ arr[i] should hold. We can use this to divide the array into at most k non-overlapping sequences, where arr[i] will belong to the (i%k)th sequence.",
      "Now our problem boils down to performing the minimum operations on each sequence such that it becomes non-decreasing. Our answer will be the sum of operations on each sequence.",
      "Which indices of a sequence should we not change in order to count the minimum operations? Can finding the longest non-decreasing subsequence of the sequence help?"
    ]
  },
  {
    "title": "Number of Smooth Descent Periods of a Stock",
    "description": "You are given an integer array prices representing the daily price history of a stock, where prices[i] is the stock price on the ith day.\nA smooth descent period of a stock consists of one or more contiguous days such that the price on each day is lower than the price on the preceding day by exactly 1. The first day of the period is exempted from this rule.\nReturn the number of smooth descent periods.\n \n",
    "examples": [
      {
        "input": "Input: prices = [3,2,1,4]",
        "output": "Output: 7",
        "explanation": "Explanation: There are 7 smooth descent periods:"
      },
      {
        "input": "Input: prices = [8,6,7,7]",
        "output": "Output: 4",
        "explanation": "Explanation: There are 4 smooth descent periods: [8], [6], [7], and [7]"
      },
      {
        "input": "Input: prices = [1]",
        "output": "Output: 1",
        "explanation": "Explanation: There is 1 smooth descent period: [1]"
      }
    ],
    "topics": [
      "Array",
      "Math",
      "Dynamic Programming"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= prices.length <= 105",
      "1 <= prices[i] <= 105"
    ],
    "hints": [
      "Any array is a series of adjacent longest possible smooth descent periods. For example, [5,3,2,1,7,6] is [5] + [3,2,1] + [7,6].",
      "Think of a 2-pointer approach to traverse the array and find each longest possible period.",
      "Suppose you found the longest possible period with a length of k. How many periods are within that period? How can you count them quickly? Think of the formula to calculate the sum of 1, 2, 3, ..., k."
    ]
  },
  {
    "title": "Adding Spaces to a String",
    "description": "You are given a 0-indexed string s and a 0-indexed integer array spaces that describes the indices in the original string where spaces will be added. Each space should be inserted before the character at the given index.\n\nFor example, given s = \"EnjoyYourCoffee\" and spaces = [5, 9], we place spaces before 'Y' and 'C', which are at indices 5 and 9 respectively. Thus, we obtain \"Enjoy Your Coffee\".\n\nReturn the modified string after the spaces have been added.\n \n",
    "examples": [
      {
        "input": "Input: s = \"LeetcodeHelpsMeLearn\", spaces = [8,13,15]",
        "output": "Output: \"Leetcode Helps Me Learn\"",
        "explanation": "Explanation: "
      },
      {
        "input": "Input: s = \"icodeinpython\", spaces = [1,5,7,9]",
        "output": "Output: \"i code in py thon\"",
        "explanation": ""
      },
      {
        "input": "Input: s = \"spacing\", spaces = [0,1,2,3,4,5,6]",
        "output": "Output: \" s p a c i n g\"",
        "explanation": ""
      }
    ],
    "topics": [
      "Array",
      "String",
      "Simulation"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= s.length <= 3 * 105",
      "s consists only of lowercase and uppercase English letters.",
      "1 <= spaces.length <= 3 * 105",
      "0 <= spaces[i] <= s.length - 1",
      "All the values of spaces are strictly increasing."
    ],
    "hints": [
      "Create a new string, initially empty, as the modified string. Iterate through the original string and append each character of the original string to the new string. However, each time you reach a character that requires a space before it, append a space before appending the character.",
      "Since the array of indices for the space locations is sorted, use a pointer to keep track of the next index to place a space. Only increment the pointer once a space has been appended.",
      "Ensure that your append operation can be done in O(1)."
    ]
  },
  {
    "title": "Find First Palindromic String in the Array",
    "description": "Given an array of strings words, return the first palindromic string in the array. If there is no such string, return an empty string \"\".\nA string is palindromic if it reads the same forward and backward.\n \n",
    "examples": [
      {
        "input": "Input: words = [\"abc\",\"car\",\"ada\",\"racecar\",\"cool\"]",
        "output": "Output: \"ada\"",
        "explanation": "Explanation: The first string that is palindromic is \"ada\"."
      },
      {
        "input": "Input: words = [\"notapalindrome\",\"racecar\"]",
        "output": "Output: \"racecar\"",
        "explanation": "Explanation: The first and only string that is palindromic is \"racecar\"."
      },
      {
        "input": "Input: words = [\"def\",\"ghi\"]",
        "output": "Output: \"\"",
        "explanation": "Explanation: There are no palindromic strings, so the empty string is returned."
      }
    ],
    "topics": [
      "Array",
      "Two Pointers",
      "String"
    ],
    "difficulty": "Easy",
    "constraints": [
      "1 <= words.length <= 100",
      "1 <= words[i].length <= 100",
      "words[i] consists only of lowercase English letters."
    ],
    "hints": [
      "Iterate through the elements in order. As soon as the current element is a palindrome, return it.",
      "To check if an element is a palindrome, can you reverse the string?"
    ]
  },
  {
    "title": "Maximum Fruits Harvested After at Most K Steps",
    "description": "Fruits are available at some positions on an infinite x-axis. You are given a 2D integer array fruits where fruits[i] = [positioni, amounti] depicts amounti fruits at the position positioni. fruits is already sorted by positioni in ascending order, and each positioni is unique.\nYou are also given an integer startPos and an integer k. Initially, you are at the position startPos. From any position, you can either walk to the left or right. It takes one step to move one unit on the x-axis, and you can walk at most k steps in total. For every position you reach, you harvest all the fruits at that position, and the fruits will disappear from that position.\nReturn the maximum total number of fruits you can harvest.\n \n",
    "examples": [
      {
        "input": "Input: fruits = [[2,8],[6,3],[8,6]], startPos = 5, k = 4",
        "output": "Output: 9",
        "explanation": "Explanation: "
      },
      {
        "input": "Input: fruits = [[0,9],[4,1],[5,7],[6,2],[7,4],[10,9]], startPos = 5, k = 4",
        "output": "Output: 14",
        "explanation": "Explanation: "
      },
      {
        "input": "Input: fruits = [[0,3],[6,4],[8,5]], startPos = 3, k = 2",
        "output": "Output: 0",
        "explanation": ""
      }
    ],
    "topics": [
      "Array",
      "Binary Search",
      "Sliding Window",
      "Prefix Sum"
    ],
    "difficulty": "Hard",
    "constraints": [
      "1 <= fruits.length <= 105",
      "fruits[i].length == 2",
      "0 <= startPos, positioni <= 2 * 105",
      "positioni-1 < positioni for any i > 0 (0-indexed)",
      "1 <= amounti <= 104",
      "0 <= k <= 2 * 105"
    ],
    "hints": [
      "Does an optimal path have very few patterns? For example, could a path that goes left, turns and goes right, then turns again and goes left be any better than a path that simply goes left, turns, and goes right?",
      "The optimal path turns at most once. That is, the optimal path is one of these: to go left only; to go right only; to go left, turn and go right; or to go right, turn and go left.",
      "Moving x steps left then k-x steps right gives you a range of positions that you can reach.",
      "Use prefix sums to get the sum of all fruits for each possible range.",
      "Use a similar strategy for all the paths that go right, then turn and go left."
    ]
  },
  {
    "title": "Watering Plants II",
    "description": "Alice and Bob want to water n plants in their garden. The plants are arranged in a row and are labeled from 0 to n - 1 from left to right where the ith plant is located at x = i.\nEach plant needs a specific amount of water. Alice and Bob have a watering can each, initially full. They water the plants in the following way:\n\nAlice waters the plants in order from left to right, starting from the 0th plant. Bob waters the plants in order from right to left, starting from the (n - 1)th plant. They begin watering the plants simultaneously.\nIt takes the same amount of time to water each plant regardless of how much water it needs.\nAlice/Bob must water the plant if they have enough in their can to fully water it. Otherwise, they first refill their can (instantaneously) then water the plant.\nIn case both Alice and Bob reach the same plant, the one with more water currently in his/her watering can should water this plant. If they have the same amount of water, then Alice should water this plant.\n\nGiven a 0-indexed integer array plants of n integers, where plants[i] is the amount of water the ith plant needs, and two integers capacityA and capacityB representing the capacities of Alice's and Bob's watering cans respectively, return the number of times they have to refill to water all the plants.\n \n",
    "examples": [
      {
        "input": "Input: plants = [2,2,3,3], capacityA = 5, capacityB = 5",
        "output": "Output: 1",
        "explanation": ""
      },
      {
        "input": "Input: plants = [2,2,3,3], capacityA = 3, capacityB = 4",
        "output": "Output: 2",
        "explanation": ""
      },
      {
        "input": "Input: plants = [5], capacityA = 10, capacityB = 8",
        "output": "Output: 0",
        "explanation": ""
      }
    ],
    "topics": [
      "Array",
      "Two Pointers",
      "Simulation"
    ],
    "difficulty": "Medium",
    "constraints": [
      "n == plants.length",
      "1 <= n <= 105",
      "1 <= plants[i] <= 106",
      "max(plants[i]) <= capacityA, capacityB <= 109"
    ],
    "hints": [
      "Try \"simulating\" the process.",
      "Since watering each plant takes the same amount of time, where will Alice and Bob meet if they start watering the plants simultaneously? How can you use this to optimize your solution?",
      "What will you do when both Alice and Bob have to water the same plant?"
    ]
  },
  {
    "title": "Sum of Subarray Ranges",
    "description": "You are given an integer array nums. The range of a subarray of nums is the difference between the largest and smallest element in the subarray.\nReturn the sum of all subarray ranges of nums.\nA subarray is a contiguous non-empty sequence of elements within an array.\n \n",
    "examples": [
      {
        "input": "Input: nums = [1,2,3]",
        "output": "Output: 4",
        "explanation": "Explanation: The 6 subarrays of nums are the following:"
      },
      {
        "input": "Input: nums = [1,3,3]",
        "output": "Output: 4",
        "explanation": "Explanation: The 6 subarrays of nums are the following:"
      },
      {
        "input": "Input: nums = [4,-2,-3,4,1]",
        "output": "Output: 59",
        "explanation": "Explanation: The sum of all subarray ranges of nums is 59."
      }
    ],
    "topics": [
      "Array",
      "Stack",
      "Monotonic Stack"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= nums.length <= 1000",
      "-109 <= nums[i] <= 109",
      "",
      " ",
      "Follow-up: Could you find a solution with O(n) time complexity?"
    ],
    "hints": [
      "Can you get the max/min of a certain subarray by using the max/min of a smaller subarray within it?",
      "Notice that the max of the subarray from index i to j is equal to max of (max of the subarray from index i to j-1) and nums[j]."
    ]
  },
  {
    "title": "Rings and Rods",
    "description": "There are n rings and each ring is either red, green, or blue. The rings are distributed across ten rods labeled from 0 to 9.\nYou are given a string rings of length 2n that describes the n rings that are placed onto the rods. Every two characters in rings forms a color-position pair that is used to describe each ring where:\n\nThe first character of the ith pair denotes the ith ring's color ('R', 'G', 'B').\nThe second character of the ith pair denotes the rod that the ith ring is placed on ('0' to '9').\n\nFor example, \"R3G2B1\" describes n == 3 rings: a red ring placed onto the rod labeled 3, a green ring placed onto the rod labeled 2, and a blue ring placed onto the rod labeled 1.\nReturn the number of rods that have all three colors of rings on them.\n \n",
    "examples": [
      {
        "input": "Input: rings = \"B0B6G0R6R0R6G9\"",
        "output": "Output: 1",
        "explanation": "Explanation: "
      },
      {
        "input": "Input: rings = \"B0R0G0R9R0B0G0\"",
        "output": "Output: 1",
        "explanation": "Explanation: "
      },
      {
        "input": "Input: rings = \"G4\"",
        "output": "Output: 0",
        "explanation": "Explanation: "
      }
    ],
    "topics": [
      "Hash Table",
      "String"
    ],
    "difficulty": "Easy",
    "constraints": [
      "rings.length == 2 * n",
      "1 <= n <= 100",
      "rings[i] where i is even is either 'R', 'G', or 'B' (0-indexed).",
      "rings[i] where i is odd is a digit from '0' to '9' (0-indexed)."
    ],
    "hints": [
      "For every rod, look through ‘rings’ to see if the rod contains all colors.",
      "Create 3 booleans, 1 for each color, to store if that color is present for the current rod. If all 3 are true after looking through the string, then the rod contains all the colors."
    ]
  },
  {
    "title": "Abbreviating the Product of a Range",
    "description": "You are given two positive integers left and right with left <= right. Calculate the product of all integers in the inclusive range [left, right].\nSince the product may be very large, you will abbreviate it following these steps:\n\nCount all trailing zeros in the product and remove them. Let us denote this count as C.\n\n\t\nFor example, there are 3 trailing zeros in 1000, and there are 0 trailing zeros in 546.\n\n\nDenote the remaining number of digits in the product as d. If d > 10, then express the product as <pre>...<suf> where <pre> denotes the first 5 digits of the product, and <suf> denotes the last 5 digits of the product after removing all trailing zeros. If d <= 10, we keep it unchanged.\n\t\nFor example, we express 1234567654321 as 12345...54321, but 1234567 is represented as 1234567.\n\n\nFinally, represent the product as a string \"<pre>...<suf>eC\".\n\t\nFor example, 12345678987600000 will be represented as \"12345...89876e5\".\n\n\n\nReturn a string denoting the abbreviated product of all integers in the inclusive range [left, right].\n \n",
    "examples": [
      {
        "input": "Input: left = 1, right = 4",
        "output": "Output: \"24e0\"",
        "explanation": "Explanation: The product is 1 × 2 × 3 × 4 = 24."
      },
      {
        "input": "Input: left = 2, right = 11",
        "output": "Output: \"399168e2\"",
        "explanation": "Explanation: The product is 39916800."
      },
      {
        "input": "Input: left = 371, right = 375",
        "output": "Output: \"7219856259e3\"",
        "explanation": "Explanation: The product is 7219856259000."
      }
    ],
    "topics": [
      "Math"
    ],
    "difficulty": "Hard",
    "constraints": [
      "1 <= left <= right <= 104"
    ],
    "hints": [
      "Calculating the number of trailing zeros, the last five digits, and the first five digits can all be done separately.",
      "Use a prime factorization property to find the number of trailing zeros. Use modulo to find the last 5 digits. Use a logarithm property to find the first 5 digits.",
      "The number of trailing zeros C is nothing but the number of times the product is completely divisible by 10. Since 2 and 5 are the only prime factors of 10,  C will be equal to the minimum number of times 2 or 5 appear in the prime factorization of the product.",
      "Iterate through the integers from left to right. For every integer, keep dividing it by 2 as long as it is divisible by 2 and C occurrences of 2 haven't been removed in total. Repeat this process for 5. Finally, multiply the integer under modulo of 10^5 with the product obtained till now to obtain the last five digits.",
      "The product P can be represented as P=10^(x+y) where x is the integral part and y is the fractional part of x+y. Using the property \"if S = A * B, then log(S) = log(A) + log(B)\", we can write x+y = log_10(P) = sum(log_10(i)) for each integer i in [left, right]. Once we obtain the sum, the first five digits can be represented as floor(10^(y+4))."
    ]
  },
  {
    "title": "Check if a Parentheses String Can Be Valid",
    "description": "A parentheses string is a non-empty string consisting only of '(' and ')'. It is valid if any of the following conditions is true:\n\nIt is ().\nIt can be written as AB (A concatenated with B), where A and B are valid parentheses strings.\nIt can be written as (A), where A is a valid parentheses string.\n\nYou are given a parentheses string s and a string locked, both of length n. locked is a binary string consisting only of '0's and '1's. For each index i of locked,\n\nIf locked[i] is '1', you cannot change s[i].\nBut if locked[i] is '0', you can change s[i] to either '(' or ')'.\n\nReturn true if you can make s a valid parentheses string. Otherwise, return false.\n \n",
    "examples": [
      {
        "input": "Input: s = \"))()))\", locked = \"010100\"",
        "output": "Output: true",
        "explanation": "Explanation: locked[1] == '1' and locked[3] == '1', so we cannot change s[1] or s[3]."
      },
      {
        "input": "Input: s = \"()()\", locked = \"0000\"",
        "output": "Output: true",
        "explanation": "Explanation: We do not need to make any changes because s is already valid."
      },
      {
        "input": "Input: s = \")\", locked = \"0\"",
        "output": "Output: false",
        "explanation": "Explanation: locked permits us to change s[0]. "
      }
    ],
    "topics": [
      "String",
      "Stack",
      "Greedy"
    ],
    "difficulty": "Medium",
    "constraints": [
      "n == s.length == locked.length",
      "1 <= n <= 105",
      "s[i] is either '(' or ')'.",
      "locked[i] is either '0' or '1'."
    ],
    "hints": [
      "Can an odd length string ever be valid?",
      "From left to right, if a locked ')' is encountered, it must be balanced with either a locked '(' or an unlocked index on its left. If neither exist, what conclusion can be drawn? If both exist, which one is more preferable to use?",
      "After the above, we may have locked indices of '(' and additional unlocked indices. How can you balance out the locked '(' now? What if you cannot balance any locked '('?"
    ]
  },
  {
    "title": "Find All Possible Recipes from Given Supplies",
    "description": "You have information about n different recipes. You are given a string array recipes and a 2D string array ingredients. The ith recipe has the name recipes[i], and you can create it if you have all the needed ingredients from ingredients[i]. Ingredients to a recipe may need to be created from other recipes, i.e., ingredients[i] may contain a string that is in recipes.\nYou are also given a string array supplies containing all the ingredients that you initially have, and you have an infinite supply of all of them.\nReturn a list of all the recipes that you can create. You may return the answer in any order.\nNote that two recipes may contain each other in their ingredients.\n \n",
    "examples": [
      {
        "input": "Input: recipes = [\"bread\"], ingredients = [[\"yeast\",\"flour\"]], supplies = [\"yeast\",\"flour\",\"corn\"]",
        "output": "Output: [\"bread\"]",
        "explanation": ""
      },
      {
        "input": "Input: recipes = [\"bread\",\"sandwich\"], ingredients = [[\"yeast\",\"flour\"],[\"bread\",\"meat\"]], supplies = [\"yeast\",\"flour\",\"meat\"]",
        "output": "Output: [\"bread\",\"sandwich\"]",
        "explanation": ""
      },
      {
        "input": "Input: recipes = [\"bread\",\"sandwich\",\"burger\"], ingredients = [[\"yeast\",\"flour\"],[\"bread\",\"meat\"],[\"sandwich\",\"meat\",\"bread\"]], supplies = [\"yeast\",\"flour\",\"meat\"]",
        "output": "Output: [\"bread\",\"sandwich\",\"burger\"]",
        "explanation": ""
      }
    ],
    "topics": [
      "Array",
      "Hash Table",
      "String",
      "Graph",
      "Topological Sort"
    ],
    "difficulty": "Medium",
    "constraints": [
      "n == recipes.length == ingredients.length",
      "1 <= n <= 100",
      "1 <= ingredients[i].length, supplies.length <= 100",
      "1 <= recipes[i].length, ingredients[i][j].length, supplies[k].length <= 10",
      "recipes[i], ingredients[i][j], and supplies[k] consist only of lowercase English letters.",
      "All the values of recipes and supplies combined are unique.",
      "Each ingredients[i] does not contain any duplicate values."
    ],
    "hints": [
      "Can we use a data structure to quickly query whether we have a certain ingredient?",
      "Once we verify that we can make a recipe, we can add it to our ingredient data structure. We can then check if we can make more recipes as a result of this."
    ]
  },
  {
    "title": "Maximum Number of Words Found in Sentences",
    "description": "A sentence is a list of words that are separated by a single space with no leading or trailing spaces.\nYou are given an array of strings sentences, where each sentences[i] represents a single sentence.\nReturn the maximum number of words that appear in a single sentence.\n \n",
    "examples": [
      {
        "input": "Input: sentences = [\"alice and bob love leetcode\", \"i think so too\", \"this is great thanks very much\"]",
        "output": "Output: 6",
        "explanation": "Explanation: "
      },
      {
        "input": "Input: sentences = [\"please wait\", \"continue to fight\", \"continue to win\"]",
        "output": "Output: 3",
        "explanation": "Explanation: It is possible that multiple sentences contain the same number of words. "
      }
    ],
    "topics": [
      "Array",
      "String"
    ],
    "difficulty": "Easy",
    "constraints": [
      "1 <= sentences.length <= 100",
      "1 <= sentences[i].length <= 100",
      "sentences[i] consists only of lowercase English letters and ' ' only.",
      "sentences[i] does not have leading or trailing spaces.",
      "All the words in sentences[i] are separated by a single space."
    ],
    "hints": [
      "Process each sentence separately and count the number of words by looking for the number of space characters in the sentence and adding it by 1."
    ]
  },
  {
    "title": "Step-By-Step Directions From a Binary Tree Node to Another",
    "description": "You are given the root of a binary tree with n nodes. Each node is uniquely assigned a value from 1 to n. You are also given an integer startValue representing the value of the start node s, and a different integer destValue representing the value of the destination node t.\nFind the shortest path starting from node s and ending at node t. Generate step-by-step directions of such path as a string consisting of only the uppercase letters 'L', 'R', and 'U'. Each letter indicates a specific direction:\n\n'L' means to go from a node to its left child node.\n'R' means to go from a node to its right child node.\n'U' means to go from a node to its parent node.\n\nReturn the step-by-step directions of the shortest path from node s to node t.\n \n",
    "examples": [
      {
        "input": "Input: root = [5,1,2,3,null,6,4], startValue = 3, destValue = 6",
        "output": "Output: \"UURL\"",
        "explanation": "Explanation: The shortest path is: 3 → 1 → 5 → 2 → 6."
      },
      {
        "input": "Input: root = [2,1], startValue = 2, destValue = 1",
        "output": "Output: \"L\"",
        "explanation": "Explanation: The shortest path is: 2 → 1."
      }
    ],
    "topics": [
      "String",
      "Tree",
      "Depth-First Search",
      "Binary Tree"
    ],
    "difficulty": "Medium",
    "constraints": [
      "The number of nodes in the tree is n.",
      "2 <= n <= 105",
      "1 <= Node.val <= n",
      "All the values in the tree are unique.",
      "1 <= startValue, destValue <= n",
      "startValue != destValue"
    ],
    "hints": [
      "The shortest path between any two nodes in a tree must pass through their Lowest Common Ancestor (LCA). The path will travel upwards from node s to the LCA and then downwards from the LCA to node t.",
      "Find the path strings from root → s, and root → t. Can you use these two strings to prepare the final answer?",
      "Remove the longest common prefix of the two path strings to get the path LCA → s, and LCA → t. Each step in the path of LCA → s should be reversed as 'U'."
    ]
  },
  {
    "title": "Delete the Middle Node of a Linked List",
    "description": "You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.\nThe middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing, where ⌊x⌋ denotes the largest integer less than or equal to x.\n\nFor n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.\n\n \n",
    "examples": [
      {
        "input": "Input: head = [1,3,4,7,1,2,6]",
        "output": "Output: [1,3,4,1,2,6]",
        "explanation": ""
      },
      {
        "input": "Input: head = [1,2,3,4]",
        "output": "Output: [1,2,4]",
        "explanation": ""
      },
      {
        "input": "Input: head = [2,1]",
        "output": "Output: [2]",
        "explanation": ""
      }
    ],
    "topics": [
      "Linked List",
      "Two Pointers"
    ],
    "difficulty": "Medium",
    "constraints": [
      "The number of nodes in the list is in the range [1, 105].",
      "1 <= Node.val <= 105"
    ],
    "hints": [
      "If a point with a speed s moves n units in a given time, a point with speed 2 * s will move 2 * n units at the same time. Can you use this to find the middle node of a linked list?",
      "If you are given the middle node, the node before it, and the node after it, how can you modify the linked list?"
    ]
  },
  {
    "title": "Finding 3-Digit Even Numbers",
    "description": "You are given an integer array digits, where each element is a digit. The array may contain duplicates.\nYou need to find all the unique integers that follow the given requirements:\n\nThe integer consists of the concatenation of three elements from digits in any arbitrary order.\nThe integer does not have leading zeros.\nThe integer is even.\n\nFor example, if the given digits were [1, 2, 3], integers 132 and 312 follow the requirements.\nReturn a sorted array of the unique integers.\n \n",
    "examples": [
      {
        "input": "Input: digits = [2,1,3,0]",
        "output": "Output: [102,120,130,132,210,230,302,310,312,320]",
        "explanation": "Explanation: All the possible integers that follow the requirements are in the output array. "
      },
      {
        "input": "Input: digits = [2,2,8,8,2]",
        "output": "Output: [222,228,282,288,822,828,882]",
        "explanation": "Explanation: The same digit can be used as many times as it appears in digits. "
      },
      {
        "input": "Input: digits = [3,7,5]",
        "output": "Output: []",
        "explanation": "Explanation: No even integers can be formed using the given digits."
      }
    ],
    "topics": [
      "Array",
      "Hash Table",
      "Sorting",
      "Enumeration"
    ],
    "difficulty": "Easy",
    "constraints": [
      "3 <= digits.length <= 100",
      "0 <= digits[i] <= 9"
    ],
    "hints": [
      "The range of possible answers includes all even numbers between 100 and 999 inclusive. Could you check each possible answer to see if it could be formed from the digits in the array?"
    ]
  },
  {
    "title": "Find All People With Secret",
    "description": "You are given an integer n indicating there are n people numbered from 0 to n - 1. You are also given a 0-indexed 2D integer array meetings where meetings[i] = [xi, yi, timei] indicates that person xi and person yi have a meeting at timei. A person may attend multiple meetings at the same time. Finally, you are given an integer firstPerson.\nPerson 0 has a secret and initially shares the secret with a person firstPerson at time 0. This secret is then shared every time a meeting takes place with a person that has the secret. More formally, for every meeting, if a person xi has the secret at timei, then they will share the secret with person yi, and vice versa.\nThe secrets are shared instantaneously. That is, a person may receive the secret and share it with people in other meetings within the same time frame.\nReturn a list of all the people that have the secret after all the meetings have taken place. You may return the answer in any order.\n \n",
    "examples": [
      {
        "input": "Input: n = 6, meetings = [[1,2,5],[2,3,8],[1,5,10]], firstPerson = 1",
        "output": "Output: [0,1,2,3,5]",
        "explanation": ""
      },
      {
        "input": "Input: n = 4, meetings = [[3,1,3],[1,2,2],[0,3,3]], firstPerson = 3",
        "output": "Output: [0,1,3]",
        "explanation": ""
      },
      {
        "input": "Input: n = 5, meetings = [[3,4,2],[1,2,1],[2,3,1]], firstPerson = 1",
        "output": "Output: [0,1,2,3,4]",
        "explanation": ""
      }
    ],
    "topics": [
      "Depth-First Search",
      "Breadth-First Search",
      "Union Find",
      "Graph",
      "Sorting"
    ],
    "difficulty": "Hard",
    "constraints": [
      "2 <= n <= 105",
      "1 <= meetings.length <= 105",
      "meetings[i].length == 3",
      "0 <= xi, yi <= n - 1",
      "xi != yi",
      "1 <= timei <= 105",
      "1 <= firstPerson <= n - 1"
    ],
    "hints": [
      "Could you model all the meetings happening at the same time as a graph?",
      "What data structure can you use to efficiently share the secret?",
      "You can use the union-find data structure to quickly determine who knows the secret and share the secret."
    ]
  },
  {
    "title": "Removing Minimum and Maximum From Array",
    "description": "You are given a 0-indexed array of distinct integers nums.\nThere is an element in nums that has the lowest value and an element that has the highest value. We call them the minimum and maximum respectively. Your goal is to remove both these elements from the array.\nA deletion is defined as either removing an element from the front of the array or removing an element from the back of the array.\nReturn the minimum number of deletions it would take to remove both the minimum and maximum element from the array.\n \n",
    "examples": [
      {
        "input": "Input: nums = [2,10,7,5,4,1,8,6]",
        "output": "Output: 5",
        "explanation": "Explanation: "
      },
      {
        "input": "Input: nums = [0,-4,19,1,8,-2,-3,5]",
        "output": "Output: 3",
        "explanation": "Explanation: "
      },
      {
        "input": "Input: nums = [101]",
        "output": "Output: 1",
        "explanation": "Explanation:  "
      }
    ],
    "topics": [
      "Array",
      "Greedy"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= nums.length <= 105",
      "-105 <= nums[i] <= 105",
      "The integers in nums are distinct."
    ],
    "hints": [
      "There can only be three scenarios for deletions such that both minimum and maximum elements are removed:",
      "Scenario 1: Both elements are removed by only deleting from the front.",
      "Scenario 2: Both elements are removed by only deleting from the back.",
      "Scenario 3: Delete from the front to remove one of the elements, and delete from the back to remove the other element.",
      "Compare which of the three scenarios results in the minimum number of moves."
    ]
  },
  {
    "title": "K Radius Subarray Averages",
    "description": "You are given a 0-indexed array nums of n integers, and an integer k.\nThe k-radius average for a subarray of nums centered at some index i with the radius k is the average of all elements in nums between the indices i - k and i + k (inclusive). If there are less than k elements before or after the index i, then the k-radius average is -1.\nBuild and return an array avgs of length n where avgs[i] is the k-radius average for the subarray centered at index i.\nThe average of x elements is the sum of the x elements divided by x, using integer division. The integer division truncates toward zero, which means losing its fractional part.\n\nFor example, the average of four elements 2, 3, 1, and 5 is (2 + 3 + 1 + 5) / 4 = 11 / 4 = 2.75, which truncates to 2.\n\n \n",
    "examples": [
      {
        "input": "Input: nums = [7,4,3,9,1,8,5,2,6], k = 3",
        "output": "Output: [-1,-1,-1,5,4,4,-1,-1,-1]",
        "explanation": ""
      },
      {
        "input": "Input: nums = [100000], k = 0",
        "output": "Output: [100000]",
        "explanation": ""
      },
      {
        "input": "Input: nums = [8], k = 100000",
        "output": "Output: [-1]",
        "explanation": "Explanation: "
      }
    ],
    "topics": [
      "Array",
      "Sliding Window"
    ],
    "difficulty": "Medium",
    "constraints": [
      "n == nums.length",
      "1 <= n <= 105",
      "0 <= nums[i], k <= 105"
    ],
    "hints": [
      "To calculate the average of a subarray, you need the sum and the K. K is already given. How could you quickly calculate the sum of a subarray?",
      "Use the Prefix Sums method to calculate the subarray sums.",
      "It is possible that the sum of all the elements does not fit in a 32-bit integer type. Be sure to use a 64-bit integer type for the prefix sum array."
    ]
  },
  {
    "title": "Find Target Indices After Sorting Array",
    "description": "You are given a 0-indexed integer array nums and a target element target.\nA target index is an index i such that nums[i] == target.\nReturn a list of the target indices of nums after sorting nums in non-decreasing order. If there are no target indices, return an empty list. The returned list must be sorted in increasing order.\n \n",
    "examples": [
      {
        "input": "Input: nums = [1,2,5,2,3], target = 2",
        "output": "Output: [1,2]",
        "explanation": "Explanation: After sorting, nums is [1,2,2,3,5]."
      },
      {
        "input": "Input: nums = [1,2,5,2,3], target = 3",
        "output": "Output: [3]",
        "explanation": "Explanation: After sorting, nums is [1,2,2,3,5]."
      },
      {
        "input": "Input: nums = [1,2,5,2,3], target = 5",
        "output": "Output: [4]",
        "explanation": "Explanation: After sorting, nums is [1,2,2,3,5]."
      }
    ],
    "topics": [
      "Array",
      "Binary Search",
      "Sorting"
    ],
    "difficulty": "Easy",
    "constraints": [
      "1 <= nums.length <= 100",
      "1 <= nums[i], target <= 100"
    ],
    "hints": [
      "Try \"sorting\" the array first.",
      "Now find all indices in the array whose values are equal to target."
    ]
  },
  {
    "title": "Sequentially Ordinal Rank Tracker",
    "description": "A scenic location is represented by its name and attractiveness score, where name is a unique string among all locations and score is an integer. Locations can be ranked from the best to the worst. The higher the score, the better the location. If the scores of two locations are equal, then the location with the lexicographically smaller name is better.\nYou are building a system that tracks the ranking of locations with the system initially starting with no locations. It supports:\n\nAdding scenic locations, one at a time.\nQuerying the ith best location of all locations already added, where i is the number of times the system has been queried (including the current query).\n\t\nFor example, when the system is queried for the 4th time, it returns the 4th best location of all locations already added.\n\n\n\nNote that the test data are generated so that at any time, the number of queries does not exceed the number of locations added to the system.\nImplement the SORTracker class:\n\nSORTracker() Initializes the tracker system.\nvoid add(string name, int score) Adds a scenic location with name and score to the system.\nstring get() Queries and returns the ith best location, where i is the number of times this method has been invoked (including this invocation).\n\n \n",
    "examples": [
      {
        "input": "Input\n[\"SORTracker\", \"add\", \"add\", \"get\", \"add\", \"get\", \"add\", \"get\", \"add\", \"get\", \"add\", \"get\", \"get\"]",
        "output": "Output\n[null, null, null, \"branford\", null, \"alps\", null, \"bradford\", null, \"bradford\", null, \"bradford\", \"orland\"]",
        "explanation": "Explanation\nSORTracker tracker = new SORTracker(); // Initialize the tracker system."
      }
    ],
    "topics": [
      "Design",
      "Heap (Priority Queue)",
      "Data Stream",
      "Ordered Set"
    ],
    "difficulty": "Hard",
    "constraints": [
      "name consists of lowercase English letters, and is unique among all locations.",
      "1 <= name.length <= 10",
      "1 <= score <= 105",
      "At any time, the number of calls to get does not exceed the number of calls to add.",
      "At most 4 * 104 calls in total will be made to add and get."
    ],
    "hints": [
      "If the problem were to find the median of a stream of scenery locations while they are being added, can you solve it?",
      "We can use a similar approach as an optimization to avoid repeated sorting.",
      "Employ two heaps: left heap and right heap. The left heap is a max-heap, and the right heap is a min-heap. The size of the left heap is k + 1 (best locations), where k is the number of times the get method was invoked. The other locations are maintained in the right heap.",
      "Every time when add is being called, we add it to the left heap. If the size of the left heap exceeds k + 1, we move the head element to the right heap.",
      "When the get method is invoked again (the k + 1 time it is invoked), we can return the head element of the left heap. But before returning it, if the right heap is not empty, we maintain the left heap to have the best k + 2 items by moving the best location from the right heap to the left heap."
    ]
  },
  {
    "title": "Detonate the Maximum Bombs",
    "description": "You are given a list of bombs. The range of a bomb is defined as the area where its effect can be felt. This area is in the shape of a circle with the center as the location of the bomb.\nThe bombs are represented by a 0-indexed 2D integer array bombs where bombs[i] = [xi, yi, ri]. xi and yi denote the X-coordinate and Y-coordinate of the location of the ith bomb, whereas ri denotes the radius of its range.\nYou may choose to detonate a single bomb. When a bomb is detonated, it will detonate all bombs that lie in its range. These bombs will further detonate the bombs that lie in their ranges.\nGiven the list of bombs, return the maximum number of bombs that can be detonated if you are allowed to detonate only one bomb.\n \n",
    "examples": [
      {
        "input": "Input: bombs = [[2,1,3],[6,1,4]]",
        "output": "Output: 2",
        "explanation": ""
      },
      {
        "input": "Input: bombs = [[1,1,5],[10,10,5]]",
        "output": "Output: 1",
        "explanation": ""
      },
      {
        "input": "Input: bombs = [[1,2,3],[2,3,1],[3,4,2],[4,5,3],[5,6,4]]",
        "output": "Output: 5",
        "explanation": ""
      }
    ],
    "topics": [
      "Array",
      "Math",
      "Depth-First Search",
      "Breadth-First Search",
      "Graph",
      "Geometry"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= bombs.length <= 100",
      "bombs[i].length == 3",
      "1 <= xi, yi, ri <= 105"
    ],
    "hints": [
      "How can we model the relationship between different bombs? Can \"graphs\" help us?",
      "Bombs are nodes and are connected to other bombs in their range by directed edges.",
      "If we know which bombs will be affected when any bomb is detonated, how can we find the total number of bombs that will be detonated if we start from a fixed bomb?",
      "Run a Depth First Search (DFS) from every node, and all the nodes it reaches are the bombs that will be detonated."
    ]
  },
  {
    "title": "Find Good Days to Rob the Bank",
    "description": "You and a gang of thieves are planning on robbing a bank. You are given a 0-indexed integer array security, where security[i] is the number of guards on duty on the ith day. The days are numbered starting from 0. You are also given an integer time.\nThe ith day is a good day to rob the bank if:\n\nThere are at least time days before and after the ith day,\nThe number of guards at the bank for the time days before i are non-increasing, and\nThe number of guards at the bank for the time days after i are non-decreasing.\n\nMore formally, this means day i is a good day to rob the bank if and only if security[i - time] >= security[i - time + 1] >= ... >= security[i] <= ... <= security[i + time - 1] <= security[i + time].\nReturn a list of all days (0-indexed) that are good days to rob the bank. The order that the days are returned in does not matter.\n \n",
    "examples": [
      {
        "input": "Input: security = [5,3,3,3,5,6,2], time = 2",
        "output": "Output: [2,3]",
        "explanation": ""
      },
      {
        "input": "Input: security = [1,1,1,1,1], time = 0",
        "output": "Output: [0,1,2,3,4]",
        "explanation": ""
      },
      {
        "input": "Input: security = [1,2,3,4,5,6], time = 2",
        "output": "Output: []",
        "explanation": ""
      }
    ],
    "topics": [
      "Array",
      "Dynamic Programming",
      "Prefix Sum"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= security.length <= 105",
      "0 <= security[i], time <= 105"
    ],
    "hints": [
      "The trivial solution is to check the time days before and after each day. There are a lot of repeated operations using this solution. How could we optimize this solution?",
      "We can use precomputation to make the solution faster.",
      "Use an array to store the number of days before the ith day that is non-increasing, and another array to store the number of days after the ith day that is non-decreasing."
    ]
  },
  {
    "title": "Find Subsequence of Length K With the Largest Sum",
    "description": "You are given an integer array nums and an integer k. You want to find a subsequence of nums of length k that has the largest sum.\nReturn any such subsequence as an integer array of length k.\nA subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.\n \n",
    "examples": [
      {
        "input": "Input: nums = [2,1,3,3], k = 2",
        "output": "Output: [3,3]",
        "explanation": ""
      },
      {
        "input": "Input: nums = [-1,-2,3,4], k = 3",
        "output": "Output: [-1,3,4]",
        "explanation": "Explanation: "
      },
      {
        "input": "Input: nums = [3,4,3,3], k = 2",
        "output": "Output: [3,4]",
        "explanation": ""
      }
    ],
    "topics": [
      "Array",
      "Hash Table",
      "Sorting",
      "Heap (Priority Queue)"
    ],
    "difficulty": "Easy",
    "constraints": [
      "1 <= nums.length <= 1000",
      "-105 <= nums[i] <= 105",
      "1 <= k <= nums.length"
    ],
    "hints": [
      "From a greedy perspective, what k elements should you pick?",
      "Could you sort the array while maintaining the index?"
    ]
  },
  {
    "title": "Sum of k-Mirror Numbers",
    "description": "A k-mirror number is a positive integer without leading zeros that reads the same both forward and backward in base-10 as well as in base-k.\n\nFor example, 9 is a 2-mirror number. The representation of 9 in base-10 and base-2 are 9 and 1001 respectively, which read the same both forward and backward.\nOn the contrary, 4 is not a 2-mirror number. The representation of 4 in base-2 is 100, which does not read the same both forward and backward.\n\nGiven the base k and the number n, return the sum of the n smallest k-mirror numbers.\n \n",
    "examples": [
      {
        "input": "Input: k = 2, n = 5",
        "output": "Output: 25",
        "explanation": ""
      },
      {
        "input": "Input: k = 3, n = 7",
        "output": "Output: 499",
        "explanation": ""
      },
      {
        "input": "Input: k = 7, n = 17",
        "output": "Output: 20379000",
        "explanation": "Explanation: The 17 smallest 7-mirror numbers are:"
      }
    ],
    "topics": [
      "Math",
      "Enumeration"
    ],
    "difficulty": "Hard",
    "constraints": [
      "2 <= k <= 9",
      "1 <= n <= 30"
    ],
    "hints": [
      "Since we need to reduce search space, instead of checking if every number is a palindrome in base-10, can we try to \"generate\" the palindromic numbers?",
      "If you are provided with a d digit number, how can you generate a palindrome with 2*d or 2*d - 1 digit?",
      "Try brute-forcing and checking if the palindrome you generated is a \"k-Mirror\" number."
    ]
  },
  {
    "title": "Valid Arrangement of Pairs",
    "description": "You are given a 0-indexed 2D integer array pairs where pairs[i] = [starti, endi]. An arrangement of pairs is valid if for every index i where 1 <= i < pairs.length, we have endi-1 == starti.\nReturn any valid arrangement of pairs.\nNote: The inputs will be generated such that there exists a valid arrangement of pairs.\n \n",
    "examples": [
      {
        "input": "Input: pairs = [[5,1],[4,5],[11,9],[9,4]]",
        "output": "Output: [[11,9],[9,4],[4,5],[5,1]]",
        "explanation": ""
      },
      {
        "input": "Input: pairs = [[1,3],[3,2],[2,1]]",
        "output": "Output: [[1,3],[3,2],[2,1]]",
        "explanation": ""
      },
      {
        "input": "Input: pairs = [[1,2],[1,3],[2,1]]",
        "output": "Output: [[1,2],[2,1],[1,3]]",
        "explanation": ""
      }
    ],
    "topics": [
      "Depth-First Search",
      "Graph",
      "Eulerian Circuit"
    ],
    "difficulty": "Hard",
    "constraints": [
      "1 <= pairs.length <= 105",
      "pairs[i].length == 2",
      "0 <= starti, endi <= 109",
      "starti != endi",
      "No two pairs are exactly the same.",
      "There exists a valid arrangement of pairs."
    ],
    "hints": [
      "Could you convert this into a graph problem?",
      "Consider the pairs as edges and each number as a node.",
      "We have to find an Eulerian path of this graph. Hierholzer’s algorithm can be used."
    ]
  },
  {
    "title": "Stamping the Grid",
    "description": "You are given an m x n binary matrix grid where each cell is either 0 (empty) or 1 (occupied).\nYou are then given stamps of size stampHeight x stampWidth. We want to fit the stamps such that they follow the given restrictions and requirements:\n\nCover all the empty cells.\nDo not cover any of the occupied cells.\nWe can put as many stamps as we want.\nStamps can overlap with each other.\nStamps are not allowed to be rotated.\nStamps must stay completely inside the grid.\n\nReturn true if it is possible to fit the stamps while following the given restrictions and requirements. Otherwise, return false.\n \n",
    "examples": [
      {
        "input": "Input: grid = [[1,0,0,0],[1,0,0,0],[1,0,0,0],[1,0,0,0],[1,0,0,0]], stampHeight = 4, stampWidth = 3",
        "output": "Output: true",
        "explanation": "Explanation: We have two overlapping stamps (labeled 1 and 2 in the image) that are able to cover all the empty cells."
      },
      {
        "input": "Input: grid = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]], stampHeight = 2, stampWidth = 2 ",
        "output": "Output: false ",
        "explanation": "Explanation: There is no way to fit the stamps onto all the empty cells without the stamps going outside the grid."
      }
    ],
    "topics": [
      "Array",
      "Greedy",
      "Matrix",
      "Prefix Sum"
    ],
    "difficulty": "Hard",
    "constraints": [
      "m == grid.length",
      "n == grid[r].length",
      "1 <= m, n <= 105",
      "1 <= m * n <= 2 * 105",
      "grid[r][c] is either 0 or 1.",
      "1 <= stampHeight, stampWidth <= 105"
    ],
    "hints": [
      "We can check if every empty cell is a part of a consecutive row of empty cells that has a width of at least stampWidth as well as a consecutive column of empty cells that has a height of at least stampHeight.",
      "We can prove that this condition is sufficient and necessary to fit the stamps while following the given restrictions and requirements.",
      "For each row, find every consecutive row of empty cells, and mark all the cells where the consecutive row is at least stampWidth wide. Do the same for the columns with stampHeight. Then, you can check if every cell is marked twice."
    ]
  },
  {
    "title": "Two Furthest Houses With Different Colors",
    "description": "There are n houses evenly lined up on the street, and each house is beautifully painted. You are given a 0-indexed integer array colors of length n, where colors[i] represents the color of the ith house.\nReturn the maximum distance between two houses with different colors.\nThe distance between the ith and jth houses is abs(i - j), where abs(x) is the absolute value of x.\n \n",
    "examples": [
      {
        "input": "Input: colors = [1,1,1,6,1,1,1]",
        "output": "Output: 3",
        "explanation": "Explanation: In the above image, color 1 is blue, and color 6 is red."
      },
      {
        "input": "Input: colors = [1,8,3,8,3]",
        "output": "Output: 4",
        "explanation": "Explanation: In the above image, color 1 is blue, color 8 is yellow, and color 3 is green."
      },
      {
        "input": "Input: colors = [0,1]",
        "output": "Output: 1",
        "explanation": "Explanation: The furthest two houses with different colors are house 0 and house 1."
      }
    ],
    "topics": [
      "Array",
      "Greedy"
    ],
    "difficulty": "Easy",
    "constraints": [
      "n == colors.length",
      "2 <= n <= 100",
      "0 <= colors[i] <= 100",
      "Test data are generated such that at least two houses have different colors."
    ],
    "hints": [
      "The constraints are small. Can you try the combination of every two houses?",
      "Greedily, the maximum distance will come from either the pair of the leftmost house and possibly some house on the right with a different color, or the pair of the rightmost house and possibly some house on the left with a different color."
    ]
  },
  {
    "title": "Process Restricted Friend Requests",
    "description": "You are given an integer n indicating the number of people in a network. Each person is labeled from 0 to n - 1.\nYou are also given a 0-indexed 2D integer array restrictions, where restrictions[i] = [xi, yi] means that person xi and person yi cannot become friends, either directly or indirectly through other people.\nInitially, no one is friends with each other. You are given a list of friend requests as a 0-indexed 2D integer array requests, where requests[j] = [uj, vj] is a friend request between person uj and person vj.\nA friend request is successful if uj and vj can be friends. Each friend request is processed in the given order (i.e., requests[j] occurs before requests[j + 1]), and upon a successful request, uj and vj become direct friends for all future friend requests.\nReturn a boolean array result, where each result[j] is true if the jth friend request is successful or false if it is not.\nNote: If uj and vj are already direct friends, the request is still successful.\n \n",
    "examples": [
      {
        "input": "Input: n = 3, restrictions = [[0,1]], requests = [[0,2],[2,1]]",
        "output": "Output: [true,false]",
        "explanation": ""
      },
      {
        "input": "Input: n = 3, restrictions = [[0,1]], requests = [[1,2],[0,2]]",
        "output": "Output: [true,false]",
        "explanation": ""
      },
      {
        "input": "Input: n = 5, restrictions = [[0,1],[1,2],[2,3]], requests = [[0,4],[1,2],[3,1],[3,4]]",
        "output": "Output: [true,false,true,false]",
        "explanation": ""
      }
    ],
    "topics": [
      "Union Find",
      "Graph"
    ],
    "difficulty": "Hard",
    "constraints": [
      "2 <= n <= 1000",
      "0 <= restrictions.length <= 1000",
      "restrictions[i].length == 2",
      "0 <= xi, yi <= n - 1",
      "xi != yi",
      "1 <= requests.length <= 1000",
      "requests[j].length == 2",
      "0 <= uj, vj <= n - 1",
      "uj != vj"
    ],
    "hints": [
      "For each request, we could loop through all restrictions. Can you think of doing a check-in close to O(1)?",
      "Could you use Union Find?"
    ]
  },
  {
    "title": "Decode the Slanted Ciphertext",
    "description": "A string originalText is encoded using a slanted transposition cipher to a string encodedText with the help of a matrix having a fixed number of rows rows.\noriginalText is placed first in a top-left to bottom-right manner.\n\nThe blue cells are filled first, followed by the red cells, then the yellow cells, and so on, until we reach the end of originalText. The arrow indicates the order in which the cells are filled. All empty cells are filled with ' '. The number of columns is chosen such that the rightmost column will not be empty after filling in originalText.\nencodedText is then formed by appending all characters of the matrix in a row-wise fashion.\n\nThe characters in the blue cells are appended first to encodedText, then the red cells, and so on, and finally the yellow cells. The arrow indicates the order in which the cells are accessed.\nFor example, if originalText = \"cipher\" and rows = 3, then we encode it in the following manner:\n\nThe blue arrows depict how originalText is placed in the matrix, and the red arrows denote the order in which encodedText is formed. In the above example, encodedText = \"ch ie pr\".\nGiven the encoded string encodedText and number of rows rows, return the original string originalText.\nNote: originalText does not have any trailing spaces ' '. The test cases are generated such that there is only one possible originalText.\n \n",
    "examples": [
      {
        "input": "Input: encodedText = \"ch   ie   pr\", rows = 3",
        "output": "Output: \"cipher\"",
        "explanation": "Explanation: This is the same example described in the problem description."
      },
      {
        "input": "Input: encodedText = \"iveo    eed   l te   olc\", rows = 4",
        "output": "Output: \"i love leetcode\"",
        "explanation": "Explanation: The figure above denotes the matrix that was used to encode originalText. "
      },
      {
        "input": "Input: encodedText = \"coding\", rows = 1",
        "output": "Output: \"coding\"",
        "explanation": "Explanation: Since there is only 1 row, both originalText and encodedText are the same."
      }
    ],
    "topics": [
      "String",
      "Simulation"
    ],
    "difficulty": "Medium",
    "constraints": [
      "0 <= encodedText.length <= 106",
      "encodedText consists of lowercase English letters and ' ' only.",
      "encodedText is a valid encoding of some originalText that does not have trailing spaces.",
      "1 <= rows <= 1000",
      "The testcases are generated such that there is only one possible originalText."
    ],
    "hints": [
      "How can you use rows and encodedText to find the number of columns of the matrix?",
      "Once you have the number of rows and columns, you can create the matrix and place encodedText in it. How should you place it in the matrix?",
      "How should you traverse the matrix to \"decode\" originalText?"
    ]
  },
  {
    "title": "Reverse Nodes in Even Length Groups",
    "description": "You are given the head of a linked list.\nThe nodes in the linked list are sequentially assigned to non-empty groups whose lengths form the sequence of the natural numbers (1, 2, 3, 4, ...). The length of a group is the number of nodes assigned to it. In other words,\n\nThe 1st node is assigned to the first group.\nThe 2nd and the 3rd nodes are assigned to the second group.\nThe 4th, 5th, and 6th nodes are assigned to the third group, and so on.\n\nNote that the length of the last group may be less than or equal to 1 + the length of the second to last group.\nReverse the nodes in each group with an even length, and return the head of the modified linked list.\n \n",
    "examples": [
      {
        "input": "Input: head = [5,2,6,3,9,1,7,3,8,4]",
        "output": "Output: [5,6,2,3,9,1,4,8,3,7]",
        "explanation": ""
      },
      {
        "input": "Input: head = [1,1,0,6]",
        "output": "Output: [1,0,1,6]",
        "explanation": ""
      },
      {
        "input": "Input: head = [1,1,0,6,5]",
        "output": "Output: [1,0,1,5,6]",
        "explanation": ""
      }
    ],
    "topics": [
      "Linked List"
    ],
    "difficulty": "Medium",
    "constraints": [
      "The number of nodes in the list is in the range [1, 105].",
      "0 <= Node.val <= 105"
    ],
    "hints": [
      "Consider the list structure ...A → (B → ... → C) → D..., where the nodes between B and C (inclusive) form a group, A is the last node of the previous group, and D is the first node of the next group. How can you utilize this structure?",
      "Suppose you have B → ... → C reversed (because it was of even length) so that it is now C → ... → B. What references do you need to fix so that the transitions between the previous, current, and next groups are correct?",
      "A.next should be set to C, and B.next should be set to D.",
      "Once the current group is finished being modified, you need to find the new A, B, C, and D nodes for the next group. How can you use the old A, B, C, and D nodes to find the new ones?",
      "The new A is either the old B or old C depending on if the group was of even or odd length. The new B is always the old D. The new C and D can be found based on the new B and the next group's length.",
      "You can set the initial values of A, B, C, and D to A = null, B = head, C = head, D = head.next. Repeat the steps from the previous hints until D is null."
    ]
  },
  {
    "title": "Time Needed to Buy Tickets",
    "description": "There are n people in a line queuing to buy tickets, where the 0th person is at the front of the line and the (n - 1)th person is at the back of the line.\nYou are given a 0-indexed integer array tickets of length n where the number of tickets that the ith person would like to buy is tickets[i].\nEach person takes exactly 1 second to buy a ticket. A person can only buy 1 ticket at a time and has to go back to the end of the line (which happens instantaneously) in order to buy more tickets. If a person does not have any tickets left to buy, the person will leave the line.\nReturn the time taken for the person at position k (0-indexed) to finish buying tickets.\n \n",
    "examples": [
      {
        "input": "Input: tickets = [2,3,2], k = 2",
        "output": "Output: 6",
        "explanation": "Explanation: "
      },
      {
        "input": "Input: tickets = [5,1,1,1], k = 0",
        "output": "Output: 8",
        "explanation": ""
      }
    ],
    "topics": [
      "Array",
      "Queue",
      "Simulation"
    ],
    "difficulty": "Easy",
    "constraints": [
      "n == tickets.length",
      "1 <= n <= 100",
      "1 <= tickets[i] <= 100",
      "0 <= k < n"
    ],
    "hints": [
      "Loop through the line of people and decrement the number of tickets for each to buy one at a time as if simulating the line moving forward. Keep track of how many tickets have been sold up until person k has no more tickets to buy.",
      "Remember that those who have no more tickets to buy will leave the line."
    ]
  },
  {
    "title": "Count Fertile Pyramids in a Land",
    "description": "A farmer has a rectangular grid of land with m rows and n columns that can be divided into unit cells. Each cell is either fertile (represented by a 1) or barren (represented by a 0). All cells outside the grid are considered barren.\nA pyramidal plot of land can be defined as a set of cells with the following criteria:\n\nThe number of cells in the set has to be greater than 1 and all cells must be fertile.\nThe apex of a pyramid is the topmost cell of the pyramid. The height of a pyramid is the number of rows it covers. Let (r, c) be the apex of the pyramid, and its height be h. Then, the plot comprises of cells (i, j) where r <= i <= r + h - 1 and c - (i - r) <= j <= c + (i - r).\n\nAn inverse pyramidal plot of land can be defined as a set of cells with similar criteria:\n\nThe number of cells in the set has to be greater than 1 and all cells must be fertile.\nThe apex of an inverse pyramid is the bottommost cell of the inverse pyramid. The height of an inverse pyramid is the number of rows it covers. Let (r, c) be the apex of the pyramid, and its height be h. Then, the plot comprises of cells (i, j) where r - h + 1 <= i <= r and c - (r - i) <= j <= c + (r - i).\n\nSome examples of valid and invalid pyramidal (and inverse pyramidal) plots are shown below. Black cells indicate fertile cells.\n\nGiven a 0-indexed m x n binary matrix grid representing the farmland, return the total number of pyramidal and inverse pyramidal plots that can be found in grid.\n \n",
    "examples": [
      {
        "input": "Input: grid = [[0,1,1,0],[1,1,1,1]]",
        "output": "Output: 2",
        "explanation": "Explanation: The 2 possible pyramidal plots are shown in blue and red respectively."
      },
      {
        "input": "Input: grid = [[1,1,1],[1,1,1]]",
        "output": "Output: 2",
        "explanation": "Explanation: The pyramidal plot is shown in blue, and the inverse pyramidal plot is shown in red. "
      },
      {
        "input": "Input: grid = [[1,1,1,1,0],[1,1,1,1,1],[1,1,1,1,1],[0,1,0,0,1]]",
        "output": "Output: 13",
        "explanation": "Explanation: There are 7 pyramidal plots, 3 of which are shown in the 2nd and 3rd figures."
      }
    ],
    "topics": [
      "Array",
      "Dynamic Programming",
      "Matrix"
    ],
    "difficulty": "Hard",
    "constraints": [
      "m == grid.length",
      "n == grid[i].length",
      "1 <= m, n <= 1000",
      "1 <= m * n <= 105",
      "grid[i][j] is either 0 or 1."
    ],
    "hints": [
      "Think about how dynamic programming can help solve the problem.",
      "For any fixed cell (r, c), can you calculate the maximum height of the pyramid for which it is the apex? Let us denote this value as dp[r][c].",
      "How will the values at dp[r+1][c-1] and dp[r+1][c+1] help in determining the value at dp[r][c]?",
      "For the cell (r, c), is there a relation between the number of pyramids for which it serves as the apex and dp[r][c]? How does it help in calculating the answer?"
    ]
  },
  {
    "title": "Minimum Cost Homecoming of a Robot in a Grid",
    "description": "There is an m x n grid, where (0, 0) is the top-left cell and (m - 1, n - 1) is the bottom-right cell. You are given an integer array startPos where startPos = [startrow, startcol] indicates that initially, a robot is at the cell (startrow, startcol). You are also given an integer array homePos where homePos = [homerow, homecol] indicates that its home is at the cell (homerow, homecol).\nThe robot needs to go to its home. It can move one cell in four directions: left, right, up, or down, and it can not move outside the boundary. Every move incurs some cost. You are further given two 0-indexed integer arrays: rowCosts of length m and colCosts of length n.\n\nIf the robot moves up or down into a cell whose row is r, then this move costs rowCosts[r].\nIf the robot moves left or right into a cell whose column is c, then this move costs colCosts[c].\n\nReturn the minimum total cost for this robot to return home.\n \n",
    "examples": [
      {
        "input": "Input: startPos = [1, 0], homePos = [2, 3], rowCosts = [5, 4, 3], colCosts = [8, 2, 6, 7]",
        "output": "Output: 18",
        "explanation": "Explanation: One optimal path is that:"
      },
      {
        "input": "Input: startPos = [0, 0], homePos = [0, 0], rowCosts = [5], colCosts = [26]",
        "output": "Output: 0",
        "explanation": "Explanation: The robot is already at its home. Since no moves occur, the total cost is 0."
      }
    ],
    "topics": [
      "Array",
      "Greedy",
      "Matrix"
    ],
    "difficulty": "Medium",
    "constraints": [
      "m == rowCosts.length",
      "n == colCosts.length",
      "1 <= m, n <= 105",
      "0 <= rowCosts[r], colCosts[c] <= 104",
      "startPos.length == 2",
      "homePos.length == 2",
      "0 <= startrow, homerow < m",
      "0 <= startcol, homecol < n"
    ],
    "hints": [
      "Irrespective of what path the robot takes, it will have to traverse all the rows between startRow and homeRow and all the columns between startCol and homeCol.",
      "Hence, making any other move other than traversing the required rows and columns will potentially incur more cost which can be avoided."
    ]
  },
  {
    "title": "Minimum Number of Food Buckets to Feed the Hamsters",
    "description": "You are given a 0-indexed string hamsters where hamsters[i] is either:\n\n'H' indicating that there is a hamster at index i, or\n'.' indicating that index i is empty.\n\nYou will add some number of food buckets at the empty indices in order to feed the hamsters. A hamster can be fed if there is at least one food bucket to its left or to its right. More formally, a hamster at index i can be fed if you place a food bucket at index i - 1 and/or at index i + 1.\nReturn the minimum number of food buckets you should place at empty indices to feed all the hamsters or -1 if it is impossible to feed all of them.\n \n",
    "examples": [
      {
        "input": "Input: hamsters = \"H..H\"",
        "output": "Output: 2",
        "explanation": "Explanation: We place two food buckets at indices 1 and 2."
      },
      {
        "input": "Input: hamsters = \".H.H.\"",
        "output": "Output: 1",
        "explanation": "Explanation: We place one food bucket at index 2."
      },
      {
        "input": "Input: hamsters = \".HHH.\"",
        "output": "Output: -1",
        "explanation": "Explanation: If we place a food bucket at every empty index as shown, the hamster at index 2 will not be able to eat."
      }
    ],
    "topics": [
      "String",
      "Dynamic Programming",
      "Greedy"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= hamsters.length <= 105",
      "hamsters[i] is either'H' or '.'."
    ],
    "hints": [
      "When is it impossible to collect the rainwater from all the houses?",
      "When one or more houses do not have an empty space adjacent to it.",
      "Assuming the rainwater from all previous houses is collected. If there is a house at index i and you are able to place a bucket at index i - 1 or i + 1, where should you put it?",
      "It is always better to place a bucket at index i + 1 because it can collect the rainwater from the next house as well."
    ]
  },
  {
    "title": "Count Common Words With One Occurrence",
    "description": "Given two string arrays words1 and words2, return the number of strings that appear exactly once in each of the two arrays.\n \n",
    "examples": [
      {
        "input": "Input: words1 = [\"leetcode\",\"is\",\"amazing\",\"as\",\"is\"], words2 = [\"amazing\",\"leetcode\",\"is\"]",
        "output": "Output: 2",
        "explanation": ""
      },
      {
        "input": "Input: words1 = [\"b\",\"bb\",\"bbb\"], words2 = [\"a\",\"aa\",\"aaa\"]",
        "output": "Output: 0",
        "explanation": "Explanation: There are no strings that appear in each of the two arrays."
      },
      {
        "input": "Input: words1 = [\"a\",\"ab\"], words2 = [\"a\",\"a\",\"a\",\"ab\"]",
        "output": "Output: 1",
        "explanation": "Explanation: The only string that appears exactly once in each of the two arrays is \"ab\"."
      }
    ],
    "topics": [
      "Array",
      "Hash Table",
      "String",
      "Counting"
    ],
    "difficulty": "Easy",
    "constraints": [
      "1 <= words1.length, words2.length <= 1000",
      "1 <= words1[i].length, words2[j].length <= 30",
      "words1[i] and words2[j] consists only of lowercase English letters."
    ],
    "hints": [
      "Could you try every word?",
      "Could you use a hash map to achieve a good complexity?"
    ]
  },
  {
    "title": "Maximum Path Quality of a Graph",
    "description": "There is an undirected graph with n nodes numbered from 0 to n - 1 (inclusive). You are given a 0-indexed integer array values where values[i] is the value of the ith node. You are also given a 0-indexed 2D integer array edges, where each edges[j] = [uj, vj, timej] indicates that there is an undirected edge between the nodes uj and vj, and it takes timej seconds to travel between the two nodes. Finally, you are given an integer maxTime.\nA valid path in the graph is any path that starts at node 0, ends at node 0, and takes at most maxTime seconds to complete. You may visit the same node multiple times. The quality of a valid path is the sum of the values of the unique nodes visited in the path (each node's value is added at most once to the sum).\nReturn the maximum quality of a valid path.\nNote: There are at most four edges connected to each node.\n \n",
    "examples": [
      {
        "input": "Input: values = [0,32,10,43], edges = [[0,1,10],[1,2,15],[0,3,10]], maxTime = 49",
        "output": "Output: 75",
        "explanation": ""
      },
      {
        "input": "Input: values = [5,10,15,20], edges = [[0,1,10],[1,2,10],[0,3,10]], maxTime = 30",
        "output": "Output: 25",
        "explanation": ""
      },
      {
        "input": "Input: values = [1,2,3,4], edges = [[0,1,10],[1,2,11],[2,3,12],[1,3,13]], maxTime = 50",
        "output": "Output: 7",
        "explanation": ""
      }
    ],
    "topics": [
      "Array",
      "Backtracking",
      "Graph"
    ],
    "difficulty": "Hard",
    "constraints": [
      "n == values.length",
      "1 <= n <= 1000",
      "0 <= values[i] <= 108",
      "0 <= edges.length <= 2000",
      "edges[j].length == 3 ",
      "0 <= uj < vj <= n - 1",
      "10 <= timej, maxTime <= 100",
      "All the pairs [uj, vj] are unique.",
      "There are at most four edges connected to each node.",
      "The graph may not be connected."
    ],
    "hints": [
      "How many nodes can you visit within maxTime seconds?",
      "Can you try every valid path?"
    ]
  },
  {
    "title": "Minimized Maximum of Products Distributed to Any Store",
    "description": "You are given an integer n indicating there are n specialty retail stores. There are m product types of varying amounts, which are given as a 0-indexed integer array quantities, where quantities[i] represents the number of products of the ith product type.\nYou need to distribute all products to the retail stores following these rules:\n\nA store can only be given at most one product type but can be given any amount of it.\nAfter distribution, each store will have been given some number of products (possibly 0). Let x represent the maximum number of products given to any store. You want x to be as small as possible, i.e., you want to minimize the maximum number of products that are given to any store.\n\nReturn the minimum possible x.\n \n",
    "examples": [
      {
        "input": "Input: n = 6, quantities = [11,6]",
        "output": "Output: 3",
        "explanation": "Explanation: One optimal way is:"
      },
      {
        "input": "Input: n = 7, quantities = [15,10,10]",
        "output": "Output: 5",
        "explanation": "Explanation: One optimal way is:"
      },
      {
        "input": "Input: n = 1, quantities = [100000]",
        "output": "Output: 100000",
        "explanation": "Explanation: The only optimal way is:"
      }
    ],
    "topics": [
      "Array",
      "Binary Search"
    ],
    "difficulty": "Medium",
    "constraints": [
      "m == quantities.length",
      "1 <= m <= n <= 105",
      "1 <= quantities[i] <= 105"
    ],
    "hints": [
      "There exists a monotonic nature such that when x is smaller than some number, there will be no way to distribute, and when x is not smaller than that number, there will always be a way to distribute.",
      "If you are given a number k, where the number of products given to any store does not exceed k, could you determine if all products can be distributed?",
      "Implement a function canDistribute(k), which returns true if you can distribute all products such that any store will not be given more than k products, and returns false if you cannot. Use this function to binary search for the smallest possible k."
    ]
  },
  {
    "title": "Vowels of All Substrings",
    "description": "Given a string word, return the sum of the number of vowels ('a', 'e', 'i', 'o', and 'u') in every substring of word.\nA substring is a contiguous (non-empty) sequence of characters within a string.\nNote: Due to the large constraints, the answer may not fit in a signed 32-bit integer. Please be careful during the calculations.\n \n",
    "examples": [
      {
        "input": "Input: word = \"aba\"",
        "output": "Output: 6",
        "explanation": "Explanation: "
      },
      {
        "input": "Input: word = \"abc\"",
        "output": "Output: 3",
        "explanation": "Explanation: "
      },
      {
        "input": "Input: word = \"ltcd\"",
        "output": "Output: 0",
        "explanation": "Explanation: There are no vowels in any substring of \"ltcd\"."
      }
    ],
    "topics": [
      "Math",
      "String",
      "Dynamic Programming",
      "Combinatorics"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= word.length <= 105",
      "word consists of lowercase English letters."
    ],
    "hints": [
      "Since generating substrings is not an option, can we count the number of substrings a vowel appears in?",
      "How much does each vowel contribute to the total sum?"
    ]
  },
  {
    "title": "Count Vowel Substrings of a String",
    "description": "A substring is a contiguous (non-empty) sequence of characters within a string.\nA vowel substring is a substring that only consists of vowels ('a', 'e', 'i', 'o', and 'u') and has all five vowels present in it.\nGiven a string word, return the number of vowel substrings in word.\n \n",
    "examples": [
      {
        "input": "Input: word = \"aeiouu\"",
        "output": "Output: 2",
        "explanation": "Explanation: The vowel substrings of word are as follows (underlined):"
      },
      {
        "input": "Input: word = \"unicornarihan\"",
        "output": "Output: 0",
        "explanation": "Explanation: Not all 5 vowels are present, so there are no vowel substrings."
      },
      {
        "input": "Input: word = \"cuaieuouac\"",
        "output": "Output: 7",
        "explanation": "Explanation: The vowel substrings of word are as follows (underlined):"
      }
    ],
    "topics": [
      "Hash Table",
      "String"
    ],
    "difficulty": "Easy",
    "constraints": [
      "1 <= word.length <= 100",
      "word consists of lowercase English letters only."
    ],
    "hints": [
      "While generating substrings starting at any index, do you need to continue generating larger substrings if you encounter a consonant?",
      "Can you store the count of characters to avoid generating substrings altogether?"
    ]
  },
  {
    "title": "Check if an Original String Exists Given Two Encoded Strings",
    "description": "An original string, consisting of lowercase English letters, can be encoded by the following steps:\n\nArbitrarily split it into a sequence of some number of non-empty substrings.\nArbitrarily choose some elements (possibly none) of the sequence, and replace each with its length (as a numeric string).\nConcatenate the sequence as the encoded string.\n\nFor example, one way to encode an original string \"abcdefghijklmnop\" might be:\n\nSplit it as a sequence: [\"ab\", \"cdefghijklmn\", \"o\", \"p\"].\nChoose the second and third elements to be replaced by their lengths, respectively. The sequence becomes [\"ab\", \"12\", \"1\", \"p\"].\nConcatenate the elements of the sequence to get the encoded string: \"ab121p\".\n\nGiven two encoded strings s1 and s2, consisting of lowercase English letters and digits 1-9 (inclusive), return true if there exists an original string that could be encoded as both s1 and s2. Otherwise, return false.\nNote: The test cases are generated such that the number of consecutive digits in s1 and s2 does not exceed 3.\n \n",
    "examples": [
      {
        "input": "Input: s1 = \"internationalization\", s2 = \"i18n\"",
        "output": "Output: true",
        "explanation": "Explanation: It is possible that \"internationalization\" was the original string."
      },
      {
        "input": "Input: s1 = \"l123e\", s2 = \"44\"",
        "output": "Output: true",
        "explanation": "Explanation: It is possible that \"leetcode\" was the original string."
      },
      {
        "input": "Input: s1 = \"a5b\", s2 = \"c5b\"",
        "output": "Output: false",
        "explanation": "Explanation: It is impossible."
      }
    ],
    "topics": [
      "String",
      "Dynamic Programming"
    ],
    "difficulty": "Hard",
    "constraints": [
      "1 <= s1.length, s2.length <= 40",
      "s1 and s2 consist of digits 1-9 (inclusive), and lowercase English letters only.",
      "The number of consecutive digits in s1 and s2 does not exceed 3."
    ],
    "hints": [
      "For s1 and s2, divide each into a sequence of single alphabet strings and digital strings. The problem now becomes comparing if two sequences are equal.",
      "A single alphabet string has no variation, but a digital string has variations. For example: \"124\" can be interpreted as 1+2+4, 12+4, 1+24, and 124 wildcard characters.",
      "There are four kinds of comparisons: a single alphabet vs another; a single alphabet vs a number, a number vs a single alphabet, and a number vs another number. In the case of a number vs another (a single alphabet or a number), can you decrease the number by the min length of both?",
      "There is a recurrence relation in the search which ends when either a single alphabet != another, or one sequence ran out, or both sequences ran out."
    ]
  },
  {
    "title": "Minimum Operations to Convert Number",
    "description": "You are given a 0-indexed integer array nums containing distinct numbers, an integer start, and an integer goal. There is an integer x that is initially set to start, and you want to perform operations on x such that it is converted to goal. You can perform the following operation repeatedly on the number x:\nIf 0 <= x <= 1000, then for any index i in the array (0 <= i < nums.length), you can set x to any of the following:\n\nx + nums[i]\nx - nums[i]\nx ^ nums[i] (bitwise-XOR)\n\nNote that you can use each nums[i] any number of times in any order. Operations that set x to be out of the range 0 <= x <= 1000 are valid, but no more operations can be done afterward.\nReturn the minimum number of operations needed to convert x = start into goal, and -1 if it is not possible.\n \n",
    "examples": [
      {
        "input": "Input: nums = [2,4,12], start = 2, goal = 12",
        "output": "Output: 2",
        "explanation": "Explanation: We can go from 2 → 14 → 12 with the following 2 operations."
      },
      {
        "input": "Input: nums = [3,5,7], start = 0, goal = -4",
        "output": "Output: 2",
        "explanation": "Explanation: We can go from 0 → 3 → -4 with the following 2 operations. "
      },
      {
        "input": "Input: nums = [2,8,16], start = 0, goal = 1",
        "output": "Output: -1",
        "explanation": "Explanation: There is no way to convert 0 into 1."
      }
    ],
    "topics": [
      "Array",
      "Breadth-First Search"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= nums.length <= 1000",
      "-109 <= nums[i], goal <= 109",
      "0 <= start <= 1000",
      "start != goal",
      "All the integers in nums are distinct."
    ],
    "hints": [
      "Once x drops below 0 or goes above 1000, is it possible to continue performing operations on x?",
      "How can you use BFS to find the minimum operations?"
    ]
  },
  {
    "title": "Find the Minimum and Maximum Number of Nodes Between Critical Points",
    "description": "A critical point in a linked list is defined as either a local maxima or a local minima.\nA node is a local maxima if the current node has a value strictly greater than the previous node and the next node.\nA node is a local minima if the current node has a value strictly smaller than the previous node and the next node.\nNote that a node can only be a local maxima/minima if there exists both a previous node and a next node.\nGiven a linked list head, return an array of length 2 containing [minDistance, maxDistance] where minDistance is the minimum distance between any two distinct critical points and maxDistance is the maximum distance between any two distinct critical points. If there are fewer than two critical points, return [-1, -1].\n \n",
    "examples": [
      {
        "input": "Input: head = [3,1]",
        "output": "Output: [-1,-1]",
        "explanation": "Explanation: There are no critical points in [3,1]."
      },
      {
        "input": "Input: head = [5,3,1,2,5,1,2]",
        "output": "Output: [1,3]",
        "explanation": "Explanation: There are three critical points:"
      },
      {
        "input": "Input: head = [1,3,2,2,3,2,2,2,7]",
        "output": "Output: [3,3]",
        "explanation": "Explanation: There are two critical points:"
      }
    ],
    "topics": [
      "Linked List"
    ],
    "difficulty": "Medium",
    "constraints": [
      "The number of nodes in the list is in the range [2, 105].",
      "1 <= Node.val <= 105"
    ],
    "hints": [
      "The maximum distance must be the distance between the first and last critical point.",
      "For each adjacent critical point, calculate the difference and check if it is the minimum distance."
    ]
  },
  {
    "title": "Smallest Index With Equal Value",
    "description": "Given a 0-indexed integer array nums, return the smallest index i of nums such that i mod 10 == nums[i], or -1 if such index does not exist.\nx mod y denotes the remainder when x is divided by y.\n \n",
    "examples": [
      {
        "input": "Input: nums = [0,1,2]",
        "output": "Output: 0",
        "explanation": "Explanation: "
      },
      {
        "input": "Input: nums = [4,3,2,1]",
        "output": "Output: 2",
        "explanation": "Explanation: "
      },
      {
        "input": "Input: nums = [1,2,3,4,5,6,7,8,9,0]",
        "output": "Output: -1",
        "explanation": "Explanation: No index satisfies i mod 10 == nums[i]."
      }
    ],
    "topics": [
      "Array"
    ],
    "difficulty": "Easy",
    "constraints": [
      "1 <= nums.length <= 100",
      "0 <= nums[i] <= 9"
    ],
    "hints": [
      "Starting with i=0, check the condition for each index. The first one you find to be true is the smallest index."
    ]
  },
  {
    "title": "Maximum Number of Tasks You Can Assign",
    "description": "You have n tasks and m workers. Each task has a strength requirement stored in a 0-indexed integer array tasks, with the ith task requiring tasks[i] strength to complete. The strength of each worker is stored in a 0-indexed integer array workers, with the jth worker having workers[j] strength. Each worker can only be assigned to a single task and must have a strength greater than or equal to the task's strength requirement (i.e., workers[j] >= tasks[i]).\nAdditionally, you have pills magical pills that will increase a worker's strength by strength. You can decide which workers receive the magical pills, however, you may only give each worker at most one magical pill.\nGiven the 0-indexed integer arrays tasks and workers and the integers pills and strength, return the maximum number of tasks that can be completed.\n \n",
    "examples": [
      {
        "input": "Input: tasks = [3,2,1], workers = [0,3,3], pills = 1, strength = 1",
        "output": "Output: 3",
        "explanation": ""
      },
      {
        "input": "Input: tasks = [5,4], workers = [0,0,0], pills = 1, strength = 5",
        "output": "Output: 1",
        "explanation": ""
      },
      {
        "input": "Input: tasks = [10,15,30], workers = [0,10,10,10,10], pills = 3, strength = 10",
        "output": "Output: 2",
        "explanation": ""
      }
    ],
    "topics": [
      "Array",
      "Binary Search",
      "Greedy",
      "Queue",
      "Sorting",
      "Monotonic Queue"
    ],
    "difficulty": "Hard",
    "constraints": [
      "n == tasks.length",
      "m == workers.length",
      "1 <= n, m <= 5 * 104",
      "0 <= pills <= m",
      "0 <= tasks[i], workers[j], strength <= 109"
    ],
    "hints": [
      "Is it possible to assign the first k smallest tasks to the workers?",
      "How can you efficiently try every k?"
    ]
  },
  {
    "title": "Most Beautiful Item for Each Query",
    "description": "You are given a 2D integer array items where items[i] = [pricei, beautyi] denotes the price and beauty of an item respectively.\nYou are also given a 0-indexed integer array queries. For each queries[j], you want to determine the maximum beauty of an item whose price is less than or equal to queries[j]. If no such item exists, then the answer to this query is 0.\nReturn an array answer of the same length as queries where answer[j] is the answer to the jth query.\n \n",
    "examples": [
      {
        "input": "Input: items = [[1,2],[3,2],[2,4],[5,6],[3,5]], queries = [1,2,3,4,5,6]",
        "output": "Output: [2,4,5,5,6,6]",
        "explanation": ""
      },
      {
        "input": "Input: items = [[1,2],[1,2],[1,3],[1,4]], queries = [1]",
        "output": "Output: [4]",
        "explanation": "Explanation: "
      },
      {
        "input": "Input: items = [[10,1000]], queries = [5]",
        "output": "Output: [0]",
        "explanation": ""
      }
    ],
    "topics": [
      "Array",
      "Binary Search",
      "Sorting"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= items.length, queries.length <= 105",
      "items[i].length == 2",
      "1 <= pricei, beautyi, queries[j] <= 109"
    ],
    "hints": [
      "Can we process the queries in a smart order to avoid repeatedly checking the same items?",
      "How can we use the answer to a query for other queries?"
    ]
  },
  {
    "title": "Walking Robot Simulation II",
    "description": "A width x height grid is on an XY-plane with the bottom-left cell at (0, 0) and the top-right cell at (width - 1, height - 1). The grid is aligned with the four cardinal directions (\"North\", \"East\", \"South\", and \"West\"). A robot is initially at cell (0, 0) facing direction \"East\".\nThe robot can be instructed to move for a specific number of steps. For each step, it does the following.\n\nAttempts to move forward one cell in the direction it is facing.\nIf the cell the robot is moving to is out of bounds, the robot instead turns 90 degrees counterclockwise and retries the step.\n\nAfter the robot finishes moving the number of steps required, it stops and awaits the next instruction.\nImplement the Robot class:\n\nRobot(int width, int height) Initializes the width x height grid with the robot at (0, 0) facing \"East\".\nvoid step(int num) Instructs the robot to move forward num steps.\nint[] getPos() Returns the current cell the robot is at, as an array of length 2, [x, y].\nString getDir() Returns the current direction of the robot, \"North\", \"East\", \"South\", or \"West\".\n\n \n",
    "examples": [
      {
        "input": "Input\n[\"Robot\", \"step\", \"step\", \"getPos\", \"getDir\", \"step\", \"step\", \"step\", \"getPos\", \"getDir\"]",
        "output": "Output\n[null, null, null, [4, 0], \"East\", null, null, null, [1, 2], \"West\"]",
        "explanation": "Explanation\nRobot robot = new Robot(6, 3); // Initialize the grid and the robot at (0, 0) facing East."
      }
    ],
    "topics": [
      "Design",
      "Simulation"
    ],
    "difficulty": "Medium",
    "constraints": [
      "2 <= width, height <= 100",
      "1 <= num <= 105",
      "At most 104 calls in total will be made to step, getPos, and getDir."
    ],
    "hints": [
      "The robot only moves along the perimeter of the grid. Can you think if modulus can help you quickly compute which cell it stops at?",
      "After the robot moves one time, whenever the robot stops at some cell, it will always face a specific direction. i.e., The direction it faces is determined by the cell it stops at.",
      "Can you precompute what direction it faces when it stops at each cell along the perimeter, and reuse the results?"
    ]
  },
  {
    "title": "Check Whether Two Strings are Almost Equivalent",
    "description": "Two strings word1 and word2 are considered almost equivalent if the differences between the frequencies of each letter from 'a' to 'z' between word1 and word2 is at most 3.\nGiven two strings word1 and word2, each of length n, return true if word1 and word2 are almost equivalent, or false otherwise.\nThe frequency of a letter x is the number of times it occurs in the string.\n \n",
    "examples": [
      {
        "input": "Input: word1 = \"aaaa\", word2 = \"bccb\"",
        "output": "Output: false",
        "explanation": "Explanation: There are 4 'a's in \"aaaa\" but 0 'a's in \"bccb\"."
      },
      {
        "input": "Input: word1 = \"abcdeef\", word2 = \"abaaacc\"",
        "output": "Output: true",
        "explanation": "Explanation: The differences between the frequencies of each letter in word1 and word2 are at most 3:"
      },
      {
        "input": "Input: word1 = \"cccddabba\", word2 = \"babababab\"",
        "output": "Output: true",
        "explanation": "Explanation: The differences between the frequencies of each letter in word1 and word2 are at most 3:"
      }
    ],
    "topics": [
      "Hash Table",
      "String",
      "Counting"
    ],
    "difficulty": "Easy",
    "constraints": [
      "n == word1.length == word2.length",
      "1 <= n <= 100",
      "word1 and word2 consist only of lowercase English letters."
    ],
    "hints": [
      "What data structure can we use to count the frequency of each character?",
      "Are there edge cases where a character is present in one string but not the other?"
    ]
  },
  {
    "title": "Parallel Courses III",
    "description": "You are given an integer n, which indicates that there are n courses labeled from 1 to n. You are also given a 2D integer array relations where relations[j] = [prevCoursej, nextCoursej] denotes that course prevCoursej has to be completed before course nextCoursej (prerequisite relationship). Furthermore, you are given a 0-indexed integer array time where time[i] denotes how many months it takes to complete the (i+1)th course.\nYou must find the minimum number of months needed to complete all the courses following these rules:\n\nYou may start taking a course at any time if the prerequisites are met.\nAny number of courses can be taken at the same time.\n\nReturn the minimum number of months needed to complete all the courses.\nNote: The test cases are generated such that it is possible to complete every course (i.e., the graph is a directed acyclic graph).\n \n",
    "examples": [
      {
        "input": "Input: n = 3, relations = [[1,3],[2,3]], time = [3,2,5]",
        "output": "Output: 8",
        "explanation": "Explanation: The figure above represents the given graph and the time required to complete each course. "
      },
      {
        "input": "Input: n = 5, relations = [[1,5],[2,5],[3,5],[3,4],[4,5]], time = [1,2,3,4,5]",
        "output": "Output: 12",
        "explanation": "Explanation: The figure above represents the given graph and the time required to complete each course."
      }
    ],
    "topics": [
      "Array",
      "Dynamic Programming",
      "Graph",
      "Topological Sort"
    ],
    "difficulty": "Hard",
    "constraints": [
      "1 <= n <= 5 * 104",
      "0 <= relations.length <= min(n * (n - 1) / 2, 5 * 104)",
      "relations[j].length == 2",
      "1 <= prevCoursej, nextCoursej <= n",
      "prevCoursej != nextCoursej",
      "All the pairs [prevCoursej, nextCoursej] are unique.",
      "time.length == n",
      "1 <= time[i] <= 104",
      "The given graph is a directed acyclic graph."
    ],
    "hints": [
      "What is the earliest time a course can be taken?",
      "How would you solve the problem if all courses take equal time?",
      "How would you generalize this approach?"
    ]
  },
  {
    "title": "Count Nodes With the Highest Score",
    "description": "There is a binary tree rooted at 0 consisting of n nodes. The nodes are labeled from 0 to n - 1. You are given a 0-indexed integer array parents representing the tree, where parents[i] is the parent of node i. Since node 0 is the root, parents[0] == -1.\nEach node has a score. To find the score of a node, consider if the node and the edges connected to it were removed. The tree would become one or more non-empty subtrees. The size of a subtree is the number of the nodes in it. The score of the node is the product of the sizes of all those subtrees.\nReturn the number of nodes that have the highest score.\n \n",
    "examples": [
      {
        "input": "Input: parents = [-1,2,0,2,0]",
        "output": "Output: 3",
        "explanation": ""
      },
      {
        "input": "Input: parents = [-1,2,0]",
        "output": "Output: 2",
        "explanation": ""
      }
    ],
    "topics": [
      "Array",
      "Tree",
      "Depth-First Search",
      "Binary Tree"
    ],
    "difficulty": "Medium",
    "constraints": [
      "n == parents.length",
      "2 <= n <= 105",
      "parents[0] == -1",
      "0 <= parents[i] <= n - 1 for i != 0",
      "parents represents a valid binary tree."
    ],
    "hints": [
      "For each node, you need to find the sizes of the subtrees rooted in each of its children. Maybe DFS?",
      "How to determine the number of nodes in the rest of the tree? Can you subtract the size of the subtree rooted at the node from the total number of nodes of the tree?",
      "Use these values to compute the score of the node. Track the maximum score, and how many nodes achieve such score."
    ]
  },
  {
    "title": "Next Greater Numerically Balanced Number",
    "description": "An integer x is numerically balanced if for every digit d in the number x, there are exactly d occurrences of that digit in x.\nGiven an integer n, return the smallest numerically balanced number strictly greater than n.\n \n",
    "examples": [
      {
        "input": "Input: n = 1",
        "output": "Output: 22",
        "explanation": "Explanation: "
      },
      {
        "input": "Input: n = 1000",
        "output": "Output: 1333",
        "explanation": "Explanation: "
      },
      {
        "input": "Input: n = 3000",
        "output": "Output: 3133",
        "explanation": "Explanation: "
      }
    ],
    "topics": [
      "Math",
      "Backtracking",
      "Enumeration"
    ],
    "difficulty": "Medium",
    "constraints": [
      "0 <= n <= 106"
    ],
    "hints": [
      "How far away can the next greater numerically balanced number be from n?",
      "With the given constraints, what is the largest numerically balanced number?"
    ]
  },
  {
    "title": "Number of Valid Words in a Sentence",
    "description": "A sentence consists of lowercase letters ('a' to 'z'), digits ('0' to '9'), hyphens ('-'), punctuation marks ('!', '.', and ','), and spaces (' ') only. Each sentence can be broken down into one or more tokens separated by one or more spaces ' '.\nA token is a valid word if all three of the following are true:\n\nIt only contains lowercase letters, hyphens, and/or punctuation (no digits).\nThere is at most one hyphen '-'. If present, it must be surrounded by lowercase characters (\"a-b\" is valid, but \"-ab\" and \"ab-\" are not valid).\nThere is at most one punctuation mark. If present, it must be at the end of the token (\"ab,\", \"cd!\", and \".\" are valid, but \"a!b\" and \"c.,\" are not valid).\n\nExamples of valid words include \"a-b.\", \"afad\", \"ba-c\", \"a!\", and \"!\".\nGiven a string sentence, return the number of valid words in sentence.\n \n",
    "examples": [
      {
        "input": "Input: sentence = \"cat and  dog\"",
        "output": "Output: 3",
        "explanation": "Explanation: The valid words in the sentence are \"cat\", \"and\", and \"dog\"."
      },
      {
        "input": "Input: sentence = \"!this  1-s b8d!\"",
        "output": "Output: 0",
        "explanation": "Explanation: There are no valid words in the sentence."
      },
      {
        "input": "Input: sentence = \"alice and  bob are playing stone-game10\"",
        "output": "Output: 5",
        "explanation": "Explanation: The valid words in the sentence are \"alice\", \"and\", \"bob\", \"are\", and \"playing\"."
      }
    ],
    "topics": [
      "String"
    ],
    "difficulty": "Easy",
    "constraints": [
      "1 <= sentence.length <= 1000",
      "sentence only contains lowercase English letters, digits, ' ', '-', '!', '.', and ','.",
      "There will be at least 1 token."
    ],
    "hints": [
      "Iterate through the string to split it by spaces.",
      "Count the number of characters of each type (letters, numbers, hyphens, and punctuations)."
    ]
  },
  {
    "title": "Second Minimum Time to Reach Destination",
    "description": "A city is represented as a bi-directional connected graph with n vertices where each vertex is labeled from 1 to n (inclusive). The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself. The time taken to traverse any edge is time minutes.\nEach vertex has a traffic signal which changes its color from green to red and vice versa every change minutes. All signals change at the same time. You can enter a vertex at any time, but can leave a vertex only when the signal is green. You cannot wait at a vertex if the signal is green.\nThe second minimum value is defined as the smallest value strictly larger than the minimum value.\n\nFor example the second minimum value of [2, 3, 4] is 3, and the second minimum value of [2, 2, 4] is 4.\n\nGiven n, edges, time, and change, return the second minimum time it will take to go from vertex 1 to vertex n.\nNotes:\n\nYou can go through any vertex any number of times, including 1 and n.\nYou can assume that when the journey starts, all signals have just turned green.\n\n \n",
    "examples": [
      {
        "input": "Input: n = 5, edges = [[1,2],[1,3],[1,4],[3,4],[4,5]], time = 3, change = 5",
        "output": "Output: 13",
        "explanation": ""
      },
      {
        "input": "Input: n = 2, edges = [[1,2]], time = 3, change = 2",
        "output": "Output: 11",
        "explanation": ""
      }
    ],
    "topics": [
      "Breadth-First Search",
      "Graph",
      "Shortest Path"
    ],
    "difficulty": "Hard",
    "constraints": [
      "2 <= n <= 104",
      "n - 1 <= edges.length <= min(2 * 104, n * (n - 1) / 2)",
      "edges[i].length == 2",
      "1 <= ui, vi <= n",
      "ui != vi",
      "There are no duplicate edges.",
      "Each vertex can be reached directly or indirectly from every other vertex.",
      "1 <= time, change <= 103"
    ],
    "hints": [
      "How much is change actually necessary while calculating the required path?",
      "How many extra edges do we need to add to the shortest path?"
    ]
  },
  {
    "title": "Count Number of Maximum Bitwise-OR Subsets",
    "description": "Given an integer array nums, find the maximum possible bitwise OR of a subset of nums and return the number of different non-empty subsets with the maximum bitwise OR.\nAn array a is a subset of an array b if a can be obtained from b by deleting some (possibly zero) elements of b. Two subsets are considered different if the indices of the elements chosen are different.\nThe bitwise OR of an array a is equal to a[0] OR a[1] OR ... OR a[a.length - 1] (0-indexed).\n \n",
    "examples": [
      {
        "input": "Input: nums = [3,1]",
        "output": "Output: 2",
        "explanation": "Explanation: The maximum possible bitwise OR of a subset is 3. There are 2 subsets with a bitwise OR of 3:"
      },
      {
        "input": "Input: nums = [2,2,2]",
        "output": "Output: 7",
        "explanation": "Explanation: All non-empty subsets of [2,2,2] have a bitwise OR of 2. There are 23 - 1 = 7 total subsets."
      },
      {
        "input": "Input: nums = [3,2,1,5]",
        "output": "Output: 6",
        "explanation": "Explanation: The maximum possible bitwise OR of a subset is 7. There are 6 subsets with a bitwise OR of 7:"
      }
    ],
    "topics": [
      "Array",
      "Backtracking",
      "Bit Manipulation"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= nums.length <= 16",
      "1 <= nums[i] <= 105"
    ],
    "hints": [
      "Can we enumerate all possible subsets?",
      "The maximum bitwise-OR is the bitwise-OR of the whole array."
    ]
  },
  {
    "title": "Simple Bank System",
    "description": "You have been tasked with writing a program for a popular bank that will automate all its incoming transactions (transfer, deposit, and withdraw). The bank has n accounts numbered from 1 to n. The initial balance of each account is stored in a 0-indexed integer array balance, with the (i + 1)th account having an initial balance of balance[i].\nExecute all the valid transactions. A transaction is valid if:\n\nThe given account number(s) are between 1 and n, and\nThe amount of money withdrawn or transferred from is less than or equal to the balance of the account.\n\nImplement the Bank class:\n\nBank(long[] balance) Initializes the object with the 0-indexed integer array balance.\nboolean transfer(int account1, int account2, long money) Transfers money dollars from the account numbered account1 to the account numbered account2. Return true if the transaction was successful, false otherwise.\nboolean deposit(int account, long money) Deposit money dollars into the account numbered account. Return true if the transaction was successful, false otherwise.\nboolean withdraw(int account, long money) Withdraw money dollars from the account numbered account. Return true if the transaction was successful, false otherwise.\n\n \n",
    "examples": [
      {
        "input": "Input\n[\"Bank\", \"withdraw\", \"transfer\", \"deposit\", \"transfer\", \"withdraw\"]",
        "output": "Output\n[null, true, true, true, false, false]",
        "explanation": "Explanation\nBank bank = new Bank([10, 100, 20, 50, 30]);"
      }
    ],
    "topics": [
      "Array",
      "Hash Table",
      "Design",
      "Simulation"
    ],
    "difficulty": "Medium",
    "constraints": [
      "n == balance.length",
      "1 <= n, account, account1, account2 <= 105",
      "0 <= balance[i], money <= 1012",
      "At most 104 calls will be made to each function transfer, deposit, withdraw."
    ],
    "hints": [
      "How do you determine if a transaction will fail?",
      "Simply apply the operations if the transaction is valid."
    ]
  },
  {
    "title": "Check if Numbers Are Ascending in a Sentence",
    "description": "A sentence is a list of tokens separated by a single space with no leading or trailing spaces. Every token is either a positive number consisting of digits 0-9 with no leading zeros, or a word consisting of lowercase English letters.\n\nFor example, \"a puppy has 2 eyes 4 legs\" is a sentence with seven tokens: \"2\" and \"4\" are numbers and the other tokens such as \"puppy\" are words.\n\nGiven a string s representing a sentence, you need to check if all the numbers in s are strictly increasing from left to right (i.e., other than the last number, each number is strictly smaller than the number on its right in s).\nReturn true if so, or false otherwise.\n \n",
    "examples": [
      {
        "input": "Input: s = \"1 box has 3 blue 4 red 6 green and 12 yellow marbles\"",
        "output": "Output: true",
        "explanation": "Explanation: The numbers in s are: 1, 3, 4, 6, 12."
      },
      {
        "input": "Input: s = \"hello world 5 x 5\"",
        "output": "Output: false",
        "explanation": "Explanation: The numbers in s are: 5, 5. They are not strictly increasing."
      },
      {
        "input": "Input: s = \"sunset is at 7 51 pm overnight lows will be in the low 50 and 60 s\"",
        "output": "Output: false",
        "explanation": "Explanation: The numbers in s are: 7, 51, 50, 60. They are not strictly increasing."
      }
    ],
    "topics": [
      "String"
    ],
    "difficulty": "Easy",
    "constraints": [
      "3 <= s.length <= 200",
      "s consists of lowercase English letters, spaces, and digits from 0 to 9, inclusive.",
      "The number of tokens in s is between 2 and 100, inclusive.",
      "The tokens in s are separated by a single space.",
      "There are at least two numbers in s.",
      "Each number in s is a positive number less than 100, with no leading zeros.",
      "s contains no leading or trailing spaces."
    ],
    "hints": [
      "Use string tokenization of your language to extract all the tokens of the string easily.",
      "For each token extracted, how can you tell if it is a number? Does the first letter being a digit mean something?",
      "Compare the number with the previously occurring number to check if ascending order is maintained."
    ]
  },
  {
    "title": "Number of Valid Move Combinations On Chessboard",
    "description": "There is an 8 x 8 chessboard containing n pieces (rooks, queens, or bishops). You are given a string array pieces of length n, where pieces[i] describes the type (rook, queen, or bishop) of the ith piece. In addition, you are given a 2D integer array positions also of length n, where positions[i] = [ri, ci] indicates that the ith piece is currently at the 1-based coordinate (ri, ci) on the chessboard.\nWhen making a move for a piece, you choose a destination square that the piece will travel toward and stop on.\n\nA rook can only travel horizontally or vertically from (r, c) to the direction of (r+1, c), (r-1, c), (r, c+1), or (r, c-1).\nA queen can only travel horizontally, vertically, or diagonally from (r, c) to the direction of (r+1, c), (r-1, c), (r, c+1), (r, c-1), (r+1, c+1), (r+1, c-1), (r-1, c+1), (r-1, c-1).\nA bishop can only travel diagonally from (r, c) to the direction of (r+1, c+1), (r+1, c-1), (r-1, c+1), (r-1, c-1).\n\nYou must make a move for every piece on the board simultaneously. A move combination consists of all the moves performed on all the given pieces. Every second, each piece will instantaneously travel one square towards their destination if they are not already at it. All pieces start traveling at the 0th second. A move combination is invalid if, at a given time, two or more pieces occupy the same square.\nReturn the number of valid move combinations​​​​​.\nNotes:\n\nNo two pieces will start in the same square.\nYou may choose the square a piece is already on as its destination.\nIf two pieces are directly adjacent to each other, it is valid for them to move past each other and swap positions in one second.\n\n \n",
    "examples": [
      {
        "input": "Input: pieces = [\"rook\"], positions = [[1,1]]",
        "output": "Output: 15",
        "explanation": "Explanation: The image above shows the possible squares the piece can move to."
      },
      {
        "input": "Input: pieces = [\"queen\"], positions = [[1,1]]",
        "output": "Output: 22",
        "explanation": "Explanation: The image above shows the possible squares the piece can move to."
      },
      {
        "input": "Input: pieces = [\"bishop\"], positions = [[4,3]]",
        "output": "Output: 12",
        "explanation": "Explanation: The image above shows the possible squares the piece can move to."
      }
    ],
    "topics": [
      "Array",
      "String",
      "Backtracking",
      "Simulation"
    ],
    "difficulty": "Hard",
    "constraints": [
      "n == pieces.length ",
      "n == positions.length",
      "1 <= n <= 4",
      "pieces only contains the strings \"rook\", \"queen\", and \"bishop\".",
      "There will be at most one queen on the chessboard.",
      "1 <= xi, yi <= 8",
      "Each positions[i] is distinct."
    ],
    "hints": [
      "N is small, we can generate all possible move combinations.",
      "For each possible move combination, determine which ones are valid."
    ]
  },
  {
    "title": "Plates Between Candles",
    "description": "There is a long table with a line of plates and candles arranged on top of it. You are given a 0-indexed string s consisting of characters '*' and '|' only, where a '*' represents a plate and a '|' represents a candle.\nYou are also given a 0-indexed 2D integer array queries where queries[i] = [lefti, righti] denotes the substring s[lefti...righti] (inclusive). For each query, you need to find the number of plates between candles that are in the substring. A plate is considered between candles if there is at least one candle to its left and at least one candle to its right in the substring.\n\nFor example, s = \"||**||**|*\", and a query [3, 8] denotes the substring \"*||**|\". The number of plates between candles in this substring is 2, as each of the two plates has at least one candle in the substring to its left and right.\n\nReturn an integer array answer where answer[i] is the answer to the ith query.\n \n",
    "examples": [
      {
        "input": "Input: s = \"**|**|***|\", queries = [[2,5],[5,9]]",
        "output": "Output: [2,3]",
        "explanation": ""
      },
      {
        "input": "Input: s = \"***|**|*****|**||**|*\", queries = [[1,17],[4,5],[14,17],[5,11],[15,16]]",
        "output": "Output: [9,0,0,0,0]",
        "explanation": ""
      }
    ],
    "topics": [
      "Array",
      "String",
      "Binary Search",
      "Prefix Sum"
    ],
    "difficulty": "Medium",
    "constraints": [
      "3 <= s.length <= 105",
      "s consists of '*' and '|' characters.",
      "1 <= queries.length <= 105",
      "queries[i].length == 2",
      "0 <= lefti <= righti < s.length"
    ],
    "hints": [
      "Can you find the indices of the most left and right candles for a given substring, perhaps by using binary search (or better) over an array of indices of all the bars?",
      "Once the indices of the most left and right bars are determined, how can you efficiently count the number of plates within the range? Prefix sums?"
    ]
  },
  {
    "title": "Two Best Non-Overlapping Events",
    "description": "You are given a 0-indexed 2D integer array of events where events[i] = [startTimei, endTimei, valuei]. The ith event starts at startTimei and ends at endTimei, and if you attend this event, you will receive a value of valuei. You can choose at most two non-overlapping events to attend such that the sum of their values is maximized.\nReturn this maximum sum.\nNote that the start time and end time is inclusive: that is, you cannot attend two events where one of them starts and the other ends at the same time. More specifically, if you attend an event with end time t, the next event must start at or after t + 1.\n \n",
    "examples": [
      {
        "input": "Input: events = [[1,3,2],[4,5,2],[2,4,3]]",
        "output": "Output: 4",
        "explanation": "Explanation: Choose the green events, 0 and 1 for a sum of 2 + 2 = 4."
      },
      {
        "input": "Input: events = [[1,3,2],[4,5,2],[1,5,5]]",
        "output": "Output: 5",
        "explanation": "Explanation: Choose event 2 for a sum of 5."
      },
      {
        "input": "Input: events = [[1,5,3],[1,5,1],[6,6,5]]",
        "output": "Output: 8",
        "explanation": "Explanation: Choose events 0 and 2 for a sum of 3 + 5 = 8."
      }
    ],
    "topics": [
      "Array",
      "Binary Search",
      "Dynamic Programming",
      "Sorting",
      "Heap (Priority Queue)"
    ],
    "difficulty": "Medium",
    "constraints": [
      "2 <= events.length <= 105",
      "events[i].length == 3",
      "1 <= startTimei <= endTimei <= 109",
      "1 <= valuei <= 106"
    ],
    "hints": [
      "How can sorting the events on the basis of their start times help? How about end times?",
      "How can we quickly get the maximum score of an interval not intersecting with the interval we chose?"
    ]
  },
  {
    "title": "Kth Distinct String in an Array",
    "description": "A distinct string is a string that is present only once in an array.\nGiven an array of strings arr, and an integer k, return the kth distinct string present in arr. If there are fewer than k distinct strings, return an empty string \"\".\nNote that the strings are considered in the order in which they appear in the array.\n \n",
    "examples": [
      {
        "input": "Input: arr = [\"d\",\"b\",\"c\",\"b\",\"c\",\"a\"], k = 2",
        "output": "Output: \"a\"",
        "explanation": ""
      },
      {
        "input": "Input: arr = [\"aaa\",\"aa\",\"a\"], k = 1",
        "output": "Output: \"aaa\"",
        "explanation": ""
      },
      {
        "input": "Input: arr = [\"a\",\"b\",\"a\"], k = 3",
        "output": "Output: \"\"",
        "explanation": ""
      }
    ],
    "topics": [
      "Array",
      "Hash Table",
      "String",
      "Counting"
    ],
    "difficulty": "Easy",
    "constraints": [
      "1 <= k <= arr.length <= 1000",
      "1 <= arr[i].length <= 5",
      "arr[i] consists of lowercase English letters."
    ],
    "hints": [
      "Try 'mapping' the strings to check if they are unique or not."
    ]
  },
  {
    "title": "Partition Array Into Two Arrays to Minimize Sum Difference",
    "description": "You are given an integer array nums of 2 * n integers. You need to partition nums into two arrays of length n to minimize the absolute difference of the sums of the arrays. To partition nums, put each element of nums into one of the two arrays.\nReturn the minimum possible absolute difference.\n \n",
    "examples": [
      {
        "input": "Input: nums = [3,9,7,3]",
        "output": "Output: 2",
        "explanation": "Explanation: One optimal partition is: [3,9] and [7,3]."
      },
      {
        "input": "Input: nums = [-36,36]",
        "output": "Output: 72",
        "explanation": "Explanation: One optimal partition is: [-36] and [36]."
      },
      {
        "input": "Input: nums = [2,-1,0,4,-2,-9]",
        "output": "Output: 0",
        "explanation": "Explanation: One optimal partition is: [2,4,-9] and [-1,0,-2]."
      }
    ],
    "topics": [
      "Array",
      "Two Pointers",
      "Binary Search",
      "Dynamic Programming",
      "Bit Manipulation",
      "Ordered Set",
      "Bitmask"
    ],
    "difficulty": "Hard",
    "constraints": [
      "1 <= n <= 15",
      "nums.length == 2 * n",
      "-107 <= nums[i] <= 107"
    ],
    "hints": [
      "The target sum for the two partitions is sum(nums) / 2.",
      "Could you reduce the time complexity if you arbitrarily divide nums into two halves (two arrays)? Meet-in-the-Middle?",
      "For both halves, pre-calculate a 2D array where the kth index will store all possible sum values if only k elements from this half are added.",
      "For each sum of k elements in the first half, find the best sum of n-k elements in the second half such that the two sums add up to a value closest to the target sum from hint 1. These two subsets will form one array of the partition."
    ]
  },
  {
    "title": "Stock Price Fluctuation ",
    "description": "You are given a stream of records about a particular stock. Each record contains a timestamp and the corresponding price of the stock at that timestamp.\nUnfortunately due to the volatile nature of the stock market, the records do not come in order. Even worse, some records may be incorrect. Another record with the same timestamp may appear later in the stream correcting the price of the previous wrong record.\nDesign an algorithm that:\n\nUpdates the price of the stock at a particular timestamp, correcting the price from any previous records at the timestamp.\nFinds the latest price of the stock based on the current records. The latest price is the price at the latest timestamp recorded.\nFinds the maximum price the stock has been based on the current records.\nFinds the minimum price the stock has been based on the current records.\n\nImplement the StockPrice class:\n\nStockPrice() Initializes the object with no price records.\nvoid update(int timestamp, int price) Updates the price of the stock at the given timestamp.\nint current() Returns the latest price of the stock.\nint maximum() Returns the maximum price of the stock.\nint minimum() Returns the minimum price of the stock.\n\n \n",
    "examples": [
      {
        "input": "Input\n[\"StockPrice\", \"update\", \"update\", \"current\", \"maximum\", \"update\", \"maximum\", \"update\", \"minimum\"]",
        "output": "Output\n[null, null, null, 5, 10, null, 5, null, 2]",
        "explanation": "Explanation\nStockPrice stockPrice = new StockPrice();"
      }
    ],
    "topics": [
      "Hash Table",
      "Design",
      "Heap (Priority Queue)",
      "Data Stream",
      "Ordered Set"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= timestamp, price <= 109",
      "At most 105 calls will be made in total to update, current, maximum, and minimum.",
      "current, maximum, and minimum will be called only after update has been called at least once."
    ],
    "hints": [
      "How would you solve the problem for offline queries (all queries given at once)?",
      "Think about which data structure can help insert and delete the most optimal way."
    ]
  },
  {
    "title": "Minimum Operations to Make a Uni-Value Grid",
    "description": "You are given a 2D integer grid of size m x n and an integer x. In one operation, you can add x to or subtract x from any element in the grid.\nA uni-value grid is a grid where all the elements of it are equal.\nReturn the minimum number of operations to make the grid uni-value. If it is not possible, return -1.\n \n",
    "examples": [
      {
        "input": "Input: grid = [[2,4],[6,8]], x = 2",
        "output": "Output: 4",
        "explanation": "Explanation: We can make every element equal to 4 by doing the following: "
      },
      {
        "input": "Input: grid = [[1,5],[2,3]], x = 1",
        "output": "Output: 5",
        "explanation": "Explanation: We can make every element equal to 3."
      },
      {
        "input": "Input: grid = [[1,2],[3,4]], x = 2",
        "output": "Output: -1",
        "explanation": "Explanation: It is impossible to make every element equal."
      }
    ],
    "topics": [
      "Array",
      "Math",
      "Sorting",
      "Matrix"
    ],
    "difficulty": "Medium",
    "constraints": [
      "m == grid.length",
      "n == grid[i].length",
      "1 <= m, n <= 105",
      "1 <= m * n <= 105",
      "1 <= x, grid[i][j] <= 104"
    ],
    "hints": [
      "Is it possible to make two integers a and b equal if they have different remainders dividing by x?",
      "If it is possible, which number should you select to minimize the number of operations?",
      "What if the elements are sorted?"
    ]
  },
  {
    "title": "Two Out of Three",
    "description": "Given three integer arrays nums1, nums2, and nums3, return a distinct array containing all the values that are present in at least two out of the three arrays. You may return the values in any order.\n \n",
    "examples": [
      {
        "input": "Input: nums1 = [1,1,3,2], nums2 = [2,3], nums3 = [3]",
        "output": "Output: [3,2]",
        "explanation": "Explanation: The values that are present in at least two arrays are:"
      },
      {
        "input": "Input: nums1 = [3,1], nums2 = [2,3], nums3 = [1,2]",
        "output": "Output: [2,3,1]",
        "explanation": "Explanation: The values that are present in at least two arrays are:"
      },
      {
        "input": "Input: nums1 = [1,2,2], nums2 = [4,3,3], nums3 = [5]",
        "output": "Output: []",
        "explanation": "Explanation: No value is present in at least two arrays."
      }
    ],
    "topics": [
      "Array",
      "Hash Table"
    ],
    "difficulty": "Easy",
    "constraints": [
      "1 <= nums1.length, nums2.length, nums3.length <= 100",
      "1 <= nums1[i], nums2[j], nums3[k] <= 100"
    ],
    "hints": [
      "What data structure can we use to help us quickly find whether an element belongs in an array?",
      "Can we count the frequencies of the elements in each array?"
    ]
  },
  {
    "title": "Smallest K-Length Subsequence With Occurrences of a Letter",
    "description": "You are given a string s, an integer k, a letter letter, and an integer repetition.\nReturn the lexicographically smallest subsequence of s of length k that has the letter letter appear at least repetition times. The test cases are generated so that the letter appears in s at least repetition times.\nA subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.\nA string a is lexicographically smaller than a string b if in the first position where a and b differ, string a has a letter that appears earlier in the alphabet than the corresponding letter in b.\n \n",
    "examples": [
      {
        "input": "Input: s = \"leet\", k = 3, letter = \"e\", repetition = 1",
        "output": "Output: \"eet\"",
        "explanation": "Explanation: There are four subsequences of length 3 that have the letter 'e' appear at least 1 time:"
      },
      {
        "input": "Input: s = \"leetcode\", k = 4, letter = \"e\", repetition = 2",
        "output": "Output: \"ecde\"",
        "explanation": "Explanation: \"ecde\" is the lexicographically smallest subsequence of length 4 that has the letter \"e\" appear at least 2 times."
      },
      {
        "input": "Input: s = \"bb\", k = 2, letter = \"b\", repetition = 2",
        "output": "Output: \"bb\"",
        "explanation": "Explanation: \"bb\" is the only subsequence of length 2 that has the letter \"b\" appear at least 2 times."
      }
    ],
    "topics": [
      "String",
      "Stack",
      "Greedy",
      "Monotonic Stack"
    ],
    "difficulty": "Hard",
    "constraints": [
      "1 <= repetition <= k <= s.length <= 5 * 104",
      "s consists of lowercase English letters.",
      "letter is a lowercase English letter, and appears in s at least repetition times."
    ],
    "hints": [
      "Use stack. For every character to be appended, decide how many character(s) from the stack needs to get popped based on the stack length and the count of the required character.",
      "Pop the extra characters out from the stack and return the characters in the stack (reversed)."
    ]
  },
  {
    "title": "Stone Game IX",
    "description": "Alice and Bob continue their games with stones. There is a row of n stones, and each stone has an associated value. You are given an integer array stones, where stones[i] is the value of the ith stone.\nAlice and Bob take turns, with Alice starting first. On each turn, the player may remove any stone from stones. The player who removes a stone loses if the sum of the values of all removed stones is divisible by 3. Bob will win automatically if there are no remaining stones (even if it is Alice's turn).\nAssuming both players play optimally, return true if Alice wins and false if Bob wins.\n \n",
    "examples": [
      {
        "input": "Input: stones = [2,1]",
        "output": "Output: true",
        "explanation": ""
      },
      {
        "input": "Input: stones = [2]",
        "output": "Output: false",
        "explanation": ""
      },
      {
        "input": "Input: stones = [5,1,2,4,3]",
        "output": "Output: false",
        "explanation": "Explanation: Bob will always win. One possible way for Bob to win is shown below:"
      }
    ],
    "topics": [
      "Array",
      "Math",
      "Greedy",
      "Counting",
      "Game Theory"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= stones.length <= 105",
      "1 <= stones[i] <= 104"
    ],
    "hints": [
      "There are limited outcomes given the current sum and the stones remaining.",
      "Can we greedily simulate starting with taking a stone with remainder 1 or 2 divided by 3?"
    ]
  },
  {
    "title": "Find Missing Observations",
    "description": "You have observations of n + m 6-sided dice rolls with each face numbered from 1 to 6. n of the observations went missing, and you only have the observations of m rolls. Fortunately, you have also calculated the average value of the n + m rolls.\nYou are given an integer array rolls of length m where rolls[i] is the value of the ith observation. You are also given the two integers mean and n.\nReturn an array of length n containing the missing observations such that the average value of the n + m rolls is exactly mean. If there are multiple valid answers, return any of them. If no such array exists, return an empty array.\nThe average value of a set of k numbers is the sum of the numbers divided by k.\nNote that mean is an integer, so the sum of the n + m rolls should be divisible by n + m.\n \n",
    "examples": [
      {
        "input": "Input: rolls = [3,2,4,3], mean = 4, n = 2",
        "output": "Output: [6,6]",
        "explanation": "Explanation: The mean of all n + m rolls is (3 + 2 + 4 + 3 + 6 + 6) / 6 = 4."
      },
      {
        "input": "Input: rolls = [1,5,6], mean = 3, n = 4",
        "output": "Output: [2,3,2,2]",
        "explanation": "Explanation: The mean of all n + m rolls is (1 + 5 + 6 + 2 + 3 + 2 + 2) / 7 = 3."
      },
      {
        "input": "Input: rolls = [1,2,3,4], mean = 6, n = 4",
        "output": "Output: []",
        "explanation": "Explanation: It is impossible for the mean to be 6 no matter what the 4 missing rolls are."
      }
    ],
    "topics": [
      "Array",
      "Math",
      "Simulation"
    ],
    "difficulty": "Medium",
    "constraints": [
      "m == rolls.length",
      "1 <= n, m <= 105",
      "1 <= rolls[i], mean <= 6"
    ],
    "hints": [
      "What should the sum of the n rolls be?",
      "Could you generate an array of size n such that each element is between 1 and 6?"
    ]
  },
  {
    "title": "Minimum Moves to Convert String",
    "description": "You are given a string s consisting of n characters which are either 'X' or 'O'.\nA move is defined as selecting three consecutive characters of s and converting them to 'O'. Note that if a move is applied to the character 'O', it will stay the same.\nReturn the minimum number of moves required so that all the characters of s are converted to 'O'.\n \n",
    "examples": [
      {
        "input": "Input: s = \"XXX\"",
        "output": "Output: 1",
        "explanation": "Explanation: XXX -> OOO"
      },
      {
        "input": "Input: s = \"XXOX\"",
        "output": "Output: 2",
        "explanation": "Explanation: XXOX -> OOOX -> OOOO"
      },
      {
        "input": "Input: s = \"OOOO\"",
        "output": "Output: 0",
        "explanation": "Explanation: There are no 'X's in s to convert."
      }
    ],
    "topics": [
      "String",
      "Greedy"
    ],
    "difficulty": "Easy",
    "constraints": [
      "3 <= s.length <= 1000",
      "s[i] is either 'X' or 'O'."
    ],
    "hints": [
      "Find the smallest substring you need to consider at a time.",
      "Try delaying a move as long as possible."
    ]
  },
  {
    "title": "The Time When the Network Becomes Idle",
    "description": "There is a network of n servers, labeled from 0 to n - 1. You are given a 2D integer array edges, where edges[i] = [ui, vi] indicates there is a message channel between servers ui and vi, and they can pass any number of messages to each other directly in one second. You are also given a 0-indexed integer array patience of length n.\nAll servers are connected, i.e., a message can be passed from one server to any other server(s) directly or indirectly through the message channels.\nThe server labeled 0 is the master server. The rest are data servers. Each data server needs to send its message to the master server for processing and wait for a reply. Messages move between servers optimally, so every message takes the least amount of time to arrive at the master server. The master server will process all newly arrived messages instantly and send a reply to the originating server via the reversed path the message had gone through.\nAt the beginning of second 0, each data server sends its message to be processed. Starting from second 1, at the beginning of every second, each data server will check if it has received a reply to the message it sent (including any newly arrived replies) from the master server:\n\nIf it has not, it will resend the message periodically. The data server i will resend the message every patience[i] second(s), i.e., the data server i will resend the message if patience[i] second(s) have elapsed since the last time the message was sent from this server.\nOtherwise, no more resending will occur from this server.\n\nThe network becomes idle when there are no messages passing between servers or arriving at servers.\nReturn the earliest second starting from which the network becomes idle.\n \n",
    "examples": [
      {
        "input": "Input: edges = [[0,1],[1,2]], patience = [0,2,1]",
        "output": "Output: 8",
        "explanation": ""
      },
      {
        "input": "Input: edges = [[0,1],[0,2],[1,2]], patience = [0,10,10]",
        "output": "Output: 3",
        "explanation": "Explanation: Data servers 1 and 2 receive a reply back at the beginning of second 2."
      }
    ],
    "topics": [
      "Array",
      "Breadth-First Search",
      "Graph"
    ],
    "difficulty": "Medium",
    "constraints": [
      "n == patience.length",
      "2 <= n <= 105",
      "patience[0] == 0",
      "1 <= patience[i] <= 105 for 1 <= i < n",
      "1 <= edges.length <= min(105, n * (n - 1) / 2)",
      "edges[i].length == 2",
      "0 <= ui, vi < n",
      "ui != vi",
      "There are no duplicate edges.",
      "Each server can directly or indirectly reach another server."
    ],
    "hints": [
      "What method can you use to find the shortest time taken for a message from a data server to reach the master server? How can you use this value and the server's patience value to determine the time at which the server sends its last message?",
      "What is the time when the last message sent from a server gets back to the server?",
      "For each data server, by the time the server receives the first returned messages, how many messages has the server sent?"
    ]
  },
  {
    "title": "Kth Smallest Product of Two Sorted Arrays",
    "description": "Given two sorted 0-indexed integer arrays nums1 and nums2 as well as an integer k, return the kth (1-based) smallest product of nums1[i] * nums2[j] where 0 <= i < nums1.length and 0 <= j < nums2.length.\n \n",
    "examples": [
      {
        "input": "Input: nums1 = [2,5], nums2 = [3,4], k = 2",
        "output": "Output: 8",
        "explanation": "Explanation: The 2 smallest products are:"
      },
      {
        "input": "Input: nums1 = [-4,-2,0,3], nums2 = [2,4], k = 6",
        "output": "Output: 0",
        "explanation": "Explanation: The 6 smallest products are:"
      },
      {
        "input": "Input: nums1 = [-2,-1,0,1,2], nums2 = [-3,-1,2,4,5], k = 3",
        "output": "Output: -6",
        "explanation": "Explanation: The 3 smallest products are:"
      }
    ],
    "topics": [
      "Array",
      "Binary Search"
    ],
    "difficulty": "Hard",
    "constraints": [
      "1 <= nums1.length, nums2.length <= 5 * 104",
      "-105 <= nums1[i], nums2[j] <= 105",
      "1 <= k <= nums1.length * nums2.length",
      "nums1 and nums2 are sorted."
    ],
    "hints": [
      "Can we split this problem into four cases depending on the sign of the numbers?",
      "Can we binary search the value?"
    ]
  },
  {
    "title": "Remove Colored Pieces if Both Neighbors are the Same Color",
    "description": "There are n pieces arranged in a line, and each piece is colored either by 'A' or by 'B'. You are given a string colors of length n where colors[i] is the color of the ith piece.\nAlice and Bob are playing a game where they take alternating turns removing pieces from the line. In this game, Alice moves first.\n\nAlice is only allowed to remove a piece colored 'A' if both its neighbors are also colored 'A'. She is not allowed to remove pieces that are colored 'B'.\nBob is only allowed to remove a piece colored 'B' if both its neighbors are also colored 'B'. He is not allowed to remove pieces that are colored 'A'.\nAlice and Bob cannot remove pieces from the edge of the line.\nIf a player cannot make a move on their turn, that player loses and the other player wins.\n\nAssuming Alice and Bob play optimally, return true if Alice wins, or return false if Bob wins.\n \n",
    "examples": [
      {
        "input": "Input: colors = \"AAABABB\"",
        "output": "Output: true",
        "explanation": ""
      },
      {
        "input": "Input: colors = \"AA\"",
        "output": "Output: false",
        "explanation": ""
      },
      {
        "input": "Input: colors = \"ABBBBBBBAAA\"",
        "output": "Output: false",
        "explanation": ""
      }
    ],
    "topics": [
      "Math",
      "String",
      "Greedy",
      "Game Theory"
    ],
    "difficulty": "Medium",
    "constraints": [
      "1 <= colors.length <= 105",
      "colors consists of only the letters 'A' and 'B'"
    ],
    "hints": [
      "Does the number of moves a player can make depend on what the other player does? No",
      "How many moves can Alice make if colors == \"AAAAAA\"",
      "If a group of n consecutive pieces has the same color, the player can take n - 2 of those pieces if n is greater than or equal to 3"
    ]
  },
  {
    "title": "Minimum Number of Moves to Seat Everyone",
    "description": "There are n seats and n students in a room. You are given an array seats of length n, where seats[i] is the position of the ith seat. You are also given the array students of length n, where students[j] is the position of the jth student.\nYou may perform the following move any number of times:\n\nIncrease or decrease the position of the ith student by 1 (i.e., moving the ith student from position x to x + 1 or x - 1)\n\nReturn the minimum number of moves required to move each student to a seat such that no two students are in the same seat.\nNote that there may be multiple seats or students in the same position at the beginning.\n \n",
    "examples": [
      {
        "input": "Input: seats = [3,1,5], students = [2,7,4]",
        "output": "Output: 4",
        "explanation": "Explanation: The students are moved as follows:"
      },
      {
        "input": "Input: seats = [4,1,5,9], students = [1,3,2,6]",
        "output": "Output: 7",
        "explanation": "Explanation: The students are moved as follows:"
      },
      {
        "input": "Input: seats = [2,2,6,6], students = [1,3,2,6]",
        "output": "Output: 4",
        "explanation": "Explanation: Note that there are two seats at position 2 and two seats at position 6."
      }
    ],
    "topics": [
      "Array",
      "Sorting"
    ],
    "difficulty": "Easy",
    "constraints": [
      "n == seats.length == students.length",
      "1 <= n <= 100",
      "1 <= seats[i], students[j] <= 100"
    ],
    "hints": [
      "Can we sort the arrays to help solve the problem?",
      "Can we greedily match each student to a seat?",
      "The smallest positioned student will go to the smallest positioned chair, and then the next smallest positioned student will go to the next smallest positioned chair, and so on."
    ]
  },
  {
    "title": "The Score of Students Solving Math Expression",
    "description": "You are given a string s that contains digits 0-9, addition symbols '+', and multiplication symbols '*' only, representing a valid math expression of single digit numbers (e.g., 3+5*2). This expression was given to n elementary school students. The students were instructed to get the answer of the expression by following this order of operations:\n\nCompute multiplication, reading from left to right; Then,\nCompute addition, reading from left to right.\n\nYou are given an integer array answers of length n, which are the submitted answers of the students in no particular order. You are asked to grade the answers, by following these rules:\n\nIf an answer equals the correct answer of the expression, this student will be rewarded 5 points;\nOtherwise, if the answer could be interpreted as if the student applied the operators in the wrong order but had correct arithmetic, this student will be rewarded 2 points;\nOtherwise, this student will be rewarded 0 points.\n\nReturn the sum of the points of the students.\n \n",
    "examples": [
      {
        "input": "Input: s = \"7+3*1*2\", answers = [20,13,42]",
        "output": "Output: 7",
        "explanation": "Explanation: As illustrated above, the correct answer of the expression is 13, therefore one student is rewarded 5 points: [20,13,42]"
      },
      {
        "input": "Input: s = \"3+5*2\", answers = [13,0,10,13,13,16,16]",
        "output": "Output: 19",
        "explanation": "Explanation: The correct answer of the expression is 13, therefore three students are rewarded 5 points each: [13,0,10,13,13,16,16]"
      },
      {
        "input": "Input: s = \"6+0*1\", answers = [12,9,6,4,8,6]",
        "output": "Output: 10",
        "explanation": "Explanation: The correct answer of the expression is 6."
      }
    ],
    "topics": [
      "Array",
      "Math",
      "String",
      "Dynamic Programming",
      "Stack",
      "Memoization"
    ],
    "difficulty": "Hard",
    "constraints": [
      "3 <= s.length <= 31",
      "s represents a valid expression that contains only digits 0-9, '+', and '*' only.",
      "All the integer operands in the expression are in the inclusive range [0, 9].",
      "1 <= The count of all operators ('+' and '*') in the math expression <= 15",
      "Test data are generated such that the correct answer of the expression is in the range of [0, 1000].",
      "n == answers.length",
      "1 <= n <= 104",
      "0 <= answers[i] <= 1000"
    ],
    "hints": [
      "The number of operators in the equation is less. Could you find the right answer then generate all possible answers using different orders of operations?",
      "Divide the equation into blocks separated by the operators, and use memoization on the results of blocks for optimization.",
      "Use set and the max limit of the answer for further optimization."
    ]
  },
  {
    "title": "Check if Word Can Be Placed In Crossword",
    "description": "You are given an m x n matrix board, representing the current state of a crossword puzzle. The crossword contains lowercase English letters (from solved words), ' ' to represent any empty cells, and '#' to represent any blocked cells.\nA word can be placed horizontally (left to right or right to left) or vertically (top to bottom or bottom to top) in the board if:\n\nIt does not occupy a cell containing the character '#'.\nThe cell each letter is placed in must either be ' ' (empty) or match the letter already on the board.\nThere must not be any empty cells ' ' or other lowercase letters directly left or right of the word if the word was placed horizontally.\nThere must not be any empty cells ' ' or other lowercase letters directly above or below the word if the word was placed vertically.\n\nGiven a string word, return true if word can be placed in board, or false otherwise.\n \n",
    "examples": [
      {
        "input": "Input: board = [[\"#\", \" \", \"#\"], [\" \", \" \", \"#\"], [\"#\", \"c\", \" \"]], word = \"abc\"",
        "output": "Output: true",
        "explanation": "Explanation: The word \"abc\" can be placed as shown above (top to bottom)."
      },
      {
        "input": "Input: board = [[\" \", \"#\", \"a\"], [\" \", \"#\", \"c\"], [\" \", \"#\", \"a\"]], word = \"ac\"",
        "output": "Output: false",
        "explanation": "Explanation: It is impossible to place the word because there will always be a space/letter above or below it."
      },
      {
        "input": "Input: board = [[\"#\", \" \", \"#\"], [\" \", \" \", \"#\"], [\"#\", \" \", \"c\"]], word = \"ca\"",
        "output": "Output: true",
        "explanation": "Explanation: The word \"ca\" can be placed as shown above (right to left). "
      }
    ],
    "topics": [
      "Array",
      "Matrix",
      "Enumeration"
    ],
    "difficulty": "Medium",
    "constraints": [
      "m == board.length",
      "n == board[i].length",
      "1 <= m * n <= 2 * 105",
      "board[i][j] will be ' ', '#', or a lowercase English letter.",
      "1 <= word.length <= max(m, n)",
      "word will contain only lowercase English letters."
    ],
    "hints": [
      "Check all possible placements for the word.",
      "There is a limited number of places where a word can start."
    ]
  },
  {
    "title": "Grid Game",
    "description": "You are given a 0-indexed 2D array grid of size 2 x n, where grid[r][c] represents the number of points at position (r, c) on the matrix. Two robots are playing a game on this matrix.\nBoth robots initially start at (0, 0) and want to reach (1, n-1). Each robot may only move to the right ((r, c) to (r, c + 1)) or down ((r, c) to (r + 1, c)).\nAt the start of the game, the first robot moves from (0, 0) to (1, n-1), collecting all the points from the cells on its path. For all cells (r, c) traversed on the path, grid[r][c] is set to 0. Then, the second robot moves from (0, 0) to (1, n-1), collecting the points on its path. Note that their paths may intersect with one another.\nThe first robot wants to minimize the number of points collected by the second robot. In contrast, the second robot wants to maximize the number of points it collects. If both robots play optimally, return the number of points collected by the second robot.\n \n",
    "examples": [
      {
        "input": "Input: grid = [[2,5,4],[1,5,1]]",
        "output": "Output: 4",
        "explanation": "Explanation: The optimal path taken by the first robot is shown in red, and the optimal path taken by the second robot is shown in blue."
      },
      {
        "input": "Input: grid = [[3,3,1],[8,5,2]]",
        "output": "Output: 4",
        "explanation": "Explanation: The optimal path taken by the first robot is shown in red, and the optimal path taken by the second robot is shown in blue."
      },
      {
        "input": "Input: grid = [[1,3,1,15],[1,3,3,1]]",
        "output": "Output: 7",
        "explanation": "Explanation: The optimal path taken by the first robot is shown in red, and the optimal path taken by the second robot is shown in blue."
      }
    ],
    "topics": [
      "Array",
      "Matrix",
      "Prefix Sum"
    ],
    "difficulty": "Medium",
    "constraints": [
      "grid.length == 2",
      "n == grid[r].length",
      "1 <= n <= 5 * 104",
      "1 <= grid[r][c] <= 105"
    ],
    "hints": [
      "There are n choices for when the first robot moves to the second row.",
      "Can we use prefix sums to help solve this problem?"
    ]
  },
  {
    "title": "Maximum Difference Between Increasing Elements",
    "description": "Given a 0-indexed integer array nums of size n, find the maximum difference between nums[i] and nums[j] (i.e., nums[j] - nums[i]), such that 0 <= i < j < n and nums[i] < nums[j].\nReturn the maximum difference. If no such i and j exists, return -1.\n \n",
    "examples": [
      {
        "input": "Input: nums = [7,1,5,4]",
        "output": "Output: 4",
        "explanation": ""
      },
      {
        "input": "Input: nums = [9,4,3,2]",
        "output": "Output: -1",
        "explanation": ""
      },
      {
        "input": "Input: nums = [1,5,2,10]",
        "output": "Output: 9",
        "explanation": ""
      }
    ],
    "topics": [
      "Array"
    ],
    "difficulty": "Easy",
    "constraints": [
      "n == nums.length",
      "2 <= n <= 1000",
      "1 <= nums[i] <= 109"
    ],
    "hints": [
      "Could you keep track of the minimum element visited while traversing?",
      "We have a potential candidate for the answer if the prefix min is lesser than nums[i]."
    ]
  },
  {
    "title": "Longest Subsequence Repeated k Times",
    "description": "You are given a string s of length n, and an integer k. You are tasked to find the longest subsequence repeated k times in string s.\nA subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.\nA subsequence seq is repeated k times in the string s if seq * k is a subsequence of s, where seq * k represents a string constructed by concatenating seq k times.\n\nFor example, \"bba\" is repeated 2 times in the string \"bababcba\", because the string \"bbabba\", constructed by concatenating \"bba\" 2 times, is a subsequence of the string \"bababcba\".\n\nReturn the longest subsequence repeated k times in string s. If multiple such subsequences are found, return the lexicographically largest one. If there is no such subsequence, return an empty string.\n \n",
    "examples": [
      {
        "input": "Input: s = \"letsleetcode\", k = 2",
        "output": "Output: \"let\"",
        "explanation": "Explanation: There are two longest subsequences repeated 2 times: \"let\" and \"ete\"."
      },
      {
        "input": "Input: s = \"bb\", k = 2",
        "output": "Output: \"b\"",
        "explanation": "Explanation: The longest subsequence repeated 2 times is \"b\"."
      },
      {
        "input": "Input: s = \"ab\", k = 2",
        "output": "Output: \"\"",
        "explanation": "Explanation: There is no subsequence repeated 2 times. Empty string is returned."
      }
    ],
    "topics": [
      "String",
      "Backtracking",
      "Greedy",
      "Counting",
      "Enumeration"
    ],
    "difficulty": "Hard",
    "constraints": [
      "n == s.length",
      "2 <= n, k <= 2000",
      "2 <= n < k * 8",
      "s consists of lowercase English letters."
    ],
    "hints": [
      "The length of the longest subsequence does not exceed n/k. Do you know why?",
      "Find the characters that could be included in the potential answer. A character occurring more than or equal to k times can be used in the answer up to (count of the character / k) times.",
      "Try all possible candidates in reverse lexicographic order, and check the string for the subsequence condition."
    ]
  },
  {
    "title": "Detect Squares",
    "description": "You are given a stream of points on the X-Y plane. Design an algorithm that:\n\nAdds new points from the stream into a data structure. Duplicate points are allowed and should be treated as different points.\nGiven a query point, counts the number of ways to choose three points from the data structure such that the three points and the query point form an axis-aligned square with positive area.\n\nAn axis-aligned square is a square whose edges are all the same length and are either parallel or perpendicular to the x-axis and y-axis.\nImplement the DetectSquares class:\n\nDetectSquares() Initializes the object with an empty data structure.\nvoid add(int[] point) Adds a new point point = [x, y] to the data structure.\nint count(int[] point) Counts the number of ways to form axis-aligned squares with point point = [x, y] as described above.\n\n \n",
    "examples": [
      {
        "input": "Input\n[\"DetectSquares\", \"add\", \"add\", \"add\", \"count\", \"count\", \"add\", \"count\"]",
        "output": "Output\n[null, null, null, null, 1, 0, null, 2]",
        "explanation": "Explanation\nDetectSquares detectSquares = new DetectSquares();"
      }
    ],
    "topics": [
      "Array",
      "Hash Table",
      "Design",
      "Counting"
    ],
    "difficulty": "Medium",
    "constraints": [
      "point.length == 2",
      "0 <= x, y <= 1000",
      "At most 3000 calls in total will be made to add and count."
    ],
    "hints": [
      "Maintain the frequency of all the points in a hash map.",
      "Traverse the hash map and if any point has the same y-coordinate as the query point, consider this point and the query point to form one of the horizontal lines of the square."
    ]
  },
  {
    "title": "Sum of Beauty in the Array",
    "description": "You are given a 0-indexed integer array nums. For each index i (1 <= i <= nums.length - 2) the beauty of nums[i] equals:\n\n2, if nums[j] < nums[i] < nums[k], for all 0 <= j < i and for all i < k <= nums.length - 1.\n1, if nums[i - 1] < nums[i] < nums[i + 1], and the previous condition is not satisfied.\n0, if none of the previous conditions holds.\n\nReturn the sum of beauty of all nums[i] where 1 <= i <= nums.length - 2.\n \n",
    "examples": [
      {
        "input": "Input: nums = [1,2,3]",
        "output": "Output: 2",
        "explanation": "Explanation: For each index i in the range 1 <= i <= 1:"
      },
      {
        "input": "Input: nums = [2,4,6,4]",
        "output": "Output: 1",
        "explanation": "Explanation: For each index i in the range 1 <= i <= 2:"
      },
      {
        "input": "Input: nums = [3,2,1]",
        "output": "Output: 0",
        "explanation": "Explanation: For each index i in the range 1 <= i <= 1:"
      }
    ],
    "topics": [
      "Array"
    ],
    "difficulty": "Medium",
    "constraints": [
      "3 <= nums.length <= 105",
      "1 <= nums[i] <= 105"
    ],
    "hints": [
      "Use suffix/prefix arrays.",
      "prefix[i] records the maximum value in range (0, i - 1) inclusive.",
      "suffix[i] records the minimum value in range (i + 1, n - 1) inclusive."
    ]
  },
  {
    "title": "Final Value of Variable After Performing Operations",
    "description": "There is a programming language with only four operations and one variable X:\n\n++X and X++ increments the value of the variable X by 1.\n--X and X-- decrements the value of the variable X by 1.\n\nInitially, the value of X is 0.\nGiven an array of strings operations containing a list of operations, return the final value of X after performing all the operations.\n \n",
    "examples": [
      {
        "input": "Input: operations = [\"--X\",\"X++\",\"X++\"]",
        "output": "Output: 1",
        "explanation": ""
      },
      {
        "input": "Input: operations = [\"++X\",\"++X\",\"X++\"]",
        "output": "Output: 3",
        "explanation": "Explanation: The operations are performed as follows:"
      },
      {
        "input": "Input: operations = [\"X++\",\"++X\",\"--X\",\"X--\"]",
        "output": "Output: 0",
        "explanation": ""
      }
    ],
    "topics": [
      "Array",
      "String",
      "Simulation"
    ],
    "difficulty": "Easy",
    "constraints": [
      "1 <= operations.length <= 100",
      "operations[i] will be either \"++X\", \"X++\", \"--X\", or \"X--\"."
    ],
    "hints": [
      "There are only two operations to keep track of.",
      "Use a variable to store the value after each operation."
    ]
  },
  {
    "title": "Maximum Number of Ways to Partition an Array",
    "description": "You are given a 0-indexed integer array nums of length n. The number of ways to partition nums is the number of pivot indices that satisfy both conditions:\n\n1 <= pivot < n\nnums[0] + nums[1] + ... + nums[pivot - 1] == nums[pivot] + nums[pivot + 1] + ... + nums[n - 1]\n\nYou are also given an integer k. You can choose to change the value of one element of nums to k, or to leave the array unchanged.\nReturn the maximum possible number of ways to partition nums to satisfy both conditions after changing at most one element.\n \n",
    "examples": [
      {
        "input": "Input: nums = [2,-1,2], k = 3",
        "output": "Output: 1",
        "explanation": "Explanation: One optimal approach is to change nums[0] to k. The array becomes [3,-1,2]."
      },
      {
        "input": "Input: nums = [0,0,0], k = 1",
        "output": "Output: 2",
        "explanation": "Explanation: The optimal approach is to leave the array unchanged."
      },
      {
        "input": "Input: nums = [22,4,-25,-20,-15,15,-16,7,19,-10,0,-13,-14], k = -33",
        "output": "Output: 4",
        "explanation": "Explanation: One optimal approach is to change nums[2] to k. The array becomes [22,4,-33,-20,-15,15,-16,7,19,-10,0,-13,-14]."
      }
    ],
    "topics": [
      "Array",
      "Hash Table",
      "Counting",
      "Enumeration",
      "Prefix Sum"
    ],
    "difficulty": "Hard",
    "constraints": [
      "n == nums.length",
      "2 <= n <= 105",
      "-105 <= k, nums[i] <= 105"
    ],
    "hints": [
      "A pivot point splits the array into equal prefix and suffix. If no change is made to the array, the goal is to find the number of pivot p such that prefix[p-1] == suffix[p].",
      "Consider how prefix and suffix will change when we change a number nums[i] to k.",
      "When sweeping through each element, can you find the total number of pivots where the difference of prefix and suffix happens to equal to the changes of k-nums[i]."
    ]
  },
  {
    "title": "Maximize the Confusion of an Exam",
    "description": "A teacher is writing a test with n true/false questions, with 'T' denoting true and 'F' denoting false. He wants to confuse the students by maximizing the number of consecutive questions with the same answer (multiple trues or multiple falses in a row).\nYou are given a string answerKey, where answerKey[i] is the original answer to the ith question. In addition, you are given an integer k, the maximum number of times you may perform the following operation:\n\nChange the answer key for any question to 'T' or 'F' (i.e., set answerKey[i] to 'T' or 'F').\n\nReturn the maximum number of consecutive 'T's or 'F's in the answer key after performing the operation at most k times.\n \n",
    "examples": [
      {
        "input": "Input: answerKey = \"TTFF\", k = 2",
        "output": "Output: 4",
        "explanation": "Explanation: We can replace both the 'F's with 'T's to make answerKey = \"TTTT\"."
      },
      {
        "input": "Input: answerKey = \"TFFT\", k = 1",
        "output": "Output: 3",
        "explanation": "Explanation: We can replace the first 'T' with an 'F' to make answerKey = \"FFFT\"."
      },
      {
        "input": "Input: answerKey = \"TTFTTFTT\", k = 1",
        "output": "Output: 5",
        "explanation": "Explanation: We can replace the first 'F' to make answerKey = \"TTTTTFTT\""
      }
    ],
    "topics": [
      "String",
      "Binary Search",
      "Sliding Window",
      "Prefix Sum"
    ],
    "difficulty": "Medium",
    "constraints": [
      "n == answerKey.length",
      "1 <= n <= 5 * 104",
      "answerKey[i] is either 'T' or 'F'",
      "1 <= k <= n"
    ],
    "hints": [
      "Can we use the maximum length at the previous position to help us find the answer for the current position?",
      "Can we use binary search to find the maximum consecutive same answer at every position?"
    ]
  },
  {
    "title": "Number of Pairs of Strings With Concatenation Equal to Target",
    "description": "Given an array of digit strings nums and a digit string target, return the number of pairs of indices (i, j) (where i != j) such that the concatenation of nums[i] + nums[j] equals target.\n \n",
    "examples": [
      {
        "input": "Input: nums = [\"777\",\"7\",\"77\",\"77\"], target = \"7777\"",
        "output": "Output: 4",
        "explanation": "Explanation: Valid pairs are:"
      },
      {
        "input": "Input: nums = [\"123\",\"4\",\"12\",\"34\"], target = \"1234\"",
        "output": "Output: 2",
        "explanation": "Explanation: Valid pairs are:"
      },
      {
        "input": "Input: nums = [\"1\",\"1\",\"1\"], target = \"11\"",
        "output": "Output: 6",
        "explanation": "Explanation: Valid pairs are:"
      }
    ],
    "topics": [
      "Array",
      "String"
    ],
    "difficulty": "Medium",
    "constraints": [
      "2 <= nums.length <= 100",
      "1 <= nums[i].length <= 100",
      "2 <= target.length <= 100",
      "nums[i] and target consist of digits.",
      "nums[i] and target do not have leading zeros."
    ],
    "hints": [
      "Try to concatenate every two different strings from the list.",
      "Count the number of pairs with concatenation equals to target."
    ]
  },
  {
    "title": "Convert 1D Array Into 2D Array",
    "description": "You are given a 0-indexed 1-dimensional (1D) integer array original, and two integers, m and n. You are tasked with creating a 2-dimensional (2D) array with  m rows and n columns using all the elements from original.\nThe elements from indices 0 to n - 1 (inclusive) of original should form the first row of the constructed 2D array, the elements from indices n to 2 * n - 1 (inclusive) should form the second row of the constructed 2D array, and so on.\nReturn an m x n 2D array constructed according to the above procedure, or an empty 2D array if it is impossible.\n \n",
    "examples": [
      {
        "input": "Input: original = [1,2,3,4], m = 2, n = 2",
        "output": "Output: [[1,2],[3,4]]",
        "explanation": "Explanation: The constructed 2D array should contain 2 rows and 2 columns."
      },
      {
        "input": "Input: original = [1,2,3], m = 1, n = 3",
        "output": "Output: [[1,2,3]]",
        "explanation": "Explanation: The constructed 2D array should contain 1 row and 3 columns."
      },
      {
        "input": "Input: original = [1,2], m = 1, n = 1",
        "output": "Output: []",
        "explanation": "Explanation: There are 2 elements in original."
      }
    ],
    "topics": [
      "Array",
      "Matrix",
      "Simulation"
    ],
    "difficulty": "Easy",
    "constraints": [
      "1 <= original.length <= 5 * 104",
      "1 <= original[i] <= 105",
      "1 <= m, n <= 4 * 104"
    ],
    "hints": [
      "When is it possible to convert original into a 2D array and when is it impossible?",
      "It is possible if and only if m * n == original.length",
      "If it is possible to convert original to a 2D array, keep an index i such that original[i] is the next element to add to the 2D array."
    ]
  },
  {
    "title": "Smallest Missing Genetic Value in Each Subtree",
    "description": "There is a family tree rooted at 0 consisting of n nodes numbered 0 to n - 1. You are given a 0-indexed integer array parents, where parents[i] is the parent for node i. Since node 0 is the root, parents[0] == -1.\nThere are 105 genetic values, each represented by an integer in the inclusive range [1, 105]. You are given a 0-indexed integer array nums, where nums[i] is a distinct genetic value for node i.\nReturn an array ans of length n where ans[i] is the smallest genetic value that is missing from the subtree rooted at node i.\nThe subtree rooted at a node x contains node x and all of its descendant nodes.\n \n",
    "examples": [
      {
        "input": "Input: parents = [-1,0,0,2], nums = [1,2,3,4]",
        "output": "Output: [5,1,1,1]",
        "explanation": "Explanation: The answer for each subtree is calculated as follows:"
      },
      {
        "input": "Input: parents = [-1,0,1,0,3,3], nums = [5,4,6,2,1,3]",
        "output": "Output: [7,1,1,4,2,1]",
        "explanation": "Explanation: The answer for each subtree is calculated as follows:"
      },
      {
        "input": "Input: parents = [-1,2,3,0,2,4,1], nums = [2,3,4,5,6,7,8]",
        "output": "Output: [1,1,1,1,1,1,1]",
        "explanation": "Explanation: The value 1 is missing from all the subtrees."
      }
    ],
    "topics": [
      "Dynamic Programming",
      "Tree",
      "Depth-First Search",
      "Union Find"
    ],
    "difficulty": "Hard",
    "constraints": [
      "n == parents.length == nums.length",
      "2 <= n <= 105",
      "0 <= parents[i] <= n - 1 for i != 0",
      "parents[0] == -1",
      "parents represents a valid tree.",
      "1 <= nums[i] <= 105",
      "Each nums[i] is distinct."
    ],
    "hints": [
      "If the subtree doesn't contain 1, then the missing value will always be 1.",
      "What data structure allows us to dynamically update the values that are currently not present?"
    ]
  },
  {
    "title": "Maximum Product of the Length of Two Palindromic Subsequences",
    "description": "Given a string s, find two disjoint palindromic subsequences of s such that the product of their lengths is maximized. The two subsequences are disjoint if they do not both pick a character at the same index.\nReturn the maximum possible product of the lengths of the two palindromic subsequences.\nA subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters. A string is palindromic if it reads the same forward and backward.\n \n",
    "examples": [
      {
        "input": "Input: s = \"leetcodecom\"",
        "output": "Output: 9",
        "explanation": "Explanation: An optimal solution is to choose \"ete\" for the 1st subsequence and \"cdc\" for the 2nd subsequence."
      },
      {
        "input": "Input: s = \"bb\"",
        "output": "Output: 1",
        "explanation": "Explanation: An optimal solution is to choose \"b\" (the first character) for the 1st subsequence and \"b\" (the second character) for the 2nd subsequence."
      },
      {
        "input": "Input: s = \"accbcaxxcxx\"",
        "output": "Output: 25",
        "explanation": "Explanation: An optimal solution is to choose \"accca\" for the 1st subsequence and \"xxcxx\" for the 2nd subsequence."
      }
    ],
    "topics": [
      "String",
      "Dynamic Programming",
      "Backtracking",
      "Bit Manipulation",
      "Bitmask"
    ],
    "difficulty": "Medium",
    "constraints": [
      "2 <= s.length <= 12",
      "s consists of lowercase English letters only."
    ],
    "hints": [
      "Could you generate all possible pairs of disjoint subsequences?",
      "Could you find the maximum length palindrome in each subsequence for a pair of disjoint subsequences?"
    ]
  },
  {
    "title": "Number of Pairs of Interchangeable Rectangles",
    "description": "You are given n rectangles represented by a 0-indexed 2D integer array rectangles, where rectangles[i] = [widthi, heighti] denotes the width and height of the ith rectangle.\nTwo rectangles i and j (i < j) are considered interchangeable if they have the same width-to-height ratio. More formally, two rectangles are interchangeable if widthi/heighti == widthj/heightj (using decimal division, not integer division).\nReturn the number of pairs of interchangeable rectangles in rectangles.\n \n",
    "examples": [
      {
        "input": "Input: rectangles = [[4,8],[3,6],[10,20],[15,30]]",
        "output": "Output: 6",
        "explanation": "Explanation: The following are the interchangeable pairs of rectangles by index (0-indexed):"
      },
      {
        "input": "Input: rectangles = [[4,5],[7,8]]",
        "output": "Output: 0",
        "explanation": "Explanation: There are no interchangeable pairs of rectangles."
      }
    ],
    "topics": [
      "Array",
      "Hash Table",
      "Math",
      "Counting",
      "Number Theory"
    ],
    "difficulty": "Medium",
    "constraints": [
      "n == rectangles.length",
      "1 <= n <= 105",
      "rectangles[i].length == 2",
      "1 <= widthi, heighti <= 105"
    ],
    "hints": [
      "Store the rectangle height and width ratio in a hashmap.",
      "Traverse the ratios, and for each ratio, use the frequency of the ratio to add to the total pair count."
    ]
  },
  {
    "title": "Reverse Prefix of Word",
    "description": "Given a 0-indexed string word and a character ch, reverse the segment of word that starts at index 0 and ends at the index of the first occurrence of ch (inclusive). If the character ch does not exist in word, do nothing.\n\nFor example, if word = \"abcdefd\" and ch = \"d\", then you should reverse the segment that starts at 0 and ends at 3 (inclusive). The resulting string will be \"dcbaefd\".\n\nReturn the resulting string.\n \n",
    "examples": [
      {
        "input": "Input: word = \"abcdefd\", ch = \"d\"",
        "output": "Output: \"dcbaefd\"",
        "explanation": ""
      },
      {
        "input": "Input: word = \"xyxzxe\", ch = \"z\"",
        "output": "Output: \"zxyxxe\"",
        "explanation": ""
      },
      {
        "input": "Input: word = \"abcd\", ch = \"z\"",
        "output": "Output: \"abcd\"",
        "explanation": ""
      }
    ],
    "topics": [
      "Two Pointers",
      "String"
    ],
    "difficulty": "Easy",
    "constraints": [
      "1 <= word.length <= 250",
      "word consists of lowercase English letters.",
      "ch is a lowercase English letter."
    ],
    "hints": [
      "Find the first index where ch appears.",
      "Find a way to reverse a substring of word."
    ]
  },
  {
    "title": "GCD Sort of an Array",
    "description": "You are given an integer array nums, and you can perform the following operation any number of times on nums:\n\nSwap the positions of two elements nums[i] and nums[j] if gcd(nums[i], nums[j]) > 1 where gcd(nums[i], nums[j]) is the greatest common divisor of nums[i] and nums[j].\n\nReturn true if it is possible to sort nums in non-decreasing order using the above swap method, or false otherwise.\n \n",
    "examples": [
      {
        "input": "Input: nums = [7,21,3]",
        "output": "Output: true",
        "explanation": "Explanation: We can sort [7,21,3] by performing the following operations:"
      },
      {
        "input": "Input: nums = [5,2,6,2]",
        "output": "Output: false",
        "explanation": "Explanation: It is impossible to sort the array because 5 cannot be swapped with any other element."
      },
      {
        "input": "Input: nums = [10,5,9,3,15]",
        "output": "Output: true",
        "explanation": ""
      }
    ],
    "topics": [
      "Array",
      "Math",
      "Union Find",
      "Sorting"
    ],
    "difficulty": "Hard",
    "constraints": [
      "1 <= nums.length <= 3 * 104",
      "2 <= nums[i] <= 105"
    ],
    "hints": [
      "Can we build a graph with all the prime numbers and the original array?",
      "We can use union-find to determine which indices are connected (i.e., which indices can be swapped)."
    ]
  },
  {
    "title": "First Day Where You Have Been in All the Rooms",
    "description": "There are n rooms you need to visit, labeled from 0 to n - 1. Each day is labeled, starting from 0. You will go in and visit one room a day.\nInitially on day 0, you visit room 0. The order you visit the rooms for the coming days is determined by the following rules and a given 0-indexed array nextVisit of length n:\n\nAssuming that on a day, you visit room i,\nif you have been in room i an odd number of times (including the current visit), on the next day you will visit a room with a lower or equal room number specified by nextVisit[i] where 0 <= nextVisit[i] <= i;\nif you have been in room i an even number of times (including the current visit), on the next day you will visit room (i + 1) mod n.\n\nReturn the label of the first day where you have been in all the rooms. It can be shown that such a day exists. Since the answer may be very large, return it modulo 109 + 7.\n \n",
    "examples": [
      {
        "input": "Input: nextVisit = [0,0]",
        "output": "Output: 2",
        "explanation": ""
      },
      {
        "input": "Input: nextVisit = [0,0,2]",
        "output": "Output: 6",
        "explanation": ""
      },
      {
        "input": "Input: nextVisit = [0,1,2,0]",
        "output": "Output: 6",
        "explanation": ""
      }
    ],
    "topics": [
      "Array",
      "Dynamic Programming"
    ],
    "difficulty": "Medium",
    "constraints": [
      "n == nextVisit.length",
      "2 <= n <= 105",
      "0 <= nextVisit[i] <= i"
    ],
    "hints": [
      "The only way to get to room i+1 is when you are visiting room i and room i has been visited an even number of times.",
      "After visiting room i an odd number of times, you are required to visit room nextVisit[i] where nextVisit[i] <= i. It takes a fixed amount of days for you to come back from room nextVisit[i] to room i. Then, you have visited room i even number of times.nextVisit[i]",
      "Can you use Dynamic Programming to avoid recomputing the number of days it takes to visit room i from room nextVisit[i]?"
    ]
  }
];

questionsWithParseableExamples = [  ];
uniqueTopics = {  };

## Only for use with input strings starting with "Input: "
def standardizeInput(fullInput):

  ## Remove the initial / leading "Input: " substring
  fullInput = fullInput[len("Input: ")::];

  ## This will hold the final standardized input string
  finalString = "";

  currentParameterString = "";

  ## Initialize a variable to track if you are currently within at the start, within, or at the end of string from the opening quote to the closing quote
  ## Initialize a variable to track if you are currently within at the start, within, or at the end of a list from the opening bracket to the closing bracket
  ## Initialize a variable to track what bracket depth currently at
  inString, inList, inListDepth = False, False, 0;

  ## Iterate over the string of parameters
  for x in range(len(fullInput)):

    ## Get the current character
    currentCharacter = fullInput[x];

    ## Initialize two variables to track if you have to reset if you hit the closing quote of a string or closing bracket of a list
    resetInString, resetInList = False, False;

    ## If you are at the start or end of a string
    if currentCharacter == "\"":

      ## If you hit a quote and you are within a string, that means you are at the closing quote of the string
      if inString:
        resetInString = True;

      ## In any case (opening or closing quote) you are still over part of the string
      inString = True;

    ## If you may be at the start of a true list, or within a string that has a bracket inside it
    elif currentCharacter == "[":

      ## If you are not within a string and are at a opening bracket, you are within a list
      if not inString:

        ## Mark that you are within an actual list
        inList = True;

        ## Increment the list depth
        inListDepth += 1;

    ## If you may may at the end of a true list, or within a string that has a bracket inside it
    elif currentCharacter == "]":

      ## If you are not in a string, you are at the bracket of a true list, therefore mark for a reset of being in a list
      if not inString:
        resetInList = True;

    ## If you are at a space character
    elif currentCharacter == " ":

      ## If you have at least processed one character and the last processed character is a ",", you are at a " ", it was a sequence of ", "
      if len(finalString) > 0 and finalString[-1] == ",":

        ## Need to expand the handling of this here...
        ## If you are in a true list and not in a string, we have factored out the edge case of [3, 5] --> when almost all leetcode lists are formatted as [3,5]
        ## By continuing, you skip the current space in order to fix formatting
        if inList and not inString:
          continue;

    ## Account for the current character
    finalString += currentCharacter;

    ## If we have a reset to make for strings
    if resetInString:

      ## Mark leaving the string
      inString = False;

    ## If we have a reset to make for lists
    if resetInList:
      
      ## Decrement the list depth
      inListDepth -= 1;

      ## If we are now at a depth of 0
      if inListDepth == 0:

        ## Mark leaving the full true list
        inList = False;

  return finalString;





## Finds and injects parameter type into test case
def injectParameterType(value):
  

  ## Create the set of numerical characters (digits and the negative symbol)
  numericalSet = set([ "-" ]) | set([ chr(48 + digit) for digit in range(10) ]);
  
  ## If we have a quote at the start and end of the parameter value, we have a string
  if value[0] == "\"" and value[-1] == "\"":
    return "STRING";
  
  ## If we have a numerical character at the start and end of the parameter value, we have a number
  elif value[0] in numericalSet and value[-1] in numericalSet:

    ## If there is a . in the number, we have a double / float
    if "." in value:
      return "DOUBLE";
    
    ## Otherwise, we have an integer
    return "INTEGER";

  ## Must be some sort of list

  ## Initialize a variable to track if you are currently within at the start, within, or at the end of string from the opening quote to the closing quote
  ## Initialize a variable to track what bracket depth currently at
  ## Initialize a variable to track what the global valid list maximum depth is
  inString, listDepth, maxListDepth = False, 0, 0;

  ## Initialize a variable to track if there ever has been a string found
  ## Initialize a variable to track if there ever has been a integer found
  foundString, foundIntegerNotInString = False, False;

  ## Iterate over all characters in the parameter value
  for char in value:
    
    ## If at an quote, you are either at the start or end of a string
    if char == "\"":

      ## If you were not in a string before, you are at the opening quote of a string
      if not inString:

        ## Mark you are in a string, can be reset
        inString = True;

        ## Mark you have found a string at some point, no possibility of reset
        foundString = True;

      ## Otherwise, you are at the closing quote of a string
      else:
        inString = False;

    ## If at an opening bracket, we are either at the start of a true list or in a string with an opening bracket
    elif char == "[":

      ## If we are not in a string, we are at the start of a true list
      if not inString:

        ## Increment the true list depth
        listDepth += 1;

        ## Track the max true list depth across the entire parameter value
        maxListDepth = max(maxListDepth, listDepth);

    ## If at a closing bracket, we are either at the end of  true list or in a string with a closing bracket
    elif char == "]":

      ## If we are not in a string, we are at the start of a true list
      if not inString:

        ## Decrement the true list depth
        listDepth -= 1;
    
    ## If we find at the end of a numerical string
    elif char in numericalSet and not inString:
      foundIntegerNotInString = True;

  ## Represent the true list depth in string format
  listInject = "[]" * maxListDepth;

  ## If we have something with a string as a base element
  if foundString:
    return f"STRING{listInject}";
  
  ## If we have something with a double as a base element
  elif "." in value:
    return f"DOUBLE{listInject}";
  
  ## If we have something with an integer as a base element
  elif foundIntegerNotInString:
    return f"INTEGER{listInject}";
  
  ## If we have something with a boolean as a base element
  else:
    return f"BOOLEAN{listInject}";


def generateListType(elementType, depth, language):

  if depth == 0:
    return elementType;
  
  listMap = {
    "java": "ArrayList",
    "cpp": "vector"
  };

  return f"{listMap[language]}<{generateListType(elementType, depth - 1, language)}>";


def transformType(pseudoType, language):

  listDepth = pseudoType.count("[]");

  if language == "python": return "";

  elif language == "javascript": return "";

  elif language == "cpp":
    if pseudoType == "INTEGER": return "int";
    elif pseudoType == "INTEGER[]": return "vector<int>";
    elif pseudoType == "INTEGER[][]": return "vector<vector<int>>";
    elif pseudoType == "DOUBLE": return "double";
    elif pseudoType == "DOUBLE[]": return "vector<double>";
    elif pseudoType == "DOUBLE[][]": return "vector<vector<double>>";
    elif pseudoType == "STRING": return "string";
    elif pseudoType == "STRING[]": return "vector<string>";
    elif pseudoType == "STRING[][]": return "vector<vector<string>>";
    elif pseudoType == "BOOLEAN": return "bool";
    elif pseudoType == "BOOLEAN[]": return "vector<bool>";
    elif pseudoType == "BOOLEAN[][]": return "vector<vector<bool>>";

  elif language == "java":
    if pseudoType == "INTEGER": return "int";
    elif pseudoType == "INTEGER[]": return "ArrayList<Integer>";
    elif pseudoType == "INTEGER[][]": return "ArrayList<ArrayList<Integer>>";
    elif pseudoType == "DOUBLE": return "double";
    elif pseudoType == "DOUBLE[]": return "ArrayList<Double>";
    elif pseudoType == "DOUBLE[][]": return "ArrayList<ArrayList<Double>>";
    elif pseudoType == "STRING": return "String";
    elif pseudoType == "STRING[]": return "ArrayList<String>";
    elif pseudoType == "STRING[][]": return "ArrayList<ArrayList<String>>";
    elif pseudoType == "BOOLEAN": return "boolean";
    elif pseudoType == "BOOLEAN[]": return "ArrayList<Boolean>";
    elif pseudoType == "BOOLEAN[][]": return "ArrayList<ArrayList<Boolean>>";




def createLanguageSpecificFunctionSignatureParameters(parameterTokens, language):

  finalParameterInjectionData = [  ];

  for parameterToken in parameterTokens:
    languageSpecificTransformedType = transformType(parameterToken['type'], language);
    hasPrefixableLangaugeSpecificTransformedType = languageSpecificTransformedType != "";

    finalParameterInjectionData.append(f"{languageSpecificTransformedType}{' ' if hasPrefixableLangaugeSpecificTransformedType else ''}{parameterToken['name']}");

  return ", ".join(finalParameterInjectionData);


## This will perform reformatting if we are dealing with lists, however regardless of the data type of the value, it will still be processed through this function (and correctly at that)
def languageParameterReformatter(listData, language):

  letterSet = set([ chr(x) for x in range(65, 91) ]) | set([ chr(x) for x in range(97, 123) ]);

  pythonBooleanTransformFlag = False;

  pseudoTypeDetected = injectParameterType(listData);
  if language == "python" and "BOOLEAN" in pseudoTypeDetected:
    pythonBooleanTransformFlag = True;

  parameterString = "";
  inString = False;

  for char in listData:

    if not inString:
      if char == "\"":
        inString = True;


      if char == "[":

        if language == "java":
          parameterString += "new ArrayList<>(Arrays.asList(";
        elif language == "cpp":
          parameterString +=  "{";
        else:
          parameterString += char;

      elif char == "]":

        if language == "java":
          parameterString += "))";
        elif language == "cpp":
          parameterString += "}";
        else:
          parameterString += char;

      else:
        parameterString += char;

    else:

      if char == "\"":
        inString = False;

      parameterString += char;

  if pythonBooleanTransformFlag:
    parameterString = parameterString.replace("true", "True").replace("false", "False");

  return parameterString;

def createLanguageSpecificFunctionCallParameters(parameterTokens, language):

  finalParameterInjectionData = [  ];

  for parameterToken in parameterTokens:
    finalParameterInjectionData.append(languageParameterReformatter(parameterToken["value"], language));

  return ", ".join(finalParameterInjectionData);
        


def generateTestTemplate(testCases, returnType, language):
  
  testingTemplateInjection = "";

  testCaseIndex = 0;

  for INPUT_PARAMETER_VALUES, EXPECTED_OUTPUT in testCases:

    isListReturnType = "[]" in returnType;
    transformedReturnType = transformType(returnType, language);

    if language == "python":
      testingTemplateInjection += f"if solution({INPUT_PARAMETER_VALUES}) != {EXPECTED_OUTPUT}:\n\tprint('" + TEST_INJECTION_PLACEMENT_TERM_SWAP + str(testCaseIndex) + "');\n\texit();\n";

    elif language == "javascript":
      ## handle special case of list...

      

      testingTemplateInjection += f"if (JSON.stringify(solution({INPUT_PARAMETER_VALUES})) != JSON.stringify({EXPECTED_OUTPUT}))" + " {\n" + "\tconsole.log('" + TEST_INJECTION_PLACEMENT_TERM_SWAP + str(testCaseIndex) + "');\n\texit();\n};\n";
    
    elif language == "java":
      testingTemplateInjection += f"\t\tif (new Solution().solution({INPUT_PARAMETER_VALUES}){'.toString()' if isListReturnType else ''} != {EXPECTED_OUTPUT}{'.toString()' if isListReturnType else ''})" + " {\n" + "\t\t\tSystem.out.println(" + TEST_INJECTION_PLACEMENT_TERM_SWAP + str(testCaseIndex) + "\");\n\t\t\tSystem.exit(0);\n\t\t};\n";

    elif language == "cpp":
      testingTemplateInjection += f"\tif (solution({INPUT_PARAMETER_VALUES}) != {transformedReturnType if isListReturnType else ''}({EXPECTED_OUTPUT}))" + " {\n" + "\t\tcout << \"" + TEST_INJECTION_PLACEMENT_TERM_SWAP + str(testCaseIndex) + "\" << endl;\n\t\texit(0);\n\t};\n";
  
    testingTemplateInjection += "\n\n";
    testCaseIndex += 1;

  if language == "python":
    testingTemplateInjection += "\nprint('ACCEPTED_" + TEST_INJECTION_PLACEMENT_TERM_SWAP + "');\n";
  elif language == "javascript":
    testingTemplateInjection += "\nconsole.log('ACCEPTED_" + TEST_INJECTION_PLACEMENT_TERM_SWAP + "');\n"
  elif language == "java":
    testingTemplateInjection += "\n\t\tSystem.out.println(\"ACCEPTED_" + TEST_INJECTION_PLACEMENT_TERM_SWAP + "\");\n";
  elif language == "cpp":
    testingTemplateInjection += "\tcout << \"ACCEPTED_" + TEST_INJECTION_PLACEMENT_TERM_SWAP + "\" << endl;";
  
  languageTestingTemplates = {
    "python": f"\n\n{testingTemplateInjection}",
    "javascript": f"\n\n{testingTemplateInjection}",
    "java": "\n\nclass Main {\n\tpublic static void main(String[] args) {\n\n" + testingTemplateInjection + "\t};\n};\n",
    "cpp": "\n\nint main() {\n\n" + testingTemplateInjection + "\n\n\treturn 0;\n};\n"
  };

  return languageTestingTemplates[language];

def buildLanguageTemplates(examples, returnType):

  languageTemplates = {

    "python": {
      
      "injectionLocations": [
        3
      ],

      "template": [
        "\n\n",
        "def solution",
        "(",
        "INJECTION",
        ")",
        ":\n",
        "\t",
        ## "\n\n",
        ## TEST_INJECTION_PLACEMENT_TERM_SWAP,
        "\n\n"
      ],

    },

    "javascript": {
      
      "injectionLocations": [
        3
      ],

      "template": [
        "\n\n",
        "const solution = ",
        "(",
        "INJECTION",
        ")",
        " => {\n",
        "\t",
        "\n",
        "\n"
        "}",
        ## "\n\n",
        ## TEST_INJECTION_PLACEMENT_TERM_SWAP,
        "\n\n"
      ],

    },

    "cpp": {
      
      "injectionLocations": [
        1,
        5
      ],

      "template": [
        "\n\n",
        "INJECTION",
        " ",
        "solution",
        "(",
        "INJECTION",
        ")",
        " {",
        "\n\n",
        "}",
        ## "\n\n",
        ## TEST_INJECTION_PLACEMENT_TERM_SWAP,
        "\n\n"
      ],

    },

    "java": {

      "injectionLocations": [
        5,
        9
      ],

      "template": [
        "\n\n",
        "class Solution",
        " {",
        "\n\n",
        "\t",
        "INJECTION",
        " ",
        "solution",
        "(",
        "INJECTION",
        ")",
        " {",
        "\n\n",
        "\t",
        "}",
        "\n\n",
        ## TEST_INJECTION_PLACEMENT_TERM_SWAP,
        ## "\n\n",
        "}",
        "\n\n"
      ]

    }

  };

  resultingTemplates = {  };

  for language, templateData in languageTemplates.items():
      
    testCaseParameterTokens = [  ];

    for example in question["examples"]:
      parameterTokens = [
        parameterToken.split(" = ")
        for parameterToken in standardizeInput(example["input"]).split(", ")
      ];

      testCaseParameterTokens.append([
        {
          "name": paramVarName,
          "value": paramVarValue,
          "type": injectParameterType(paramVarValue)
        }
        for paramVarName, paramVarValue in parameterTokens
      ]);

    ## Parse out the parameters [ name, value ] pairs from the first example's standardized input string


    ## For function signature
    transformedFunctionSignatureParameters = createLanguageSpecificFunctionSignatureParameters(testCaseParameterTokens[0], language);

    ## Not for function signature, for function call
    transformedFunctionCallParameters = [
      createLanguageSpecificFunctionCallParameters(parameterTokens, language)
      for parameterTokens in testCaseParameterTokens
    ];

    transformedTestCaseSolutions = [
      languageParameterReformatter(data, language)
      for data in [
        example["output"][len("Output: ")::]
        for example in examples
      ]
    ];

    pairedInputsAndSolutions = [
      [
        transformedFunctionCallParameters[x],
        transformedTestCaseSolutions[x]
      ]
      for x in range(len(examples))
    ];

    if len(templateData["injectionLocations"]) == 1:
      templateData["template"][templateData["injectionLocations"][0]] = "".join(transformedFunctionSignatureParameters);
    else:
      templateData["template"][templateData["injectionLocations"][0]] = transformType(returnType, language);
      templateData["template"][templateData["injectionLocations"][1]] = "".join(transformedFunctionSignatureParameters);

    resultingTemplates[language] = {
      "submissionTemplate": "".join(templateData["template"]),
      "transformedReturnType": transformType(returnType, language),
      "generalReturnType": returnType,
      "testCases": pairedInputsAndSolutions,
      "testingTemplate": generateTestTemplate(pairedInputsAndSolutions, returnType, language)
    };

    if language == "python":
      resultingTemplates[language]["libraries"] = [
        "from collections import *"
      ];
    elif language == "java":
      resultingTemplates[language]["libraries"] = [
        "import java.util.*;",
        "import java.io.*;"
      ];
    elif language == "cpp":
      resultingTemplates[language]["libraries"] = [
        "#include <vector>",
        "#include <string>",
        "#include <algorithm>",
        "#include <iostream>"
      ]
    elif language == "javascript":
      resultingTemplates[language]["libraries"] = [

      ];
  
    print(f"{language}:\n{resultingTemplates[language]['testingTemplate']}");

  return resultingTemplates;




for question in questions:

  ## If the question is of the special variant or it only has one example
  if re.search(r"Input\n", question["examples"][0]["input"]) or len(question["examples"]) < 2:
    continue;

  ## Normalization for our schema

  question["isApproved"] = True;
  question["templates"] = buildLanguageTemplates(question["examples"], injectParameterType(question["examples"][0]["output"][len("Output: ")::]));

  questionsWithParseableExamples.append(question);

  ## Add all topics to set to get all unique topics
  for topic in question["topics"]:

    if topic not in uniqueTopics:
      uniqueTopics[topic] = 1;
    else:
      uniqueTopics[topic] += 1;


uniqueTopics = [ (topic, frequency) for topic, frequency in uniqueTopics.items() ];
uniqueTopics.sort(key=lambda topicTuple: topicTuple[1], reverse=True);

uniqueTopicsSortedByFrequency = [ f"{topic} - {frequency}" for topic, frequency in uniqueTopics ];


QUESTIONS_OUTPUT_FILE_NAME = "manipulatedQuestions.json";
QUESTIONS_TOPICS_OUTPUT_FILE_NAME = "manipulatedQuestionsTopics.json";


if QUESTIONS_OUTPUT_FILE_NAME in os.listdir():
  os.remove(QUESTIONS_OUTPUT_FILE_NAME);

with open(QUESTIONS_OUTPUT_FILE_NAME, "w") as f:
  json.dump(questionsWithParseableExamples, f, ensure_ascii=False, indent=4);

#####

if QUESTIONS_TOPICS_OUTPUT_FILE_NAME in os.listdir():
    os.remove(QUESTIONS_TOPICS_OUTPUT_FILE_NAME);

with open(QUESTIONS_TOPICS_OUTPUT_FILE_NAME, "w") as f:
  json.dump([ topicFrequencyString for topicFrequencyString in uniqueTopicsSortedByFrequency ], f, ensure_ascii=False, indent=4);