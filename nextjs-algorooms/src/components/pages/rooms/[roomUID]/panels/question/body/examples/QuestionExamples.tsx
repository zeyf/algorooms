import { useStorage } from "../../../../../../../../../liveblocks.config";
import { questionExamplesInterface } from "./Interfaces";
import QuestionExample from "./QuestionExample";


export default ({

}) => {

    const questionExamples = useStorage(r => r.currentQuestion.examples);

    return (
        <section className="whitespace-pre-line bg-black bg-opacity-30 rounded-md p-5">
            {
                questionExamples.map(
                    (data) => <QuestionExample
                        { ...data }
                    />
                )
            }
        </section>
    )
};