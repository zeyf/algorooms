import {
  LiveList,
  LiveObject,
  createClient
} from "@liveblocks/client";

import {
  createRoomContext
} from "@liveblocks/react";

// Create the client connection to LiveBlocks
export const client = createClient({
  publicApiKey: process.env.LB_PUBLIC_API_KEY
});

// Type schema for the editor texts for the different languages supported as of right now
export type EditorTexts = {
  python: string,
  javascript: string,
  // cpp: string,
  // java: string
};

// Type schema for presence -- a user's own unique state that is shared
export type Presence = {
  isTypingCode: boolean,
  isTypingMessage: boolean,
  username: string,
  color: string,
  cursorLocationData: any,
  joined: number,
  votedToExecuteCode: boolean
};

// Type schema for storage -- non-unique shared data
export type Storage = {
  uid: string,
  resetEditorTexts: LiveObject<EditorTexts>,
  activeEditorTexts: LiveObject<EditorTexts>,
  lobbyAccess: string,
  difficulty: string,
  topics: LiveList<string>,
  messages: LiveList<TextChatMessage>,
  questions: LiveList<string>,
  host: string,
  language: string,
  startMinutes: number,
  startSeconds: number,
  minutesLeft: number,
  secondsLeft: number,
  inRound: boolean,
  awaitingQuestion: boolean,
  currentQuestion: any, // to be question object
  runCodeInQueue: boolean,
  submitCodeInQueue: boolean,
  voteCount: number,
  hasRanCodeOnQuestion: boolean,
  ranCodeOutputOnQuestion: {
    state: string,
    userOutput: string,
    expectedOutput: string,
    testCaseIndex: number,
    totalTestCases: number
  }
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