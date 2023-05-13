import { questionExampleInterface } from "./Interfaces";

export default ({
    input,
    output,
    explanation
}) => (
    <section>
        <p><strong>Input</strong>{ `: ${input}` }</p>
        <br/>
        <p><strong>Output</strong>{ `: ${output}` }</p>
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