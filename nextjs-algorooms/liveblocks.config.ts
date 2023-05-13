import {
    LiveList,
    createClient
} from "@liveblocks/client";

import {
    createRoomContext
} from "@liveblocks/react";

// Create the client connection to LiveBlocks
export const client = createClient({
  publicApiKey: "pk_dev_7rSbiCxmktdPPA-hgYZsTSxKsm3d3WUtHWKcq8wYTBLEV6lJKnWHGmEkZzEGsfMS",
});

// Type schema for presence -- a user's own unique state that is shared
export type Presence = {
    isTypingCode: boolean,
    isTypingMessage: boolean,
    isRunningCode: boolean,
    isSubmittingCode: boolean,
    username: string,
    color: string,
    cursorLocationData: any,
    joined: number
};

// Type schema for storage -- non-unique shared data
export type Storage = {
    uid: string,
    editorText: string,
    lobbyAccess: string,
    difficulty: string,
    topics: LiveList<string>,
    messages: LiveList<TextChatMessage>,
    questions: LiveList<string>,
    host: string,
    language: string,
    startMinutes: number,
    minutesLeft: number,
    secondsLeft: number,
    inRound: boolean,
    awaitingQuestion: boolean,
    currentQuestion: any // to be question object
};

// Type schema for text chat messages
export type TextChatMessage = {
    username: string,
    message: string,
    timestamp: number,
    color: string
};

// Access to context provider and hooks
export const {
    suspense: {
        RoomProvider,
        useOthers,
        useStorage,
        useUpdateMyPresence,
        useMutation,
        useSelf,
        useRoom
    }
} = createRoomContext<Presence, Storage>(client);