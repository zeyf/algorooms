import { questionExamplesInterface } from "./Interfaces";
import QuestionExample from "./QuestionExample";


export default ({
    questionExamples
}:questionExamplesInterface) => (
    <section>
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
);