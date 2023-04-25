import buildRoute from "@/utilities/buildRoute";
import { useUser } from "@auth0/nextjs-auth0/client";
import axios from "axios";
import { createContext, useEffect, useState } from "react";
import { appUserContextInterface } from "./Interfaces";
import { useRouter } from "next/router";

export const AppUserContext = createContext<appUserContextInterface>({
    username: ""
});

export function AppUserContextComponent({ children }:any) {

    const {
        user
    } = useUser();

    const [
        username,
        setUsername
    ] = useState<string>("");

    const router = useRouter();

    useEffect(() => {

        if (user)
            (async () => {

                const {
                    sub
                } = user;

                const response = await axios.get(buildRoute(`/api/users/verifyAuth/${sub}`)).then(res => res.data);

                const {
                    exists,
                    profileData
                } = response;

                if (exists)
                    setUsername(profileData.username);  
                else if (router.pathname !== "/firsttimeuser") {
                    router.push("/firsttimeuser");
                };

            })();

    }, [ user ]);

    return <AppUserContext.Provider value={{
            username
        }}>
            { children }
        </AppUserContext.Provider>
};