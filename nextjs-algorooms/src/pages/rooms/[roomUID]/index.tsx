// Import statements
import React, { useContext, useEffect } from 'react';
import { withPageAuthRequired } from '@auth0/nextjs-auth0';

import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

import Header from '@/components/shared/Header';
import axios from 'axios';
import { useRouter } from 'next/router';
import RoomContextLayer from '@/contexts/RoomContextLayer';
import { RoomContext } from '@/contexts/RoomContextLayer';
import Head from 'next/head';

import { EditorTexts, Presence, RoomProvider, Storage, TextChatMessage } from '../../../../liveblocks.config';
import { LiveList, LiveObject } from '@liveblocks/client';
import { AppUserContext } from '@/contexts/AppUserContextLayer';

import randomColor from "randomcolor";
import RoomLoadWrapper from '@/components/pages/rooms/[roomUID]/RoomLoadWrapper';
import { ClientSideSuspense } from '@liveblocks/react';
import Content from '@/components/shared/Content';

export default ({
  exists,
  data
}: any) => {





  // Get router for redirection
  const router = useRouter();
  
  // Get self socket
  const {
    socket,
  } = useContext(RoomContext);

  // Get self username
  const {
    username
  } = useContext(AppUserContext);
  
  // Define the default presence
  const initialPresence: Presence = {
    isTypingCode: false,
    isTypingMessage: false,
    cursorLocationData: {  },
    color: randomColor(),
    joined: Date.now(),
    votedToExecuteCode: false,
    username
  };

  // Define the default storage
  const initialStorage: Storage = {
    uid: data.uid,
    activeEditorTexts: new LiveObject<EditorTexts>({
      python: "",
      // cpp: "",
      // java: "",
      javascript: ""
    }),
    resetEditorTexts: new LiveObject<EditorTexts>({
      python: "",
      // cpp: "",
      // java: "",
      javascript: ""
    }),
    hasRanCodeOnQuestion: false,
    ranCodeOutputOnQuestion: {
      state: "",
      userOutput: "",
      expectedOutput: "",
      testCaseIndex: -1,
      totalTestCases: -1
    },
    runCodeInQueue: false,
    submitCodeInQueue: false,
    voteCount: 0,
    lobbyAccess: data.lobbyAccess,
    difficulty: data.difficulty,
    topics: new LiveList<string>(data.topics),
    messages: new LiveList<TextChatMessage>(),
    questions: new LiveList<string>(data.questions),
    host: data.host,
    language: "python",
    startMinutes: 1,
    startSeconds: 0,
    minutesLeft: 1,
    secondsLeft: 0,
    inRound: false,
    awaitingQuestion: false,
    isVotingOpen: false,
    currentQuestion: {
      title: "You should start a round!",
      uid: "BRUH",
      difficulty: "Simple",
      description: "You should start a round... for real tho.",
      topics: [  ],
      constraints: [  ],
      hints: [  ],
      examples: [  ]
    }
  };


  // Establish socket connection with backend
  useEffect(() => {
    socket.connect();

    // socket.on('connect', () => {
    //   socket.emit("joinRoom", data.uid, socket.id);
    // });

    socket.on("members", ({ message, username }) => toast(message));
    socket.on("startRound", (username, message) => toast(message));
  });

  // Ensure username is loaded before rendering the true room
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
        <ToastContainer />
        <Header />
        <Content>
          <RoomContextLayer
            { ...data }
          >
            <RoomProvider
              shouldInitiallyConnect={true}
              id={data.uid}
              initialPresence={initialPresence}
              initialStorage={initialStorage}
            >
              {/* Allows for full suspense rendering of hook calls before initial render */}
              <ClientSideSuspense fallback={<p>Loading...</p>}>
                { () => <RoomLoadWrapper roomUID={data.uid}/> }
              </ClientSideSuspense>
            </RoomProvider>
          </RoomContextLayer>  
        </Content>
      </div>
    </>
  );





};

// Auth-guarding the /rooms/[roomUID] page
export const getServerSideProps = withPageAuthRequired({

  async getServerSideProps(context:any) {

    // Pull out the parameter aka roomUID
    const {
      params: {
        roomUID
      }
    } = context;

    // Make a request to verify the room exists
    const response = await axios.get(`http://localhost:4000/api/rooms/verify/${roomUID}`).then(res => res.data);



    // Pull out the response
    const {
      exists,
      roomData
    } = response;

    if (!exists) {
      return {
        props: {}, 
        redirect: {
          permanent: true,
          destination: "/404?injectable=room",
        }
      }
    }
    if (exists && roomData.occupied === roomData.capacity)
    return {
      props: {},
      redirect: {
        permanent: true,
        destination: "/rooms?is_full=true",
      }
    };

    // Send response as props
    return {
      props: {
        exists,
        data: roomData
      },
    };
  }

});
