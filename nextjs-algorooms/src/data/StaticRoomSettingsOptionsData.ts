import processTopic from "@/utilities/createTopicURLSlug";

export default {

    selectableDifficulties: [
        "Easy",
        "Medium",
        "Hard",
    ].map(difficulty => {

        return {
            label: difficulty,
            value: difficulty
        };

    }),

    selectableTopics: [
        "Array - 315",
        "String - 121",
        "Hash Table - 102",
        "Math - 86",
        "Greedy - 85",
        "Sorting - 82",
        "Dynamic Programming - 64",
        "Binary Search - 55",
        "Prefix Sum - 44",
        "Simulation - 41",
        "Matrix - 36",
        "Heap (Priority Queue) - 35",
        "Graph - 33",
        "Depth-First Search - 32",
        "Counting - 32",
        "Bit Manipulation - 31",
        "Breadth-First Search - 29",
        "Two Pointers - 29",
        "Tree - 27",
        "Enumeration - 25",
        "Number Theory - 21",
        "Sliding Window - 18",
        "Stack - 18",
        "Union Find - 15",
        "Binary Tree - 14",
        "Backtracking - 11",
        "Ordered Set - 9",
        "Topological Sort - 8",
        "Linked List - 8",
        "Binary Indexed Tree - 7",
        "Segment Tree - 7",
        "Queue - 7",
        "Monotonic Stack - 7",
        "Shortest Path - 5",
        "Combinatorics - 5",
        "Bitmask - 4",
        "Brainteaser - 4",
        "Geometry - 4",
        "Divide and Conquer - 4",
        "Rolling Hash - 4",
        "Hash Function - 4",
        "Memoization - 4",
        "Recursion - 3",
        "Monotonic Queue - 3",
        "String Matching - 3",
        "Merge Sort - 2",
        "Trie - 2",
        "Game Theory - 2",
        "Radix Sort - 1",
        "Quickselect - 1",
        "Suffix Array - 1",
        "Eulerian Circuit - 1"
    ].map(topicString => {

        const [
            topic,
            frequency
        ] = topicString.split(" - ");
    
        return {
            label: topicString,
            value: topic,
            urlSlug: `/topics/${processTopic(topic)}`,
            frequency: Number(frequency)
        }

    })

};