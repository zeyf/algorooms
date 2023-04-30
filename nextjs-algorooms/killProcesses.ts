// Pull out command line executor
const {
    exec
} = require("child_process");

// Get command line arguments
const arguments = process.argv;

// If there is somethign missing or the port is not a number
if (arguments.length < 3 || Number.isNaN(Number(arguments[2]))) {
    throw new Error(`There has been an error with your command line arguments!\nArguments:\n[\n\t${arguments.toString().replace(/,./gi, ",\n\t")}\n]`);
};

// Get the port
const PORT = arguments[2];

// Get all processes running at the port
exec(`lsof -i :${PORT}`, (error, stdout, stderr) => {

    // There are no processes running at the port
    if (stdout === "")
        console.log(`There are no processes running on PORT ${PORT}!\nMOVING ON...`);
    // There is an error
    else if (error)
        throw new Error(error);
    // There is no error
    else {

        // Store the mapping if needed
        const mapping = {
            0: "PROCESS_NAME",
            1: "PROCESS_ID",
            2: "PROCESS_USER",
            3: "PROCESS_IP_TYPE",
            4: "PROCESS_DEVICE_ADDRESS",
            5: "PROCESS_SIZE_OFFSET",
            6: "PROCESS_NODE",
            7: "PROCESS_SOURCE_LOCATION"
        };

        // Cleans processes @ port information
        let portProcessesList = stdout.split("\n").map((line, index) => line.split(" ").filter(el => el != ""));
        portProcessesList = portProcessesList.slice(1, portProcessesList.length - 1).map(([ PROCESS_NAME, PROCESS_ID ]) => Number(PROCESS_ID));

        // Iterate over all processes running at the port
        for (const RUNNING_PROCESS_ID_AT_PORT of portProcessesList) {

            // Kill the process
            exec(`kill -9 ${RUNNING_PROCESS_ID_AT_PORT}`, (error, stdout, stderr) => {
                // If there is an error
                if (error)
                    throw new Error(`There was an error processing command kill -9 ${RUNNING_PROCESS_ID_AT_PORT}\n${error}`);
                // The processes has been killed
                else
                    console.log(`KILLED PROCESS ${RUNNING_PROCESS_ID_AT_PORT} @ PORT ${PORT}`);
            });
        };

    };
});
