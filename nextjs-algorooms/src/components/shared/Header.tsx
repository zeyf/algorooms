// Module imports
import React from "react";
import { Navbar, Button } from "flowbite-react";
import { Nav, Container } from 'react-bootstrap';

// Interface imports
import { headerInterface } from "./Interfaces";

const Header = ({
    
}:headerInterface) => {

    // Code

    return (
        <Navbar fluid={true} rounded={true} className="w-screen bg-[#051135] drop-shaddow-{4px}">
            <Navbar.Brand href="/algorooms/nextjs-algorooms/src/pages/index.tsx">
                <span className="self-center whitespace-nowrap text-xl font-semibold text-green-500 dark:text-white">Algorooms</span>
            </Navbar.Brand>
            <Navbar.Collapse>
                <Navbar.Link href="/algorooms/nextjs-algorooms/src/pages/index.tsx" className="text-green-500">Rooms</Navbar.Link>
            </Navbar.Collapse>
        </Navbar>
    );

};

export default Header;