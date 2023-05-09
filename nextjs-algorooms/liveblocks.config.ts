import { LiveList, LiveObject, createClient } from "@liveblocks/client";
import { createRoomContext } from "@liveblocks/react";

const client = createClient({
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

type TextChatMessage = {
    username: string,
    message: string,
    timestamp: number
};

type Storage = {
    uid: string,
    editorText: string,
    lobbyAccess: string,
    difficulty: string,
    topics: LiveList<string>,
    members: LiveList<string>,
    messages: LiveList<string>,
    host: string
};

export const {
    RoomProvider,
    useOthers,
    useStorage,
    useUpdateMyPresence,
    useMutation,
    useSelf
} = createRoomContext<Presence, Storage>(client);