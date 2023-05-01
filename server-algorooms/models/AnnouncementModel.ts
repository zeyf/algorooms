
import mongoose from 'mongoose';
const Schema = mongoose.Schema;

// Create the interface for the Question
export interface IAnnouncement extends mongoose.Document {
    title: string,
    message: string,
    timestamp: number,
    by: string,
    uid: string
};

export const announcementSchematic = new Schema({
    title: {
        type: String,
        required: true
    },
    message: {
        type: String,
        required: true
    },
    timestamp: {
        type: Number,
        required: true
    },
    by: {
        type: String,
        required: true
    },
    uid: {
        type: String,
        required: true
    }
})

export default mongoose.model<IAnnouncement>('Announcement', announcementSchematic);