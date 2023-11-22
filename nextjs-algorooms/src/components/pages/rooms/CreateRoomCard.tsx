import React, { useContext } from "react";
import { Checkbox } from "@material-tailwind/react";
import { useState } from "react";
import JoinRoomCard from "./JoinRoomCard";
import Select from "react-select";
import { useRouter } from "next/router";
import buildRoute from "@/utilities/buildRoute";
import axios from "axios";
import { useSelf } from "../../../../liveblocks.config";
import { AppUserContext } from "@/contexts/AppUserContextLayer";
import StaticRoomSettingsOptionsData from "@/data/StaticRoomSettingsOptionsData";
import {toast} from 'react-toastify';

const {
  selectableDifficulties,
  selectableTopics
} = StaticRoomSettingsOptionsData;

export default ({
  isPress,
  setIsPress
}) => {

  const [ data, setData ] = useState<any>({
    name: "",
    capacity: 1,
    topics: [  ],
    difficulty: "",
    lobbyAccess: "Public"
  });

  const router = useRouter();

  const {
    username
  } = useContext(AppUserContext);

  const createRoom = async () => {

    /*
    
    Nice to have:
      - Error handling for no name
      - Error handling for no topics
    */

  // Check if the room have a name
  if(data.name.trim() != "") {
    setIsPress(true)
    const response = await axios.post(buildRoute("/api/rooms/create"), { ...data, host: username }).then(res => res.data);
  
      const {
        uid
      } = response;
  
      router.push(`/rooms/${uid}`);
  } else {
    toast("Please enter a room name")
  }
  };

  const setButtonColorOnCondition = (condition:boolean):string => condition ? "bg-darkAccent text-white" : "bg-greenAccent text-darkAccent";

  return (
    <div className="w-[537px] h-[713px]">
      <div className="h-full flex flex-col rounded-2xl bg-white bg-opacity-25 shadow-xl">
        <form className="h-full flex flex-col justify-around p-10">
          <div className="flex justify-center w-full">
            <div>
              <input
                type="text"
                placeholder="Room Name"
                onChange={(event) => {
                  setData({ ...data, name: event.target.value});
                }}
                className="w-[348px] bg-white bg-opacity-0 border-b border-white border-t-0 border-l-0 border-r-0 placeholder-white text-white"
              />
            </div>
          </div>
          <p className="flex justify-center text-base text-white dark:text-gray-400 sm:text-lg translate-y-[0px]">
            Select Number of People
          </p>
          <div className="flex justify-center gap-[11px] translate-y-[-20px]">
            {
              [1,2,3,4,5,6].map(
                (possibleCapacity:number) => (
                  <button
                    className={`${setButtonColorOnCondition(data.capacity === possibleCapacity)} w-[50px] h-[50px] rounded font-bold hover:opacity-75`}
                    onClick={(event) => {
                        event.preventDefault()
                        setData({ ...data, capacity: possibleCapacity })}
                      }
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

            <div>
              <Select
                name="colors"
                className="w-full basic-multi-select text-black"
                classNamePrefix="select"
                isMulti={true}
                options={selectableTopics}
                onChange={(selections:any) => setData({ ...data, topics: selections.map((selection:any) => selection.value) })}
              />

            <p className="my-4 flex justify-center text-base text-white dark:text-gray-400 sm:text-lg translate-y-[0px]">
              Select Difficulty
            </p>
              <Select
                name="colors"
                className="w-full basic-multi-select text-black"
                classNamePrefix="select"
                options={selectableDifficulties}
                onChange={(selection:any) => setData({ ...data, difficulty: selection.value })}
              />
            </div>

          </div>
          <div className="flex flex-col justify-center gap-[20px] translate-y-[-30px]">
            <p className="my-4 flex justify-center text-base text-white dark:text-gray-400 sm:text-lg translate-y-[-20px]">
              Select Lobby Access
            </p>
            <div>
              <button
                type="button"
                className={`${setButtonColorOnCondition(data.lobbyAccess === "Public")} w-[150px] h-[60px] mx-2 bg font-bold py-2 px-4 rounded translate-y-[-20px]`}
                onClick={(event) => {
                    event.preventDefault()
                    setData({ ...data, lobbyAccess: "Public" })}
                  }
                >
                  Public
                </button>
              <button
                type="button"
                className={`${setButtonColorOnCondition(data.lobbyAccess === "Private")} w-[150px] h-[60px] mx-2 bg font-bold py-2 px-4 rounded translate-y-[-20px]`}
                onClick={(event) => {
                    event.preventDefault()
                    setData({ ...data, lobbyAccess: "Private" })}
                  }
              >
                Private
              </button>
            </div>
          </div>
          <div className="flex justify-center translate-y-[-40px]">
            <button
              type="button"
              className="bg-greenAccent hover:bg-darkAccent hover:text-white text-black w-[200px] h-[60px] font-bold rounded"
              disabled={isPress}
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
