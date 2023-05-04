// Module imports
import React, { useContext } from 'react';
import { Navbar } from 'flowbite-react';
import Image from 'next/image';
import Logo from '../images/AlgoRoomsLogo.png';
import { IoPersonCircleOutline } from 'react-icons/io5';
import { useUser } from '@auth0/nextjs-auth0/client';
import Link from 'next/link';

// Interface imports
import { headerInterface } from './Interfaces';
import { AppUserContext } from '@/contexts/AppUserContextLayer';

const Header = ({}: headerInterface) => {
  // Code

  const {
    isLoading,
    user,
    error
  } = useUser();

  const {
    username
  } = useContext(AppUserContext);

  return (
    <div className="w-screen h-16 bg-darkAccent drop-shadow-lg flex flex-row rounded-b-lg items-center">
      <div className="absolute left-3">
        <Link href="/">
          <Image alt="Logo" src={Logo} width={125} height={125} />
        </Link>
      </div>

      <div className="flex flex-row space-x-7 items-center absolute right-5">

        <div className="flex items-center justify-around">

          <Link href={"/announcements"} className="text-white mx-2">
            Announcements
          </Link>
        
          <Link href={"/rooms"} className="text-white mx-2">
            Rooms
          </Link>

          {user ? (
            <Link
              href="/api/auth/logout"
              className="text-white mx-2"
            >
              Sign Out
            </Link>
          ) : (
            <Link
              href="/api/auth/login"
              className="text-white mx-2"
            >
              Sign In
            </Link>
          )}

        </div>

        {isLoading || !user ? (
          <IoPersonCircleOutline
            className="text-white w-6 h-6"
            href="/api/auth/login"
          ></IoPersonCircleOutline>
        ) : (
          <Link href={`/profile/${username}`}>
            <img
              className="text-white w-6 h-6 rounded-full"
              alt="user"
              src={isLoading || !user ? '' : user.picture || ''}
              width={120}
              height={120}
            />
          </Link>
        )}
      </div>
    </div>
  );
};

export default Header;
