import React from 'react';
import { Input } from "@material-tailwind/react";


export default () => {
    return (
        <div className="bg-gradient-to-tr from-navbar to to-[#24366c] w-screen h-screen flex justify-center items-center">
            <div className="w-[500px] h-[300px] bg-[#2f3a58] rounded-lg drop-shadow-lg flex items-center justify-center">
                <div className="w-[300px]">
                    <Input variant="standard" label="Username" className='fill-white'/>
                </div>
                
            </div>
        </div>
    )
}

