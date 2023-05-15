// Module imports
import React, { useEffect } from "react";

// Interface imports
import { codeTesterInterface } from "./Interfaces";
import { useStorage } from "../../../../../../../liveblocks.config";

export default ({

}:codeTesterInterface) => {

    const codeTestIteration = useStorage(r => r);

    useEffect(() => {

    }, [ codeTestIteration ]);

    return (
        <section className="bg-white w-full">
            
        </section>
    );

};
