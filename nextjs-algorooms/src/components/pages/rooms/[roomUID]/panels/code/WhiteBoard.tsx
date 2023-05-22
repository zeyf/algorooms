// module imports
import { RoomContext } from "@/contexts/RoomContextLayer"
import { useContext } from "react"
import { IoCloseSharp } from "react-icons/io5";


export default () => {
    const {
        whiteBoard,
        setWhiteBoard
    } = useContext(RoomContext)

    return (
        <div className="h-5/6 w-5/6 bg-white absolute z-40 rounded-lg drop-shadow-2xl -translate-y-6">
            <IoCloseSharp size={40} className="absolute right-0 text-black hover:text-gray-500" onClick={() => setWhiteBoard(!whiteBoard)}/>
        </div>
    )
}