// Import statements
import React from "react";
import { withPageAuthRequired } from "@auth0/nextjs-auth0";
import QuestionPanel from "@/components/pages/rooms/[roomUID]/panels/question/QuestionPanel";
import CodePanel from "@/components/pages/rooms/[roomUID]/panels/code/CodePanel";
import TextPanel from "@/components/pages/rooms/[roomUID]/panels/text/TextPanel";

import { codePanelInterface } from "@/components/pages/rooms/[roomUID]/panels/code/Interfaces";
import { textPanelInterface } from "@/components/pages/rooms/[roomUID]/panels/text/Interfaces";

///

import Split from "react-split";
import Header from "@/components/shared/Header";
import QuestionDummyData from "./QuestionDummyData";

export default () => {

    return (
        <>
            <Header />
            <div className="bg-[#222C4A] w-screen h-screen flex flex-row-reverse justify-center items-center">
                <div className="w-2/3 h-screen flex flex-col justify-center items-center">
                    
                    <Split className={`w-screen flex`}>

                        <QuestionPanel
                            { ...QuestionDummyData }
                        />
                        
                        <CodePanel />
                        {/*
                        <TextPanel
                            // Props
                            
                        /> 
                        */}
                    </Split>


                </div>
            </div>
        </>
    )
    

};

// Auth-guarding the /rooms/[roomUID] page
export const getServerSideProps = withPageAuthRequired({
    async getServerSideProps(ctx) {
        return {
            props: {

            }
        };
    }
});