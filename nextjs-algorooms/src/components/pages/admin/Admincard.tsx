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
                        <div className="h-[50px] w-[975] border-b-2 border-t-0 border-r-0 border-l-0">
                            <div className="flex h-full">
                                <div className="w-1/6 flex items-center justify-center text-lg border-r-2 text-white">
                                Name
                                </div>
                                <div className="w-1/6 flex items-center justify-center text-lg border-r-2 text-white">
                                Difficulty
                                </div>
                                <div className="w-1/6 flex items-center justify-center text-lg border-r-2 text-white">
                                Topic
                                </div>
                                <div className="w-2/6 flex items-center justify-center text-lg border-r-2 text-white">
                                Description
                                </div>
                                <div className="w-1/6 flex items-center justify-center text-lg text-white">
                                Decision
                                </div>
                            </div>
                        </div>
                        <div className="h-[160px]">
                            
                        </div>
                    </div>
                </div>
                <div className="p-4">
                    <h2 className="text-3xl text-white mt-8 ml-8">
                        Create Announcement
                    </h2>
                </div>
                <div className="flex flex-col w-[975px] h-[200px] mx-auto">
                    <textarea className="bg-transparent w-full h-full rounded-xl border-2 border-white text-white" />
                    <div className="flex justify-end mt-2">
                        <button
                        type="button"
                        className="bg-greenAccent hover:bg-darkAccent hover:text-white text-black w-[150px] h-[60px] font-bold rounded-lg text-lg"
                        >
                        Send
                        </button>
                    </div>
                </div>
            </div>
        </div>
    );
};