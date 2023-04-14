import { useRouter } from "next/router";

export default ({

}) => {

    const {
        query: {
            injectable
        }
    } = useRouter();

    return (
        <div className="h-screen w-screen bg-darkAccent flex justify-center items-center">
            <div>
                <span className="text-white text-2xl">{`404 - This${` ${injectable}`} page was not found.`}</span>
            </div>
        </div>
    );

};