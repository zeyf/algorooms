import React from "react";
import Select from "react-select";
import { useState } from "react";
import { MdContentCopy } from "react-icons/md";

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
    { value: "Easy", label: "Easy" },
    { value: "Medium", label: "Medium" },
    { value: "Hard", label: "Hard" },
];

const SettingsPop = () => {

    const [ data, setData ] = useState<any>({
        selectedTopics: [],
        selectedLobbyAccess: "Public",
    });

    const setButtonColorOnCondition = (condition:boolean):string => condition ? "bg-darkAccent text-white" : "bg-greenAccent text-darkAccent";

    const handleCopyLink = () => {
        const currentUrl = window.location.href;
        navigator.clipboard.writeText(currentUrl).then(() => {});
    };

    return(
        <div className="w-[270px] h-[300px]">
            <div className="h-full flex-col rounded-2xl bg-[#222C4A] shadow-xl border-black border-[3px]">
                <div className="flex flex-col translate-x-[42.5px] translate-y-[35px] justify-center z-50 text-white w-[185px]">
                    <Select
                        name="colors"
                        className="w-full basic-multi-select text-black"
                        classNamePrefix="select"
                        isMulti={true}
                        options={options}
                        placeholder="Topics"
                        menuPortalTarget={document.body}
                        styles={{ menuPortal: (base) => ({ ...base, zIndex: 99 }) }}
                    />
                </div>
                <div className="flex flex-col translate-x-[42.5px] translate-y-[55px] justify-center z-50 text-white w-[185px]">
                    <Select
                        name="colors"
                        className="w-full basic-multi-select text-black"
                        classNamePrefix="select"
                        isMulti={true}
                        options={optionsDiff}
                        placeholder="Difficulty"
                        menuPortalTarget={document.body}
                        styles={{ menuPortal: (base) => ({ ...base, zIndex: 99 }) }}
                    />
                </div>
            </div>
            <div className="flex flex-col justify-center translate-y-[-140px] translate-x-[45px]">
                <div>
                    <button
                        type="button"
                        className={`${setButtonColorOnCondition(data.selectedLobbyAccess === "Public")} w-[92px] h-[41px] bg font-bold py-2 rounded-tl-[15px] rounded-bl-[15px]`}
                        onClick={() => setData({ ...data, selectedLobbyAccess: "Public" })}
                    >
                        Public
                    </button>
                    <button
                        type="button"
                        className={`${setButtonColorOnCondition(data.selectedLobbyAccess === "Private")} w-[92px] h-[41px] bg font-bold py-2 rounded-tr-[15px] rounded-br-[15px]`}
                        onClick={() => setData({ ...data, selectedLobbyAccess: "Private" })}
                    >
                        Private
                    </button>
                </div>
            </div>
            <button
                type="button"
                className="w-[71px] h-[46px] bg-darkAccent font-bold py-2 rounded-[15px] mt-4 translate-y-[-135px] translate-x-[100px] border-white border-[3px]"
                onClick={() => {
                    const url = window.location.href;
                    navigator.clipboard.writeText(url).then(() => {});
                }}
                >
                    <MdContentCopy className="text-white text-2xl ml-[23px]" />
            </button>
        </div>
    );
};

export default SettingsPop;