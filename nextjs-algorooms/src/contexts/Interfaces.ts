export interface roomContextLayerInterface {
    uid: string,
    socket: any,

    members: any[],
    setMembers?: Function,
    messages: any[],
    setMessages?: Function,
    language: string,
    setLanguage?: Function,
    code: string,
    setCode?: Function,
    runningCode: boolean,
    setRunningCode?: Function,
    submittingCode: boolean,
    setSubmittingCode?: Function,
    topics: string[],
    setTopics?: Function,
    lobbyAccess: string,
    setLobbyAccess?: Function,
    difficulty: string,
    setDifficulty?: Function
};