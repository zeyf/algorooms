import { questionExampleInterface } from "./Interfaces";

export default ({
    questionExampleInput,
    questionExampleOutput,
    questionExampleExplanation
}:questionExampleInterface) => (
    <section>
        <p><strong>Input</strong>{ `: ${questionExampleInput}` }</p>
        <br/>
        <p><strong>Output</strong>{ `: ${questionExampleOutput}` }</p>
        <br/>
        {
            questionExampleExplanation !== "" &&
                <>
                    <p><strong>Explanation</strong>{ `: ${questionExampleExplanation}` }</p>
                    <br/>
                </>
        }
    </section>
);