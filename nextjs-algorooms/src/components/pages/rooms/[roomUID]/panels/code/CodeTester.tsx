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
        <section>
            <div className="bg-[#303841] w-[822px] h-[150px] rounded-lg mt-3">
                
            </div>
        </section>
    );

};
