import { AppUserContext } from "@/contexts/AppUserContextLayer";
import buildRoute from "@/utilities/buildRoute";
import axios from "axios";
import { useRouter } from "next/router";
import React, { useContext, useRef, useState } from "react";
import { FaCheck, FaTimes } from 'react-icons/fa';

type AdminSubmissionProps = {
    name: string;
    difficulty: string;
    topics: string;
    description: string;
    input:string;
    output: string;
    explanation: string;
    constraints: string;
    hints: string;
};

const AdminSubmission = ({
    name,
    difficulty,
    topics,
    description,
    input,
    output,
    explanation,
    constraints,
    hints,
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

    const router = useRouter();

    const questions = [
        {name: "tempName1", difficulty: "Easy", topics: "Arrays", description: "Temp description for temp 1 and it is much longer than the other descriptions.", input: "[1, 2, 3, 4, 5]", output: "1", explanation: "Because it is the minimum value.", constraints: "2 < nums.length < 1000", hints: "Keep it simple, to the point, and simple as well"},
        {name: "tempName2", difficulty: "Medium", topics: "Trees", description: "Temp description for temp 2", input: "[1, 2, 3, 4, 5]", output: "1", explanation: "Because it is the minimum value.", constraints: "2 < nums.length < 1000", hints: "Keep it simple, to the point, and simple as well"},
        {name: "tempName3", difficulty: "Hard", topics: "Graphing", description: "Temp description for temp 3 and it is also much longer than the other descriptions", input: "[1, 2, 3, 4, 5]", output: "1", explanation: "Because it is the minimum value.", constraints: "2 < nums.length < 1000", hints: "Keep it simple, to the point, and simple as well"},
        {name: "tempName4", difficulty: "Easy", topics: "Hash", description: "Temp description for temp 4", input: "[1, 2, 3, 4, 5]", output: "1", explanation: "Because it is the minimum value.", constraints: "2 < nums.length < 1000", hints: "Keep it simple, to the point, and simple as well"},
        {name: "tempName3", difficulty: "Hard", topics: "Graphing", description: "Temp description for temp 3", input: "[1, 2, 3, 4, 5]", output: "1", explanation: "Because it is the minimum value.", constraints: "2 < nums.length < 1000", hints: "Keep it simple, to the point, and simple as well"},
        {name: "tempName4", difficulty: "Easy", topics: "Hash", description: "Temp description for temp 4", input: "[1, 2, 3, 4, 5]", output: "1", explanation: "Because it is the minimum value.", constraints: "2 < nums.length < 1000", hints: "Keep it simple, to the point, and simple as well"},
    ];

    const [
        madeAnnouncement,
        setMadeAnnouncement
    ] = useState(false);

    const {
        username
    } = useContext(AppUserContext);

    const announcementMessageRef = useRef(null),
          announcementTitleRef = useRef(null);
    
    const createAnnouncement = async () => {

        const response = await axios.post(buildRoute("/api/announcements/create"), {
            title: announcementTitleRef.current.value,
            message: announcementMessageRef.current.value,
            by: username
        }).then(res => res.data);

        const {
            created,
            uid
        } = response;

        setMadeAnnouncement(true);

        setTimeout(() => {
            setMadeAnnouncement(false);
            router.push(`/announcements/${uid}`);
        }, 2000);

    };

    return (
        <div className="w-[1150px] h-[700px]">
            <div className="h-full rounded-2xl bg-white bg-opacity-25 shadow-xl">
                <div className="p-4">
                    <h2 className="text-3xl text-white mt-8 ml-8">
                        Pending Questions
                    </h2>
                </div>
                <div className="w-[975px] h-[212px] mx-auto">
                    <div className="h-full rounded-xl border-2">
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
                        <div className="hide-scrollbar h-[160px] translate-y-[-2px] overflow-y-scroll overflow-hidden">
                            {questions.map((question, index) => (
                                <div key={index} style={{ scrollSnapAlign: 'start' }}>
                                    <AdminSubmission 
                                        name={question.name} 
                                        difficulty={question.difficulty} 
                                        topics={question.topics} 
                                        description={question.description}
                                        input={question.input}
                                        output={question.output}
                                        explanation={question.explanation}
                                        constraints={question.constraints}
                                        hints={question.hints}
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
                    <input
                        placeholder="Enter title"
                        ref={announcementTitleRef}
                    />
                    <textarea
                        placeholder="Enter message"
                        className="bg-transparent w-full h-full rounded-xl border-2 border-white text-white"
                        ref={announcementMessageRef}
                    />
                    <div className="flex justify-end mt-2">
                        <button
                            type="button"
                            className="bg-greenAccent hover:bg-darkAccent hover:text-white text-black w-[150px] h-[60px] font-bold rounded-lg text-lg"
                            onClick={createAnnouncement}
                        >
                        Create
                        </button>
                    </div>

                    {
                        madeAnnouncement && <span className="text-green-500">Created! redirecting to announcement...</span>
                    }

                </div>
            </div>
        </div>
    );
};