import Head from 'next/head';
import { useState } from 'react';
import Select from 'react-select';

interface dataInterface {
  questionName: string;
  difficulty: string;
  topics: Array<string>;
  questionDescription: string;
  input: string;
  output: string;
  explanation: string;
  constraints: string;
  hint: string;
}

const difficultyOptions = [
  { value: 'Simpler', label: 'Simpler' },
  { value: 'Simple', label: 'Simple' },
  { value: 'Not Simple', label: 'Not Simple' },
];

const topicOptions = [
  { value: 'Strings', label: 'Strings' },
  { value: 'Arrays', label: 'Arrays' },
  { value: 'Stacks', label: 'Stacks' },
  { value: 'Queues', label: 'Queues' },
  { value: 'Linked Lists', label: 'Linked Lists' },
  { value: 'Trees', label: 'Trees' },
  { value: 'Tries', label: 'Tries' },
  { value: 'Recursion', label: 'Recursion' },
  { value: 'Hash Tables', label: 'Hash Tables' },
  { value: 'Graphs', label: 'Graphs' },
  { value: 'Bitwise', label: 'Bitwise' },
];

export default () => {
  const [data, setData] = useState<dataInterface>({
    questionName: '',
    difficulty: '',
    topics: [],
    questionDescription: '',
    input: '',
    output: '',
    explanation: '',
    constraints: '',
    hint: '',
  });

  const handleSubmit = () => {
    // Handle empty fields
    if (
      Object.keys(data).length === 0 ||
      data.questionName === '' ||
      data.difficulty === '' ||
      data.topics.length === 0 ||
      data.questionDescription === '' ||
      data.input === '' ||
      data.output === '' ||
      data.explanation === '' ||
      data.constraints === '' ||
      data.hint === ''
    )
      return;

    submitQuestion();
  };

  const submitQuestion = async () => {
    // const response = await axios.post(...);
    console.log('submitted');
  };

  return (
    <>
      <Head>
        <title>{`Question Submission`}</title>
        <meta name="description" content="Submit questions" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <div className="bg-gradient-to-tr from-darkAccent to to-gradientEnd w-screen h-screen flex flex-col">
        <div className="bg-white bg-opacity-25 rounded-[15px] p-6 m-20 h-full">
          <h2 className="text-white text-center">Question Submission</h2>
          {/* First row */}
          <div className="flex justify-around gap-10">
            {/* Question Name */}
            <div className="w-1/3">
              <input
                type="text"
                placeholder="Question Name"
                onChange={(e) => {
                  setData({ ...data, questionName: e.target.value });
                }}
                className="w-full text-black"
              />
            </div>
            {/* Difficulty */}
            <div className="w-1/3">
              <Select
                name="difficulty"
                placeholder="Select Difficulty"
                className="w-full text-black"
                classNamePrefix="select"
                options={difficultyOptions}
                onChange={(e: any) =>
                  setData({
                    ...data,
                    difficulty: e.value,
                  })
                }
              />
            </div>
            {/* Topics */}
            <div className="w-1/3">
              <Select
                name="topics"
                placeholder="Select Topics"
                className="w-full text-black"
                classNamePrefix="select"
                isMulti={true}
                options={topicOptions}
                onChange={(selections: any) =>
                  setData({
                    ...data,
                    topics: selections.map((selection: any) => selection.value),
                  })
                }
              />
            </div>
          </div>
          {/* Second row */}
          <div className="flex w-full">
            {/* Description */}
            <textarea
              className="w-full"
              name="description"
              placeholder="Description..."
              rows={4}
              onChange={(e: any) =>
                setData({ ...data, questionDescription: e.target.value })
              }
            />
          </div>
          {/* Third row */}
          <div className="flex justify-around gap-10">
            {/* Input */}
            <div className="w-1/3">
              <textarea
                name="input"
                placeholder="Input..."
                onChange={(e) => {
                  setData({ ...data, input: e.target.value });
                }}
                className="w-full text-black"
              />
            </div>
            {/* Output */}
            <div className="w-1/3">
              <textarea
                name="output"
                placeholder="Output..."
                className="w-full text-black"
                onChange={(e: any) =>
                  setData({ ...data, output: e.target.value })
                }
              />
            </div>
            {/* Explanation */}
            <div className="w-1/3">
              <textarea
                name="topics"
                placeholder="Explanation..."
                className="w-full text-black"
                onChange={(e: any) =>
                  setData({ ...data, explanation: e.target.value })
                }
              />
            </div>
          </div>
          {/* Fourth row */}
          <div className="flex justify-between">
            {/* Constraints */}
            <>
              <label className="text-white" htmlFor="constraints">
                Constraints
              </label>
              <input
                name="constraints"
                type="text"
                onChange={(e) => {
                  setData({ ...data, constraints: e.target.value });
                }}
                className="w-full text-black"
              />
            </>
            {/* Hint */}
            <>
              <label className="text-white" htmlFor="constraints">
                Hint
              </label>
              <input
                name="hint"
                type="text"
                onChange={(e) => {
                  setData({ ...data, hint: e.target.value });
                }}
                className="w-full text-black"
              />
            </>
          </div>
          <button onClick={handleSubmit}> Submit </button>
        </div>
      </div>
    </>
  );
};
