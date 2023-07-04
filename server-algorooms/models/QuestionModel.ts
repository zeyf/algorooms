
import mongoose from 'mongoose';
const Schema = mongoose.Schema;

interface languageTemplate {
    submissionTemplate: string,
    transformedReturnType: string,
    generalReturnType: string,
    testCases: Array<string>,
    testingTemplate: string,
    libraries: Array<string>
};

type templateSet = {
    python: languageTemplate,
    javascript: languageTemplate,
    java: languageTemplate,
    cpp: languageTemplate
};

interface example {
    input: string,
    output: string,
    explanation: string
};

// Create the interface for the Question
export interface IQuestion extends mongoose.Document {
    uid: number,
    title: string,
    description: string,
    examples: Array<example>,
    topics: Array<string>,
    constraints: Array<string>,
    hints: Array<string>,
    difficulty: string,
    isApproved: boolean,
    templates: templateSet
};

export const questionSchematic = new Schema({
    uid: {
        type: String,
        required: true
    },
    title: {
        type: String,
        required: true
    },
    description: {
        type: String,
        required: true
    },
    examples: {
        type: Array<example>,
        required: true
    },
    topics: {
        type: Array<String>,
        required: true
    },
    constraints: {
        type: Array<String>,
        required: true
    },
    hints: {
        type: Array<String>,
        required: true
    },
    difficulty: {
        type: String,
        required: true
    },
    isApproved: {
        type: Boolean,
        required: true
    },
    templates: {
        type: Schema.Types.Mixed,
        required: true
    }
})

const Question = mongoose.model<IQuestion>('Question', questionSchematic);
export default Question;