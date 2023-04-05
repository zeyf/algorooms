
import mongoose from 'mongoose';
const Schema = mongoose.Schema;

export interface Question {
    title: string,
    index: string,
    difficulty: string,
    topic: string,
    description: string,
    constraints: Array<string>,
    hints: Array<string>
};

export interface IUser extends mongoose.Document {
    name: string,
    nickname: string,
    picture: string,
    email: string,
    sid: string,
    sub: string,
    questionsSolved: {
        simpler: number,
        simple: number,
        notSimple: number
    },
    bestTopics: Array<string>
}

export const userSchematic = new Schema({
    name: {
        type: String,
        required: true
    },
    nickname: {
        type: String,
        required: true
    },
    picture: {
        type: String,
        required: true
    },
    email: {
        type: String,
        required: true
    },
    sid: {
        type: String,
        required: true
    },
    sub: {
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
    }
})

const User = mongoose.model<IUser>('User', userSchematic);
export default User;