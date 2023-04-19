// Module imports
import React from 'react';
import { useUser } from '@auth0/nextjs-auth0/client';
import Image from 'next/image';
// Add this when text chat is working
// import RoomMember from './header/RoomMember';

// Interface imports
import { textFeedInterface } from './Interfaces';

export default ({}: textFeedInterface) => {
  // Code
  const { isLoading, user, error } = useUser();

  return (
    <section>
      {/* Body */}
      <div className="overflow-y-auto max-h-[400px] bg-lightAccent flex">
        <div className="my-2 mx-2">
          {/* Replace below with message component later on */}
          <span className="text-white flex flex-row">
            <Image
              src={isLoading || !user ? '' : user.picture || ''}
              alt="user"
              width={30}
              height={30}
              className="rounded-full w-fit h-fit"
            />
            <span>
              : Lorem ipsum dolor sit amet consectetur adipisicing elit. Quis
              dolorem optio fugiat cum, animi dolore eveniet, repudiandae
              consequuntur placeat culpa voluptatibus. Expedita at amet enim
              iusto exercitationem id laudantium dolore quibusdam, magni quod
              obcaecati rerum asperiores sequi totam, adipisci commodi
              voluptatem voluptates reprehenderit eos officia repudiandae iste.
              Quas atque minus eos, sint iusto necessitatibus earum nemo iure
              ullam omnis eum quam vel accusantium debitis repellendus autem
              voluptatem veritatis, hic esse ipsa laborum suscipit possimus
              quasi libero. Illo eius at vero, sequi numquam possimus facilis
              delectus voluptates? Tenetur quam accusamus, et, illum cumque
              maiores vel aliquam, consequatur ipsum dolorum libero maxime?
            </span>
          </span>
        </div>
      </div>
    </section>
  );
};
