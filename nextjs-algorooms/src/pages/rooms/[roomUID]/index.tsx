// Import statements
import React, { useContext, useEffect } from 'react';
import { withPageAuthRequired } from '@auth0/nextjs-auth0';
import QuestionPanel from '@/components/pages/rooms/[roomUID]/panels/question/QuestionPanel';
import CodePanel from '@/components/pages/rooms/[roomUID]/panels/code/CodePanel';
import TextPanel from '@/components/pages/rooms/[roomUID]/panels/text/TextPanel';
import { io } from 'socket.io-client';

import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

import CodeTester from '@/components/pages/rooms/[roomUID]/panels/code/CodeTester';
import { codePanelInterface } from '@/components/pages/rooms/[roomUID]/panels/code/Interfaces';
import { textPanelInterface } from '@/components/pages/rooms/[roomUID]/panels/text/Interfaces';

///

import Split from 'react-split';
import Header from '@/components/shared/Header';
import axios from 'axios';
import { useRouter } from 'next/router';
import RoomContextLayer from '@/contexts/RoomContextLayer';
import { RoomContext } from '@/contexts/RoomContextLayer';
import Head from 'next/head';


import { Presence, RoomProvider } from '../../../../liveblocks.config';
import { LiveList } from '@liveblocks/client';
import { AppUserContext } from '@/contexts/AppUserContextLayer';

import randomColor from "randomcolor";

export default ({
  exists,
  data
}: any) => {

  const router = useRouter();
  
  const {
    socket
  } = useContext(RoomContext);

  const {
    username
  } = useContext(AppUserContext);
  
  const initialPresence: Presence = {
    isTypingCode: false,
    isTypingMessage: false,
    isRunningCode: false,
    isSubmittingCode: false,
    cursorLocationData: {  },
    username,
    color: randomColor()
  };

  useEffect(() => {

    if (!exists)
      router.push("/404?injectable=room");
    
  }, [  ]);


  useEffect(() => {
    socket.connect();
    // socket.on('connect', () => {
    //   socket.emit("joinRoom", data.uid, socket.id);
    // });

    // socket.on("members", ({ message, username }) => toast(message));
  });

  if (username === "")
    return <p>Loading...</p>

  return (
    <>
      <Head>
        <title>{`AlgoRooms 🚀 | Room: ${data.name} - ${data.uid} | Topics: ${data.topics.toString().replace(/,/gi, ", ")} | Difficulty: ${data.difficulty} | Lobby Access: ${data.lobbyAccess}`}</title>
        <meta name="description" content="Generated by create next app" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <div className="bg-[#222C4A] w-screen h-screen overflow-hidden">
        {/*  */}
        <ToastContainer />
        <Header />
        <RoomContextLayer
          { ...data }
        >
          <RoomProvider
            id={data.uid}
            initialPresence={initialPresence}
            initialStorage={{
              uid: "",
              editorText: "",
              lobbyAccess: "",
              difficulty: "",
              topics: new LiveList<string>(data.topics),
              members: new LiveList<string>([ username ]),
              host: "",
              messages: new LiveList<string>()
            }}
          >

            <div className="w-screen h-screen flex flex-row-reverse justify-center items-center">
              <div className="w-2/3 h-screen flex flex-col justify-center items-center">
                <Split sizes={[25, 60, 15]} minSize={[0, 822, 0]} className={`w-screen flex`}>
                  <div className="max-h-screen overflow-y-auto ml-1 min-h-screen">
                    {/* <QuestionPanel {...{QuestionDummyData}} /> */}
                  </div>

                  <div className="flex justify-center mt-10">
                    <CodePanel />
                  </div>

                  <TextPanel />
                </Split>
              </div>
            </div>
          </RoomProvider>
        </RoomContextLayer>
      </div>
    </>
  );

};

// Auth-guarding the /rooms/[roomUID] page
export const getServerSideProps = withPageAuthRequired({
  async getServerSideProps(context:any) {

    const {
      params: {
        roomUID
      }
    } = context;

    const response = await axios.get(`http://localhost:4000/api/rooms/verify/${roomUID}`).then(res => res.data);

    const {
      exists,
      roomData
    } = response;

    return {
      props: {
        exists,
        data: roomData
      },
    };
  },
});
