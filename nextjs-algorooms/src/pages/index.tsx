import { io } from "socket.io-client"
import LoginButton from "../components/pages/home/button";
import Header from "../components/shared/Header";

const socket = io('http://localhost:3000')

export default () => {
  return (
    <div className="bg-[#222C4A] w-screen h-screen">
      <Header/>
    </div>
  )
}
