// 62^25 unique UIDs possible if length = 25

export default (
    length:number = 25
) => {

    // 62 possible character placements at each given index
    const classes = [
        ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'],
        ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
        ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    ];

    // Stores the UID string to be created
    let uid = "";

    for (let x = 0; x < length; ++x) {
        // Select a pseudorandom character class index (will be in the range [0, 2] as is now considering Math.random returns a float in range (0.0, 1.0))
        const randomClassIndex = Math.floor(Math.random() * classes.length);

        // Select a pseudorandom character from the random class and append to the string
        uid += classes[randomClassIndex][Math.floor(Math.random() * classes[randomClassIndex].length)];
    };

    // Return the pseudorandom room UID
    return uid;
};