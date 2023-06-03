// Module imports
import React from "react";

// Interface imports
import { questionTopicInterface } from "./Interfaces";
import Link from "next/link";
import createTopicURLSlug from "@/utilities/createTopicURLSlug";

export default ({
    questionTopic
}:questionTopicInterface) => {

    // Code

    return (
        <Link
            href={`/topics/${createTopicURLSlug(questionTopic)}`}
            className="font-bold hover:text-accentColor"
        >
            { questionTopic }
        </Link>
    );

};
