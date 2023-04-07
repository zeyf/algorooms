import React from "react";
import { Select, Option } from "@material-tailwind/react";
import { Checkbox } from "@material-tailwind/react";

const CreateRoomCard = () => {
  return (
    <div className="w-[537px] h-[713px]">
      <div className="h-full flex flex-col rounded-2xl bg-white bg-opacity-25 shadow-xl">
        <form className="h-full flex flex-col justify-around p-10">
          <div className="flex justify-center w-full translate-y-[25px]">
            <div>
              <input
                type="text"
                placeholder="Room Name"
                className="w-[348px] bg-white bg-opacity-0 border-b border-white border-t-0 border-l-0 border-r-0 placeholder-white text-white"
              />
            </div>
          </div>
          <p className="flex justify-center text-base text-white dark:text-gray-400 sm:text-lg translate-y-[0px]">
            Select Number of People
          </p>
          <div className="flex justify-center gap-[11px] translate-y-[-35px]">
            <button type="button" className="bg-[#19F8A7] hover:bg-[#051135] focus:bg-[#051135] active:bg-[#051135] focus:text-white active:text-white hover:text-white text-black w-[50px] h-[50px] rounded font-bold">
              1
            </button>
            <button type="button" className="bg-[#19F8A7] hover:bg-[#051135] focus:bg-[#051135] active:bg-[#051135] focus:text-white active:text-white hover:text-white text-black w-[50px] h-[50px] rounded font-bold">
              2
            </button>
            <button type="button" className="bg-[#19F8A7] hover:bg-[#051135] focus:bg-[#051135] active:bg-[#051135] focus:text-white active:text-white hover:text-white text-black w-[50px] h-[50px] rounded font-bold">
              3
            </button>
            <button type="button" className="bg-[#19F8A7] hover:bg-[#051135] focus:bg-[#051135] active:bg-[#051135] focus:text-white active:text-white hover:text-white text-black w-[50px] h-[50px] rounded font-bold">
              4
            </button>
            <button type="button" className="bg-[#19F8A7] hover:bg-[#051135] focus:bg-[#051135] active:bg-[#051135] focus:text-white active:text-white hover:text-white text-black w-[50px] h-[50px] rounded font-bold">
              5
            </button>
            <button type="button" className="bg-[#19F8A7] hover:bg-[#051135] focus:bg-[#051135] active:bg-[#051135] focus:text-white active:text-white hover:text-white text-black w-[50px] h-[50px] rounded font-bold">
              6
            </button>
          </div>
          <div className="flex justify-center translate-y-[-40px] translate-x-[54px] z-50 text-white w-[348px]">
            <Select variant="standard" label="Select Topics" className="border-white text-white">
              <Option>Strings</Option>
              <Option>Arrays</Option>
              <Option>Stacks</Option>
              <Option>Queues</Option>
              <Option>Linked List</Option>
              <Option>Trees</Option>
              <Option>Tries</Option>
              <Option>Recursion</Option>
              <Option>Hash</Option>
              <Option>Graphing</Option>
              <Option>Bitwise</Option>
            </Select>
          </div>
          <div className="flex justify-center gap-[48px] translate-y-[-30px]">
          <button type="button" className="w-[150px] h-[60px] bg-[#19F8A7] hover:bg-[#051135] focus:bg-[#051135] active:bg-[#051135] focus:text-white active:text-white hover:text-white text-black font-bold py-2 px-4 rounded">Public</button>
          <button type="button" className="w-[150px] h-[60px] bg-[#19F8A7] hover:bg-[#051135] focus:bg-[#051135] active:bg-[#051135] focus:text-white active:text-white hover:text-white text-black font-bold py-2 px-4 rounded">Private</button>
          </div>
          <div className="flex justify-center translate-y-[-40px]">
            <button type="submit" className="bg-[#19F8A7] hover:bg-[#051135] hover:text-white text-black w-[200px] h-[60px] font-bold rounded">Create Room</button>
          </div>
        </form>
      </div>
    </div>
  );
};

export default CreateRoomCard;
