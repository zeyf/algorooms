import Head from 'next/head';
import { useState } from 'react';
import Select from 'react-select';
import axios from 'axios';
import buildRoute from '@/utilities/buildRoute';
import { AiOutlineCheck } from 'react-icons/ai';
import Header from '@/components/shared/Header';

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
    // const response = await axios
    //   .post(buildRoute('/api/questions/create'), data)
    //   .then((res) => res.data);

    // const { created } = response;

    // console.log(created);
    let created: boolean = false;
    if (created) {
      console.log('submitted');
    } else {
      console.log('uh oh');
    }
  };

  const verifyConstraints = () => {
    console.log('verify');
  };

  const verifyHints = () => {
    console.log('verify');
  };

  return (
    <>
      <Head>
        <title>AlgoRooms 🚀 | Question Submission</title>
        <meta name="description" content="Submit questions" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <div className="to flex h-screen w-screen flex-col bg-gradient-to-tr from-darkAccent to-gradientEnd">
        <Header />
        <h2 className="text-center text-5xl font-bold text-greenAccent mt-[40px]">
            Question Submission
        </h2>
        <div className="m-10 h-full rounded-[15px] bg-white bg-opacity-25 p-10 flex flex-col justify-between">
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
                className="w-full rounded h-[38px] bg-transparent border-2 border-white rounded-lg text-white"
              />
            </div>
            {/* Difficulty */}
            <div className="w-1/3">
              <Select
                name="difficulty"
                placeholder="Select Difficulty"
                className="w-full text-black h-auto"
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
                className="w-full rounded text-black"
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
          <div className="flex w-full gap-10">
            {/* Description */}
            <textarea
              className="w-full bg-transparent border-2 border-white rounded-lg text-white"
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
                rows={4}
                onChange={(e) => {
                  setData({ ...data, input: e.target.value });
                }}
                className="w-full bg-transparent border-2 border-white rounded-lg text-white"
              />
            </div>
            {/* Output */}
            <div className="w-1/3">
              <textarea
                name="output"
                placeholder="Output..."
                rows={4}
                className="w-full bg-transparent border-2 border-white rounded-lg text-white"
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
                rows={4}
                className="w-full bg-transparent border-2 border-white rounded-lg text-white"
                onChange={(e: any) =>
                  setData({ ...data, explanation: e.target.value })
                }
              />
            </div>
          </div>
          {/* Fourth row */}
          <div className="flex justify-between gap-10">
            {/* Constraints */}
            <div className="w-1/2">
              {/* <label className="text-white" htmlFor="constraints">
                Constraints
              </label> */}
              <div className="flex w-full">
                <input
                  name="constraints"
                  type="text"
                  placeholder="Constraints"
                  onChange={(e) => {
                    setData({ ...data, constraints: e.target.value });
                  }}
                  className="w-full bg-transparent border-l-2 border-t-2 border-b-2 border-r-0 border-white rounded-tl-lg rounded-bl-lg text-white"
                />
                <div
                  className="cursor-pointer rounded-r bg-greenAccent p-3 hover:bg-darkAccent hover:text-white"
                  onClick={verifyHints}
                >
                  <AiOutlineCheck />
                </div>
              </div>
            </div>
            {/* Hints */}
            <div className="w-1/2">
              {/* <label className="text-white" htmlFor="constraints">
                Hints
              </label> */}
              <div className="flex w-full">
                <input
                  name="hints"
                  type="text"
                  placeholder="Hints"
                  onChange={(e) => {
                    setData({ ...data, hints: e.target.value });
                  }}
                  className="w-full bg-transparent border-l-2 border-t-2 border-b-2 border-r-0 border-white rounded-tl-lg rounded-bl-lg text-white"
                />
                <div
                  className="cursor-pointer rounded-r bg-greenAccent p-3 hover:bg-darkAccent hover:text-white"
                  onClick={verifyConstraints}
                >
                  <AiOutlineCheck />
                </div>
              </div>
            </div>
          </div>
          <div className="flex justify-end">
            <button
              type="button"
              className="h-[60px] w-[200px] rounded bg-greenAccent font-bold text-black hover:bg-darkAccent hover:text-white"
              onClick={handleSubmit}
            >
              Submit
            </button>
          </div>
        </div>
      </div>
    </>
  );
};
