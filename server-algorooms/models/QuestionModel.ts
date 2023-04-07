
import mongoose from 'mongoose';
const Schema = mongoose.Schema;

// Create the interface for the Question
export interface IQuestion extends mongoose.Document {
    title: string,
    index: number,
    difficulty: string,
    topic: string,
    description: string,
    constraints: Array<string>,
    hints: Array<string>
};

export const questionSchematic = new Schema({
    title: {
        type: String,
        required: true
    },
    index: {
        type: Number,
        required: true
    },
    difficulty: {
        type: String,
        required: true
    },
    topic: {
        type: String,
        required: true
    },
    description: {
        type: String,
        required: true
    },
    constraints: {
        type: Array<String>,
        required: true
    },
    hints: {
        type: Array<String>,
        required: true
    }
})

const Question = mongoose.model<IQuestion>('Question', questionSchematic);
export default Question;