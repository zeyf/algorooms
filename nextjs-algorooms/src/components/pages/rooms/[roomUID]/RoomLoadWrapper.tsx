import { useContext, useEffect } from "react";
import { useMutation, useOthers, useRoom, useSelf, useStorage } from "../../../../../liveblocks.config";
import { AppUserContext } from "@/contexts/AppUserContextLayer";
import Split from "react-split";
import CodePanel from "./panels/code/CodePanel";
import TextPanel from "./panels/text/TextPanel";
import QuestionPanel from "./panels/question/QuestionPanel";
import { RoomContext } from "@/contexts/RoomContextLayer";
import WhiteBoard from "./panels/code/WhiteBoard";

export default ({

}) => {

  // Room Context
  const {
    whiteBoard
  } = useContext(RoomContext);

  // Get the room
  const room = useRoom();

  // Check if you are connected to the room
  const connected = room.getConnectionState() === "open";

  // Get self presence
  const myPresence = useSelf(me => me);

  // Get all others' presences
  const others = useOthers();

  // Get current room host
  const currentHost = useStorage(r => r.host);





  // Changes the new host
  const setNewHost = useMutation(({ storage }, user) => {

    // Changes the room host
    storage.set("host", user);

  }, [  ]);

  // Finds and sets the new host
  const establishNewHost = () => {

    // Sort all users, including self, by the timestamp they joined the room at
    const usersSortedByJoinTime = [ myPresence, ...others ].sort((a, b) => b.presence.joined - a.presence.joined);

    // The best possible host
    const candidateHost = usersSortedByJoinTime.pop().presence.username;

    // Do not perform an "update" of the host if the best possible host is the current host
    if (candidateHost !== currentHost)
      setNewHost(candidateHost);

  };

  // Handles establishing of a new host when a user connects to a room or others leave the room
  useEffect(() => establishNewHost(), [ connected, myPresence, others.length ]);





  return (

      <div className="w-screen h-screen flex justify-center items-center">
        {
          whiteBoard && <WhiteBoard />
        }   
        <div className="w-2/3 h-screen flex flex-col justify-center items-center">
          <Split sizes={[25, 60, 15]} minSize={[0, 822, 0]} className={`w-screen flex`}>
            <div className="max-h-screen overflow-y-auto ml-1 min-h-screen">
              <QuestionPanel />
            </div>
  
            <div className="flex justify-center mt-10">
              <CodePanel />
            </div>
  
            <TextPanel />
          </Split>
        </div>
      </div>
  );
};