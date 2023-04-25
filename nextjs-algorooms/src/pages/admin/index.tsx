import React from 'react';
import Header from '@/components/shared/Header';
import Admincard from '@/components/pages/admin/Admincard';

export default () => {
    return (
        <nav className="bg-gradient-to-tr from-darkAccent to to-gradientEnd w-screen h-screen flex flex-col">
            <Header />
            <div className="flex flex-col h-screen justify-center">
                <div className="flex justify-center space-x-[171px]">
                    <div className="text-center">
                        <h2 className="text-5xl font-bold text-greenAccent mb-[40px]">
                            ADMIN PANEL
                        </h2>
                        <Admincard />
                    </div>
                </div>
            </div>
        </nav>
    );
};
