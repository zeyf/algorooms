
import mongoose from 'mongoose';
const Schema = mongoose.Schema;

// Create the interface for the Question
export interface ISubmission extends mongoose.Document {
    username: string,
    questionUID: string,
    questionTitle: string,
    timestamp: number,
    language: string,
    code: string,
    uid: string
};

export const submissionSchematic = new Schema({
    uid: {
        type: String,
        required: true
    },
    username: {
        type: String,
        required: true
    },
    questionUID: {
        type: String,
        required: true
    },
    questionTitle: {
        type: String,
        required: true
    },
    timestamp: {
        type: Number,
        required: true
    },
    language: {
        type: String,
        required: true
    },
    code: {
        type: String,
        required: true
    }
});

export default mongoose.model<ISubmission>('Submission', submissionSchematic);