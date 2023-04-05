import React from "react";
import { Card, Label, Checkbox, Button, Dropdown } from "flowbite-react";

const CreateRoomCard = () => {
  return (
    <div className="w-[537px] h-[713px]">
      <Card className="h-full flex flex-col">
        <form className="h-full flex flex-col justify-around p-10">
          <div className="flex justify-center w-full">
            <div>
              <input
                type="text"
                placeholder="Room Name"
                className="w-[348px] border-b border-gray-500 border-t-0 border-l-0 border-r-0"
              />
            </div>
          </div>
          <p className="flex justify-center text-base text-gray-500 dark:text-gray-400 sm:text-lg translate-y-[-20px]">
            Select Number of People
          </p>
          <div className="flex justify-center gap-[11px] translate-y-[-50px]">
            <button className="bg-[#19F8A7] hover:bg-[#051135] hover:text-white text-black w-[50px] h-[50px] rounded font-bold">
              1
            </button>
            <button className="bg-[#19F8A7] hover:bg-[#051135] hover:text-white text-black w-[50px] h-[50px] rounded font-bold">
              2
            </button>
            <button className="bg-[#19F8A7] hover:bg-[#051135] hover:text-white text-black w-[50px] h-[50px] rounded font-bold">
              3
            </button>
            <button className="bg-[#19F8A7] hover:bg-[#051135] hover:text-white text-black w-[50px] h-[50px] rounded font-bold">
              4
            </button>
            <button className="bg-[#19F8A7] hover:bg-[#051135] hover:text-white text-black w-[50px] h-[50px] rounded font-bold">
              5
            </button>
            <button className="bg-[#19F8A7] hover:bg-[#051135] hover:text-white text-black w-[50px] h-[50px] rounded font-bold">
              6
            </button>
          </div>
          <div className="flex justify-center translate-y-[-45px] z-50">
            <Dropdown label="Select Topics" className="" inline={true}>
              <Dropdown.Item>
              <Checkbox id="arrays" />
                Arrays</Dropdown.Item>
              <Dropdown.Item>
              <Checkbox id="trees" />
                Trees</Dropdown.Item>
              <Dropdown.Item>
              <Checkbox id="linked" />
                Linked List</Dropdown.Item>
              <Dropdown.Item>
              <Checkbox id="bitwise" />
                Bit Wise</Dropdown.Item>
              <Dropdown.Item>
              <Checkbox id="stacks" />
                Stacks</Dropdown.Item>
              <Dropdown.Item>
              <Checkbox id="graphing" />
                Graphing</Dropdown.Item>
              <Dropdown.Item>
              <Checkbox id="hash" />
                Hash</Dropdown.Item>
            </Dropdown>
          </div>
          <div className="flex justify-center gap-[48px] translate-y-[-30px]">
          <button className="w-[150px] h-[60px] bg-[#19F8A7] hover:bg-[#051135] focus:bg-[#051135] active:bg-[#051135] hover:text-white text-black font-bold py-2 px-4 rounded">Public</button>
          <button className="w-[150px] h-[60px] bg-[#19F8A7] hover:bg-[#051135] hover:text-white text-black font-bold py-2 px-4 rounded">Private</button>
          </div>
          <div className="flex justify-center translate-y-[-20px]">
            <button type="submit" className="bg-[#19F8A7] hover:bg-[#051135] hover:text-white text-black w-[200px] h-[61px] font-bold rounded">Create Room</button>
          </div>
        </form>
      </Card>
    </div>
  );
};

export default CreateRoomCard;
