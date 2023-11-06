/* eslint-disable import/no-anonymous-default-export */
// Import statements
import Head from 'next/head';
import React, { useEffect } from 'react';
import CreateRoomCard from '@/components/pages/rooms/CreateRoomCard';
import JoinRoomCard from '@/components/pages/rooms/JoinRoomCard';
import Header from '@/components/shared/Header';
import axios from 'axios';

import { withPageAuthRequired } from '@auth0/nextjs-auth0';
import buildRoute from '@/utilities/buildRoute';
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

// eslint-disable-next-line react/display-name
export default ({ query, rooms }: any) => {

  useEffect(() => {
    if (query?.is_full === "true") {
      toast.error("The room is full, please try another room")
    }
  }, [query])

  return (
    <>
      <Head>
        <title>{`AlgoRooms 🚀 | Rooms: ${rooms.length} Public AlgoRooms`}</title>
        <meta name="description" content="Generated by create next app" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <div className="bg-gradient-to-tr from-darkAccent to to-gradientEnd w-screen h-screen flex flex-col">
        <ToastContainer />
        <Header />
        <div className="flex flex-col h-screen justify-center">
          <div className="text-center xl:flex xl:justify-center xl:space-x-6">
            <div className="mb-6 xl:mb-0">
              <h2 className="text-5xl font-bold text-white mb-4 xl:mb-40">
                Join a room
              </h2>
              <JoinRoomCard rooms={rooms} />
            </div>
            <div className="mb-6 xl:mb-0">
              <h2 className="text-5xl font-bold text-white mb-4 xl:mb-40">
                Create a room
              </h2>
              <CreateRoomCard />
            </div>
          </div>
        </div>
      </div>
    </>
  );
};

// Auth-guarding the /rooms page
export const getServerSideProps = withPageAuthRequired({
  async getServerSideProps(context) {
    const response = await axios
      .get(buildRoute('/api/rooms/public'))
      .then((res) => res.data);

    const { query } = context
    const { rooms } = response;

    return {
      props: {
        rooms: rooms.map((room: any) => {
          return {
            ...room,
            topics: room.topics.toString().replace(/,/gi, ', '),
          };
        }),
        query,
      },
    };
  },
});
