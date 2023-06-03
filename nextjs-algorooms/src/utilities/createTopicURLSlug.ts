export default topic =>
    topic
    // Done to remove any occurences like Heap (Priority Queue), which will ultimately reduce to "heap"
    .replaceAll(/\(.*\)/gi, "")
    // Now split the left over string by spaces in
    .split(" ")
    // In case this there were multiple terms to the string between the replace action
    // Example: "Heap (Priority Queue) DSA" --> "Heap  DSA" --> ["Heap", "", "DSA"]
    // We can end up filtering out empty strings that come from the splitting, removing the possibility of errors like consecutive -'s
    .filter(topic => topic.length > 0)
    // Now that we only have relevant and easily-typable tokens for the topic URL slug, join them by -'s
    .join("-")
    // Just for safety -- trim the string in case of leading / trailing whitespace
    .trim()
    // Convert the entire string to lowercase as convention
    .toLowerCase();