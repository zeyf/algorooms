import React from "react";
import { FaCheck, FaTimes } from 'react-icons/fa';

type AdminSubmissionProps = {
    name: string;
    difficulty: string;
    topics: string;
    description: string;
};

const AdminSubmission = ({
    name,
    difficulty,
    topics,
    description,
}: AdminSubmissionProps) => {
    
    return (
        <div className="flex h-[40px] w-[975px] translate-x-[-2px] hover:bg-white hover:bg-opacity-25">
            <div className="w-1/6 flex items-center justify-center text-lg border-r-2 border-t text-white overflow-hidden">
                <div className="truncate ml-2">
                    { name }
                </div>
            </div>
            <div className="w-1/6 flex items-center justify-center text-lg border-r-2 border-t text-white">
                { difficulty }
            </div>
            <div className="w-1/6 flex items-center justify-center text-lg border-r-2 border-t text-white overflow-hidden">
                <div className="truncate ml-2">
                    { topics }
                </div>
            </div>
            <div className="w-2/6 flex items-center justify-center text-lg border-r-2 border-t text-white overflow-hidden">
                <div className="truncate ml-2">
                    { description }
                </div>
            </div>
            <div className="w-1/6 flex items-center justify-center text-lg text-white border-t gap-1">
                <button className="w-[75px] h-[30px] bg-greenAccent text-black rounded hover:scale-110 hover:bg-[#14C786] hover:border hover:border-black">< FaCheck className="ml-2" /></button>
                <button className="w-[75px] h-[30px] bg-[#EB1313] text-black rounded hover:scale-110 hover:bg-[#B10F0F] hover:border hover:border-black">< FaTimes className="ml-2" /></button>
            </div>
        </div>
    );
};

export default ({

}) => {

    const questions = [
        {name: "tempName1", difficulty: "Easy", topics: "Arrays", description: "Temp description for temp 1 and it is much longer than the other descriptions"},
        {name: "tempName2", difficulty: "Medium", topics: "Trees", description: "Temp description for temp 2"},
        {name: "tempName3", difficulty: "Hard", topics: "Graphing", description: "Temp description for temp 3 and it is also much longer than the other descriptions"},
        {name: "tempName4", difficulty: "Easy", topics: "Hash", description: "Temp description for temp 4"},
        {name: "tempName3", difficulty: "Hard", topics: "Graphing", description: "Temp description for temp 3"},
        {name: "tempName4", difficulty: "Easy", topics: "Hash", description: "Temp description for temp 4"},
    ];

    return (
        <div className="w-[1150px] h-[700px]">
            <div className="h-full rounded-2xl bg-white bg-opacity-25 shadow-xl">
                <div className="p-4">
                    <h2 className="text-3xl text-white mt-8 ml-8">
                        Pending Questions
                    </h2>
                </div>
                <div className="w-[975px] h-[212px] mx-auto">
                    <div className="h-full rounded-xl border border-2">
                        <div className="h-[50px] w-[975px] border-b-2 border-t-0 border-r-0 border-l-0 translate-x-[-2px]">
                            <div className="flex h-full">
                                <div className="w-1/6 flex items-center justify-center text-lg border-r-2 text-white bg-white bg-opacity-25 rounded-tl-xl">
                                Name
                                </div>
                                <div className="w-1/6 flex items-center justify-center text-lg border-r-2 text-white bg-white bg-opacity-25">
                                Difficulty
                                </div>
                                <div className="w-1/6 flex items-center justify-center text-lg border-r-2 text-white bg-white bg-opacity-25">
                                Topics
                                </div>
                                <div className="w-2/6 flex items-center justify-center text-lg border-r-2 text-white bg-white bg-opacity-25">
                                Description
                                </div>
                                <div className="w-1/6 flex items-center justify-center text-lg text-white bg-white bg-opacity-25 rounded-tr-lg">
                                Decision
                                </div>
                            </div>
                        </div>
                        <div className="h-[160px] translate-y-[-2px] overflow-y-scroll overflow-hidden">
                            {questions.map((question, index) => (
                                <div key={index} style={{ scrollSnapAlign: 'start' }}>
                                    <AdminSubmission 
                                        name={question.name} 
                                        difficulty={question.difficulty} 
                                        topics={question.topics} 
                                        description={question.description} 
                                    />
                                </div>
                            ))}
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