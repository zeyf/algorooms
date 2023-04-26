import React from "react";

export default ({

}) => {

    return (
        <div className="w-[1150px] h-[700px]">
            <div className="h-full rounded-2xl bg-white bg-opacity-25 shadow-xl">
                <div className="p-4">
                    <h2 className="text-3xl text-white mt-8 ml-8">
                        Pending Questions
                    </h2>
                </div>
                <div className="w-[975px] h-[210px] mx-auto">
                    <div className="h-full rounded-xl border border-2">

                    </div>
                </div>
                <div className="p-4">
                    <h2 className="text-3xl text-white mt-8 ml-8">
                        Create Announcement
                    </h2>
                </div>
                <div className="w-[975px] h-[150px] mx-auto">
                    <textarea className="bg-transparent w-full h-full rounded-xl border-2 border-white text-white"/>
                </div>
            </div>
        </div>
    );
};