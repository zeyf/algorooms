import React from "react";
import { Button } from "flowbite-react";
const LoginButton = () => {
    return(
        <div>
            <Button color="white" className="border-2 border-black w-[376px] h-[45px] font-abc my-4">Continue with Google</Button>
            <Button color="white" className="border-2 border-black w-[376px] h-[45px] font-abc my-4">Continue with GitHub</Button>
            <Button color="white" className="border-2 border-black w-[376px] h-[45px] font-abc my-4">Continue with LinkedIn</Button>
            <Button color="white" className="border-2 border-black w-[376px] h-[45px] font-abc my-4">Continue with Facebook</Button>
        </div>
        
    )
}

export default LoginButton; 