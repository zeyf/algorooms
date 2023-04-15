// Module imports
import React from "react";
import { useUser } from '@auth0/nextjs-auth0/client';

// Interface imports
import { textFeedInterface } from "./Interfaces";


export default ({

}:textFeedInterface) => {

    // Code
    const {
        isLoading,
        user,
        error
      } = useUser();

    return (
        <section>
            {/* Body */}
            <div  className="overflow-y-auto max-h-[400px] bg-darkAccent flex">
                <div className="my-2 mx-2">
                    <span className="text-white flex flex-row">
                        <img src={isLoading || !user ? '' : user.picture || ''} alt="user"
                        className="w-6 h-6 rounded-full"/>
                        : Hello there!
                    </span> 
                </div>
            </div>
        </section>
    );

};
