// Used to log requests to route endpoints

export function REQUEST_LOG(
    routeBase: string,
    {
        method,
        path,
        body,
        params,
        query
    }: any
):void {
    
    // For logging styling for separation
    const BAR = "======";

    // Lambda to pad time with a 0
    const formatTime = (integer:number):string => `${integer < 10 ? "0" : ""}${integer}`;

    // Get current date
    const date = new Date();
    
    // Get the current hour in integer
    let hours: number | string = date.getHours();

    // Get the current period
    const period = hours < 12 ? "AM" : "PM";

    // Convert hour to string
    hours = formatTime(date.getHours());

    // Get the current minute and millisecond
    const minutes = formatTime(date.getMinutes()),
          milliseconds = formatTime(Math.floor(date.getMilliseconds() / 60));

    // The base logString
    let logString = `${BAR}\n\n${hours}:${minutes}:${milliseconds} ${period} -> ${method} :: ${routeBase}${path}\n\n`;

    // If we have a body, print its contents
    if (Object.keys(body).length > 0) {
        logString += "BODY:\n\n";

        for (const key in body)
            logString += `${key} : ${body[key]}\n`;
        
        logString += "\n";
    };

    // If we have parameters, add its contents
    if (Object.keys(params).length > 0) {
        logString += "PARAMS:\n\n";

        for (const key in params)
            logString += `${key} : ${params[key]}\n`;
        
        logString += "\n";
    };

    // If we have queries, add its contents
    if (Object.keys(query).length > 0) {
        logString += "QUERY:\n\n";

        for (const key in query)
            logString += `${key} : ${query[key]}\n`;
        
        logString += "\n";
    };

    // Log the contents
    console.log(`${logString}${BAR}`);
};


export function RESPONSE_LOG_AND_PASS(sendData:any):any {
    console.log(`RESPONSE:`);
    console.log(sendData);
    console.log("==================");
    return sendData;
};

