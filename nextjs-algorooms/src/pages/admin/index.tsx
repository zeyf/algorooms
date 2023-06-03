import React from 'react';
import Header from '@/components/shared/Header';
import AdminCard from '@/components/pages/admin/AdminCard';
import Head from 'next/head';
import buildRoute from "@/utilities/buildRoute";
import axios from "axios";
import { withPageAuthRequired } from '@auth0/nextjs-auth0';

export default ({
    questions
}) => {
    return (
        <>
            <Head>
            <title>{`AlgoRooms 🚀 | Admin`}</title>
            <meta name="description" content="Generated by create next app" />
            <meta name="viewport" content="width=device-width, initial-scale=1" />
            <link rel="icon" href="/favicon.ico" />
            </Head>
            <nav className="bg-gradient-to-tr from-darkAccent to to-gradientEnd w-screen h-screen flex flex-col">
                <Header />
                <div className="flex flex-col h-screen justify-center">
                    <div className="flex justify-center space-x-[171px]">
                        <div className="text-center">
                            <h2 className="text-5xl font-bold text-greenAccent mb-[40px]">
                                ADMIN PANEL
                            </h2>
                            <AdminCard questions={questions}/>
                        </div>
                    </div>
                </div>
            </nav>
        </>
    );
};

export const getServerSideProps = withPageAuthRequired({
    getServerSideProps: async () => {
        // Get the questions to be approved
        const response = await axios.get(buildRoute("/api/questions/approve")).then(res => res.data);

        const questions = response.questions;

        return {
            props: {
                questions
            }
        };

    }
});
