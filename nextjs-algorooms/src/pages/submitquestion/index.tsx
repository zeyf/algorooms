import Head from 'next/head';
import { useState } from 'react';
import Select from 'react-select';
import axios from 'axios';
import buildRoute from '@/utilities/buildRoute';

interface dataInterface {
  title: string;
  difficulty: string;
  topics: Array<string>;
  description: string;
  input: string;
  output: string;
  explanation: string;
  constraints: string;
  hints: string;
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
    title: '',
    difficulty: '',
    topics: [],
    description: '',
    input: '',
    output: '',
    explanation: '',
    constraints: '',
    hints: '',
  });

  const handleSubmit = () => {
    // Handle empty fields
    if (
      Object.keys(data).length === 0 ||
      data.title === '' ||
      data.difficulty === '' ||
      data.topics.length === 0 ||
      data.description === '' ||
      data.input === '' ||
      data.output === '' ||
      data.explanation === '' ||
      data.constraints === '' ||
      data.hints === ''
    )
      return;

    submitQuestion();
  };

  const submitQuestion = async () => {
    const response = await axios
      .post(buildRoute("/api/questions/create"), data)
      .then((res) => res.data)
    
    const { created } = response;
    
    if (created) {
      console.log('submitted');
    } else {
      console.log('uh oh');
    }
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
                  setData({ ...data, title: e.target.value });
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
                setData({ ...data, description: e.target.value })
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
            {/* Hints */}
            <>
              <label className="text-white" htmlFor="constraints">
                Hints
              </label>
              <input
                name="hints"
                type="text"
                onChange={(e) => {
                  setData({ ...data, hints: e.target.value });
                }}
                className="w-full text-black"
              />
            </>
          </div>
          <button
            type="button"
            className="bg-greenAccent hover:bg-darkAccent hover:text-white text-black w-[200px] h-[60px] font-bold rounded"
            onClick={handleSubmit}
          >
            Submit
          </button>
        </div>
      </div>
    </>
  );
};
