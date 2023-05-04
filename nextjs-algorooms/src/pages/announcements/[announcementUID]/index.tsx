import Announcement from "@/components/pages/announcements/shared/Announcement";
import Header from "@/components/shared/Header";
import buildRoute from "@/utilities/buildRoute";
import axios from "axios";
import Link from "next/link";
import { useRouter } from "next/router";
import { useEffect } from "react";

export default ({
    exists,
    title,
    message,
    timestamp,
    by,
    uid
}) => {

    const router = useRouter();

    useEffect(() => {
        if (!exists)
            router.push("/404?injectable=announcement");
    }, [  ]);
    
    return (
        <>
            <Header />
            <Announcement
                { ...{ title, message, timestamp, by, uid } }
            />
        </>
    )

};

export const getServerSideProps = async context => {

    const {
        params: {
            announcementUID
        }
    } = context;

    const response = await axios.get(buildRoute(`/api/announcements/verify/${announcementUID}`)).then(res => res.data);

    let {
        exists,
        announcement
    } = response;

    announcement = announcement === null ? {  } : announcement;

    return {
        props: {
            exists,
            ...announcement
        }
    }

};