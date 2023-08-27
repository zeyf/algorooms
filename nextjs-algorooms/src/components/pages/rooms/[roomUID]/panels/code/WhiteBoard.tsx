// module imports
import { RoomContext } from "@/contexts/RoomContextLayer"
import { useContext } from "react"
import { IoCloseSharp } from "react-icons/io5";
// import { Whiteboard } from 'whiteboard-react';


export default () => {
    const {
        whiteBoard,
        setWhiteBoard
    } = useContext(RoomContext)

    return (
        <div className="h-5/6 w-5/6 bg-white absolute z-40 rounded-lg drop-shadow-2xl -translate-y-6">
            <IoCloseSharp size={40} className="absolute right-0 text-black hover:text-gray-500 z-50" onClick={() => setWhiteBoard(!whiteBoard)}/>
            {/* <Whiteboard /> */}
        </div>
    )
}