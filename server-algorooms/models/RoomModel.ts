
import mongoose from 'mongoose';
const Schema = mongoose.Schema;

// Create the interface for the Question
export interface IRoom extends mongoose.Document {
    uid: string,
    name: string,
    lobbyAccess: string,
    occupied: number,
    capacity: number,
    difficulty: string,
    topics: string[]
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
    lobbyAccess: {
        type: String,
        required: true
    },
    occupied: {
        type: Number,
        required: true
    },
    capacity: {
        type: Number,
        required: true
    },
    difficulty: {
        type: String,
        required: true
    },
    topics: {
        type: Array<String>,
        required: true
    }
});

const Room = mongoose.model<IRoom>('Room', roomSchematic);
export default Room;