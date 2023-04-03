// Module imports
import React from "react";
import { Navbar } from "flowbite-react";
import  Image from 'next/image';
import Logo from '../images/AlgoRoomsLogo.png';
import { IoPersonCircleOutline } from "react-icons/io5"
import { useUser } from '@auth0/nextjs-auth0/client';

// Interface imports
import { headerInterface } from "./Interfaces";

const Header = ({
    
}:headerInterface) => {

    // Code

    const { user, isLoading, error } = useUser();

    return (
        <Navbar fluid={true} rounded={true} className="w-screen h-15 bg-navbar drop-shaddow-[4px]">
            <Image alt="Logo" src={Logo} width={120} height={120}/>
            <div className="flex flex-row space-x-7 items-center">

                {
                    user ?
                    <Navbar.Link href="/api/auth/logout" className="text-white -translate-y-3" >Sign Out</Navbar.Link>
                    :
                    <Navbar.Link href="/api/auth/login" className="text-white -translate-y-3" >Sign In</Navbar.Link>
                }
                
                {
                    isLoading || !user ? 
                    <IoPersonCircleOutline className="text-white w-6 h-6"></IoPersonCircleOutline>
                    :
                    <img className="text-white w-6 h-6 rounded-full" alt="user" src={isLoading || !user ? "" : user.picture || ""} width={120} height={120}/>
                }
            </div>
        </Navbar>
    );

};  

export default Header;