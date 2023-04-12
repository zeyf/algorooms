// Module imports
import React from 'react';
import { Navbar } from 'flowbite-react';
import Image from 'next/image';
import Logo from '../images/AlgoRoomsLogo.png';
import { IoPersonCircleOutline } from 'react-icons/io5';
import { useUser } from '@auth0/nextjs-auth0/client';
import Link from 'next/link';

// Interface imports
import { headerInterface } from './Interfaces';

const Header = ({}: headerInterface) => {
  // Code

  const { user, isLoading, error } = useUser();
  return (
    <div className="w-screen h-16 bg-darkAccent drop-shadow-lg flex flex-row rounded-b-lg items-center">
      <div className="absolute left-3">
        <Image alt="Logo" src={Logo} width={125} height={125} />
      </div>

      <div className="flex flex-row space-x-7 items-center absolute right-5">
        <Link href={'/rooms'} className="text-white">
          Rooms
        </Link>
        {user ? (
          <Navbar.Link
            href="/api/auth/logout"
            className="text-white -translate-y-3"
          >
            Sign Out
          </Navbar.Link>
        ) : (
          <Navbar.Link
            href="/api/auth/login"
            className="text-white -translate-y-3"
          >
            Sign In
          </Navbar.Link>
        )}

        {isLoading || !user ? (
          <IoPersonCircleOutline
            className="text-white w-6 h-6"
            href="/api/auth/login"
          ></IoPersonCircleOutline>
        ) : (
          <a href={`/profile/${user.nickname}`}>
            <Image
              className="text-white w-6 h-6 rounded-full"
              alt="user"
              src={isLoading || !user ? '' : user.picture || ''}
              width={120}
              height={120}
            />
          </a>
        )}
      </div>
    </div>
  );
};

export default Header;
