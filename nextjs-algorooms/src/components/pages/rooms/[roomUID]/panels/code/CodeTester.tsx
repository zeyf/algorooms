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

  const {
    state,
    userOutput,
    expectedOutput,
    testCaseIndex,
    totalTestCases
  } = useStorage(r => r.ranCodeOutputOnQuestion);

  return (
    <div className="bg-darkAccent w-full h-full rounded text-white font-mono p-5">
      {
        testCaseIndex === -1 ? 
        <div></div>
        :
        <section>
          <section>{ `EXPECTED OUTPUT: ${expectedOutput}` }</section>
          <section>{ `USER OUTPUT: ${userOutput}` }</section>
          <section>{ `STATE: ${state}` }</section>
          <section>{ `PASSED ${testCaseIndex + Number(state === 'ACCEPTED')} / ${totalTestCases} TEST CASES` }</section>
        </section>
      }
    </div>
  );
};
