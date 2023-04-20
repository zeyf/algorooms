// Import statements
import React, { useEffect } from 'react';
import { withPageAuthRequired } from '@auth0/nextjs-auth0';
import QuestionPanel from '@/components/pages/rooms/[roomUID]/panels/question/QuestionPanel';
import CodePanel from '@/components/pages/rooms/[roomUID]/panels/code/CodePanel';
import TextPanel from '@/components/pages/rooms/[roomUID]/panels/text/TextPanel';
import CodeTester from '@/components/pages/rooms/[roomUID]/panels/code/CodeTester';
import { io } from 'socket.io-client';

import { codePanelInterface } from '@/components/pages/rooms/[roomUID]/panels/code/Interfaces';
import { textPanelInterface } from '@/components/pages/rooms/[roomUID]/panels/text/Interfaces';

///

import Split from 'react-split';
import Header from '@/components/shared/Header';
import QuestionDummyData from './QuestionDummyData';
import axios from 'axios';
import { useRouter } from 'next/router';

const socket = io('http://localhost:4000', {autoConnect:false})

export default ({
  exists,
  data
}: any) => {



  const router = useRouter();

  useEffect(() => {

    if (!exists)
      router.push("/404?injectable=room");
  }, [  ]);


    useEffect(() => {
      console.log("ran1")
      socket.connect()
      socket.on('connect', () => {socket.emit("joinRoom", data.uid, socket.id)})
    })

    return (
      <div className="bg-[#222C4A] w-screen h-screen overflow-hidden">
        <Header />
        <div className="w-screen h-screen flex flex-row-reverse justify-center items-center">
          <div className="w-2/3 h-screen flex flex-col justify-center items-center">
            <Split sizes={[25, 60, 15]} className={`w-screen flex`}>
              <div className="max-h-screen overflow-y-auto ml-1 min-h-screen">
                <QuestionPanel {...QuestionDummyData} />
              </div>

              <div className="flex justify-center mt-10">
                <CodePanel socket={socket} uid={data.uid}/>
              </div>

              <TextPanel
                socket={socket}
              />
            </Split>
          </div>
        </div>
      </div>
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
