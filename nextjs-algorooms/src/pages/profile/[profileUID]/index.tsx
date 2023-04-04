import Image from "next/image";
import ProgressBar from "@/components/pages/profile/ProgressBar";
import { useUser } from "@auth0/nextjs-auth0/client";

interface DynamicProfilePageProps {
    profileExists: boolean,
    profileUID: string,
    profileData: {  }
};

const DynamicProfilePage = ({
    profileExists, profileUID, profileData
}:DynamicProfilePageProps) => {

    if (!profileExists) {
        return <h1>Profile Does Not Exist!</h1>
    }

    const currExp = 1100, maxExp = 6100;
    
    const {
        user,
        isLoading,
        error
    } = useUser();
    
    if (isLoading) {
        <p>Loading...</p>
    } else if (!user)
        return <p>WTF!</p>
    else 
        return (
            <div className="grid auto-row-fr grid-cols-2">
            <div className="flex justify-between items-center col-span-2">
            {/* User */}
            <div className="flex-col w-1/3 p-2 h-full">
                {/* Avatar and User Info */}
                <div>
                <div className="flex justify-between">
                    {/* Avatar */}
                    <img
                    className="rounded-full"
                    src={user.picture || ""}
                    height={188}
                    width={188}
                    alt=""
                    />
                    {/* User Info */}
                    <div className="flex-col">
                    <h1 className="text-lg">{user.nickname || ""}</h1>
                    <h3 className="text-sm">Joined 23 March 2023</h3>
                    </div>
                </div>
                </div>
                {/* Exp bar */}
                <div className="flex justify-between items-center">
                {/* Level */}
                <h3>{100}</h3>
    
                {/* Exp Bar */}
                <ProgressBar backgroundColor={"bg-green-300"} accentColor={"bg-green-800"} numerator={currExp} denominator={maxExp} width={"full"} height={"3"}/>
                </div>
            </div>
    
            {/* Problems */}
            <div className="w-1/3 p-2 h-full">
                <h3>Problems</h3>
                <div className="flex-col justify-between w-full h-full">
                {/* Simpler */}
                <section className="flex flex-col items-start">
                    <span className="font-bold my-2">Simpler</span>
                    <ProgressBar backgroundColor={"bg-green-300"} accentColor={"bg-green-800"}
                        numerator={5} denominator={25}
                        width={"full"} height={"4"}
                    />

                </section>
                <section className="flex flex-col items-start">
                    <span className="font-bold my-2">Simple</span>
                    <ProgressBar backgroundColor={"bg-yellow-300"} accentColor={"bg-yellow-800"}
                        numerator={5} denominator={25}
                        width={"full"} height={"4"}
                    />

                </section>
                
                <section className="flex flex-col items-start">
                    <span className="font-bold my-2">Not Simple</span>
                    <ProgressBar backgroundColor={"bg-red-300"} accentColor={"bg-red-800"}
                        numerator={5} denominator={25}
                        width={"full"} height={"4"}
                    />

                </section>
                </div>
            </div>
    
            {/* Topics */}
            <div className="w-1/3 p-2 h-full">
                Topics
            </div>
            </div>
            
            {/* Statis */}
            <div>
            Statistics
            </div>
    
            {/* Rating */}
            <div>
            Rating
            </div>
        </div>
        );

};

export async function getServerSideProps(data:any) {

    const {
        query: {
            profileUID
        }
    } = data;

    // const response = await fetch(`localhost:4000/api/profile/search/${profileUID}`).then((res:any) => {
    //     return res;
    // });

    return {
        props: {
            profileExists: true,
            profileUID
        }
    };

}

export default DynamicProfilePage;