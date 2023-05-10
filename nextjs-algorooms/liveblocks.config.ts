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
    cursorLocationData: any
};

export type TextChatMessage = {
    username: string,
    message: string,
    timestamp: number,
    color: string
};

type Storage = {
    uid: string,
    editorText: string,
    lobbyAccess: string,
    difficulty: string,
    topics: LiveList<string>,
    messages: LiveList<TextChatMessage>,
    host: string,
    language: string
};

export const {
    RoomProvider,
    useOthers,
    useStorage,
    useUpdateMyPresence,
    useMutation,
    useSelf
} = createRoomContext<Presence, Storage>(client);