import '@/styles/globals.css'
import type { AppProps } from 'next/app'
import { UserProvider } from '@auth0/nextjs-auth0/client';
import { createContext } from 'react';

import { AppUserContextComponent } from "../contexts/AppUserContextLayer";

const App = ({ Component, pageProps }: AppProps) => {

  return (
    <UserProvider>
        <AppUserContextComponent>
            <Component {...pageProps} />
        </AppUserContextComponent>
    </UserProvider>
  );
  
}


export default App;