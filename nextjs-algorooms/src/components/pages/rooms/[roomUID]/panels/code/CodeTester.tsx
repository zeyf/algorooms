// Module imports
import React, { useEffect } from "react";

// Interface imports
import { codeTesterInterface } from "./Interfaces";
import { useStorage } from "../../../../../../../liveblocks.config";

export default ({

}:codeTesterInterface) => {

  const codeTestIteration = useStorage(r => r);

  useEffect(() => {

  }, [ codeTestIteration ]);

  const codeResult = useStorage(r => r.ranCodeOutputOnQuestion);

  return (
    <div className="bg-darkAccent w-full h-full rounded text-white font-mono p-5">
      { codeResult.state }
    </div>
  );
};
