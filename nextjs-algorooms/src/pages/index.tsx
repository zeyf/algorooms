import { io } from "socket.io-client"

const socket = io('http://localhost:3000')

export default () => {
  return (
    <div className="bg-[#222C4A] w-screen h-screen flex justify-center items-center">
      <div className="bg-white w-[565px] h-[647px] rounded-lg ">

      </div>
    </div>
  )
}
