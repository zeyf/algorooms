import Image from 'next/image';
import ProgressBar from '@/components/pages/profile/ProgressBar';
import { useUser } from '@auth0/nextjs-auth0/client';
import Title from '@/components/pages/profile/Title';
import Subtitle from '@/components/pages/profile/Subtitle';

export default () => {
  const account_level = 68;
  const currExp = 1100;
  const maxExp = 6100;

  const { user, isLoading, error } = useUser();

  // If we are still checking whether or not the user is logged in through Auth0 layer
  if (isLoading) {
  } else {
    // If we have already checked and have access to the true state of the user
    // And we are not at a user
    if (!user) {
    }
  }

  return (
    <div className="grid auto-row-fr grid-cols-2">
      <div className="flex justify-between items-center col-span-2">
        {/* User */}
        <div className="flex-col w-1/3 p-2 h-full">
          {/* Avatar and User Info */}
          <div>
            <div className="flex justify-between">
              {/* Avatar */}
              <Image
                className="rounded-full"
                src={(user && user.picture) || ''}
                height={188}
                width={188}
                alt=""
              />
              {/* User Info */}
              <div className="flex-col">
                <Title text="John Huber" alignment="left" />
                <Subtitle text="Joined 23 March 2023" alignment="left" />
              </div>
            </div>
          </div>
          {/* Exp bar */}
          <div className="flex justify-between items-center">
            {/* Level */}
            <h3>{account_level}</h3>

            {/* Exp Bar */}
            <ProgressBar
              backgroundColor={'black'}
              accentColor={'green-500'}
              numerator={currExp}
              denominator={maxExp}
              width={'full'}
              height={'3'}
            />
          </div>
        </div>

        {/* Problems */}
        <div className="w-1/3 p-2 h-full">
          <Title text="Problems" alignment="left" />
          <div className="flex-col justify-between w-full h-full">
            {/* Simpler */}
            <ProgressBar
              backgroundColor={'green-800'}
              accentColor={'green-500'}
              numerator={5}
              denominator={25}
              width={'full'}
              height={'3'}
            />

            {/* Simple */}
            <ProgressBar
              backgroundColor={'yellow-800'}
              accentColor={'yellow-500'}
              numerator={5}
              denominator={25}
              width={'full'}
              height={'3'}
            />

            {/* Not Simple */}
            <ProgressBar
              backgroundColor={'red-800'}
              accentColor={'red-500'}
              numerator={5}
              denominator={25}
              width={'full'}
              height={'3'}
            />
          </div>
        </div>

        {/* Topics */}
        <div className="w-1/3 p-2 h-full">
          <Title text="Topics" alignment="left" />
        </div>
      </div>

      {/* Recently Solved Problems */}
      <div>
        <Title text="Recently Solved Problems" alignment="center" />
      </div>
    </div>
  );
};
