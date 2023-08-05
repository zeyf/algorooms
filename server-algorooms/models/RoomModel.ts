
import mongoose from 'mongoose';
import { IQuestion } from './QuestionModel';
const Schema = mongoose.Schema;

// Create the interface for the Question
export interface IRoom extends mongoose.Document {
    uid: string,
    name: string,
    host: string,
    lobbyAccess: string,
    difficulty: string,
    topics: Array<string>,
    questions: Array<number>
    occupied: number,
    capacity: number
};

export const roomSchematic = new Schema({
    uid: {
        type: String,
        required: true
    },
    name: {
        type: String,
        required: true
    },
    host: {
        type: String,
        required: true
    },
    lobbyAccess: {
        type: String,
        required: true
    },
    difficulty: {
        type: String,
        required: true
    },
    topics: {
        type: Array<String>,
        required: true
    },
    questions: {
        type: Array<String>,
        required: true
    },
    occupied: {
        type: Number,
        required: true
    },
    capacity: {
        type: Number,
        required: true
    }
});

const Room = mongoose.model<IRoom>('Room', roomSchematic);
export default Room;