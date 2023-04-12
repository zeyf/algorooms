import Image from 'next/image';
import ProgressBar from '@/components/pages/profile/ProgressBar';
import { useUser } from '@auth0/nextjs-auth0/client';
import Subtitle from '@/components/pages/profile/Subtitle';
import Title from '@/components/pages/profile/Title';
import Header from '@/components/shared/Header';
import { useRouter } from 'next/router';

interface DynamicProfilePageProps {
  profileExists: boolean;
  profileUID: string;
  profileData: {};
}

const DynamicProfilePage = ({
  profileExists,
  profileUID,
  profileData,
}: DynamicProfilePageProps) => {
  if (!profileExists) {
    return <h1>Profile Does Not Exist!</h1>;
  }

  const currExp = 1100,
    maxExp = 6100;

  const { user, isLoading, error } = useUser();

  if (isLoading) {
    <p>Loading...</p>;
  } else if (!user) return <p>WTF!</p>;
  else
    return (
      <>
        <div className="bg-gradient-to-tr from-navbar to to-[#24366c] w-screen h-screen flex flex-col">
          <Header />
          <div className="bg-white bg-opacity-25 rounded-[15px] p-6 m-20 h-full">
            {/* First row */}
            <div className="flex justify-between items-center col-span-full border-b-2 border-gray pb-4 h-1/2">
              {/* User */}
              <div className="flex-col w-1/2 pr-2 h-full border-r-2 border-gray">
                {/* Avatar and User Info */}
                <div>
                  <div className="flex justify-between">
                    {/* Avatar */}
                    <Image
                      className="rounded-full mr-4 mb-4"
                      src={user.picture || ''}
                      height={188}
                      width={188}
                      alt=""
                    />
                    {/* User Info */}
                    <div className="flex-col w-full">
                      <Title
                        text={user.nickname || ''}
                        alignment="left"
                        color="white"
                      />
                      <Subtitle
                        text="Joined 23 March 2023"
                        alignment="left"
                        color="white"
                      />
                      <Subtitle
                        text="Student at the University of Central Florida"
                        alignment="left"
                        color="white"
                      />
                    </div>
                  </div>
                </div>
                {/* Exp bar */}
                <div className="flex justify-between items-center">
                  {/* Level */}
                  <div className="pr-3">
                    <Subtitle text="100" alignment="left" color="white" />
                  </div>

                  {/* Exp Bar */}
                  <ProgressBar
                    backgroundColor={'bg-green-300'}
                    accentColor={'bg-green-800'}
                    numerator={currExp}
                    denominator={maxExp}
                    width={'full'}
                    height={'3'}
                  />
                </div>
              </div>

              {/* Problems */}
              <div className="w-1/2 pl-2 h-full">
                <Title text="Problems" alignment="left" color="white" />
                <div className="flex-col justify-between w-full h-full">
                  {/* Simpler */}
                  <section className="flex flex-col items-start">
                    <Subtitle text="Simpler" alignment="left" color="white" />
                    <ProgressBar
                      backgroundColor={'bg-green-300'}
                      accentColor={'bg-green-800'}
                      numerator={5}
                      denominator={25}
                      width={'full'}
                      height={'4'}
                    />
                  </section>
                  {/* Simple */}
                  <section className="flex flex-col items-start">
                    <Subtitle text="Simple" alignment="left" color="white" />
                    <ProgressBar
                      backgroundColor={'bg-yellow-300'}
                      accentColor={'bg-yellow-800'}
                      numerator={5}
                      denominator={25}
                      width={'full'}
                      height={'4'}
                    />
                  </section>
                  {/* Not Simple */}
                  <section className="flex flex-col items-start">
                    <Subtitle
                      text="Not Simple"
                      alignment="left"
                      color="white"
                    />
                    <ProgressBar
                      backgroundColor={'bg-red-300'}
                      accentColor={'bg-red-800'}
                      numerator={5}
                      denominator={25}
                      width={'full'}
                      height={'4'}
                    />
                  </section>
                </div>
              </div>
            </div>

            {/* Second row */}
            <div className="flex flex-row justify-between h-1/2 pt-4">
              {/* Recently Solved Problems */}
              <div className="w-1/3 border-r-2 border-gray">
                <Title
                  text="Recently Solved Problems"
                  alignment="center"
                  color="white"
                />
                <ol>
                  <Title
                    text="1. Minimum Array"
                    alignment="left"
                    color="white"
                  />
                  <Title
                    text="2. Selling Stock"
                    alignment="left"
                    color="white"
                  />
                  <Title
                    text="3. Shortest Path v1"
                    alignment="left"
                    color="white"
                  />
                  <Title text="4. 17 Sum" alignment="left" color="white" />
                  <Title
                    text="5. Maximum Array"
                    alignment="left"
                    color="white"
                  />
                </ol>
              </div>

              {/* Top Topics Solved */}
              <div className="w-1/3 border-r-2 border-gray">
                <Title
                  text="Top Topics Solved"
                  alignment="center"
                  color="white"
                />
                <ol>
                  <Title text="1. Arrays" alignment="left" color="white" />
                  <Title text="2. Graphs" alignment="left" color="white" />
                  <Title text="3. Hash Maps" alignment="left" color="white" />
                  <Title text="4. Trees" alignment="left" color="white" />
                  <Title
                    text="5. Bit Operations"
                    alignment="left"
                    color="white"
                  />
                </ol>
              </div>

              {/* School Affiliation */}
              <div className="w-1/3">
                <Title
                  text="School Affiliation"
                  alignment="center"
                  color="white"
                />
                <div className="flex justify-center items-center">
                  <Image
                    className="text-white"
                    alt="school"
                    src="/dummy_data/ucf.png"
                    width={220}
                    height={250}
                  />
                </div>
              </div>
            </div>
          </div>
        </div>
      </>
    );
};

export async function getServerSideProps(data: any) {
  const {
    query: { profileUID },
  } = data;

  const response = await fetch(
    `http://localhost:4000/api/user/search/${profileUID}`,
    {
      method: 'POST',
      mode: 'cors',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        source: `/profile/${profileUID}`,
      }),
    }
  ).then((res: any) => res);

  const { exists, profileData } = response;

  return {
    props: {
      profileExists: exists,
      profileData,
    },
  };
}

export default DynamicProfilePage;
