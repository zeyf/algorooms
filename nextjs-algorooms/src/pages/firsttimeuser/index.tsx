import React, { createRef, useContext, useEffect, useState } from 'react';
import { Button, Input } from '@material-tailwind/react';
import { useUser } from '@auth0/nextjs-auth0/client';
import { useRouter } from 'next/router';
import buildRoute from '@/utilities/buildRoute';
import axios from 'axios';
import { AppUserContext } from '@/contexts/AppUserContextLayer';

export default () => {
  const inputRef = createRef<any>();

  const [
    hasError,
    setHasError
  ] = useState<boolean>(false);

  const router = useRouter();

  const {
    user,
    isLoading,
    error
  } = useUser();

  const {
    username
  } = useContext(AppUserContext);

  if (isLoading) return <p>Loading...</p>;
  else if (!user) {
    router.push("/");
    return <></>;
  } else if (username) {
    router.push("/rooms");
  } else {
    const checkUsername = async e => {
      e.preventDefault();

      // This API call will check if the username is already taken. If not
      const response = await axios.get(buildRoute(`/api/users/verify/${inputRef.current.value}`)).then(res => res.data);

      // Check if the user exists from that backend response
      const {
        exists,
        profileData
      } = response;

      if (exists)
        setHasError(true);
      else {

        await axios.post(buildRoute(`/api/users/create`), {
          authuid: user.sub,
          username: inputRef.current.value,
          picture: user.picture
        }).then(res => router.push("/rooms"));

      };

    };

    // If we trigger the error, then have a timed error message
    if (hasError) setTimeout(() => setHasError(false), 2000);

    return (
      <div className="bg-gradient-to-tr from-darkAccent to to-gradientEnd w-screen h-screen flex justify-center items-center">
        <div className="w-[500px] h-[300px] bg-darkAccent rounded-lg drop-shadow-lg flex flex-col items-center justify-center">
          <div className="w-[300px]">
            <input
              ref={inputRef}
              placeholder="Username"
              className="fill-white"
            />
          </div>
          <Button
            onClick={checkUsername}
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
