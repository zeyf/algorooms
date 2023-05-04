import Announcement from "@/components/pages/announcements/shared/Announcement";
import Header from "@/components/shared/Header";
import buildRoute from "@/utilities/buildRoute";
import { withPageAuthRequired } from "@auth0/nextjs-auth0";
import axios from "axios";

export default ({
    exists,
    announcements
}) => {

    return (
        <>
            <Header />
            <section>
                <h1>Announcements</h1>
                <section>

                    { exists ?
                        announcements.map(announcementData => <Announcement { ...announcementData } />)
                        :
                        <span>There are no announcements!</span>
                    }

                </section>
            </section>
        </>
    )

};

export const getServerSideProps = async context => {

    const response = await axios.get(buildRoute("/api/announcements/all")).then(res => res.data);

    const {
        exists,
        announcements
    } = response;

    return {
        props: {
            exists,
            announcements: announcements.sort().reverse()
        }
    };

};
