import '@/styles/globals.css'
import type { AppProps } from 'next/app'
import { UserProvider } from '@auth0/nextjs-auth0/client';
import Header from '@/components/shared/Header';

export default function App({ Component, pageProps }: AppProps) {
  return (
    <UserProvider>
      <Header/>
      <Component {...pageProps} />
    </UserProvider>
  );
  
}
