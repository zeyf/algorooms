import React from "react";
import { MdPeople } from "react-icons/md";

type RoomJoinSectionProps = {
  roomName: string;
  topic: string;
  occupied: number;
  capacity: number;
}

const RoomJoinSection = ({roomName, topic, occupied, capacity}: RoomJoinSectionProps) => {
  return (
    <div className="w-[452px] h-[77px] flex items-center border rounded-xl border-black border-[4px] mx-11 mt-11 bg-white shadow-lg relative">
      <div className="flex flex-col">
        <h2 className="ml-5 text-3xl">{roomName}</h2>
        <p className="ml-5 mr-auto text-gray-500 text-lg">{topic}</p>
      </div>
      <div className="absolute right-[165px]">
        <MdPeople className="text-black text-5xl mr-2" />
      </div>
      <div className="absolute right-[120px]">
        <h2 className="text-3xl ml-10">{occupied}/{capacity}</h2>
      </div>
      <button className="bg-[#19F8A7] hover:bg-[#051135] w-[100px] h-[56px] hover:text-white text-black font-bold rounded-xl ml-auto mr-2 text-2xl">
        Join
      </button>
    </div>
  );
};

const JoinRoomCard = () => {
  const rooms = [
    {roomName: "CS Amigos", topic: "Stacks, Queues", occupied: 2, capacity: 4},
    {roomName: "Code Amigos", topic: "Linked List", occupied: 3, capacity: 5},
    {roomName: "Simple", topic: "Trees, Tries", occupied: 4, capacity: 6},
    {roomName: "On Point", topic: "Recurssion", occupied: 2, capacity: 3},
    {roomName: "Simple as well", topic: "Graphing, Hash", occupied: 1, capacity: 3},
    {roomName: "Another Room", topic: "Another Topic", occupied: 2, capacity: 4},
    {roomName: "Another Room", topic: "Another Topic", occupied: 2, capacity: 4},
  ];

  return (
    <div className="w-[567px] h-[713px] overflow-y-auto shadow-xl" style={{ scrollSnapType: 'y mandatory' }}>
      <div className="h-full flex flex-col rounded-2xl bg-white bg-opacity-25 shadow-xl divide-y divide-gray-300 overflow-y-auto pb-[30px] scrollbar scrollbar-thumb-white">
        <div className="flex flex-col items-center justify-center flex-grow">
          {rooms.map((room, index) => (
            <div key={index} style={{ scrollSnapAlign: 'start' }}>
              <RoomJoinSection roomName={room.roomName} topic={room.topic} occupied={room.occupied} capacity={room.capacity} />
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default JoinRoomCard;