import { questionExampleInterface } from "./Interfaces";

export default ({
    input,
    output,
    explanation
}) => (
    <section>
        <p><strong>Input</strong>{ `: ${input.slice(7)}` }</p>
        <br/>
        <p><strong>Output</strong>{ `: ${output.slice(8)}` }</p>
        <br/>
        {
            explanation !== "" &&
                <>
                    <p><strong>Explanation</strong>{ `: ${explanation}` }</p>
                    <br/>
                </>
        }
    </section>
);