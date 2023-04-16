

// Simple Fisher-Yates shuffle implementation

export default (
    array:any[]
):void => {

    // Iterate over all relevant possible swap locations
    for (let x = 0; x < array.length - 1; ++x) {

        // Choose a random swap index from [min(x + 1, array.length - 1), array.length - 1]
        const randomIndex = x + Math.floor(Math.random() * (array.length - x));

        // Swap the elements
        const t = array[x];
        array[x] = array[randomIndex];
        array[randomIndex] = t;

    };

};