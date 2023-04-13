import { questionExamplesInterface } from "./Interfaces";
import QuestionExample from "./QuestionExample";


export default ({questionExamples}:questionExamplesInterface) => {
    return (
        <section className="whitespace-pre-line bg-black bg-opacity-30 rounded-md p-5">
            {
                questionExamples.map(
                    ({
                        questionExampleInput,
                        questionExampleOutput,
                        questionExampleExplanation
                    }) => <QuestionExample
                        questionExampleInput={questionExampleInput}
                        questionExampleOutput={questionExampleOutput}
                        questionExampleExplanation={questionExampleExplanation}
                    />
                )
            }
        </section>
    )
};