import Header from "@/components/shared/Header";
import Link from "next/link";
import { useRouter } from "next/router";

export default ({

}) => {

    const {
        query: {
            injectable
        }
    } = useRouter();

    return (
        <>
            <Header />
            <div className="h-screen w-screen bg-darkAccent flex justify-center items-center">
                <div className="flex-col items-center">
                    <span className="text-white text-2xl">{`404 - This${` ${injectable}`} page was not found.`}</span>
                    <Link href="/" className="">
                        Go Home
                    </Link>
                </div>
            </div>
        </>
    );

};