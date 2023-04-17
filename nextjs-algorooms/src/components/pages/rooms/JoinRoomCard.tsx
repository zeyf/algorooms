import React, { useEffect } from 'react';
import { MdPeople } from 'react-icons/md';
import { useRouter } from 'next/router';
import CreateRoomCard from './CreateRoomCard';
import Link from 'next/link';

type RoomJoinSectionProps = {
  name: string;
  topics: string[];
  occupied: number;
  capacity: number;
  difficulty: string;
  uid: string;
};

const RoomJoinSection = ({
  name,
  topics,
  occupied,
  capacity,
  difficulty,
  uid,
}: RoomJoinSectionProps) => {
  const router = useRouter();

  return (
    <div className="w-[452px] h-[77px] flex items-center rounded-xl border-black border-[4px] mx-11 mt-11 bg-white shadow-lg relative">
      <div className="flex flex-col">
        <h2 className="ml-5 text-3xl">{name}</h2>
        <p className="ml-5 mr-auto text-gray-500 text-lg">{topics}</p>
      </div>
      <div className="absolute right-[165px]">
        <MdPeople className="text-black text-5xl mr-2" />
      </div>

      <span>{difficulty}</span>

      <div className="absolute right-[120px]">
        <h2 className="text-3xl ml-10">
          {occupied}/{capacity}
        </h2>
      </div>
      {/* Remember to adjust element to include roomUID */}
      <Link
        href={`/rooms/${uid}`}
        className="bg-greenAccent hover:bg-[#051135] w-[100px] h-[56px] hover:text-white text-black font-bold rounded-xl ml-auto mr-2 text-2xl"
      >
        Join
      </Link>
    </div>
  );
};

export default ({ rooms }: any) => {
  return (
    <div
      className="w-[567px] h-[713px] overflow-y-auto shadow-xl"
      style={{ scrollSnapType: 'y mandatory' }}
    >
      <div className="h-full flex flex-col rounded-2xl bg-white bg-opacity-25 drop-shadow-xl divide-y divide-gray-300 overflow-y-auto pb-[30px]  ">
        <div className="flex flex-col items-center justify-center flex-grow">
          {rooms.map(
            (
              { name, topics, occupied, capacity, difficulty, uid }: any,
              index: any
            ) => (
              <div style={{ scrollSnapAlign: 'start' }}>
                <RoomJoinSection
                  name={name}
                  topics={topics}
                  occupied={occupied}
                  capacity={capacity}
                  difficulty={difficulty}
                  uid={uid}
                  key={index}
                />
              </div>
            )
          )}
        </div>
      </div>
    </div>
  );
};
