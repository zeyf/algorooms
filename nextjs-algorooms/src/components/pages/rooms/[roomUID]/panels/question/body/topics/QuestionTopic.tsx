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
      <span className="rounded-full bg-black bg-opacity-30 w-full p-2 mx-1">
        <Link
            href={`/topics/${createTopicURLSlug(questionTopic)}`}
            className="hover:text-accentColor"
        >
            { questionTopic }
        </Link>
      </span>
    );

};
