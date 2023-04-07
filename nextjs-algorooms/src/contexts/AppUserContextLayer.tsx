import { useUser } from "@auth0/nextjs-auth0/client";
import { createContext } from "react";

interface AppUserContextInterface {
    userIsLoading: boolean,
    user: any,
    userError: any
};

export const AppUserContext = createContext<AppUserContextInterface>({
    userIsLoading: true,
    userError: undefined,
    user: undefined
});

export function AppUserContextComponent({ children }:any) {

    const {
        isLoading,
        user,
        error
    } = useUser();

    return <AppUserContext.Provider value={{
            userIsLoading: isLoading,
            userError: error,
            user
        }}>
            ({ children });
        </AppUserContext.Provider>
};