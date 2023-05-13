import React, { useContext, useEffect } from "react";
import Select from "react-select";
import { useState } from "react";
import { MdContentCopy } from "react-icons/md";
import axios from "axios";
import buildRoute from "@/utilities/buildRoute";
import { RoomContext } from "@/contexts/RoomContextLayer";
import { toast } from "react-toastify";
import { useUser } from "@auth0/nextjs-auth0/client";
import { AppUserContext } from "@/contexts/AppUserContextLayer";

const options = [
    { value: "Strings", label: "Strings" },
    { value: "Arrays", label: "Arrays" },
    { value: "Stacks", label: "Stacks" },
    { value: "Queues", label: "Queues" },
    { value: "Linked Lists", label: "Linked Lists" },
    { value: "Trees", label: "Trees" },
    { value: "Tries", label: "Tries" },
    { value: "Recursion", label: "Recursion" },
    { value: "Hash Tables", label: "Hash Tables" },
    { value: "Graphs", label: "Graphs" },
    { value: "Bitwise", label: "Bitwise" }
  ];

const optionsDiff = [
    { value: "Simpler", label: "Simpler" },
    { value: "Simple", label: "Simple" },
    { value: "Not Simple", label: "Not Simple" },
];

const SettingsPopUp = ({
    isSettingsOpen,
    setIsSettingsOpen,
    buildSettingsChangeToastMessage
}) => {

    const {
        username
    } = useContext(AppUserContext);

    const {
        socket,
        uid,

        topics,
        setTopics,
        lobbyAccess,
        setLobbyAccess,
        difficulty,
        setDifficulty
    } = useContext(RoomContext);

    const [
        data,
        setData
    ] = useState<any>({
        tempTopics: topics,
        tempLobbyAccess: lobbyAccess,
        tempDifficulty: difficulty,
        trueChange: false
    });

    useEffect(() => {
        
        return () => {

            if (data.trueChange) {

                // Reset the state on dismount
                setData({
                    tempTopics: topics,
                    tempLobbyAccess: lobbyAccess,
                    tempDifficulty: difficulty,
                    trueChange: false
                });

            } else {
                
                setData({
                    ...data,
                    trueChange: false
                });

            }

        };

    }, [  ]);

    const setButtonColorOnCondition = (condition:boolean):string => condition ? "bg-darkAccent text-white" : "bg-greenAccent text-darkAccent";

    const handleSave = async e => {
        e.preventDefault();

        const response = await axios.post(buildRoute(`/api/rooms/update/${uid}`), {
            difficulty: data.tempDifficulty,
            topics: data.tempTopics,
            lobbyAccess: data.tempLobbyAccess
        }).then(res => res.data);

        const {
            updated
        } = response;
        
        // Change to test
        if (updated) {

            setData({
                ...data,
                trueChange: true
            });

            const topicChange = data.tempTopics.sort().toString() !== topics.sort().toString() ? data.tempTopics : null,
                  difficultyChange = data.tempDifficulty !== difficulty ? data.tempDifficulty : null,
                  lobbyAccessChange = data.tempLobbyAccess !== lobbyAccess ? data.tempLobbyAccess : null

            socket.emit("backendSettingsChange", {
                topics: topicChange,
                difficulty: difficultyChange,
                lobbyAccess: lobbyAccessChange
            }, uid, username, socket.id);


            setIsSettingsOpen(false);

            if (topicChange !== null)
                setTopics(topicChange);
            if (difficultyChange !== null)
                setDifficulty(difficulty);
            if (lobbyAccessChange !== null)
                setLobbyAccess(lobbyAccessChange);

            const toastMessage = buildSettingsChangeToastMessage(
                username,
                topicChange,
                difficultyChange,
                lobbyAccessChange
            );

            if (toastMessage !== null)
                toast(toastMessage);

        };

    };

    return (
        <div className="w-auto h-[300px]">
            <div className="h-auto flex flex-col rounded-2xl  shadow-xl border-black border-[3px] items-center bg-[#222C4A]">
                <div className="flex flex-col justify-center z-50 text-white w-[185px] mt-3 ml-2 mr-2">
                    <Select
                        name="colors"
                        className="w-full basic-multi-select text-black"
                        classNamePrefix="select"
                        isMulti={true}
                        options={options}
                        placeholder="Topics"
                        menuPortalTarget={document.body}
                        styles={{ menuPortal: (base) => ({ ...base, zIndex: 99 }) }}
                        defaultValue={topics.map(topic => { return { value: topic, label: topic } })}
                        value={data.tempTopics.map(topic => { return { value: topic, label: topic } })}
                        onChange={(selections:any) => setData({ ...data, tempTopics: selections.map((selection:any) => selection.value) })}
                    />
                </div>
                <div className="text-white w-[185px] mt-2 ml-2 mr-2">
                    <Select
                        name="colors"
                        className="w-full basic-multi-select text-black"
                        classNamePrefix="select"
                        options={optionsDiff}
                        placeholder="Difficulty"
                        menuPortalTarget={document.body}
                        styles={{ menuPortal: (base) => ({ ...base, zIndex: 99 }) }}
                        defaultValue={difficulty}
                        value={data.tempDifficulty}
                        onChange={({ value, label }) => {setData({ ...data, tempDifficulty: value })}}
                    />
                </div>
                <div className="flex flex-col justify-center items-center">
                    <div className="mt-2">
                        <button
                            type="button"
                            className={`${setButtonColorOnCondition(data.tempLobbyAccess === "Public")} w-[92px] h-[41px] bg font-bold py-2 rounded-tl-[15px] rounded-bl-[15px]`}
                            onClick={() => setData({ ...data, tempLobbyAccess: "Public" })}
                        >
                            Public
                        </button>
                        <button
                            type="button"
                            className={`${setButtonColorOnCondition(data.tempLobbyAccess === "Private")} w-[92px] h-[41px] bg font-bold py-2 rounded-tr-[15px] rounded-br-[15px]`}
                            onClick={() => setData({ ...data, tempLobbyAccess: "Private" })}
                        >
                            Private
                        </button>
                    </div>
                </div>
                <div className="flex flex-row mt-5 mb-3 space-x-2">
                    <button
                    type="button"
                    className="w-[71px] h-[46px] bg-darkAccent font-bold py-2 rounded-[15px] border-white border-[3px]"
                    onClick={() => {
                        const url = window.location.href;
                        navigator.clipboard.writeText(url).then(() => {});
                    }}
                    >
                        <MdContentCopy className="text-white text-2xl ml-[23px]" />
                    </button>
                    <div className="flex w-[71px] h-[46px] bg-darkAccent font-bold rounded-[15px] items-center justify-center border-white border-[3px]">
                        <button
                            onClick={handleSave}
                            className="text-white"
                        >
                            Save
                        </button>
                    </div>
                </div>
                
            </div>




        </div>
    );
};

export default SettingsPopUp;