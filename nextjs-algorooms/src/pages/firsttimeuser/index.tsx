import React, { createRef, useEffect, useState } from 'react';
import { Button, Input } from '@material-tailwind/react';
import { useUser } from '@auth0/nextjs-auth0/client';
import { useRouter } from 'next/router';

export default () => {
  const inputRef = createRef<any>();
  const [hasError, setHasError] = useState<boolean>(false);
  const router = useRouter();

  const { user, isLoading, error } = useUser();

  if (isLoading) return <p>Loading...</p>;
  else if (!user) {
    router.push('/');
    return <></>;
  } else {
    const checkUsername = async (username: string) => {
      const { pathname } = useRouter();

      // This API call will check if the username is already taken. If not
      const response = await fetch(
        // Use this response to then call the /api/user/create route
        `http://localhost:4000/api/user/search/${username}`,
        {
          method: 'POST',
          mode: 'cors',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            source: pathname,
            authuid: user.sub,
            username,
          }),
        }
      ).then((res) => res.json());

      // Check if the user exists from that backend response
      const { exists, profileData } = response;

      // If the username already exists (therefore is already taken), then set the temporary error message to activate
      if (exists) setHasError(true);
      else {
        // In the request to the backend we will end up creating the username document for the users sub collection if it is not already in there

        // Perform the redirect to the rooms page.

        console.log(`${profileData}`);
      }
    };

    // If we trigger the error, then have a timed error message
    if (hasError) setTimeout(() => setHasError(false), 2000);

    return (
      <div className="bg-gradient-to-tr from-navbar to to-gradientEnd w-screen h-screen flex justify-center items-center">
        <div className="w-[500px] h-[300px] bg-[#2f3a58] rounded-lg drop-shadow-lg flex flex-col items-center justify-center">
          <div className="w-[300px]">
            <input
              ref={inputRef}
              placeholder="Username"
              className="fill-white"
            />
          </div>
          <Button
            onClick={() => checkUsername(inputRef.current.value)}
            className=""
          >
            Submit Username
          </Button>

          {hasError && <p className="text-red-500">This username is taken!</p>}
        </div>
      </div>
    );
  }
};
