// Module imports
import React from "react";
import { Navbar } from "flowbite-react";
import  Image from 'next/image';
import Logo from '../images/AlgoRoomsLogo.png';
import { IoPersonCircleOutline } from "react-icons/io5"

// Interface imports
import { headerInterface } from "./Interfaces";

const Header = ({
    
}:headerInterface) => {

    // Code

    return (
        <Navbar fluid={true} rounded={true} className="w-screen h-15 bg-navbar drop-shaddow-[4px]">
            <Image alt="Logo" src={Logo} width={120} height={120}/>
            <div className="flex flex-row space-x-7 items-center">
                <Navbar.Link href="/api/auth/login" className="text-white -translate-y-3" >Sign In / Sign Up</Navbar.Link>
                <IoPersonCircleOutline className="text-white w-6 h-6"></IoPersonCircleOutline>
            </div>
        </Navbar>
    );

};  

export default Header;