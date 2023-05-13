import Link from "next/link";
import { useRouter } from "next/router";
import { useEffect } from "react";

export default ({
    title,
    message,
    timestamp,
    by,
    uid
}) => {

    const date = new Date(timestamp);
    const day = date.getDay();
    const month = date.getMonth();
    const year = date.getFullYear();
    const hours = date.getHours();
    const minutes = date.getMinutes();
    
    return (
        <section className="bg-white w-[50%] mt-[20px] rounded-2xl box-border pl-[20px]">
            <Link
                className="font-bold text-lg"
                href={`/announcements/${uid}`}
            >
                { title }
            </Link>
            <span>
                {` at ${month}-${day}-${year} at ${hours}:${minutes} by `}
                <Link
                    className="font-bold text-blue-600"
                    href={`/profile/${by}`}
                >
                    { by }
                </Link>
            </span>
            <p>{ message }</p>
        </section>
    );

};