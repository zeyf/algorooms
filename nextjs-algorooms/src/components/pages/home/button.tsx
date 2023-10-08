import React from "react";
import { Button } from "flowbite-react";
const Buttons = () => {
    return(
        <div className="z-10 flex justify-center items-center">
            <Button className="w-[140px]" href="/api/auth/login">
                Get Started
            </Button>
        </div>
        
    )
}

export default Buttons; 