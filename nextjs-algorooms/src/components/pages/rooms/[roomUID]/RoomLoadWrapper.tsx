import { useContext, useEffect } from "react";
import { useMutation, useOthers, useRoom, useSelf, useStorage } from "../../../../../liveblocks.config";
import { AppUserContext } from "@/contexts/AppUserContextLayer";
import Split from "react-split";
import CodePanel from "./panels/code/CodePanel";
import TextPanel from "./panels/text/TextPanel";
import QuestionPanel from "./panels/question/QuestionPanel";

export default ({

}) => {

    const room = useRoom();
    
    const connected = room.getConnectionState() === "open";

    const others = useOthers();
    const currentHost = useStorage(r => r.host);

  
    const setNewHost = useMutation(({ storage }, user) => {
      storage.set("host", user);
    }, [  ]);

    const myPresence = useSelf(me => me);

    useEffect(() => {

        const usersSortedByJoinTime = [ myPresence, ...others ].sort((a, b) => a.presence.joined - b.presence.joined);

        const candidateHost = usersSortedByJoinTime[0].presence.username;

        if (candidateHost !== currentHost)
          setNewHost(candidateHost);

    }, [ connected, myPresence, others.length ]);

    return (
      <div className="w-screen h-screen flex flex-row-reverse justify-center items-center">
      <div className="w-2/3 h-screen flex flex-col justify-center items-center">
        <Split sizes={[25, 60, 15]} minSize={[0, 822, 0]} className={`w-screen flex`}>
          <div className="max-h-screen overflow-y-auto ml-1 min-h-screen">
            {/* <QuestionPanel /> */}
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