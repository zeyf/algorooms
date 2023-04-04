import Image from "next/image";
import ProgressBar from "@/components/pages/profile/ProgressBar";

const profile = () => {

  const account_level = 68;
  const currExp = 1100;
  const maxExp = 6100;

  return (
    <div className="grid auto-row-fr grid-cols-2">
      <div className="flex justify-between items-center col-span-2">
        {/* User */}
        <div className="flex-col w-1/3 p-2 h-full">
          {/* Avatar and User Info */}
          <div>
            <div className="flex justify-between">
              {/* Avatar */}
              <Image
                className="rounded-full"
                src="/dummy_data/borat.webp" 
                height={188}
                width={188}
                alt=""
              />
              {/* User Info */}
              <div className="flex-col">
                <h1 className="text-lg">John Huber</h1>
                <h3 className="text-sm">Joined 23 March 2023</h3>
              </div>
            </div>
          </div>
          {/* Exp bar */}
          <div className="flex justify-between items-center">
            {/* Level */}
            <h3>{account_level}</h3>

            {/* Exp Bar */}
            <ProgressBar backgroundColor={"black"} accentColor={"green-500"} numerator={currExp} denominator={maxExp} width={"full"} height={"3"}/>
          </div>
        </div>

        {/* Problems */}
        <div className="w-1/3 p-2 h-full">
          <h3>Problems</h3>
          <div className="flex-col justify-between w-full h-full">
            {/* Simpler */}
            <ProgressBar backgroundColor={"green-800"} accentColor={"green-500"} numerator={5} denominator={25} width={"full"} height={"3"}/>
            
            {/* Simple */}
            <ProgressBar backgroundColor={"yellow-800"} accentColor={"yellow-500"} numerator={5} denominator={25} width={"full"} height={"3"}/>
            
            {/* Not Simple */}
            <ProgressBar backgroundColor={"red-800"} accentColor={"red-500"} numerator={5} denominator={25} width={"full"} height={"3"}/>
          </div>
        </div>

        {/* Topics */}
        <div className="w-1/3 p-2 h-full">
          Topics
        </div>
      </div>
      
      {/* Statis */}
      <div>
        Statistics
      </div>

      {/* Rating */}
      <div>
        Rating
      </div>
    </div>
  )
}

export default profile