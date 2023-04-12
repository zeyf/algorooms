import { io } from "socket.io-client";
import Header from "../components/shared/Header";
import BigText from "@/components/pages/home/BigText";
import Editor from "../components/images/Room.png";
import Image from "next/image";
import Buttons from "@/components/pages/home/button";

// import { withApiAuthRequired } from '@auth0/nextjs-auth0';
// import { useUser } from '@auth0/nextjs-auth0/client';

// const socket = io('http://localhost:3000')

export default () => {

  return (
    <div className="bg-gradient-to-tr from-darkAccent to to-[#24366c] w-screen h-screen flex flex-col">
      <Header />
      <div className="w-1000 h-1000  flex flex-row space-x-16 justify-center mt-10 ">
        <div className="flex flex-col animate-fade-in-down">
          <BigText />
          <div className="translate-x-20 -translate-y-14">
            <Buttons />
          </div>
        </div>

        <Image src={Editor} alt="editor" width={900} height={900} className="rounded-lg translate-y-10 drop-shadow-lg animate-fade-in-down"></Image>
      </div>
      <div className="absolute bottom-0 left-0 w-screen overflow-hidden leading-none rotate-180">
        <svg data-name="Layer 1" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 120" preserveAspectRatio="none">
            <path d="M0,0V46.29c47.79,22.2,103.59,32.17,158,28,70.36-5.37,136.33-33.31,206.8-37.5C438.64,32.43,512.34,53.67,583,72.05c69.27,18,138.3,24.88,209.4,13.08,36.15-6,69.85-17.84,104.45-29.34C989.49,25,1113-14.29,1200,52.47V0Z" opacity=".25" className="fill-[#24366C]"></path>
            <path d="M0,0V15.81C13,36.92,27.64,56.86,47.69,72.05,99.41,111.27,165,111,224.58,91.58c31.15-10.15,60.09-26.07,89.67-39.8,40.92-19,84.73-46,130.83-49.67,36.26-2.85,70.9,9.42,98.6,31.56,31.77,25.39,62.32,62,103.63,73,40.44,10.79,81.35-6.69,119.13-24.28s75.16-39,116.92-43.05c59.73-5.85,113.28,22.88,168.9,38.84,30.2,8.66,59,6.17,87.09-7.5,22.43-10.89,48-26.93,60.65-49.24V0Z" opacity=".5" className="fill-[#24366C]"></path>
            <path d="M0,0V5.63C149.93,59,314.09,71.32,475.83,42.57c43-7.64,84.23-20.12,127.61-26.46,59-8.63,112.48,12.24,165.56,35.4C827.93,77.22,886,95.24,951.2,90c86.53-7,172.46-45.71,248.8-84.81V0Z" className="fill-[#24366C]"></path>
        </svg>
      </div>
    </div>
  )
}