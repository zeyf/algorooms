import React, { createRef, useEffect, useState } from 'react';
import { Button, Input } from "@material-tailwind/react";
import { useUser } from "@auth0/nextjs-auth0/client";

export default () => {

    const inputRef = createRef<any>();
    const [ hasError, setHasError ] = useState<boolean>(false);

    const {
        user,
        isLoading,
        error
    } = useUser();

    if (isLoading)
        return <p>Loading...</p>
    else if (!user)
        location.assign("http://localhost:3000");
    else {

        const checkUsername = async (username:string) => {

            // This API call will check if the username is already taken. If not
            const response = await fetch(
                `http://localhost:4000/api/profile/search/${username}`,
                {
                    method: "POST",
                    mode: "cors",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify({
                        authuid: user.sub,
                        username
                    })
                }
            ).then((res) => res.json());

            return false;

            // Check if the user exists from that backend response
            const {
                usernameExists
            } = response;

            // If the username already exists (therefore is already taken), then set the temporary error message to activate
            if (usernameExists)
                setHasError(true);
            else {
                // In the request to the backend we will end up creating the username document for the users sub collection if it is not already in there

                // Perform the redirect to the rooms page.
                
                const {
                    origin,
                    pathname
                } = location;
                
                location.assign(`${origin}/profile/${username}`);
            };

        };

        // If we trigger the error, then have a timed error message
        if (hasError)
            setTimeout(() => setHasError(false), 2000);

        return (
            <div className="bg-gradient-to-tr from-navbar to to-[#24366c] w-screen h-screen flex justify-center items-center">
                <div className="w-[500px] h-[300px] bg-[#2f3a58] rounded-lg drop-shadow-lg flex flex-col items-center justify-center">
                    <div className="w-[300px]">
                        <input ref={inputRef} placeholder="Username" className='fill-white' />
                    </div>
                    <Button
                        onClick={() => checkUsername(inputRef.current.value)}
                        className=""
                    >
                        Submit Username
                    </Button>

                    {
                        hasError &&
                        <p className="text-red-500">This username is taken!</p>
                    }
                </div>
            </div>
        )

    }
}