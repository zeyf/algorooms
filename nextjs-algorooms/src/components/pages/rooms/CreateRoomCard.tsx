import React from "react";
import { Checkbox } from "@material-tailwind/react";
import rooms from "./DummyRooms";
import { useState } from "react";
import JoinRoomCard from "./JoinRoomCard";
import Select from "react-select";
import { useRouter } from "next/router";

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

export default ({

}) => {

  const [ data, setData ] = useState<any>({
    selectedTopics: [],
    selectedLobbyAccess: "Public",
    capacity: 1
  });

  const router = useRouter();

  const createRoom = async () => {
    // logic

    // ...

    router.push("/rooms/[roomUID]");
  };

  const setButtonColorOnCondition = (condition:boolean):string => condition ? "bg-darkAccent text-white" : "bg-greenAccent text-darkAccent";
  const [roomName, setRoomName] = useState("");

  return (
    <div className="w-[537px] h-[713px] overflow-y-scroll">
      <div className="h-full flex flex-col rounded-2xl bg-white bg-opacity-25 shadow-xl">
        <form className="h-full flex flex-col justify-around p-10">
          <div className="flex justify-center w-full">
            <div>
              <input
                type="text"
                placeholder="Room Name"
                onChange={(event) => {
                  setRoomName(event.target.value);
                }}
                className="w-[348px] bg-white bg-opacity-0 border-b border-white border-t-0 border-l-0 border-r-0 placeholder-white text-white"
              />
            </div>
          </div>
          <p className="flex justify-center text-base text-white dark:text-gray-400 sm:text-lg translate-y-[0px]">
            Select Number of People
          </p>
          <div className="flex justify-center gap-[11px] translate-y-[-35px]">
            {
              [1,2,3,4,5,6].map(
                (possibleCapacity:number) => (
                  <button
                    className={`${setButtonColorOnCondition(data.capacity === possibleCapacity)} w-[50px] h-[50px] rounded font-bold hover:opacity-75`}
                    onClick={(event) => {
                      event.preventDefault();
                      setData({ ...data, capacity: possibleCapacity })
                    }}
                  >
                    { possibleCapacity }
                  </button>
                )
              )
            }
          </div>
          <div className="flex flex-col justify-center translate-y-[-40px] translate-x-[54px] z-50 text-white w-[348px]">
            <p className="my-4 flex justify-center text-base text-white dark:text-gray-400 sm:text-lg translate-y-[0px]">
              Select Topics
            </p>
            <Select
              name="colors"
              className="w-full basic-multi-select text-black"
              classNamePrefix="select"
              isMulti={true}
              options={options}
            />
          </div>
          <div className="flex flex-col justify-center gap-[20px] translate-y-[-30px]">
            <p className="my-4 flex justify-center text-base text-white dark:text-gray-400 sm:text-lg translate-y-[0px]">
              Select Lobby Access
            </p>
            <div>
              <button
                type="button"
                className={`${setButtonColorOnCondition(data.selectedLobbyAccess === "Public")} w-[150px] h-[60px] mx-2 bg font-bold py-2 px-4 rounded`}
                onClick={() => setData({ ...data, selectedLobbyAccess: "Public" })}
                >
                  Public
                </button>
              <button
                type="button"
                className={`${setButtonColorOnCondition(data.selectedLobbyAccess === "Private")} w-[150px] h-[60px] mx-2 bg font-bold py-2 px-4 rounded`}
                onClick={() => setData({ ...data, selectedLobbyAccess: "Private" })}
              >
                Private
              </button>
            </div>
          </div>
          <div className="flex justify-center translate-y-[-40px]">
            <button
              type="button"
              className="bg-greenAccent hover:bg-darkAccent hover:text-white text-black w-[200px] h-[60px] font-bold rounded"
              onClick={createRoom}
              >
                Create Room
              </button>
          </div>
        </form>
      </div>
    </div>
  );
};
