
import mongoose from 'mongoose';
const Schema = mongoose.Schema;

// Create the interface for the User
export interface IUser extends mongoose.Document {
    username: string,
    authuid?: string,
    picture: string,
    questionsSolved: {
        simpler: number,
        simple: number,
        notSimple: number
    },
    bestTopics: Array<string>,
    dateJoined: string
}

export const userSchematic = new Schema({
    authuid: {
        type: String,
        required: false
    },
    username: {
        type: String,
        required: true
    },
    picture: {
        type: String,
        required: true
    },
    questionsSolved: {
        simpler: {
            type: Number,
            required: true
        },
        simple: {
            type: Number,
            required: true
        },
        notSimple: {
            type: Number,
            required: true
        }
    },
    bestTopics: {
        type: Array<String>,
        required: true
    },
    dateJoined: {
        type: String,
        required: true
    }
})

const User = mongoose.model<IUser>('User', userSchematic);
export default User;