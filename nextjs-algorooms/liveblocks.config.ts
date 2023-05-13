import { LiveList, LiveObject, createClient } from "@liveblocks/client";
import { createRoomContext } from "@liveblocks/react";

export const client = createClient({
  publicApiKey: "pk_dev_7rSbiCxmktdPPA-hgYZsTSxKsm3d3WUtHWKcq8wYTBLEV6lJKnWHGmEkZzEGsfMS",
});

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

export type TextChatMessage = {
    username: string,
    message: string,
    timestamp: number,
    color: string
};

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